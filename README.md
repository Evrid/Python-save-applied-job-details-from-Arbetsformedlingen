# Python Save Applied Job Details from Arbetsförmedlingen

## Overview

Managing job applications can be a daunting task, especially when applying through various platforms. This Python script aims to make your life easier by automating the process of recording the details of jobs you apply for on Arbetsförmedlingen.(https://arbetsformedlingen.se/), Sweden's public employment service. The tool saves essential job details, such as Job Name, Company Name, Job Type, and Location, along with the date of application, to an Excel spreadsheet. Additionally, the HTML content of the job posting is saved locally for your future reference.

Here is a video demo: 

https://youtu.be/FVPMhePbauQ 

Open a command prompt and type: 
python --version
    If you see the error, Python is not installed or not properly configured.
    
If you haven't installed the libraries, you need to install using:
pip install requests beautifulsoup4 pandas selenium openpyxl




## Key Features
- Saves the following job details to an Excel sheet:
  - Job Name
  - Company Name
  - Job Type
  - Location
  - Applied Date
- Stores the HTML content of the job posting for offline viewing.
- User-friendly: simply provide the job URL, and the script does the rest.

## GitHub Repository
https://github.com/Evrid/Python-save-applied-job-details-from-Arbetsformedlingen

## Technologies Used
- Python
- Selenium WebDriver
- BeautifulSoup
- Pandas
- openpyxl


## How It Works
1. The script uses Selenium WebDriver to open the job URL and waits for the page to load completely.
2. BeautifulSoup parses the HTML content, and the relevant details are extracted.
3. The details are then saved to an Excel file using Pandas.
4. Additionally, the HTML content of the job posting is saved to your local directory.

## Code Insight
- The script uses WebDriverWait from Selenium to ensure that all dynamic elements are fully loaded before extraction begins.
- BeautifulSoup helps in parsing HTML content and retrieving the required information.
- Pandas DataFrame is used for storing and manipulating the job details.

## Conclusion
This tool aims to streamline the process of job applications by automating the mundane task of recording job details, allowing you to focus on what really matters in your job search. Happy job hunting!
