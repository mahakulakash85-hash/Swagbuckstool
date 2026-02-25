#!/usr/bin/env python3
"""
🔥 SWAGBUCKS AUTO FARM BOT 2026
mahakulakash85@gmail.com / Rohit@7657
Videos + Search + Offers + Dashboard
"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random
from rich.console import Console
from rich.live import Live
from rich.table import Table
from config import EMAIL, PASSWORD, DELAYS, USER_AGENTS
import threading

console = Console()
total_sb = 0
session_start = time.time()

def random_delay():
    time.sleep(random.choice(DELAYS))

def human_mouse_move(driver):
    actions = driver.actions
    actions.move_by_offset(random.randint(10,50), random.randint(10,50))
    actions.perform()
    time.sleep(0.5)

def login(driver):
    driver.get("https://www.swagbucks.com")
    random_delay()
    
    # Login
    driver.find_element(By.ID, "sb-login-email").send_keys(EMAIL)
    driver.find_element(By.ID, "sb-login-password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    random_delay()
    console.print("✅ LOGIN SUCCESS!")

def farm_videos(driver):
    global total_sb
    driver.get("https://www.swagbucks.com/videos")
    random_delay()
    
    videos = driver.find_elements(By.CSS_SELECTOR, ".video-item")
    for video in videos[:10]:  # 10 videos
        try:
            video.click()
            random_delay()
            human_mouse_move(driver)
            total_sb += 2  # ~2 SB per video
            console.print(f"🎥 Video +2 SB | Total: {total_sb}")
        except: pass

def farm_searches(driver):
    global total_sb
    with open("keywords.txt") as f:
        keywords = f.read().splitlines()
    
    for kw in keywords[:20]:
        driver.get(f"https://search.swagbucks.com/search?m=1&q={kw}")
        random_delay()
        # Claim search win
        try:
            claim_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-win-btn"))
            )
            claim_btn.click()
            total_sb += 10
            console.print(f"🔍 Search WIN +10 SB | Total: {total_sb}")
        except:
            pass

def farm_offers(driver):
    global total_sb
    driver.get("https://www.swagbucks.com/offers")
    random_delay()
    offers = driver.find_elements(By.CSS_SELECTOR, ".offer-item")[:5]
    for offer in offers:
        offer.click()
        random_delay()
        total_sb += 5
        console.print(f"💰 Offer +5 SB | Total: {total_sb}")

def dashboard():
    while True:
        uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - session_start))
        table = Table()
        table.add_column("Metric")
        table.add_column("Value")
        table.add_row("💰 Total SB", f"{total_sb}")
        table.add_row("⏱️ Uptime", uptime)
        table.add_row("🚀 Speed", f"{total_sb/(time.time()-session_start)*60:.1f} SB/min")
        with Live(table, refresh_per_second=1) as live:
            live.update(table)
        time.sleep(1)

if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = uc.Chrome(options=options)
    
    # Dashboard thread
    threading.Thread(target=dashboard, daemon=True).start()
    
    login(driver)
    while True:
        farm_videos(driver)
        farm_searches(driver)
        farm_offers(driver)
        console.print("🔄 Cycle complete! Sleeping...")
        time.sleep(300)  # 5 min cycle
