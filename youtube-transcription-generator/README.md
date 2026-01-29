## YouTube Transcription Generator (VLM Run Skill)

Generate transcriptions from YouTube videos using the VLM Run (`vlmrun`) CLI. This skill:

1. **Downloads** the YouTube video (or audio) with **yt-dlp**.
2. **Transcribes** the video with **vlmrun** (Orion visual AI).
3. **Saves** the transcript to a file (plain text or with timestamps).

For vlmrun setup and options, see **vlmrun-cli-skill**.

### 1. Prerequisites

- Python 3.10+
- `vlmrun[cli]` and `yt-dlp` installed
- `VLMRUN_API_KEY` set in your environment

```bash
pip install uv
cd youtube-transcription-generator
uv venv && source .venv/bin/activate   # or .venv\Scripts\Activate.ps1 on Windows
uv pip install -r requirements.txt
```

Set your API key (example for PowerShell):

```powershell
$env:VLMRUN_API_KEY="your-api-key-here"
[System.Environment]::SetEnvironmentVariable('VLMRUN_API_KEY', 'your-api-key-here', 'User')
```

Or copy `.env_template` to `.env` and fill in `VLMRUN_API_KEY`.

### 2. Transcribe a YouTube Video

From the `youtube-transcription-generator` directory (with venv activated):

```bash
python scripts/run_transcription.py "https://www.youtube.com/watch?v=VIDEO_ID" -o ./output
```

This will:

1. Download the video with yt-dlp into the output directory.
2. Run vlmrun to transcribe the video.
3. Save the transcript as `output/transcript.txt`.

### 3. Manual flow (download + vlmrun)

```bash
# Download with yt-dlp
yt-dlp -f "bv*[ext=mp4]+ba/best[ext=mp4]/best" -o video.mp4 "https://www.youtube.com/watch?v=VIDEO_ID"

# Transcribe with vlmrun (see vlmrun-cli-skill for options)
vlmrun chat "Transcribe this video with timestamps for each section. Output the full transcript in a clear, readable format." -i video.mp4 -o ./output
```

Save the vlmrun stdout to a file (e.g. `transcript.txt`).

### 4. Typical workflow

1. Activate the virtual environment.
2. Set `VLMRUN_API_KEY` (or use `.env`).
3. Run `python scripts/run_transcription.py <youtube_url> -o ./output`.
4. Open `output/transcript.txt` (and any artifacts in `output/`).

For more details, prompt variants, and troubleshooting, see `SKILL.md` in this directory.
