#!/usr/bin/env python3
"""
Package Revelation shaderpack for distribution.

Creates a ZIP file suitable for Iris Shaders with proper structure.

Usage:
    python pack.py [--output NAME] [--version VERSION]
"""

import os
import sys
import shutil
import zipfile
import argparse
from datetime import datetime
from pathlib import Path


def get_version():
    """Try to get version from git tag or use timestamp."""
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'describe', '--tags', '--always'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(__file__)
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return datetime.now().strftime('%Y%m%d')


def create_shaderpack(output_name='Revelation', version=None):
    """Create the shaderpack ZIP file."""
    
    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Determine output path
    if not output_name.endswith('.zip'):
        output_name = f'{output_name}.zip'
    
    output_path = project_root / output_name
    
    # Files to include in the package
    include_files = [
        'shaders',
        'README.md',
        'LICENSE',
    ]
    
    # Verify required files exist
    missing = []
    for item in include_files:
        if not (project_root / item).exists():
            missing.append(item)
    
    if missing:
        print(f'❌ Missing files: {", ".join(missing)}')
        return False
    
    # Remove old package if exists
    if output_path.exists():
        output_path.unlink()
        print(f'🗑️  Removed old package: {output_name}')
    
    print(f'📦 Creating shaderpack: {output_name}')
    
    # Create ZIP file
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for item in include_files:
                item_path = project_root / item
                
                if item_path.is_dir():
                    # Add directory contents
                    for file_path in item_path.rglob('*'):
                        if file_path.is_file():
                            arcname = file_path.relative_to(project_root)
                            zf.write(file_path, arcname)
                            print(f'  ✓ {arcname}')
                else:
                    # Add single file
                    zf.write(item_path, item)
                    print(f'  ✓ {item}')
        
        file_size = output_path.stat().st_size / (1024 * 1024)
        print(f'\n✅ Success! Created: {output_name} ({file_size:.2f} MB)')
        
        if version:
            print(f'   Version: {version}')
        
        return True
        
    except Exception as e:
        print(f'❌ Error creating package: {e}')
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Package Revelation shaderpack for distribution'
    )
    parser.add_argument(
        '--output', '-o',
        default='Revelation',
        help='Output filename (default: Revelation.zip)'
    )
    parser.add_argument(
        '--version', '-v',
        help='Version string (default: git tag or timestamp)'
    )
    
    args = parser.parse_args()
    
    version = args.version or get_version()
    success = create_shaderpack(args.output, version)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
