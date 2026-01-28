## Pitch Deck Generator (VLM Run Skill)

Generate investor-ready pitch decks using the VLM Run (`vlmrun`) CLI.  
This skill turns a structured startup brief (plus optional assets like logo, screenshots, and charts) into:

- **Markdown deck**: slide titles, bullets, speaker notes, visual suggestions
- **Optional PDF pitch document**: multi-page deck/memo
- **Optional images**: hero images and slide backgrounds to drop into slides

### 1. Prerequisites

- Python 3.10+
- `vlmrun[cli]` installed
- `VLMRUN_API_KEY` set in your environment

```bash
pip install uv
uv venv && source .venv/bin/activate   # or .venv\Scripts\Activate.ps1 on Windows
uv pip install "vlmrun[cli]"
```

Set your API key (example for PowerShell):

```powershell
$env:VLMRUN_API_KEY="your-api-key-here"
[System.Environment]::SetEnvironmentVariable('VLMRUN_API_KEY', 'your-api-key-here', 'User')
```

### 2. Create Your Startup Brief

Create `inputs/startup_brief.txt` with structured info:

```text
Startup: <name>
One-liner: <short description>

Problem:
- ...

Solution:
- ...

Market:
- ...

Business Model:
- ...

Traction:
- ...

Team:
- ...

Fundraising:
- Target round size:
- Use of funds:
```

Optional: add assets in an `assets/` folder (e.g. `logo.png`, product screenshots, charts).

### 3. Generate the Markdown Deck

From the `pitch-deck-generator` directory:

```bash
vlmrun chat -p inputs/startup_brief.txt \
  "Create a concise, VC-ready pitch deck (10–15 slides) with titles, bullets, speaker notes, and visual suggestions. Output as markdown." \
  -o ./pitch_deck_output
```

This creates a markdown deck in `pitch_deck_output/` you can paste into Keynote/PowerPoint/Google Slides.

### 4. Generate a PDF Pitch Document (Optional)

```bash
vlmrun chat \
  "Using this startup brief, create an investor-ready pitch deck as a multi-page PDF document I can share directly with investors." \
  -p inputs/startup_brief.txt \
  -o ./pitch_deck_output/pdf
```

Check `pitch_deck_output/pdf` for the generated PDF artifact.

### 5. Generate Visual Assets (Optional)

```bash
vlmrun chat \
  "Generate 6 slide background images that match the brand and tone of this startup." \
  -i assets/logo.png \
  -o ./pitch_deck_output/visuals
```

Use these images as consistent backgrounds or hero visuals in your slides.

### 6. Typical Workflow

1. Activate the virtual environment.
2. Fill in `inputs/startup_brief.txt`.
3. Run the markdown deck command.
4. Optionally run the PDF and visuals commands.
5. Import markdown/PDF/images into your slide tool and tweak design.

For more details and advanced prompts, see `SKILL.md` in this directory.
