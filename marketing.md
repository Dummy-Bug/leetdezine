# LeetDezine Marketing Plan

LeetDezine should be marketed as a system design learning brand, not just a docs website.

The content is long-form and high-effort. The mistake would be posting "I wrote a case study on rate limiters" and expecting people to click. Each page should be marketed as a series of sharp engineering insights.

## Positioning

Clear promise:

> LeetDezine helps backend engineers learn system design through deep, decision-by-decision case studies.

Target audience:

- SDE-1 and SDE-2 engineers preparing for interviews
- Backend engineers moving toward senior roles
- Students tired of shallow "draw boxes" system design content
- People who want concrete tradeoffs, failure modes, and architecture decisions

Do not market it as "system design notes." That sounds generic.

Market it as:

> System design case studies where every decision is justified.

## Main Funnel

Use this simple funnel:

```text
Short insight post
    ↓
Diagram / mini thread
    ↓
Full case study page
    ↓
Repeat exposure
    ↓
Bookmark / follow / share
```

Most people will not click the first time. The goal is repeated useful exposure.

## Channels

Start with only three channels.

### LinkedIn

Best for engineers, students, recruiters, and career-oriented reach.

Post concise lessons, diagrams, and "mistakes people make in system design" posts.

### X / Twitter

Best for sharp technical takes, diagrams, and threads.

Keep it opinionated, concrete, and easy to repost.

### DEV.to

Best for republishing edited versions of case studies as blog posts.

Use canonical URLs back to the original LeetDezine page when cross-posting.

### Optional Later

- Peerlist
- Reddit, carefully
- Hacker News, only for genuinely strong posts
- Newsletter, once there are repeat readers

## Weekly Cadence

Run this for 8 weeks:

```text
Monday: Short insight post
Tuesday: Diagram post
Wednesday: Failure-mode post
Thursday: Mini case-study thread
Friday: Link to full article with summary
Weekend: Repost best-performing idea in another format
```

Example for the rate limiter content:

```text
Monday:
"Most people place rate limiting at the API Gateway and stop thinking.
That works until Redis goes down, config DB lags, or a DDoS hits before the limiter."

Tuesday:
ASCII diagram: request flow with API Gateway, Redis, Rule DB, rate limiter.

Wednesday:
"What happens when Redis goes down in a distributed rate limiter?"

Thursday:
Thread: "5 failure modes your rate limiter design must handle."

Friday:
Full link: "I wrote the complete deep dive here."
```

## Post Formats

Use these repeatedly.

### Common Mistake

```text
Common system design mistake:

"Rate limiter protects us from DDoS."

No. A rate limiter protects application fairness.
DDoS defense starts before traffic reaches your app.
```

### Failure Mode

```text
What happens if Redis goes down in a distributed rate limiter?

Bad answer:
"All requests fail."

Better answer:
Fail open for low-risk APIs.
Fail closed for abuse-sensitive APIs.
Use local fallback counters.
Alert immediately.
```

### Tradeoff

```text
Fixed window counter is simple.
Sliding window log is accurate.
Token bucket is practical.

The interview answer is not "which is best?"
The answer is "what failure mode are we optimizing for?"
```

### Diagram-First

```text
API Gateway
   ↓
Rate Limiter
   ↓
Service

Looks simple.

Until you ask:
- Where are rules stored?
- What if Redis is down?
- What if config DB is stale?
- What if traffic is DDoS-scale?
```

### Interview Framing

```text
In a system design interview, don't just say:
"We use Redis for rate limiting."

Say:
"We use Redis for distributed counters, but we define fallback behavior when Redis is unavailable."
```

## SEO Plan

The site can rank over time, but only if each important page targets real search intent.

For every important page, make the title look like something people search.

Bad:

```text
Redis Node Down
```

Better:

```text
What Happens When Redis Goes Down in a Distributed Rate Limiter?
```

Bad:

```text
DDoS And Defense Layers
```

Better:

```text
Why a Rate Limiter Cannot Stop DDoS Alone
```

Core SEO principles:

- Make content useful, well-organized, and written for users first.
- Use descriptive page titles.
- Use descriptive URLs where possible.
- Add strong internal links between related pages.
- Add useful meta descriptions for important pages.
- Keep pages easy to read and navigate.

## Distribution System

For every deep-dive page, create these assets:

```text
1 full article
3 LinkedIn posts
3 tweets
1 diagram
1 DEV.to article
1 short comparison table
1 "interview answer" version
```

Example from one page:

Full page:

```text
DDoS And Defense Layers
```

Turn it into:

- Post 1: "Rate limiters do not stop DDoS"
- Post 2: "Where DDoS defense actually happens"
- Post 3: "Layered defense architecture"
- Diagram: CDN / WAF / Load Balancer / API Gateway / Rate Limiter
- DEV article: "Why Your Rate Limiter Won't Save You From DDoS"
- Interview answer: 90-second spoken explanation

## Community Strategy

Do not spam links.

Use this ratio:

```text
80% useful native content
20% links back to site
```

In comments and communities, answer questions directly. Then add:

> I wrote a deeper version here if useful.

This works better than dropping links.

Places to participate:

- LinkedIn comments under system design creators
- Reddit: r/systemdesign, r/leetcode, r/cscareerquestions, carefully
- DEV comments
- Peerlist posts
- Engineering Discord or Slack communities you already use

## Strongest Hook

The strongest angle:

> Most system design content shows the final diagram. LeetDezine explains the decisions that create the diagram.

Use this repeatedly.

Example:

```text
System design is not about drawing boxes.
It is about defending decisions.

Why Redis?
Why this sharding key?
What fails?
What degrades?
What gets paged?

That is what LeetDezine focuses on.
```

## First 7 Days

Do not add more content during the first week. Package what already exists.

1. Pick the best case study: Rate Limiter.
2. Create 10 short posts from it.
3. Create 3 diagrams.
4. Publish one DEV article with canonical link to the site.
5. Post daily on LinkedIn and X.
6. Track saves, comments, profile clicks, and link clicks.
7. Double down on the topic that performs.

## Metrics

Ignore vanity metrics at first.

Track:

- Profile visits
- Link clicks
- Bookmarks / saves
- Comments from engineers
- Returning users
- Search impressions in Google Search Console
- Which case study people land on first

## 30-Day Goal

```text
30 days
20-25 posts
4 DEV articles
10 diagrams
1 full case-study thread per week
Google Search Console connected
At least 100 relevant engineers aware of the site
```

## Source References

- Google SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google Helpful Content guidance: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Essentials: https://developers.google.com/search/docs/essentials
- LinkedIn content sharing help: https://www.linkedin.com/help/linkedin/answer/a797006
- DEV writing and cross-posting help: https://dev.to/help/writing-editing-scheduling
