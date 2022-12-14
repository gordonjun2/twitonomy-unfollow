try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options

    import random
    import time

    chrome_options=Options()
    chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    # chrome_options.addArguments("--window-size=1920,1080")
    # chrome_options.addArguments("--start-maximized")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    # chrome_options.add_argument("window-size=1400,2100") 
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument('--disable-dev-shm-usage')
except:
    print("Please run 'pip install -r requirements.txt' to install the required modules before running again.\n")

### Access to The Rink Booking Page ###
driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
url = 'https://www.twitonomy.com/following.php'
driver.get(url)

# Automation here (do not need to change, unless UI changes)
valid_day_time_flag = 0
start_time = time.time()

xpath_unfollow = "//tr[.//td[text()='Last 12 months']]//span[@class='btnUnFollow btn btn-mini btn-danger']"

click_book_day = WebDriverWait(driver, random.uniform(1, 2)).until(EC.element_to_be_clickable((By.XPATH, xpath_unfollow))).click()

print("--- Done! Took %s seconds ---" % (time.time() - start_time))

# Click on 'Pay Now' yourself, and all the best!