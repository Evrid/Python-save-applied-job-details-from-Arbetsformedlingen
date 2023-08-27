# Python-save-applied-job-details-from-Arbetsformedlingen




You give it a link of job you applied on Arbetsformedlingen, then it will save the Job Name,Company Name,Job Type,Location,AppliedDate to an excel, also save the html of the job to the folder.


How to use:
first cd to your folder, in my case:

Cd C:\Users\YS\Desktop\Python automatic scraping job

then:

python arbsavejob.py       


Example given link:
https://arbetsformedlingen.se/platsbanken/annonser/27968814          


Steps

First we add python to environment variables

pip install pandas
pip install requests
pip install beautifulsoup4
pip install openpyxl
pip install selenium

Indentation

Indentation: Python is very sensitive to indentation, and it looks like the indentation is inconsistent. For example, the comment "Send a request to the URL" should be aligned with the code below it, not ahead of it. This might raise an indentation error.
We can ask ChatGPT to fix the indentation 

Why must use element = WebDriverWait to wait h1

The discrepancy in the HTML content you're seeing when using print(html_content) is likely due to one of the following reasons:
Dynamic Content: Modern websites often load content dynamically using JavaScript. This content may not appear in the initial HTML source but will be added to the DOM later on. Your script might capture the HTML before the JavaScript has had a chance to run and update the DOM.
Different Pages: The pages you're scraping might not be consistent in structure. One page may have an h1 tag, while another does not.
User-Agent or Other Headers: Sometimes websites deliver different content based on the user-agent or other headers in the HTTP request. If the server identifies your scraper as a non-browser agent, it might serve a simplified or obfuscated version of the page.
Loading Time: The page's resources (e.g., CSS, JS, images) may not have fully loaded when the html_content is captured. This might result in missing elements.
AJAX Requests: Some websites load data through AJAX requests. If that's the case, simply grabbing the HTML source won't get you this data.
To improve the accuracy of your web scraping, consider using the following strategies:
Wait for Elements: Selenium has functions to wait for certain elements to appear before proceeding. Look into Selenium’s WebDriverWait for this.
python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1"))
)




why the result of soup is different of what i see using F12?
When you inspect a webpage using the browser's developer tools (F12), you're often seeing the final, rendered HTML, which includes modifications made by JavaScript running on the page. The HTML content you get using Python's requests library is the raw HTML content that comes from the server, before any client-side JavaScript has been applied.
If the content you're interested in is being loaded or modified using JavaScript, you might need to use a different approach, such as using Selenium which allows you to scrape websites by controlling a web browser.







