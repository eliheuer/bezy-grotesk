# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Bezy Grotesk is a bilingual font family supporting Latin and Arabic scripts. This is a font development repository containing UFO source files, a variable font designspace, and specimen generation tools.

## Repository Structure

- `sources/` - UFO font source files and designspace
  - `bezy-grotesk-regular.ufo/` - Regular weight master
  - `bezy-grotesk-bold.ufo/` - Bold weight master  
  - `bezy-grotesk.designspace` - Variable font definition (Weight axis: 400-700)
- `fonts/` - Compiled font files (.ttf, .woff2)
- `images/` - Marketing materials and specimen images
  - `alpha/` - Contains Python scripts for generating font specimens using DrawBot

## Font Architecture

The font is designed as a variable font with:
- **Weight axis**: 400 (Regular) to 700 (Bold)
- **Four instances defined**: Regular (400), Medium (500), SemiBold (600), Bold (700)
- **Script support**: Latin and Arabic with extensive Arabic contextual forms
- **OpenType features**: Comprehensive Arabic shaping (init, medi, fina, rlig, ccmp)

## Font Development Commands

**Note**: This repository does not contain build scripts. To compile fonts from sources:

```bash
# Install fontmake if not present
pip install fontmake

# Generate all instances from designspace
fontmake -m sources/bezy-grotesk.designspace

# Generate single master
fontmake -u sources/bezy-grotesk-regular.ufo

# Generate variable font
fontmake -m sources/bezy-grotesk.designspace --output-format variable
```

## Specimen Generation

Generate marketing/specimen images using the Python scripts:

```bash
# Generate Arabic specimen
python images/alpha/001.py --output specimen-arabic.png

# Generate Latin character set
python images/alpha/002.py --output specimen-latin.png
```

These require DrawBot, fontTools, and pytweening dependencies.

## Key UFO Components

- `glyphs/` - Individual glyph files (.glif) for Latin and Arabic characters
- `features.fea` - OpenType feature definitions (Arabic contextual alternates)
- `fontinfo.plist` - Font metadata (family name, weights, metrics)
- `kerning.plist` - Kerning pairs
- `groups.plist` - Glyph classes for kerning and features

## Arabic Script Implementation

The font includes comprehensive Arabic support with:
- Contextual forms: isolated, initial (.init), medial (.medi), final (.fina)
- Ligatures: lam-alef combinations with various diacritics
- Diacritic positioning: fatha, damma, kasra, shadda, etc.
- Complex mark-to-mark positioning for stacked diacritics