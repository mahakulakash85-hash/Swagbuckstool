#!/usr/bin/env python3
"""
🚀 GOOGLE COLAB LAUNCHER - ONE LINE INSTALLER
Run this in Google Colab with: !pip install -r requirements.txt && python run.py
"""
import os
import subprocess
import sys

def install_and_run():
    """Install dependencies and run the bot"""
    
    print("=" * 60)
    print("🔥 SWAGBUCKS BOT 2026 - COLAB SETUP")
    print("=" * 60)
    
    # Check if running in Colab
    try:
        from google.colab import drive
        print("\n✅ Google Colab detected!")
        
        # Mount Google Drive for persistence
        drive.mount('/content/drive')
        print("✅ Google Drive mounted")
        
        # Create bot directory in Drive
        bot_dir = '/content/drive/My Drive/SwagbucksBot'
        os.makedirs(bot_dir, exist_ok=True)
        os.chdir(bot_dir)
        print(f"✅ Working directory: {bot_dir}")
        
    except ImportError:
        print("\n⚠️ Not in Google Colab - Running locally")
    
    # Install requirements
    print("\n📦 Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"])
    print("✅ Dependencies installed")
    
    # Check for config
    if not os.path.exists("config.py"):
        print("\n⚠️ config.py not found!")
        print("Please update EMAIL and PASSWORD in config.py before running")
        return
    
    # Check for keywords
    if not os.path.exists("keywords.txt"):
        print("\n⚠️ keywords.txt not found!")
        print("Creating default keywords file...")
        with open("keywords.txt", "w") as f:
            f.write("""swagbucks
swagbucks videos
swagbucks search
swagbucks offers
free gift cards
amazon gift card
paypal cash
earn money online
watch videos earn money
daily poll swagbucks
swagbucks noso
swagbucks mobile
free swagbucks
survey swagbucks
swagbucks coupon
how to earn swagbucks
swagbucks hack
swagbucks bot
swagbucks tips
best swagbucks offers
swagbucks rewards
swagbucks tasks
swagbucks videos today
swagbucks search wins
swagbucks referral
swagbucks cash out
swagbucks withdrawal
swagbucks paypal
swagbucks amazon
swagbucks apps
swagbucks download
swagbucks login
swagbucks account
swagbucks registration
swagbucks verification
swagbucks support
swagbucks help
swagbucks faq
swagbucks blog
swagbucks news
swagbucks updates
swagbucks changes
swagbucks new offers
swagbucks daily deals
swagbucks flash offers
swagbucks limited time
swagbucks promo
swagbucks bonus
swagbucks special
swagbucks exclusive
swagbucks members
swagbucks points
swagbucks value
swagbucks earnings
swagbucks income
swagbucks passive
swagbucks quick
swagbucks easy
swagbucks fast
swagbucks simple
swagbucks tutorial
swagbucks guide
swagbucks how to
swagbucks strategy
swagbucks maximize
swagbucks optimize
swagbucks maximize earnings
swagbucks best way
swagbucks profitable
swagbucks high paying
swagbucks review
swagbucks reddit
swagbucks twitter
swagbucks facebook
swagbucks community
swagbucks forum
swagbucks discussion
swagbucks users
swagbucks members
swagbucks experienced
swagbucks expert
swagbucks professional
swagbucks advanced
""")
        print("✅ Default keywords created")
    
    print("\n" + "=" * 60)
    print("🚀 STARTING BOT IN 5 SECONDS...")
    print("=" * 60)
    print("\n⚠️ IMPORTANT:")
    print("1. Keep this tab open while bot runs")
    print("2. Check logs in swagbucks_bot.log")
    print("3. Monitor the console output")
    print("4. Press Ctrl+C to stop\n")
    
    import time
    for i in range(5, 0, -1):
        print(f"⏳ Starting in {i}...", end='\r')
        time.sleep(1)
    
    print("\n✅ Starting bot!\n")
    
    # Run the main bot
    os.system("python main.py")

if __name__ == "__main__":
    install_and_run()
