# Packaging Guide for Revelation

## Quick Start

### Build the shaderpack
```bash
python scripts/pack.py
```

Output: `Revelation.zip`

### With custom name or version
```bash
python scripts/pack.py --output MyShaderpack --version 1.0.0
```

## Installation

1. **Copy the ZIP file** to your Minecraft directory:
   - Windows: `%APPDATA%/.minecraft/shaderpacks/`
   - macOS: `~/Library/Application Support/minecraft/shaderpacks/`
   - Linux: `~/.minecraft/shaderpacks/`

2. **Launch Minecraft** with Iris Shaders mod (1.7.0+)

3. **Select the shaderpack** in Options → Shader Packs

## Requirements

- OpenGL 4.0+
- Iris Shaders 1.7.0 or newer
- Compatible mods (see README.md)

## Package Structure

The ZIP file contains:
```
shaders/              - All shader files (.fsh, .vsh, etc.)
README.md             - Documentation
LICENSE               - License information
```

## Development

Format shader files before packaging:
```bash
python scripts/format_shaders.py
```

Then create the package:
```bash
python scripts/pack.py
```

## Distribution

### GitHub Releases
1. Create a new release on GitHub
2. Upload `Revelation.zip` as an asset
3. Include compatibility notes and changelog

### Curseforge / Modrinth
- Upload the ZIP file directly
- Include:
  - Version number
  - Minecraft version (1.16+)
  - Iris Shaders requirement
  - Changelog
