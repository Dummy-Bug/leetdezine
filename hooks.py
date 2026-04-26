import json
import logging
import re
from pathlib import Path


class _SuppressDocsGitLogNoise(logging.Filter):
    def filter(self, record):
        message = record.getMessage()
        return not (
            "git-revision-date-localized-plugin" in message
            and "has no git logs, using current timestamp" in message
            and "/docs" in message
        )


logging.getLogger("mkdocs.plugins").addFilter(_SuppressDocsGitLogNoise())

SLUG_LABELS = {
    "nfrs": "NFRs", "cap-theorem": "CAP Theorem", "pacelc": "PACELC",
    "sql": "SQL", "acid": "ACID", "cdc": "CDC", "kv-store": "KV Store",
    "sde-1": "SDE-1", "sde-2": "SDE-2", "sde-3": "SDE-3",
    "raft": "Raft", "paxos": "Paxos", "zookeeper": "ZooKeeper",
    "crdts": "CRDTs", "l4": "L4", "l7": "L7", "sqs": "SQS",
    "rabbitmq": "RabbitMQ", "cqrs": "CQRS", "dynamodb": "DynamoDB",
    "bigtable": "Bigtable", "newsql": "NewSQL", "ntp": "NTP",
    "spof": "SPOF", "ttl": "TTL", "lru": "LRU", "lfu": "LFU",
    "hls": "HLS", "etcd": "etcd", "mapreduce": "MapReduce",
    "url-shortener": "URL Shortener",
    "unique-id-generator": "Unique ID Generator",
    "notification-system": "Notification System",
    "rate-limiter": "Rate Limiter",
    "back-of-envelope": "Back of Envelope",
    "interview-questions": "Interview Questions",
    "deep-dives": "Deep Dives",
}


def _slug_to_label(slug):
    return SLUG_LABELS.get(slug) or " ".join(w.capitalize() for w in slug.split("-"))


def _truncate_snippet(text, limit=160):
    text = re.sub(r"\s+", " ", text)
    text = text.replace('"', "").replace("“", "").replace("”", "")
    text = text.strip(" '‘’")
    if len(text) <= limit:
        return text
    truncated = text[: limit + 1].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return truncated.strip(" '‘’") + "..."


def _clean_markdown_block(block):
    block = re.sub(r"```.*?```", " ", block, flags=re.S)
    block = re.sub(r"`([^`]+)`", r"\1", block)
    block = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", block)
    block = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", block)
    block = re.sub(r"\[![-\w]+\]\s*", "", block)
    block = re.sub(r"<[^>]+>", " ", block)

    cleaned_lines = []
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("!!! "):
            continue
        line = re.sub(r"^\s*>+\s?", "", line)
        line = re.sub(r"^\s{0,3}#{1,6}\s+", "", line)
        line = re.sub(r"^\s*[-*+]\s+", "", line)
        if re.fullmatch(r"[-|:\s]+", line):
            continue
        if line.startswith("|") and line.endswith("|"):
            continue
        cleaned_lines.append(line)

    if len(cleaned_lines) > 1 and len(cleaned_lines[0]) < 45 and cleaned_lines[0][-1] not in ".!?:":
        cleaned_lines = cleaned_lines[1:]

    text = " ".join(cleaned_lines)
    text = re.sub(r"[*_~]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _derive_description(markdown, page):
    title_candidates = {
        re.sub(r"\s+", " ", value).strip().lower()
        for value in [page.title, page.meta.get("title")]
        if value
    }

    for block in re.split(r"\n\s*\n", markdown):
        if re.match(r"^\s*#{1,6}\s+", block):
            continue
        text = _clean_markdown_block(block)
        normalized = re.sub(r"\s+", " ", text).strip().lower()
        if normalized in title_candidates:
            continue
        if len(text) >= 40:
            return _truncate_snippet(text)

    fallback = _clean_markdown_block(markdown)
    if len(fallback) >= 40:
        return _truncate_snippet(fallback)
    return None


def _has_frontmatter_description(source):
    if not source.startswith("---"):
        return False
    frontmatter = source.split("---", 2)[1]
    return re.search(r"^\s*description\s*:", frontmatter, flags=re.M) is not None


def _canonical_url(page, site_url):
    return getattr(page, "canonical_url", None) or (site_url + "/" + page.url.lstrip("/"))


def _social_image_url(page, site_url):
    src_uri = getattr(page.file, "src_uri", "")
    if src_uri.endswith(".md"):
        return f"{site_url}/assets/images/social/{src_uri[:-3]}.png"
    return f"{site_url}/assets/og-image.png"


def _publisher_schema(site_url):
    return {
        "@type": "Organization",
        "@id": site_url + "/#organization",
        "name": "LeetDezine",
        "url": site_url + "/",
        "logo": {
            "@type": "ImageObject",
            "url": site_url + "/assets/images/social/index.png",
        },
    }


def _page_schema(page, config, site_url):
    title = page.meta.get("title") if page.meta and page.meta.get("title") else page.title
    description = page.meta.get("description") if page.meta else None
    canonical = _canonical_url(page, site_url)
    image = _social_image_url(page, site_url)
    publisher = _publisher_schema(site_url)

    if page.is_homepage:
        return [
            {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": "LeetDezine",
                "url": site_url + "/",
                "description": config.get("site_description"),
                "publisher": {"@id": publisher["@id"]},
            },
            publisher,
        ]

    schema_type = "WebPage" if getattr(page.file, "src_uri", "").endswith("index.md") else "BlogPosting"
    schema = {
        "@context": "https://schema.org",
        "@type": schema_type,
        "url": canonical,
        "mainEntityOfPage": canonical,
        "description": description or config.get("site_description"),
        "image": image,
        "publisher": {"@id": publisher["@id"]},
    }

    if schema_type == "BlogPosting":
        schema["headline"] = title
        schema["author"] = {
            "@type": "Organization",
            "name": "LeetDezine",
            "url": site_url + "/",
        }
        published = (
            page.meta.get("git_creation_date_localized_raw_iso_datetime")
            or page.meta.get("git_creation_date_localized_raw_iso_date")
        )
        modified = (
            page.meta.get("git_revision_date_localized_raw_iso_datetime")
            or page.meta.get("git_revision_date_localized_raw_iso_date")
        )
        if published:
            schema["datePublished"] = published
        if modified:
            schema["dateModified"] = modified
    else:
        schema["name"] = title

    return schema


# NOTE: We do NOT override page.title here. page.title powers nav tabs,
# sidebar labels, and breadcrumbs — those need to stay short. The SEO-friendly
# long title from frontmatter `title:` is read directly in overrides/main.html
# for the <title> tag only, leaving nav/sidebar/breadcrumbs untouched.


def on_page_markdown(markdown, page, config=None, files=None, **kwargs):
    """Fill missing descriptions from page content.

    Most pages currently lack explicit frontmatter descriptions. Generate a
    snippet-sized fallback from the Markdown body so meta description, social
    tags, and structured data can all stay page-specific.
    """
    if not page.meta.get("description"):
        derived = _derive_description(markdown, page)
        if derived:
            page.meta["description"] = derived
    return markdown


def on_page_context(context, page, config=None, nav=None, **kwargs):
    """Inject BreadcrumbList JSON-LD schema for every page.

    Google uses this to render breadcrumb trails in search results instead of
    raw URLs. Walks the URL path and looks up real page titles when available;
    falls back to a prettified slug for path segments without a real page.
    """
    site_url = (config["site_url"] if config and config.get("site_url")
                else "https://leetdezine.com").rstrip("/")

    if getattr(page.file, "abs_src_path", None):
        source = Path(page.file.abs_src_path).read_text()
        if not _has_frontmatter_description(source):
            markdown = source.split("---", 2)[2] if source.startswith("---") else source
            derived = _derive_description(markdown, page)
            if derived:
                page.meta["description"] = derived

    url_path = page.url.strip("/")
    segments = url_path.split("/") if url_path else []

    # For each page in nav, prefer the SEO-friendly meta.title over the
    # nav label so breadcrumbs read "Caching" instead of "Overview".
    page_titles = {}
    if nav is not None:
        for p in nav.pages:
            seo = p.meta.get("title") if hasattr(p, "meta") else None
            page_titles[p.url] = seo or p.title

    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "LeetDezine",
        "item": site_url + "/",
    }]

    cumulative = ""
    for i, segment in enumerate(segments):
        cumulative += segment + "/"
        name = page_titles.get(cumulative) or _slug_to_label(segment)
        items.append({
            "@type": "ListItem",
            "position": i + 2,
            "name": name,
            "item": site_url + "/" + cumulative,
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }
    context["breadcrumb_schema"] = json.dumps(schema, ensure_ascii=False)
    context["seo_schema"] = json.dumps(_page_schema(page, config, site_url), ensure_ascii=False)
    return context
