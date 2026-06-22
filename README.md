# AI-Powered SEO Content Production - Research Project

This repo is my research collection for a future marketing playbook on **AI-powered SEO content
production**. I went looking for people who actually build AI-assisted SEO content (or the tools and
systems behind it) and gathered their recent thinking in one place.

## Why this topic

AI has changed how SEO content gets made and how it gets found (AI Overviews, ChatGPT, Perplexity,
answer engine optimization). I wanted to learn from people doing this in practice, not in theory,
so the eventual playbook is grounded in real workflows.

## The 10 experts (and why each made my list)

1. **Ryan Law** (Ahrefs) - fully integrated AI into content but still insists on human review; honest
   about the skill gap.
2. **Julia McCoy** (BrandWell / First Movers) - found her on YouTube; her point: be so specific that
   the AI picks you without comparing.
3. **Bernard Huang** (Clearscope) - his blogs on content pruning and content quality showed me what
   AI still can't understand about an audience.
4. **Koray Tuğberk Gübür** (Holistic SEO) - on LinkedIn, all about how to structure AI content so it
   ranks (semantic SEO, topical authority).
5. **Mike King** (iPullRank) - the clearest technical view of where AI content and search are going.
6. **Aleyda Solis** (Orainti) - the most practical source; turns AI-search shifts into steps.
7. **Kevin Indig** (Growth Memo) - data-backed; ties AI content tactics to business growth.
8. **Nathan Gotch** (Gotch SEO) - hands-on tutorials; "search everywhere" (Google, ChatGPT, YouTube).
9. **Ross Hudgens** (Siege Media) - honest about what AI can and can't do in content; brand-first.
10. **Jeff Coyle** (MarketMuse) - strong on AI content planning: briefs, topic modelling.

Full links and my notes are in `research/sources.md`.

## What I collected

- **YouTube transcripts:** 8 videos across 8 experts - `research/youtube-transcripts/`
- **LinkedIn posts:** 18 posts across all 10 experts - `research/linkedin-posts/`
- **Other** (articles, frameworks, strategy guides): 4 items with my notes - `research/other/`

## How I collected it

- **YouTube transcripts:** a small Python script (`fetch_transcripts.py`) using the
  youtube-transcript-api library. I list videos in `videos.txt` (one per line as `Author, URL`) and
  it saves one clean markdown transcript per video.
- **LinkedIn posts:** collected manually into a file per author (URL, date, text, why it's useful).
- **Other material:** articles and frameworks I read along the way, saved with a short note and one
  playbook idea I'd test from each.

## Repo structure

```
/research
  sources.md            the 10 experts: links, dates, my notes
  /linkedin-posts       one file per expert (18 posts total)
  /youtube-transcripts  one file per video (8 transcripts)
  /other                extra articles / frameworks / strategy notes
fetch_transcripts.py    YouTube transcript fetcher
videos.txt              list of videos to fetch
requirements.txt
```

## Run the transcript script

```
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python fetch_transcripts.py
```

## What this could support

A few themes repeat across these ten: AI is fine for drafting and coverage but the human still owns
the angle and the judgment; comprehensiveness and information gain beat keyword stuffing; and
optimizing for AI answers (AEO/GEO) is becoming its own layer on top of SEO. A real playbook would
turn those into a repeatable system: planning and briefs, an AI-assisted drafting workflow with clear
human checkpoints, and a way to measure visibility in both search and AI answers.
