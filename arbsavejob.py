import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from selenium import webdriver
import time
import datetime  # Don't forget to import the datetime module

def scrape_and_save_job_info(url, excel_filename='+Applied jobs.xlsx'):
    # Send a request to the URL
    
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()
    
    try:
        # Navigate to the page
        driver.get(url)
        
        # Get the rendered HTML content
        html_content = driver.page_source
        
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract information
        job_name = soup.find('h1').text if soup.find('h1') else "N/A"
        company_name = soup.find('h2').text if soup.find('h2') else "N/A"
        job_type = soup.find('h3').text if soup.find('h3') else "N/A"
        
        # Finding second h3 for location
        h3_tags = soup.find_all('h3')
        location = h3_tags[1].text if len(h3_tags) > 1 else "N/A"
        
        # Store the information
        new_row = {
            'Job Name': job_name,
            'Company Name': company_name,
            'Job Type': job_type,
            'Location': location,
            'AppliedDate': datetime.datetime.now().date().strftime('%Y-%m-%d')
        }
        
        # Check if the Excel file already exists
        if os.path.exists(excel_filename):
            df = pd.read_excel(excel_filename)
        else:
            df = pd.DataFrame(columns=['Job Name', 'Company Name', 'Job Type', 'Location', 'AppliedDate'])
        
        # Append the new job to the DataFrame
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        
        # Save the DataFrame back to Excel
        df.to_excel(excel_filename, index=False)
        
        # Save the HTML content to a file named after the job
        with open(f"{job_name}.html", 'w', encoding='utf-8') as f:
            f.write(html_content)
    finally:
        # Close the Firefox browser
        driver.quit()
    
    return new_row

while True:
    # Get the URL from the user
    url = input("Please enter the job URL (or type 'exit' to quit): ")
    
    # Exit the loop if the user types 'exit'
    if url.lower() == 'exit':
        print("Exiting. Goodbye!")
        break
    
    # Scrape the job info and save it to Excel
    info = scrape_and_save_job_info(url)
    print(f"Saved job info: {info}")
