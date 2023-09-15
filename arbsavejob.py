import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_and_save_job_info(url, excel_filename='Applied_jobs.xlsx'):
    driver = webdriver.Firefox()

    try:
        driver.get(url)
        
        # Wait for the <h1> tag to appear (You can also use other tags as appropriate)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        html_content = driver.page_source

        soup = BeautifulSoup(html_content, 'html.parser')
        job_name = soup.find('h1').text if soup.find('h1') else "N/A"
        company_name = soup.find('h2').text if soup.find('h2') else "N/A"
        job_type = soup.find('h3').text if soup.find('h3') else "N/A"

        h3_tags = soup.find_all('h3')
        location = h3_tags[1].text if len(h3_tags) > 1 else "N/A"

        new_row = {
            'Job Name': job_name,
            'Company Name': company_name,
            'Job Type': job_type,
            'Location': location,
            'AppliedDate': datetime.datetime.now().date().strftime('%Y-%m-%d')
        }

        if os.path.exists(excel_filename):
            df = pd.read_excel(excel_filename)
        else:
            df = pd.DataFrame(columns=['Job Name', 'Company Name', 'Job Type', 'Location', 'AppliedDate'])

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(excel_filename, index=False)

        with open(f"{job_name}.html", 'w', encoding='utf-8') as f:
            f.write(html_content)

    finally:
        driver.quit()

    return new_row

def get_multiple_links():
    links = []
    num_links = int(input("How many job URLs do you want to input? "))
    
    for i in range(num_links):
        link = input(f"Please enter job URL {i+1}: ")
        links.append(link)

    return links

# Get the list of links
links = get_multiple_links()

for url in links:
    if url.lower() == 'exit':
        print("Exiting. Goodbye!")
        break

    info = scrape_and_save_job_info(url)
    print(f"Saved job info: {info}")
