# How I Do Content Engineering with Claude Code

- Expert: Ryan Law (Ahrefs)
- Author: Ryan Law, Director of Content Marketing, Ahrefs
- Type: Blog article
- Published: April 28, 2026
- URL: https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/

## What it covers
Ryan walks through the content automation system he built for the Ahrefs blog using Claude Code and
about 23 "skill files" chained together. It takes a keyword idea to a publish-ready draft in roughly
6-12 minutes, and they've used it to publish around 15 new articles and update ~30 more. His big
point: AI content is not good by default, this works because the skills mirror years of human
editorial experience.

## Key takeaways (in my words)
- Each skill file = one step of their real editorial process (keyword research, topic-gap analysis,
  outlining, drafting, etc.), written in Markdown with examples and output rules. A main pipeline
  skill runs them in order.
- Every step saves its own output file, so if a draft is bad you can see exactly which step went
  wrong, fix that skill, and rerun from there.
- Feed the model real data, not guesses: he wires in the Ahrefs MCP for keyword and SERP data, plus
  competitor content, deep research, and product info. "Mandate the data sources" or the LLM just
  bloviates.
- Front-load human direction: a small amount of expert context at the start beats heavy editing at
  the end.
- He still reads every word, and deliberately does NOT use this to mass-produce content; it's for
  maintaining a quality evergreen library and removing drudgery.

## One idea I'd test in a playbook
Build a small set of "skill files" for one content type (say, a comparison post), with one human
context step at the start and a human review at the end, and measure time-to-draft vs quality.
