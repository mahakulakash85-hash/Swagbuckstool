#!/usr/bin/env python3
"""
✅ Swagbucks Bot Setup Checker
Verifies all dependencies, configs, and files before running
"""
import sys
import os
import subprocess
from pathlib import Path

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}")

def check_python():
    """Check Python version"""
    print("\n🐍 Checking Python version...")
    version = sys.version_info
    required = (3, 8)
    
    if version >= required:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} (Required: 3.8+)")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} (Required: 3.8+)")
        print("   Download: https://www.python.org/downloads/")
        return False

def check_files():
    """Check required files exist"""
    print("\n📁 Checking required files...")
    files = {
        "main.py": "Main bot script",
        "config.py": "Configuration file",
        "requirements.txt": "Dependencies list",
        "keywords.txt": "Search keywords",
        "README.md": "Documentation",
    }
    
    all_exist = True
    for file, desc in files.items():
        if os.path.exists(file):
            print(f"✅ {file:<20} - {desc}")
        else:
            print(f"❌ {file:<20} - {desc} (MISSING)")
            all_exist = False
    
    return all_exist

def check_packages():
    """Check required Python packages"""
    print("\n📦 Checking Python packages...")
    packages = {
        "undetected_chromedriver": "undetected-chromedriver",
        "selenium": "selenium",
        "selenium_stealth": "selenium-stealth",
        "requests": "requests",
        "bs4": "beautifulsoup4",
        "rich": "rich",
    }
    
    all_installed = True
    for import_name, package_name in packages.items():
        try:
            __import__(import_name)
            print(f"✅ {package_name:<30} - Installed")
        except ImportError:
            print(f"❌ {package_name:<30} - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def check_config():
    """Check configuration"""
    print("\n⚙️ Checking configuration...")
    try:
        import config
        
        checks = {
            "EMAIL": hasattr(config, 'EMAIL') and config.EMAIL and '@' in config.EMAIL,
            "PASSWORD": hasattr(config, 'PASSWORD') and config.PASSWORD and len(config.PASSWORD) > 0,
            "SELECTORS": hasattr(config, 'SELECTORS') and isinstance(config.SELECTORS, dict),
        }
        
        all_valid = True
        for key, valid in checks.items():
            if valid:
                if key == "PASSWORD":
                    print(f"✅ {key:<20} - Configured (hidden)")
                else:
                    print(f"✅ {key:<20} - Configured")
            else:
                print(f"❌ {key:<20} - INVALID or MISSING")
                all_valid = False
        
        return all_valid
        
    except Exception as e:
        print(f"❌ Error loading config.py: {str(e)}")
        return False

def check_chrome():
    """Check Chrome/Chromium installation"""
    print("\n🌐 Checking Chrome installation...")
    
    chrome_paths = [
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"✅ Chrome found at: {path}")
            return True
    
    print("⚠️ Chrome not found in standard locations")
    print("   The driver will auto-download Chrome if needed")
    return True

def check_keywords():
    """Check keywords file"""
    print("\n🔍 Checking keywords file...")
    if not os.path.exists("keywords.txt"):
        print("❌ keywords.txt not found!")
        return False
    
    with open("keywords.txt", "r") as f:
        keywords = [line.strip() for line in f if line.strip()]
    
    if len(keywords) > 0:
        print(f"✅ keywords.txt found ({len(keywords)} keywords)")
        return True
    else:
        print("❌ keywords.txt is empty!")
        return False

def install_packages():
    """Offer to install missing packages"""
    print("\n" + "="*60)
    response = input("Install missing packages? (y/n): ").strip().lower()
    
    if response == 'y':
        print("\n📥 Installing packages...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Packages installed successfully!")
            return True
        else:
            print(f"❌ Installation failed: {result.stderr}")
            return False
    
    return False

def main():
    """Run all checks"""
    print_header("🔥 SWAGBUCKS BOT 2026 - SETUP CHECKER")
    
    results = {
        "Python Version": check_python(),
        "Required Files": check_files(),
        "Configuration": check_config(),
        "Keywords File": check_keywords(),
        "Chrome Installation": check_chrome(),
    }
    
    # Check packages - offer install if missing
    print("\n📦 Checking Python packages...")
    packages_ok = check_packages()
    results["Python Packages"] = packages_ok
    
    if not packages_ok:
        if install_packages():
            results["Python Packages"] = True
    
    # Summary
    print_header("📋 SUMMARY")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for check, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{check:<25} {status}")
    
    print(f"\n{passed}/{total} checks passed")
    
    # Final verdict
    print_header("READY TO RUN?")
    
    if all(results.values()):
        print("\n✅ ALL CHECKS PASSED!")
        print("\n🚀 Ready to start farming:")
        print("   python main.py")
        return 0
    else:
        print("\n❌ Some checks failed. Fix issues above first.")
        print("\n📝 Common fixes:")
        print("   1. Install Python 3.8+: https://www.python.org/downloads/")
        print("   2. Install packages: pip install -r requirements.txt")
        print("   3. Update config.py with your email and password")
        print("   4. Check keywords.txt exists and has content")
        return 1

if __name__ == "__main__":
    sys.exit(main())
