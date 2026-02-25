# Swagbucks Config 2026 - Production Ready
EMAIL = "mahakulakash85@gmail.com"
PASSWORD = "Rohit@7657"

# Anti-detect User Agents (2026 Chrome versions)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
]

# Human-like delays (seconds)
DELAYS = [2, 3, 4, 5, 6, 8, 10, 12, 15]

# Proxy rotation - Free proxies (replace with premium for production)
PROXIES = [
    # Format: "http://ip:port" or "http://user:pass@ip:port"
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
    # Add more proxies here
]

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5

# Crash recovery
RECOVERY_INTERVAL = 60  # Auto-restart every 60 seconds if crash detected
LOG_FILE = "swagbucks_bot.log"

# 2026 Updated Selectors for Swagbucks
SELECTORS = {
    "login_email": "#sb-login-email",
    "login_password": "#sb-login-password",
    "login_submit": "button[type='submit']",
    "video_item": ".video-item, .watch-video-item, [data-testid='video-card']",
    "video_play": "button.play-btn, [data-testid='play-button']",
    "search_win_btn": ".search-win-btn, button[data-testid='claim-button']",
    "offer_item": ".offer-item, [data-testid='offer-card']",
    "sb_balance": "#sb-balance, [data-testid='user-balance']",
    "dashboard_link": "a[href='/dashboard']",
}
