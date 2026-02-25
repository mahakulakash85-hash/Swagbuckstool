# 🚀 DEPLOYMENT GUIDE - Swagbucks Bot 2026

Complete guide for deploying and running the bot in different environments.

---

## 📋 Pre-Deployment Checklist

Before deploying anywhere, verify:

- [ ] Python 3.8+ installed (if running locally)
- [ ] All files in repository
- [ ] requirements.txt unchanged
- [ ] config.py updated with credentials
- [ ] Test account created (secondary account recommended)
- [ ] Internet connection stable
- [ ] 2GB+ RAM available
- [ ] Storage space for logs

Run setup checker:
```bash
python setup_check.py
```

---

## 🖥️ LOCAL DEPLOYMENT (Windows/Mac/Linux)

### Prerequisites
- Python 3.8 or higher
- Chrome or Chromium browser
- 2GB RAM minimum
- Stable internet

### Installation Steps

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/Swagbuckstool.git
cd Swagbuckstool
```

#### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Update Configuration
Edit `config.py`:
```python
EMAIL = "your_swagbucks_email@gmail.com"
PASSWORD = "your_swagbucks_password"

# Optional: Add proxies
PROXIES = [
    "http://proxy1:port",
    "http://proxy2:port",
]
```

#### 5. Verify Setup
```bash
python setup_check.py
```

#### 6. Run Bot
```bash
python main.py
```

### Managing Long-Running Process

#### Windows (Task Scheduler)
```batch
# Create a batch file: run_bot.bat
@echo off
cd C:\path\to\Swagbuckstool
python main.py
pause
```

Schedule it in Windows Task Scheduler to run daily.

#### Mac/Linux (Cron)
```bash
# Add to crontab
crontab -e

# Run at 9 AM daily
0 9 * * * cd /path/to/Swagbuckstool && python main.py >> logs.txt 2>&1
```

#### Mac/Linux (Background with nohup)
```bash
nohup python main.py > bot.log 2>&1 &
```

---

## ☁️ GOOGLE COLAB DEPLOYMENT

### Advantages
- ✅ Free cloud computing
- ✅ No local setup needed
- ✅ Automatic GPU available
- ✅ Persistent storage via Google Drive
- ✅ 12-hour session limit (but can resume)

### Setup Steps

#### 1. Open Google Colab
https://colab.research.google.com/

#### 2. Create New Notebook
Click "New Notebook"

#### 3. Cell 1: Install and Setup
```python
# Install dependencies
!pip install -r requirements.txt -q
!git clone https://github.com/yourusername/Swagbuckstool.git

# Setup Google Drive for persistence
from google.colab import drive
drive.mount('/content/drive')

# Create bot directory
import os
os.makedirs('/content/drive/My Drive/SwagbucksBot', exist_ok=True)
os.chdir('/content/drive/My Drive/SwagbucksBot')
```

#### 4. Cell 2: Update Configuration
```python
config_content = """
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
PROXIES = []
# ... rest of config
"""

with open('config.py', 'w') as f:
    f.write(config_content)
```

#### 5. Cell 3: Run Bot
```python
!python main.py
```

### Keeping Colab Session Alive
```javascript
// Paste in browser console (F12) to prevent timeout
function ClickConnect(){
  console.log("Clicking on connect button...");
  document.querySelector("colab-connect-button").click();
}

setInterval(ClickConnect, 60000);
```

### Accessing Logs in Google Drive
Logs are saved to Google Drive at:
```
My Drive/SwagbucksBot/swagbucks_bot.log
```

---

## 🐳 DOCKER DEPLOYMENT

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    chromium-browser \
    chromium-chromedriver \
    && rm -rf /var/lib/apt/lists/*

# Copy bot files
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN useradd -m -u 1000 bot && chown -R bot:bot /app
USER bot

# Run bot
CMD ["python", "main.py"]
```

### Build and Run
```bash
# Build image
docker build -t swagbucks-bot .

# Run container
docker run -it swagbucks-bot

# Run with volume for logs
docker run -it -v $(pwd)/logs:/app/logs swagbucks-bot

# Run in background
docker run -d --name swagbucks-bot swagbucks-bot
```

---

## 🖥️ VPS/SERVER DEPLOYMENT

### Recommended VPS Providers
- DigitalOcean ($4-6/month)
- Linode
- AWS EC2 (free tier available)
- Google Cloud (free tier available)

### Setup on Ubuntu 20.04 LTS

#### 1. SSH into Server
```bash
ssh root@your_vps_ip
```

#### 2. Update System
```bash
apt update && apt upgrade -y
```

#### 3. Install Dependencies
```bash
apt install -y python3.11 python3-pip chromium-browser git
```

#### 4. Clone Repository
```bash
git clone https://github.com/yourusername/Swagbuckstool.git
cd Swagbuckstool
```

#### 5. Install Python Packages
```bash
pip3 install -r requirements.txt
```

#### 6. Update Config
```bash
nano config.py
# Edit with nano editor
```

#### 7. Create Systemd Service
```bash
sudo tee /etc/systemd/system/swagbucks.service > /dev/null << EOF
[Unit]
Description=Swagbucks Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/Swagbuckstool
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
```

#### 8. Start Service
```bash
systemctl daemon-reload
systemctl start swagbucks
systemctl enable swagbucks
```

#### 9. Monitor
```bash
systemctl status swagbucks
tail -f swagbucks_bot.log
```

---

## 🔒 SECURITY BEST PRACTICES

### 1. Use Secondary Account
- Test bot on non-primary account first
- Reduces risk of main account ban

### 2. Use Proxies
```python
# In config.py
PROXIES = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
    "http://proxy3.example.com:8080",
]
```

**Free Proxy Sources:**
- https://www.freeproxylists.net/
- https://free-proxy-list.com/
- https://www.proxy-list.download/

**Premium Proxy Services:**
- Bright Data ($100+/month)
- Oxylabs (rotating proxies)
- Smartproxy ($5.5+/month)

### 3. Rotate Run Times
```python
# Don't run 24/7 - bot gets detected
# Best: 2-4 hours per day
# Randomize: 10 AM, 3 PM, 7 PM
```

### 4. Monitor Account
- Check Swagbucks account daily for restrictions
- Watch logs for errors
- Monitor earning rate for drops

### 5. Protect Credentials
- Never commit credentials to GitHub
- Use environment variables in production:

```python
import os

EMAIL = os.getenv("SWAGBUCKS_EMAIL")
PASSWORD = os.getenv("SWAGBUCKS_PASSWORD")
```

### 6. Log Analysis
```bash
# Check for errors
grep -i "error\|failed" swagbucks_bot.log

# Monitor activity
tail -f swagbucks_bot.log | grep "SB"

# Archive old logs
gzip swagbucks_bot.log.$(date +%Y%m%d)
```

---

## 📊 MONITORING & MAINTENANCE

### Daily Tasks
- [ ] Check logs for errors
- [ ] Verify SB is being earned
- [ ] Monitor account for restrictions
- [ ] Check bot is running

### Weekly Tasks
- [ ] Review average earnings
- [ ] Test with new selectors if needed
- [ ] Backup logs
- [ ] Update proxy list if using free proxies

### Monthly Tasks
- [ ] Analyze earnings trends
- [ ] Check for Swagbucks UI changes
- [ ] Update selectors if needed
- [ ] Clean old log files

### Log Rotation (Linux)
```bash
# Create logrotate config
sudo tee /etc/logrotate.d/swagbucks > /dev/null << EOF
/root/Swagbuckstool/swagbucks_bot.log {
  daily
  rotate 7
  compress
  delaycompress
  missingok
  notifempty
  create 0640 root root
}
EOF
```

---

## 🔧 TROUBLESHOOTING DEPLOYMENT

### Issue: "Chrome not found"
```bash
# Install Chrome
sudo apt-get install chromium-browser

# Or let undetected-chromedriver handle it
pip install --upgrade webdriver-manager
```

### Issue: "Permission denied"
```bash
# Make files executable
chmod +x main.py run.py setup_check.py
```

### Issue: "Proxy connection failed"
```bash
# Test proxy
curl -x http://proxy:port http://example.com

# Remove bad proxy from config.py
```

### Issue: "Bot stops randomly"
```bash
# Check logs
tail -100 swagbucks_bot.log

# May need:
# 1. Update selectors (Swagbucks changed UI)
# 2. Add proxy (IP blocked)
# 3. Wait (temporary rate limit)
```

---

## 📈 SCALING UP

### Multi-Account Setup
```bash
# Clone config for each account
cp config.py config_account1.py
cp config.py config_account2.py

# Edit each config with different credentials
nano config_account1.py
nano config_account2.py

# Create launch script
```

```python
# launch_multiple.py
import subprocess
import time

accounts = [
    ("account1", "config_account1.py"),
    ("account2", "config_account2.py"),
]

for name, config in accounts:
    print(f"Starting {name}...")
    # Start bot with specific config
    subprocess.Popen([
        "python", "main.py",
        "--config", config
    ])
    time.sleep(30)  # Stagger starts
```

---

## 📞 SUPPORT & HELP

- Check `swagbucks_bot.log` for errors
- Review `README.md` troubleshooting section
- Check selectors if bot stops
- Verify credentials work manually
- Test on secondary account first

---

**Happy Farming! 🌾💰**

*Last Updated: 2026-02-25*
