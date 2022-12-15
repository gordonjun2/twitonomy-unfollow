try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait, Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options

    import random
    import time
    from bs4 import BeautifulSoup
    from credentials import email, username, password

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

### Access to UnTweeps Page ###
driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
url = 'https://www.twitonomy.com/following.php'
driver.get(url)

# Input Variables

# For 'inactive_days_cutoff', please only use the time period below (MUST FOLLOW the same format)
# 'Last 12 months' 
# 'Last 3 months'
# 'Last 30 days'
# 'Last 7 days' 
# 'Last 24 hours'
# 'Last hour' 
# 'N/A'

inactive_days_cutoff = 'Last 3 months'

# Automation here (do not need to change, unless UI changes)
start_time = time.time()

click_sign_in = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@alt='Sign in with Twitter']"))).click()
email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@name='session[username_or_email]']")))
email_input.send_keys(email)
password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@name='session[password]']")))
password_input.send_keys(password)
click_sign_in = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@value='Sign In']"))).click()

current_url = driver.current_url

if current_url.split('https://')[1].split('.')[0] == 'twitter':
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")))
    corpus = BeautifulSoup(driver.page_source, 'html.parser')
    text_box_unprocessed = corpus.find_all("span", {"class": "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})
    text_box_processed = text_box_unprocessed[0].get_text()
    if 'Sign in to Twitter' in text_box_processed:
        email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")))
        email_input.send_keys(email, Keys.ENTER)
        username_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")))
        username_input.send_keys(username, Keys.ENTER)
        password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")))
        password_input.send_keys(password, Keys.ENTER)
    else:
        password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")))
        password_input.send_keys(password, Keys.ENTER)

current_url = driver.current_url
while current_url.split('.')[1] != 'twitonomy':
    time.sleep(1)
    current_url = driver.current_url

WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='scanInfo']")))
click_last_tweet_sort = driver.execute_script('''document.querySelector("[aria-label='Last tweet: activate to sort column ascending']").click();''')

select_display_length = Select(driver.find_element_by_xpath("//*[@aria-controls='tableFriends']"))
select_display_length.select_by_value('100')

print('Unfollowing now...\n')

refresh_flag = 1

while refresh_flag == 1:
    time.sleep(3)
    unfollow_list = driver.find_elements(By.XPATH, "//tr[.//div[@class='friendTweetDate']//span[text()='" + inactive_days_cutoff + "']]//span[@class='btnUnFollow btn btn-mini btn-danger']")
    if len(unfollow_list) > 0:
        for unfollow in unfollow_list:
            driver.execute_script("arguments[0].click();", unfollow)
            time.sleep(1)
        driver.refresh()
    else:
        refresh_flag = 0

print("--- Done! Took %s seconds ---" % (time.time() - start_time))

# Close the browser manually