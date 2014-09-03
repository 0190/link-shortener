# Link Shortener

Basic web application to make your links \"shorter\". Written in Python using [Flask](http://flask.pocoo.org/) and tested with [Selenium WebDriver](http://docs.seleniumhq.org/projects/webdriver/).

The latest version is deployed on [Heroku](http://heroku.com) and is available by [http://short-0190.herokuapp.com/](http://short-0190.herokuapp.com/).

## How to run locally

```
git clone https://github.com/0190/link-shortener.git

cd link-shortener

pip install -r requirements.txt

python link_shortener.py

```

Then go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Tests

To run tests, you will need [Firefox](http://firefox.com/). Once you make sure you have it, do the following:

```
cd test/

pip install -r requirements.txt

python test.py

```