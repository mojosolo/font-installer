# Font Installer Assistant 🎨

A simple tool to help download and install fonts from various sources by opening them in organized groups in Chrome.

## Features

- Groups font URLs by provider (Adobe, Google Fonts, DaFont, etc.)
- Opens URLs in Chrome in organized batches
- Provides step-by-step guidance for font installation
- Supports multiple font providers:
  - Adobe Fonts
  - Google Fonts
  - DaFont
  - MyFonts
  - Envato Elements

## Requirements

- Python 3.8+
- Google Chrome browser
- macOS, Linux, or Windows

## Quick Start

1. Run the installation script:

```bash
./install.sh
```

2. Run the font installer:

```bash
python src/install_fonts.py
```

3. Paste your font URLs (one per line)
4. Press Enter twice when done
5. Follow the prompts to open and download fonts

## Usage Tips

1. The tool will open URLs in groups based on their source
2. After each group opens in Chrome:
   - Download the fonts
   - Press Enter to continue to the next group
3. Once downloaded, place font files in:
   - macOS: ~/Library/Fonts/
   - Windows: C:\Windows\Fonts\
   - Linux: ~/.local/share/fonts/

## Troubleshooting

- If Chrome doesn't open, ensure it's installed and accessible from the command line
- Allow pop-ups in Chrome when prompted
- For Adobe Fonts, use Creative Cloud desktop app
- For paid fonts (MyFonts, Envato), purchase required 