# AI Skill Index

A curated collection of AI-powered workflows and skills that can be used with Claude AI assistants, Antigravity, and other AI agent platforms. Each skill is a self-contained module with scripts, documentation, and examples for specific use cases.

## 📋 Overview

This repository contains modular AI skills that combine various APIs, tools, and AI services to solve real-world tasks. Each skill folder includes:

- **README.md** - Comprehensive documentation with installation, usage, and examples
- **SKILL.md** - Agent-facing documentation for AI assistants like Claude
- **scripts/** - Executable Python scripts for the workflow
- **references/** - API documentation and technical references

## 🚀 Quick Start

### Using with Claude AI

Claude can automatically detect and use skills from this repository. When a user requests a task that matches a skill's description, Claude will:

1. Read the skill's `SKILL.md` file for instructions
2. Execute the appropriate scripts
3. Guide the user through the workflow

**Example:**
```
User: "Create a travel brochure for Paris"
Claude: [Automatically uses travel-destination-brochure skill]
```

### Using with Antigravity

Antigravity can navigate to skill directories and execute scripts directly:

1. Navigate to the skill folder: `cd skill-name/`
2. Follow the installation steps in the skill's README
3. Run the provided scripts with your parameters

**Example:**
```bash
cd travel-destination-brochure/
uv run scripts/simple_travel_brochure.py --city "Paris, France"
```

## 📚 Available Skills

| Workflow | Description |
|----------|-------------|
| [Travel Destination Brochure](travel-destination-brochure/README.md) | Build travel destination scenarios and brochures from a city name. Fetches street-level and landmark imagery from OpenStreetCam and Wikimedia Commons, then uses VLM Run (vlmrun) to generate a travel video and a travel plan. **Use with Claude:** Reference the `travel-destination-brochure` skill when users want travel brochures, destination guides, travel videos, or travel planning for a city. **Use with Antigravity:** Navigate to `travel-destination-brochure/` and run `uv run scripts/simple_travel_brochure.py --city "City Name"`. |
| [YouTube Transcription Generator](youtube-transcription-generator/README.md) | Generate transcriptions from YouTube videos using VLM Run (vlmrun). Downloads the video with yt-dlp, then transcribes with vlmrun (optional timestamps). **Use with Claude:** Reference the `youtube-transcription-generator` skill when users want YouTube transcriptions, video captions, or speech-to-text from YouTube. **Use with Antigravity:** Navigate to `youtube-transcription-generator/` and run `python scripts/run_transcription.py "<youtube_url>" -o ./output`. |

## 🛠️ Prerequisites

Most skills require:

- **Python 3.10+** - Check with `python --version` or `python3 --version`
- **uv package manager** - Install with `pip install uv` or use the official installer
- **Internet connection** - Required for API calls and downloads
- **API keys** - Some skills require API keys (check individual skill READMEs)

### Installing uv

**Windows (PowerShell):**
```powershell
pip install uv
# Or using installer
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
pip install uv
# Or using installer
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 📖 How to Use a Skill

### Step 1: Choose a Skill

Browse the table above to find a skill that matches your needs. Click the link to view detailed documentation.

### Step 2: Read the Skill's README

Each skill has comprehensive documentation including:
- Installation instructions
- Prerequisites and API key setup
- Usage examples
- Troubleshooting guides

### Step 3: Install Dependencies

Most skills use `uv` for dependency management. Navigate to the skill folder and install:

```bash
cd skill-name/
uv pip install -r requirements.txt
# Or follow the skill-specific installation instructions
```

### Step 4: Configure Environment

Set up any required VLM Run API keys or environment variables:

```bash
# Windows PowerShell
$env:API_KEY="your-key-here"

# macOS/Linux
export API_KEY="your-key-here"
```

### Step 5: Run the Skill

Execute the provided scripts according to the skill's documentation:

```bash
uv run scripts/script_name.py --parameters
```

## 🔧 Adding a New Skill

To contribute a new skill to this repository:

### 1. Create Skill Folder Structure

```
skill-name/
├── README.md          # User-facing documentation
├── SKILL.md           # Agent-facing documentation
├── .env_template      # Template for environment variables
├── requirements.txt   # Python dependencies (optional, can use PEP 723)
├── scripts/           # Executable Python scripts
│   └── main_script.py
└── references/        # API docs and technical references (optional)
    └── api_reference.md
```

### 2. Write Documentation

**README.md** should include:
- Overview and features
- Prerequisites
- Installation steps
- Usage examples
- Troubleshooting
- API references

**SKILL.md** should include:
- Skill metadata (name, description)
- Installation steps for agents
- Step-by-step workflow
- Script references
- Checklist for complete runs

### 3. Add to Main Index

Add your skill to the table in this README.md:

```markdown
| [Your Skill Name](skill-name/README.md) | Brief description. **Use with Claude:** When to use. **Use with Antigravity:** Command to run. |
```

### 4. Follow Best Practices

- Use `uv` for dependency management
- Include PEP 723 inline script metadata when possible
- Provide both simple and advanced usage examples
- Document all required API keys
- Include error handling and troubleshooting
- Test with multiple scenarios

## 📁 Project Structure

```
skill/
├── README.md                          # This file - main index
├── .gitignore                         # Git ignore rules
├── travel-destination-brochure/       # 
├── pitch-deck-generator/
```

## 🤝 Contributing

Contributions are welcome! When adding a new skill:

1. **Fork the repository**
2. **Create your skill folder** following the structure above
3. **Write comprehensive documentation** (README.md and SKILL.md)
4. **Test thoroughly** with multiple scenarios
5. **Add to the main index** table
6. **Submit a pull request**

### Skill Requirements

- ✅ Self-contained and modular
- ✅ Well-documented (README.md + SKILL.md)
- ✅ Uses `uv` for dependency management
- ✅ Includes error handling
- ✅ Provides clear examples
- ✅ Lists all prerequisites and API keys

## 🔗 Resources

### Tools and Services

- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer and resolver
- **[VLM Run](https://vlm.run)** - Visual AI agent platform
- **[OpenStreetCam](https://openstreetcam.org/)** - Street-level imagery
- **[Wikimedia Commons](https://commons.wikimedia.org/)** - Free media repository

### Documentation

- [Python PEP 723](https://peps.python.org/pep-0723/) - Inline script metadata
- [Claude Skills Documentation](https://docs.anthropic.com/) - AI agent integration
- [Antigravity Documentation](https://antigravity.ai/) - AI workflow platform

## 📝 License

Each skill may have its own license. Please check individual skill folders for license information. Skills using public APIs should respect:

- API terms of service
- Rate limits and usage policies
- Attribution requirements
- Data usage restrictions

## 🐛 Troubleshooting

### Common Issues

**Python not found:**
- Windows: Use `py` instead of `python`, or add Python to PATH
- macOS/Linux: Use `python3` instead of `python`

**uv command not found:**
- Restart terminal after installation
- Check PATH: `echo $PATH` (macOS/Linux) or `$env:PATH` (Windows)

**Script execution errors:**
- Verify Python version: `python --version` (should be 3.10+)
- Check dependencies: `uv pip list`
- Ensure you're in the correct directory
- Review the skill's troubleshooting section

**API key issues:**
- Verify environment variables are set correctly
- Check API key format and validity
- Review API documentation for rate limits

For skill-specific issues, refer to the individual skill's README.md troubleshooting section.

## 📧 Support

For issues, questions, or contributions:

1. Check the skill's README.md for troubleshooting
2. Review the skill's SKILL.md for agent usage
3. Open an issue in the repository
4. Check existing issues for similar problems

---

**Happy Building! 🚀**
