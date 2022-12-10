# Web-Scraping Glassdoor Interview

Web Scraping with BeautifulSoup and Selenium. Get interview information, interview questions, offer status, experience, and etc for Data Analyst role specifically from Glassdoor. Few top tier companies are selected for scraping, and sentiment analysis is then performed to find the connection between experience rating and interview reviews

## Features

- The web scraper has a login function will you can type your email and passward
- Enter the links of the companies you want to scrape and it will scrape all the information from the link
- Use sentiment analysis to analyze the data you collected 
- save your time when you are seeking for some interview information for specific jobs

## Future Improvement

- Some interviews don't have experience or offer status, the scraper cannot skip the missing one
- Can do more analysis based on the data, e.g. most mentioned words in interview questions, or how interview questions affect offer status
- Glassdoor sometimes has pop-up advertisment, and the scraper will stop working when that happens

# Requirements

1. [Chrome](https://www.google.com/chrome/) browser installed.
2. Download the corresponding [chromedriver](https://chromedriver.chromium.org/downloads) version to your Chrome.
3. Install the required packages to your python in the [py](https://github.com/JackieCZY/Web-Scraping-Glassdoor-Interview/blob/main/scraping.py) file

Note: The chromedriver will not work if your Chrome browser updates automatically, so you need to make sure that your chromedrive's version is the same as your Chrome browser. 
