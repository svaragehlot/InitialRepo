"""
fetch_transcripts.py
Fetch YouTube transcripts for a list of videos and save one clean markdown file per video
into research/youtube-transcripts/.

Free: uses the youtube-transcript-api library (no API key, no Google Cloud).
Install:  pip install -r requirements.txt
Run:      python fetch_transcripts.py
Windows venv run:  .\\venv\\Scripts\\python.exe fetch_transcripts.py

INPUT: a file named videos.txt in the same folder, one video per line, in either form:
    Author Name, https://www.youtube.com/watch?v=VIDEOID
    Author Name, https://youtu.be/VIDEOID
    Author Name, VIDEOID
Lines starting with # are ignored.
"""

import os
import re
import sys

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable,
    )
except ImportError:
    print("Missing dependency. Run:  pip install -r requirements.txt")
    sys.exit(1)

OUT_DIR = os.path.join("research", "youtube-transcripts")
INPUT_FILE = "videos.txt"


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-") or "untitled"


def extract_video_id(url_or_id):
    s = url_or_id.strip()
    # Already a bare ID (YouTube IDs are 11 chars)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", s):
        return s
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", s)
    return m.group(1) if m else None


def parse_line(line):
    """Return (author, video_id) or (None, None) to skip."""
    line = line.strip()
    if not line or line.startswith("#"):
        return None, None
    if "," in line:
        author, url = line.split(",", 1)
        author = author.strip()
    else:
        author, url = "unknown", line
    vid = extract_video_id(url)
    return (author, vid) if vid else (author, None)


def transcript_to_text(fetched):
    """Works across library versions: fetched items expose .text or ['text']."""
    parts = []
    for item in fetched:
        if isinstance(item, dict):
            parts.append(item.get("text", ""))
        else:
            parts.append(getattr(item, "text", ""))
    return "\n".join(p for p in parts if p).strip()


def fetch_one(video_id):
    """Return transcript text or raise. Handles old and new library APIs.

    Newer versions expose an instance method .fetch(); older versions expose the
    classmethod .get_transcript(). We pick whichever exists and let any real error
    (network, no transcript, etc.) propagate to the caller for accurate reporting.
    """
    api = YouTubeTranscriptApi()
    if hasattr(api, "fetch"):
        return transcript_to_text(api.fetch(video_id))
    return transcript_to_text(YouTubeTranscriptApi.get_transcript(video_id))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    if not os.path.exists(INPUT_FILE):
        print(f"Create {INPUT_FILE} first (one video per line). See the header of this script.")
        sys.exit(1)

    saved, skipped = 0, 0
    with open(INPUT_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        author, vid = parse_line(line)
        if author is None:
            continue
        if vid is None:
            print(f"SKIP (no video id found): {line.strip()}")
            skipped += 1
            continue
        try:
            text = fetch_one(vid)
            if not text:
                print(f"SKIP (empty transcript): {author} / {vid}")
                skipped += 1
                continue
            fname = f"{slugify(author)}_{vid}.md"
            path = os.path.join(OUT_DIR, fname)
            with open(path, "w", encoding="utf-8") as out:
                out.write(f"# {author} - YouTube transcript\n\n")
                out.write(f"- Video: https://www.youtube.com/watch?v={vid}\n")
                out.write(f"- Video ID: {vid}\n\n")
                out.write("## Transcript\n\n")
                out.write(text + "\n")
            print(f"SAVED: {path}")
            saved += 1
        except (TranscriptsDisabled, NoTranscriptFound):
            print(f"SKIP (no transcript available): {author} / {vid}")
            skipped += 1
        except VideoUnavailable:
            print(f"SKIP (video unavailable): {author} / {vid}")
            skipped += 1
        except Exception as e:
            print(f"SKIP (error: {e}): {author} / {vid}")
            skipped += 1

    print(f"\nDone. Saved {saved}, skipped {skipped}.")


if __name__ == "__main__":
    main()
