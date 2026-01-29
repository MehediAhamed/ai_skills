#!/usr/bin/env python3
"""
Download a YouTube video with yt-dlp and transcribe it with vlmrun.
Saves the transcript to <output_dir>/transcript.txt.
Requires VLMRUN_API_KEY in environment (or .env in project root).
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("yt-dlp is required. Run: uv pip install yt-dlp vlmrun", file=sys.stderr)
    sys.exit(1)
    


def load_dotenv():
    """Load .env from script's project root (youtube-transcription-generator)."""
    root = Path(__file__).resolve().parent.parent
    env_path = root / ".env"
    if env_path.is_file():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key and value and key not in os.environ:
                        os.environ[key] = value


def download_video(url: str, output_dir: Path) -> Path:
    """Download YouTube video to output_dir; returns path to the downloaded file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    outtmpl = str(output_dir / "video.%(ext)s")
    ydl_opts = {
        "outtmpl": outtmpl,
        "format": "best[ext=mp4]/best",
        "merge_output_format": "mp4",
        "quiet": False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    # Resolve path: yt-dlp may produce video.mp4 or video.mkv
    for p in output_dir.glob("video.*"):
        return p
    raise FileNotFoundError(f"No downloaded file found in {output_dir}")


def run_vlmrun_transcribe(video_path: Path, output_dir: Path, no_stream: bool = True) -> str:
    """Run vlmrun to transcribe the video; returns transcript text from stdout."""
    prompt = (
        "Transcribe this video with timestamps for each section. "
        "Output the full transcript in a clear, readable format."
    )
    cmd = [
        "vlmrun",
        "chat",
        prompt,
        "-i",
        str(video_path),
        "-o",
        str(output_dir),
    ]
    if no_stream:
        cmd.append("--no-stream")
    env = os.environ.copy()
    if "VLMRUN_API_KEY" not in env:
        print("Warning: VLMRUN_API_KEY not set. Set it in .env or your environment.", file=sys.stderr)
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        raise RuntimeError(f"vlmrun exited with code {result.returncode}")
    return result.stdout or ""


def main():
    parser = argparse.ArgumentParser(
        description="Download a YouTube video and transcribe it with vlmrun."
    )
    parser.add_argument(
        "url",
        help="YouTube video URL (e.g. https://www.youtube.com/watch?v=VIDEO_ID)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="./output",
        type=Path,
        help="Output directory for downloaded video and transcript (default: ./output)",
    )
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Let vlmrun stream output (default: no-stream for capturing transcript)",
    )
    args = parser.parse_args()

    load_dotenv()

    output_dir = args.output.resolve()
    print(f"Output directory: {output_dir}")

    print("Downloading video...")
    video_path = download_video(args.url, output_dir)
    print(f"Downloaded: {video_path}")

    print("Transcribing with vlmrun...")
    transcript = run_vlmrun_transcribe(video_path, output_dir, no_stream=not args.stream)

    transcript_path = output_dir / "transcript.txt"
    transcript_path.write_text(transcript, encoding="utf-8")
    print(f"Transcript saved to: {transcript_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
