# Twitonomy Unfollow
Use Selenium Webdriver for Chrome to unfollow inactive Twitter accounts in [Twitonomy.com](http://twitonomy.com/)

The repository [ozzie-eu/twitter-unfollow-inactive](https://github.com/ozzie-eu/twitter-unfollow-inactive) offers the same functionality, but it uses Twitter API instead. The advantage of using Twitter API is the speed, but there is a maximum request limitation within a period of time. This can be overcome by using webscraping in [Twitonomy.com](http://twitonomy.com/).

## Installation
- Clone the repository using
```
git clone https://github.com/gordonjun2/twitonomy-unfollow.git
```
- Run
```
pip install -r requirements.txt
```

## Usage
- Type in Twitter credentials in `credentials.py`
- Choose inactive days cutoff value under 'Input Variables' in `twitonomy_unfollow.py`.
- Run
```
python twitonomy_unfollow.py
```
- If error occurs due to chromedriver issue, download the correct `chromedriver.exe` version [here](https://chromedriver.chromium.org/downloads) and replace the one in this directory. 
    - Note: I am using Windows, rename the `chromedriver_win32` folder and the path in `twitonomy_unfollow.py` accordingly to what you selected to download above.
