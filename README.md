# The Rink Fast Chope
Use Selenium Webdriver for Chrome to unfollow inactive Twitter accounts in [Twitonomy.com](http://twitonomy.com/)

The repository [ozzie-eu/twitter-unfollow-inactive](https://github.com/ozzie-eu/twitter-unfollow-inactive) offers the same functionality, but it uses Twitter API instead. The advantage of using Twitter API is the speed, but there is a maximum request limitation within a period of time. This can be overcome by using webscraping in [Twitonomy.com](http://twitonomy.com/).

## Installation
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
