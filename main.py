#!/usr/bin/env python3
"""
🔥 SWAGBUCKS AUTO FARM BOT 2026 - PRODUCTION READY
mahakulakash85@gmail.com / Rohit@7657
Videos + Search + Offers + Real Balance Scrape + Crash Recovery
"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import time, random, logging, threading, json, os, sys, signal
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from config import EMAIL, PASSWORD, DELAYS, USER_AGENTS, SELECTORS, MAX_RETRIES, RETRY_DELAY, RECOVERY_INTERVAL, LOG_FILE
from datetime import datetime

# Logging setup
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

console = Console()
total_sb = 0
session_start = time.time()
crash_detected = False
last_activity = time.time()

def log_event(event):
    """Log to both console and file"""
    logger.info(event)
    console.print(f"[dim]{event}[/dim]")

def random_delay():
    """Human-like random delay"""
    delay = random.choice(DELAYS)
    time.sleep(delay)

def human_mouse_move(driver):
    """Simulate human mouse movement"""
    try:
        actions = driver.actions
        for _ in range(random.randint(2, 5)):
            actions.move_by_offset(random.randint(-50, 50), random.randint(-50, 50))
        actions.perform()
        time.sleep(random.uniform(0.2, 0.8))
    except:
        pass

def setup_driver(proxy=None):
    """Initialize undetected Chrome with anti-detect measures"""
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    
    # Proxy rotation
    if proxy:
        options.add_argument(f"--proxy-server={proxy}")
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    driver = uc.Chrome(options=options, version_main=None)
    
    # Apply selenium-stealth to avoid detection
    stealth(driver)
    
    # CDP patches for additional stealth
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {get: () => false});
            Object.defineProperty(navigator, 'plugins', {get: () => []});
            Object.defineProperty(navigator, 'languages', {get: () => ['en-US']});
            window.chrome = {runtime: {}};
        """
    })
    
    log_event("✅ Driver initialized with stealth mode")
    return driver

def login(driver, retry=0):
    """Login to Swagbucks with retry mechanism"""
    global last_activity
    try:
        driver.get("https://www.swagbucks.com")
        random_delay()
        
        # Find and fill email
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["login_email"]))
        )
        email_field.send_keys(EMAIL)
        random_delay()
        
        # Find and fill password
        password_field = driver.find_element(By.CSS_SELECTOR, SELECTORS["login_password"])
        password_field.send_keys(PASSWORD)
        random_delay()
        
        # Click submit
        submit_btn = driver.find_element(By.CSS_SELECTOR, SELECTORS["login_submit"])
        submit_btn.click()
        
        # Wait for dashboard
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["sb_balance"]))
        )
        
        last_activity = time.time()
        log_event("✅ LOGIN SUCCESS - Dashboard loaded")
        return True
        
    except Exception as e:
        log_event(f"❌ Login failed: {str(e)}")
        if retry < MAX_RETRIES:
            log_event(f"🔄 Retrying login ({retry+1}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)
            return login(driver, retry+1)
        return False

def scrape_sb_balance(driver):
    """Scrape real SB balance from dashboard"""
    try:
        balance_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["sb_balance"]))
        )
        balance_text = balance_element.text.strip()
        # Extract numeric value from text like "1,250 SB" or "1250"
        balance = ''.join(filter(str.isdigit, balance_text))
        return int(balance) if balance else 0
    except:
        return None

def farm_videos(driver):
    """Farm videos with updated 2026 selectors"""
    global total_sb, last_activity
    try:
        driver.get("https://www.swagbucks.com/videos")
        random_delay()
        
        videos = driver.find_elements(By.CSS_SELECTOR, SELECTORS["video_item"])
        log_event(f"📺 Found {len(videos)} videos")
        
        for i, video in enumerate(videos[:15]):  # 15 videos per session
            try:
                video.click()
                random_delay()
                human_mouse_move(driver)
                total_sb += 2
                last_activity = time.time()
                log_event(f"🎥 Video {i+1} | +2 SB | Total: {total_sb}")
            except Exception as e:
                log_event(f"⚠️ Video {i+1} failed: {str(e)}")
                continue
                
    except Exception as e:
        log_event(f"❌ Video farming error: {str(e)}")

def farm_searches(driver):
    """Farm search wins with retry logic"""
    global total_sb, last_activity
    try:
        if not os.path.exists("keywords.txt"):
            log_event("⚠️ keywords.txt not found")
            return
            
        with open("keywords.txt", "r") as f:
            keywords = [line.strip() for line in f if line.strip()]
        
        log_event(f"🔍 Starting search farming with {len(keywords)} keywords")
        
        for i, kw in enumerate(keywords[:25]):  # 25 searches per session
            try:
                driver.get(f"https://search.swagbucks.com/search?q={kw}")
                random_delay()
                
                # Try to claim search win
                try:
                    claim_btn = WebDriverWait(driver, 8).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, SELECTORS["search_win_btn"]))
                    )
                    claim_btn.click()
                    total_sb += 10
                    last_activity = time.time()
                    log_event(f"🎯 Search WIN {i+1} | +10 SB | Total: {total_sb}")
                except:
                    log_event(f"⏭️ Search {i+1} - no win")
                    
            except Exception as e:
                log_event(f"⚠️ Search {i+1} error: {str(e)}")
                continue
                
    except Exception as e:
        log_event(f"❌ Search farming error: {str(e)}")

def farm_offers(driver):
    """Farm offers - updated selectors"""
    global total_sb, last_activity
    try:
        driver.get("https://www.swagbucks.com/offers")
        random_delay()
        
        offers = driver.find_elements(By.CSS_SELECTOR, SELECTORS["offer_item"])
        log_event(f"💼 Found {len(offers)} offers")
        
        for i, offer in enumerate(offers[:8]):  # 8 offers per session
            try:
                offer.click()
                random_delay()
                total_sb += 5
                last_activity = time.time()
                log_event(f"💰 Offer {i+1} | +5 SB | Total: {total_sb}")
            except Exception as e:
                log_event(f"⚠️ Offer {i+1} error: {str(e)}")
                continue
                
    except Exception as e:
        log_event(f"❌ Offer farming error: {str(e)}")

def dashboard(update_interval=1):
    """Live dashboard with real-time metrics"""
    global total_sb, session_start, last_activity, crash_detected
    
    while not crash_detected:
        try:
            uptime = time.time() - session_start
            uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime))
            speed = total_sb / uptime * 60 if uptime > 0 else 0
            inactive_time = time.time() - last_activity
            
            # Crash detection
            if inactive_time > RECOVERY_INTERVAL:
                crash_detected = True
                log_event("🚨 CRASH DETECTED - Restarting...")
                break
            
            table = Table(title="⚡ SWAGBUCKS BOT 2026", show_header=True, header_style="bold magenta")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="green")
            table.add_row("💰 Total SB", f"{total_sb} SB")
            table.add_row("⏱️ Uptime", uptime_str)
            table.add_row("🚀 Speed", f"{speed:.1f} SB/min")
            table.add_row("⚙️ Status", "🟢 Active" if inactive_time < 30 else "🟡 Inactive")
            table.add_row("📝 Log File", LOG_FILE)
            
            with Live(table, refresh_per_second=1) as live:
                live.update(table)
            time.sleep(update_interval)
            
        except Exception as e:
            log_event(f"Dashboard error: {str(e)}")
            time.sleep(1)

def crash_recovery(driver):
    """Auto-restart on crash detection"""
    global crash_detected, total_sb
    
    while True:
        if crash_detected:
            log_event("🔄 Attempting crash recovery...")
            try:
                driver.quit()
            except:
                pass
            
            time.sleep(5)
            driver = setup_driver()
            
            if login(driver):
                crash_detected = False
                log_event("✅ Crash recovery successful!")
                return driver
            else:
                log_event("❌ Recovery failed, retrying...")
                time.sleep(RETRY_DELAY)
        else:
            time.sleep(1)

def signal_handler(sig, frame):
    """Handle graceful shutdown"""
    log_event("\n🛑 Shutting down gracefully...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    console.print("[bold magenta]🔥 SWAGBUCKS AUTO FARM BOT 2026[/bold magenta]")
    console.print("[dim]mahakulakash85@gmail.com | Production Ready[/dim]\n")
    
    driver = None
    try:
        driver = setup_driver()
        
        if not login(driver):
            console.print("[red]❌ Login failed. Check credentials.[/red]")
            sys.exit(1)
        
        # Dashboard thread
        dashboard_thread = threading.Thread(target=dashboard, daemon=True)
        dashboard_thread.start()
        
        # Crash recovery thread
        recovery_thread = threading.Thread(target=crash_recovery, args=(driver,), daemon=True)
        recovery_thread.start()
        
        cycle_count = 0
        while True:
            cycle_count += 1
            log_event(f"\n🔄 CYCLE {cycle_count} START")
            
            farm_videos(driver)
            farm_searches(driver)
            farm_offers(driver)
            
            # Scrape real balance
            real_balance = scrape_sb_balance(driver)
            if real_balance:
                log_event(f"📊 Real balance on Swagbucks: {real_balance} SB")
            
            cycle_sleep = random.randint(240, 360)  # 4-6 min between cycles
            log_event(f"😴 Sleeping {cycle_sleep}s before next cycle...")
            time.sleep(cycle_sleep)
            
    except KeyboardInterrupt:
        log_event("⏹️ Bot stopped by user")
    except Exception as e:
        log_event(f"💥 FATAL ERROR: {str(e)}")
        logger.exception(e)
    finally:
        if driver:
            try:
                driver.quit()
                log_event("✅ Driver closed")
            except:
                pass
        console.print("\n[yellow]📋 Check swagbucks_bot.log for details[/yellow]")
