# ⚡ QUICK START GUIDE - 5 MINUTES TO FARMING

## 🚀 Option 1: Run Locally (Windows/Mac/Linux)

### Step 1: Install Python
Download Python 3.8+ from https://www.python.org/downloads/

### Step 2: Clone or Download Bot
```bash
git clone https://github.com/yourusername/Swagbuckstool.git
cd Swagbuckstool
```

### Step 3: Install Dependencies (1 minute)
```bash
pip install -r requirements.txt
```

### Step 4: Add Your Credentials (1 minute)
Edit `config.py`:
```python
EMAIL = "your_email@gmail.com"      # Your Swagbucks email
PASSWORD = "your_password"          # Your Swagbucks password
```

### Step 5: Run the Bot! (2 minutes)
```bash
python main.py
```

You should see:
```
🔥 SWAGBUCKS AUTO FARM BOT 2026
mahakulakash85@gmail.com | Production Ready

✅ Driver initialized with stealth mode
✅ LOGIN SUCCESS - Dashboard loaded
📺 Found 15 videos
🎥 Video 1 | +2 SB | Total: 2
...
```

---

## ☁️ Option 2: Run on Google Colab (Cloud - EASIEST)

### Step 1: Open Google Colab
Go to https://colab.research.google.com/

### Step 2: Create New Notebook
Click "New Notebook"

### Step 3: Paste This in a Cell
```python
!git clone https://github.com/yourusername/Swagbuckstool.git && cd Swagbuckstool && pip install -r requirements.txt -q && python run.py
```

### Step 4: Update Credentials in Colab
```python
# In a new cell:
with open('Swagbuckstool/config.py', 'w') as f:
    f.write("""
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
# ... rest of config
""")
```

### Step 5: Run!
Press Shift+Enter and watch it farm! ✅

---

## 📊 What to Expect

### First Run
- ✅ Login to Swagbucks
- ✅ Start farming videos (2-3 minutes)
- ✅ Start earning 50+ SB
- ✅ Check console for real-time updates

### Console Output
```
💰 Total SB: 47 SB
⏱️ Uptime: 00:02:15
🚀 Speed: 20.9 SB/min
⚙️ Status: 🟢 Active
```

### Log File
Check `swagbucks_bot.log` for detailed logs:
```bash
tail -f swagbucks_bot.log
```

---

## 🛑 How to Stop

Press `Ctrl+C` in terminal to stop gracefully.

---

## ⚠️ Important Safety Tips

1. **Test First** - Use a secondary Swagbucks account
2. **Monitor** - Watch the logs for errors
3. **Use Proxies** - Add proxies to config.py for safety
4. **Run Smart** - 2-4 hours/day (not 24/7)
5. **Check Balance** - Real balance shown in console

---

## 🔧 Troubleshooting (30 seconds)

### ❌ Error: "Login failed"
**Fix:** Update EMAIL and PASSWORD in config.py, then retry

### ❌ Error: "Chrome driver not found"
**Fix:** Run `pip install -r requirements.txt` again

### ❌ Error: "No videos found"
**Fix:** Swagbucks UI may have changed. Check selectors in config.py

### ❌ Bot stops after few minutes
**Fix:** Check swagbucks_bot.log for errors, may need proxy

---

## 📈 Expected Results

| Time | SB Earned |
|------|-----------|
| 1 hour | ~170 SB |
| 2 hours | ~340 SB |
| 4 hours | ~680 SB |

*Results vary by account, region, and offers available*

---

## ✅ Verification Checklist

- [x] Python 3.8+ installed
- [x] Requirements installed (`pip install -r requirements.txt`)
- [x] Email updated in config.py
- [x] Password updated in config.py
- [x] Bot runs without errors
- [x] Console shows "✅ LOGIN SUCCESS"
- [x] SB counter is increasing
- [x] Log file exists (swagbucks_bot.log)

---

## 📞 Quick Help

**Q: Is this safe?**
A: Use rotating proxies and a secondary account for safety

**Q: Will I get banned?**
A: Possibly - bot violates ToS. Use proxies and run smartly.

**Q: How much can I earn?**
A: ~170 SB/hour on average

**Q: Do I need proxies?**
A: Recommended for security. Free proxies work but premium is better.

**Q: Can I run on my phone?**
A: Not directly. Use Google Colab or cloud server.

---

## 🎯 Next Steps

1. ✅ Follow steps above to get running
2. ✅ Monitor logs for first 10 minutes
3. ✅ Add proxies to config.py (optional but recommended)
4. ✅ Set up log monitoring: `tail -f swagbucks_bot.log`
5. ✅ Schedule regular runs (2-4 hours/day)

---

## 🚀 Ready? Start Here:

**Local Users:** `python main.py`  
**Colab Users:** Paste & run the one-liner above

---

**Happy Farming! 💰🌾**

*Questions? Check README.md and CHANGELOG.md for more details*
