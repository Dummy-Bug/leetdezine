import json
import logging


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


# NOTE: We do NOT override page.title here. page.title powers nav tabs,
# sidebar labels, and breadcrumbs — those need to stay short. The SEO-friendly
# long title from frontmatter `title:` is read directly in overrides/main.html
# for the <title> tag only, leaving nav/sidebar/breadcrumbs untouched.


def on_page_context(context, page, config=None, nav=None, **kwargs):
    """Inject BreadcrumbList JSON-LD schema for every page.

    Google uses this to render breadcrumb trails in search results instead of
    raw URLs. Walks the URL path and looks up real page titles when available;
    falls back to a prettified slug for path segments without a real page.
    """
    site_url = (config["site_url"] if config and config.get("site_url")
                else "https://leetdezine.com").rstrip("/")
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
        item = {"@type": "ListItem", "position": i + 2}
        if cumulative in page_titles:
            item["name"] = page_titles[cumulative]
            item["item"] = site_url + "/" + cumulative
        else:
            item["name"] = _slug_to_label(segment)
        items.append(item)

    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }
    context["breadcrumb_schema"] = json.dumps(schema, ensure_ascii=False)
    return context
