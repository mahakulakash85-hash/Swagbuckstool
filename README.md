# 🔥 SWAGBUCKS AUTO FARM BOT 2026 - PRODUCTION READY

**Author:** mahakulakash85@gmail.com / Rohit@7657  
**Version:** 2.0 (2026 Edition - Fully Updated)  
**Status:** ✅ Production Ready

---

## 📋 Features

✅ **Undetected Mode** - selenium-stealth + CDP patches for stealth browsing  
✅ **2026 Selectors** - Updated XPaths for Videos, Search, Offers  
✅ **Real Balance Scraping** - Live SB balance from dashboard  
✅ **Proxy Rotation** - Support for rotating free/premium proxies  
✅ **Crash Recovery** - Auto-restart on detection  
✅ **Human-like Behavior** - Random delays, mouse movements, multiple user agents  
✅ **Live Dashboard** - Real-time metrics (SB/min, uptime, status)  
✅ **Comprehensive Logging** - All events logged to swagbucks_bot.log  
✅ **Google Colab Ready** - One-liner setup for cloud deployment  

---

## 🚀 Quick Start

### Local Setup (Windows/Mac/Linux)

```bash
# 1. Clone or download the bot
git clone https://github.com/yourusername/Swagbuckstool.git
cd Swagbuckstool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Update credentials
# Edit config.py and replace EMAIL and PASSWORD with your Swagbucks account

# 4. Run the bot
python main.py
```

### Google Colab Setup (Cloud - No Installation)

```python
# Copy this ONE-LINER into a Colab cell and run:
!git clone https://github.com/yourusername/Swagbuckstool.git && cd Swagbuckstool && pip install -r requirements.txt -q && python run.py
```

Or use the Colab notebook directly (if you have one).

---

## ⚙️ Configuration

### config.py - Update These Fields

```python
# Your Swagbucks credentials
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"

# Proxy list (optional, for rotation)
PROXIES = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
]

# Recovery settings
RECOVERY_INTERVAL = 60  # Auto-restart if inactive for 60 seconds
MAX_RETRIES = 3  # Login retry attempts
```

### keywords.txt

Pre-populated with 100+ common Swagbucks searches. Add more for higher search win rates.

---

## 📊 What the Bot Does

### 1. **Video Farming** 🎥
- Watches up to 15 videos per cycle
- ~2 SB per video
- Simulates human viewing behavior

### 2. **Search Farming** 🔍
- Performs up to 25 searches per cycle
- Claims search wins (~10 SB per win)
- Random keyword selection

### 3. **Offer Farming** 💰
- Clicks up to 8 offers per cycle
- ~5 SB per offer
- Auto-scrolls and human-like timing

### 4. **Real Balance Scraping** 📊
- Pulls actual SB balance from dashboard
- Shows in console output
- Logged for verification

### 5. **Crash Recovery** 🔄
- Detects inactivity (>60 seconds)
- Auto-restarts the bot
- Logs all recovery attempts

---

## 🛡️ Anti-Detection Features

✅ **Selenium Stealth** - Hides automation signals  
✅ **CDP Patches** - Overrides navigator.webdriver detection  
✅ **Random User Agents** - 2026 Chrome/Firefox versions  
✅ **Human-like Delays** - 2-15 second random waits  
✅ **Mouse Movements** - Simulates cursor movement  
✅ **Proxy Support** - Rotate IPs for safety  

---

## 📈 Expected Earnings

| Activity | SB/Unit | Units/Hour | Total/Hour |
|----------|---------|-----------|-----------|
| Videos | 2 | 15 | 30 SB |
| Searches | 10 | 10 | 100 SB |
| Offers | 5 | 8 | 40 SB |
| **Total** | - | - | **~170 SB/hour** |

*Note: Earnings vary by account age, region, and platform availability*

---

## 📝 Logs

All activity is logged to `swagbucks_bot.log`:

```
2026-02-25 10:30:45 - INFO - ✅ LOGIN SUCCESS - Dashboard loaded
2026-02-25 10:31:12 - INFO - 📺 Found 15 videos
2026-02-25 10:31:14 - INFO - 🎥 Video 1 | +2 SB | Total: 2
```

View logs in real-time:
```bash
tail -f swagbucks_bot.log
```

---

## 🔧 Troubleshooting

### Issue: "Login Failed"
**Solution:** 
- Check EMAIL and PASSWORD in config.py
- Ensure account is not locked
- Try logging in manually to verify credentials

### Issue: "No elements found"
**Solution:**
- Swagbucks UI may have changed
- Update SELECTORS in config.py
- Check website with DevTools (F12) for new selectors

### Issue: "Connection Refused" (Proxy)
**Solution:**
- Test proxy with: `curl -x http://proxy:port http://example.com`
- Use free proxy list: https://www.freeproxylists.net/
- Remove bad proxies from PROXIES list

### Issue: "Chrome driver not found"
**Solution:**
```bash
pip install webdriver-manager
python -m webdriver_manager.drivers.chrome
```

---

## 🚨 Important Notes

⚠️ **Use at Your Own Risk**
- Violates Swagbucks Terms of Service
- May result in account ban
- Use rotating proxies for safety
- Use a secondary/test account first
- Keep proxy IPs fresh and rotating

✅ **Best Practices**
- Run 2-4 hours per day (not 24/7)
- Use premium rotating proxies for production
- Monitor logs regularly
- Test on a secondary account first
- Update selectors if bot stops working

---

## 📦 Requirements

- Python 3.8+
- Chrome/Chromium browser
- 2GB+ RAM
- Stable internet connection
- Rotating proxies (recommended)

---

## 🎯 2026 Updates

✅ Updated XPaths for Swagbucks 2026 UI  
✅ Chrome 133+ compatibility  
✅ Selenium 4.20+ support  
✅ Selenium-stealth integration  
✅ Enhanced CDP patches  
✅ Real balance scraping  
✅ Crash recovery system  
✅ Google Colab support  

---

## 📞 Support

Issues or questions?
- Check the logs in `swagbucks_bot.log`
- Review troubleshooting section above
- Update selectors if Swagbucks UI changes
- Test credentials manually first

---

## 📜 License

MIT License - Use at your own discretion

---

## 🚀 Future Enhancements

- [ ] Dashboard web UI
- [ ] Email notifications
- [ ] Multi-account management
- [ ] Smart proxy rotation
- [ ] Advanced analytics
- [ ] Mobile app integration

---

**Happy Farming! 🌾💰**

*Last Updated: 2026-02-25*
