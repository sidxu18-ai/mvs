#!/usr/bin/env python3
"""
FFmpeg Installer and Setup Script for Windows
"""

import os
import sys
import subprocess
import requests
import zipfile
from pathlib import Path
import tempfile

def check_ffmpeg():
    """Check if FFmpeg is already available."""
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ FFmpeg is already installed and accessible!")
            return True
    except FileNotFoundError:
        pass
    
    print("❌ FFmpeg not found in PATH")
    return False

def install_ffmpeg_portable():
    """Download and install portable FFmpeg."""
    try:
        print("📥 Downloading portable FFmpeg...")
        
        # Create ffmpeg directory
        ffmpeg_dir = Path("ffmpeg")
        ffmpeg_dir.mkdir(exist_ok=True)
        
        # Download URL for FFmpeg essentials build
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp_file:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    tmp_file.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r⏳ Downloading: {percent:.1f}%", end="", flush=True)
            
            print("\n📦 Extracting FFmpeg...")
            
            with zipfile.ZipFile(tmp_file.name, 'r') as zip_ref:
                # Extract to temporary location first
                extract_path = Path(tmp_file.name).parent / "ffmpeg_extract"
                zip_ref.extractall(extract_path)
                
                # Find the extracted folder (usually has version in name)
                extracted_folders = list(extract_path.glob("ffmpeg-*"))
                if extracted_folders:
                    extracted_folder = extracted_folders[0]
                    bin_folder = extracted_folder / "bin"
                    
                    if bin_folder.exists():
                        # Copy to our ffmpeg directory
                        import shutil
                        if (ffmpeg_dir / "bin").exists():
                            shutil.rmtree(ffmpeg_dir / "bin")
                        shutil.copytree(bin_folder, ffmpeg_dir / "bin")
                        
                        print(f"✅ FFmpeg installed to: {ffmpeg_dir.absolute()}")
                        
                        # Add to current session PATH
                        bin_path = str((ffmpeg_dir / "bin").absolute())
                        current_path = os.environ.get("PATH", "")
                        if bin_path not in current_path:
                            os.environ["PATH"] = f"{bin_path};{current_path}"
                            print("✅ Added FFmpeg to current session PATH")
                        
                        return True
        
        print("❌ Failed to extract FFmpeg properly")
        return False
        
    except Exception as e:
        print(f"❌ Error installing FFmpeg: {e}")
        return False

def main():
    """Main installation function."""
    print("🎬 FFmpeg Setup for AI Math Video Generator")
    print("=" * 50)
    
    if check_ffmpeg():
        return True
    
    print("\n🔧 Installing portable FFmpeg...")
    
    if install_ffmpeg_portable():
        print("\n🎉 FFmpeg installation completed!")
        print("✅ You can now generate videos with the Math Video Generator")
        return True
    else:
        print("\n💡 Alternative installation methods:")
        print("   1. winget install Gyan.FFmpeg")
        print("   2. Download from https://ffmpeg.org/download.html")
        print("   3. Use Chocolatey: choco install ffmpeg")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️ Installation cancelled by user")
        sys.exit(1)
