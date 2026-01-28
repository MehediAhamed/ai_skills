---
name: pitch-deck-generator
description: "Use VLM Run (vlmrun) for pitch deck content and images, then python-pptx to produce actual slides. vlmrun generates markdown outlines, speaker notes, and visual assets; a Python script converts that markdown into .pptx pitch deck slides (and optionally PDF). VLMRUN_API_KEY must be in .env for vlmrun; use vlmrun for content and images only—never for PDF/slide file generation."
---

## Pitch Deck Generator (VLM Run + python-pptx)

Create investor-ready pitch decks by combining your startup inputs with VLM Run for **content and images**, then **python-pptx** for **slide files**.

**Important:** VLM Run does **not** generate PDF or slide files (`.pptx`, PDF, etc.).  
This skill uses two steps:
1. **vlmrun** → **Structured markdown** (slide titles, bullets, speaker notes) and **optional images** (logos, hero images, charts).
2. **python-pptx** (via a provided script) → **Actual slide deck** (`.pptx`) from that markdown; you can then export to PDF from PowerPoint/Keynote/Google Slides.

This skill guides you to:
- **Collect startup inputs** in a structured way
- **Optionally attach assets** (logo, product screenshots, charts, PDFs)
- **Call `vlmrun`** to generate:
  - Slide outline + titles (in markdown)
  - Bullet-point content per slide
  - Speaker notes
  - Visual/design suggestions
  - Optional generated images (logos, slide backgrounds)
- **Run the markdown→slides script** to produce a `.pptx` pitch deck from the markdown output
---

## How the assistant should use this skill

When this skill is invoked inside Cursor, the AI assistant must follow these rules **before and while** generating any pitch deck outputs:

- **Check `.env` for API key**
  - Look for a `.env` (or `.env.local`) file in the current workspace root.
  - Verify it contains a line for `VLMRUN_API_KEY=<your-key-here>`.
  - If the key is missing, empty, or clearly invalid, instruct the user to add/set `VLMRUN_API_KEY` in their `.env` and/or shell environment **before** running any `vlmrun` commands.

- **Use `vlmrun` for content and images only**
  - For **pitch deck markdown** (outline, bullets, speaker notes), **logos**, **slide visuals/backgrounds**, and other pitch-related **images**, the assistant must use the `vlmrun` CLI (with `VLMRUN_API_KEY` in `.env`).
  - **Do not** ask vlmrun to produce PDF or slide files—it cannot generate them. For **actual slides (`.pptx`)** or **PDF**, use the **python-pptx** script (see "Generating slides with python-pptx" below).
  - Whenever the user asks for:
    - A pitch deck **outline or markdown** → use `vlmrun` (confirm API key first).
    - A **logo** or **slide visuals/hero images** → use `vlmrun`.
    - **Slide deck (`.pptx`)** or **PDF** → run the markdown→slides script after vlmrun has produced the markdown.

- **Slides and PDF from a library, not vlmrun**
  - To produce **pitch deck slides** (`.pptx`) or **PDF**, the assistant must use the provided **python-pptx** script that reads the vlmrun-generated markdown and creates a presentation. The user can then export to PDF from PowerPoint/Keynote/Google Slides.
  - The assistant should **not** claim that vlmrun generates PDF or slide files.

---

## Prerequisites

Before starting, ensure you have:

- **Python 3.10 or higher** installed
- **Internet connection**
- **VLMRUN_API_KEY** (required for all `vlmrun` calls)
- **vlmrun CLI** installed (via `vlmrun[cli]`)
- **python-pptx** installed (for generating `.pptx` slide decks from markdown)

> You can also refer to the `vlmrun-cli-skill` for more detailed CLI usage.

---

## Installation & Setup

You can use either `uv` (recommended) or plain `pip`. Adjust commands for your OS.

### 1. Verify Python

**Windows (PowerShell):**

```powershell
python --version
# Should show Python 3.10.x or higher
```

**macOS/Linux:**

```bash
python3 --version
# Should show Python 3.10.x or higher
```

Install/upgrade Python if needed (see `python.org` or your package manager).

### 2. Install uv (Optional but Recommended)

**Windows (PowerShell):**

```powershell
pip install uv
```

**macOS/Linux:**

```bash
pip install uv
```

Verify:

```bash
uv --version
```

### 3. Create a Virtual Environment

From your skill directory (e.g. `~/.claude/skills/pitch-deck-generator` or this repo's `pitch-deck-generator` folder):

**Windows (PowerShell):**

```powershell
cd path\to\pitch-deck-generator
uv venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
cd path/to/pitch-deck-generator
uv venv
source .venv/bin/activate
```

You should see `(.venv)` in your prompt when activated.

### 4. Install `vlmrun` CLI

```bash
uv pip install "vlmrun[cli]"
```

Or, without `uv`:

```bash
pip install "vlmrun[cli]"
```

Verify:

```bash
vlmrun --version
```

### 5. Set `VLMRUN_API_KEY`

Follow the same pattern as in `vlmrun-cli-skill`:

**Windows (PowerShell):**

```powershell
$env:VLMRUN_API_KEY="your-api-key-here"
[System.Environment]::SetEnvironmentVariable('VLMRUN_API_KEY', 'your-api-key-here', 'User')
```

**macOS/Linux:**

```bash
export VLMRUN_API_KEY="your-api-key-here"
echo 'export VLMRUN_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

Check:

```bash
# Windows
echo $env:VLMRUN_API_KEY

# macOS/Linux
echo $VLMRUN_API_KEY
```

---

## Quick Start: One-Command Pitch Deck

Use this flow when you just want a **single command** that turns your startup description into a pitch deck outline + copy.

1. **Collect structured inputs from the user:**
   - Startup name
   - One-line description
   - Problem
   - Solution / Product
   - Market & TAM
   - Business model
   - Traction / metrics
   - Team
   - Ask (how much you’re raising, use of funds)

2. **Save these into a text file** (e.g. `inputs/startup_brief.txt`) using a simple template:

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

3. **Run `vlmrun` to generate the deck (markdown):**

```bash
vlmrun chat -p inputs/startup_brief.txt \
  "Turn this startup brief into a full investor pitch deck in markdown. 
Include: Title, Problem, Solution/Product, Market, Business Model, Traction, Competition, Go-To-Market, Team, Financials (if any), and Ask. 
For each slide, output:
- Slide title
- 3–6 bullet points
- Optional speaker notes
Return everything as well-structured markdown, grouped by slide, ready to paste into a PDF or presentation software." \
  -o ./pitch_deck_output
```

4. **Result:**
   - `pitch_deck_output/` will contain a **markdown file** with the full deck content (and optionally images if you requested them).
   - **Next:** Run the markdown→slides script (see "Generating slides with python-pptx" below) to produce a `.pptx` pitch deck from that markdown.

---

## Advanced Flow: Assets-Aware Pitch Deck

Use this when you have **logo, product screenshots, charts, or PDFs** you want the model to see while writing the deck.

### 1. Prepare Assets

Create a folder like `assets/` with:
- `logo.png` (or `logo.svg`)
- Product screenshots (`screenshot1.png`, `screenshot2.png`, …)
- Charts from metrics (`mrr_chart.png`, `growth_chart.png`, …)
- Optional: `one_pager.pdf`, `executive_summary.pdf`

### 2. Refine the Brief

Use `inputs/startup_brief.txt` as above, but keep it **concise and factual**. The images will provide visual context.

### 3. Call `vlmrun` with inputs

Example (add/remove `-i` flags depending on available assets):

```bash
vlmrun chat \
  "You are an expert startup pitch deck consultant. 
Using the attached images and the text brief, create a venture-scale pitch deck:
1. Define slide titles in a logical order.
2. For each slide, provide 3–6 concise bullets optimized for investor focus.
3. Add speaker notes for complex slides (problem, solution, traction, financials).
4. Suggest at least one visual idea per slide (e.g., chart, product screenshot, diagram).
Output strictly as markdown, grouped by slide, with clear headings (## Slide N: Title)." \
  -p inputs/startup_brief.txt \
  -i assets/logo.png \
  -i assets/screenshot1.png \
  -i assets/screenshot2.png \
  -i assets/mrr_chart.png \
  -o ./pitch_deck_output
```

### 4. Optional: Generate Slide Visuals (Images and Graphs)

Ask VLM Run to produce **hero images, slide backgrounds, or charts/graphs** that match your brand and data:

```bash
vlmrun chat \
  "Generate a cohesive set of hero images and slide backgrounds for this startup pitch deck. 
Style: modern, minimal, investor-friendly, with colors that match the logo. 
Return a small set of images (e.g. 5–8) that can be reused across the deck." \
  -i assets/logo.png \
  -o ./pitch_deck_output/visuals
```

For **charts or graphs** (e.g. traction, market size), ask vlmrun to generate images from your brief or data:

```bash
vlmrun chat \
  "From this startup brief, generate 3–5 chart images for a pitch deck: market size, growth curve, use-of-funds. 
Save each as a separate image (e.g. 1.png, 2.png, 3.png) in a clear, investor-ready style." \
  -p inputs/startup_brief.txt \
  -o ./pitch_deck_output/visuals
```

Then run the markdown→pptx script with `--images-dir pitch_deck_output/visuals` so those **vlmrun-generated images and graphs are embedded into the .pptx** (one image per slide by number: 1.png → slide 1, 2.png → slide 2, etc.). No need to manually assign images in PowerPoint/Keynote.

---

## Generating slides with python-pptx

VLM Run does **not** generate PDF or slide files. Use the **python-pptx** library via the provided script to turn the vlmrun-generated markdown into a real `.pptx` pitch deck.

### Install python-pptx

From the pitch-deck-generator directory with your venv activated:

```bash
uv pip install python-pptx
# or: pip install python-pptx
```

### Run the markdown→slides script

After vlmrun has produced a markdown deck (e.g. in `pitch_deck_output/`), run:

```bash
python scripts/markdown_to_pptx.py pitch_deck_output/VLM_Run_Pitch_Deck.md -o pitch_deck_output/deck.pptx
```

- **Input:** Path to the markdown file (vlmrun output with `# Slide N: Title`, bullets, and `---` separators).
- **Output:** A `.pptx` file you can open in PowerPoint, Keynote, or Google Slides. Export to PDF from there if needed.

**Include vlmrun-generated images and graphs in the pptx**

If you generated visuals with vlmrun (hero images, charts, graphs) into a folder (e.g. `pitch_deck_output/visuals`), pass that folder with `--images-dir`. The script will embed one image per slide by **slide number** (1-based). Supported filenames: `1.png`, `2.png`, `slide_1.png`, `image_1.png`, `01.png`, etc.

```bash
# Generate deck and embed images from pitch_deck_output/visuals (1.png → slide 1, 2.png → slide 2, …)
python scripts/markdown_to_pptx.py pitch_deck_output/VLM_Run_Pitch_Deck.md -o pitch_deck_output/deck.pptx --images-dir pitch_deck_output/visuals
```

**Windows (PowerShell):**

```powershell
python scripts/markdown_to_pptx.py .\pitch_deck_output\VLM_Run_Pitch_Deck.md -o .\pitch_deck_output\deck.pptx --images-dir .\pitch_deck_output\visuals
```

**macOS/Linux:**

```bash
python scripts/markdown_to_pptx.py pitch_deck_output/VLM_Run_Pitch_Deck.md -o pitch_deck_output/deck.pptx --images-dir pitch_deck_output/visuals
```

You can also reference images **inside the markdown** with `![](path/to/image.png)`; the script will embed that image on the corresponding slide (path relative to the markdown file).

The script parses the markdown (slide titles, subtitles, bullet points), optionally embeds images/graphs from vlmrun, and builds a presentation with one slide per section. For PDF: open the `.pptx` in your slide tool and use File → Export/Save as PDF.

---

## Slide Template Prompts (Reusable)

You can call `vlmrun` multiple times to iterate on specific sections.

### Problem & Solution Slides

```bash
vlmrun chat \
  "From this startup brief, write just the Problem and Solution slides. 
Each slide should have:
- A short, powerful title
- 3–5 bullets that are specific and measurable where possible
Avoid jargon; make it easy for a generalist investor." \
  -p inputs/startup_brief.txt \
  -o ./pitch_deck_output/problem_solution
```

### Traction & Metrics Slide

```bash
vlmrun chat \
  "From this startup brief and any attached charts, write a single Traction slide. 
Focus on concrete numbers, growth rates, and user behavior, framed for seed/Series A investors." \
  -p inputs/startup_brief.txt \
  -i assets/mrr_chart.png \
  -i assets/growth_chart.png \
  -o ./pitch_deck_output/traction
```

### Team Slide

```bash
vlmrun chat \
  "Write a Team slide that highlights why this team is uniquely positioned to win. 
Include 1–2 bullets per person with prior experience, domain expertise, and notable achievements." \
  -p inputs/startup_brief.txt \
  -o ./pitch_deck_output/team
```

---

## Workflow Checklist

- [ ] Confirm `vlmrun` is installed and `VLMRUN_API_KEY` is set.
- [ ] Collect structured startup info and save to `inputs/startup_brief.txt`.
- [ ] (Optional) Place logo, screenshots, charts, PDFs into `assets/`.
- [ ] Run the **Quick Start** command to generate a full pitch deck in markdown.
- [ ] (Optional) Generate images/graphs with vlmrun into a folder (e.g. `pitch_deck_output/visuals`).
- [ ] Install **python-pptx** and run **scripts/markdown_to_pptx.py** to produce a `.pptx` slide deck; use `--images-dir pitch_deck_output/visuals` to embed vlmrun-generated images and graphs into the pptx.
- [ ] Optionally refine individual sections (Problem/Solution, Traction, Team, Ask) with focused vlmrun calls.
- [ ] Open the `.pptx` in PowerPoint/Keynote/Google Slides; export to PDF if needed; adjust design/branding.

---

## Troubleshooting

- **`vlmrun` not found**
  - Ensure virtual environment is activated.
  - Reinstall: `uv pip install "vlmrun[cli]"`.
  - On Windows, check `where vlmrun`; on macOS/Linux, `which vlmrun`.

- **Authentication errors**
  - Verify `VLMRUN_API_KEY` is set in the current shell.
  - Make sure there are no extra quotes or spaces around the key.

- **Outputs are too long or too short**
  - Adjust your prompt to specify desired length (e.g. “max 6 bullets per slide”, “<= 15 slides total”).

- **Deck feels generic**
  - Add more concrete numbers and user stories to `startup_brief.txt`.
  - Attach real product screenshots and key metrics charts via `-i` flags.

---

## Example End-to-End Session

```bash
# 1) Activate environment
cd path/to/pitch-deck-generator
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows

# 2) Edit inputs/startup_brief.txt with your startup info

# 3) Generate full deck (markdown)
vlmrun chat -p inputs/startup_brief.txt \
  "Create a concise, VC-ready pitch deck (10–15 slides) with titles, bullets, speaker notes, and visual suggestions. Output as markdown." \
  -o ./pitch_deck_output

# 4) (Optional) Generate visuals (images/graphs) with vlmrun
vlmrun chat \
  "Generate 6 slide background images that match the brand and tone of this startup. Save as 1.png, 2.png, ... 6.png." \
  -i assets/logo.png \
  -o ./pitch_deck_output/visuals

# 5) Generate slides from markdown and embed vlmrun images/graphs (python-pptx)
python scripts/markdown_to_pptx.py pitch_deck_output/VLM_Run_Pitch_Deck.md -o pitch_deck_output/deck.pptx --images-dir pitch_deck_output/visuals
```

You now have a repeatable, VLM Run–powered pipeline for generating and iterating on startup pitch decks.

