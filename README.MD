# Project-Three

## Overview
For this project we researched financial records provided by the SEC. The records detail a variety of elements: revenue, gross profit, operating and net income loss, research and development expense, selling and marketing expense, share based and allocated share based expense depreciation, cost and expenses, general and administrative expense interest expense, lease and rental expense, marketing and advertising expense, accrued liabilities, entity common stock shares, and entity public float. We looked at records for a numerous companies and decided to present our findings using the data engineering route. We conducted an analysis of the records provided by the SEC in Jupyter Notebook and were able to extract data to import onto MongoDB.

### Key Terms 

* **S&P 500** - The Standard and Poor's 500, or simply the S&P 500, is a stock market index tracking the stock performance of 500 of the largest companies listed on stock exchanges in the United States.

* **SEC** - The U.S. **Securities and Exchange Commission** is an independent agency of the United States federal government, created in the aftermath of the Wall Street Crash of 1929. The primary purpose of the SEC is to enforce the law against market manipulation.

* **EDGAR** - Electronic Data Gathering, Analysis, and Retrieval is an internal database system that performs automated collection, validation, indexing, accepted forwarding of submissions by companies and others who are required by law to file forms with the U.S. Securities and Exchange Commission.

* **CIK** - Central Index Key - Unique key that identifies a company in SEC Database

* **SEC Form 8K** - Current Report - It is the report that companies must file with the SEC to announce major events that shareholders should know about. 

* **SEC Form 10Q** - Quarterly Report - It is a comprehensive quarterly report of financial performance submitted by all public companies to the SEC.

* **SEC Form 10K** - Annual Report - It is a a comprehensive report filed annually by a publicly-traded company about its financial performance.

* **SEC Form 10Q A** - Quarterly Report Amendment. 

* **SEC Form 10K A** - Annual Report Amendment.  
 

## Source Data
1. Details of compaines included in the S&P 500 index - https://en.wikipedia.org/wiki/List_of_S%26P_500_companies   

* Screenshot of S&P 500 companies listed in the Wikipedia page
![Image Info](./source/SP500/SP500_SourceData.png)

2. Finance data of companies as reported to SEC - https://data.sec.gov/api/xbrl/companyfacts/CIK0001701605.json 

* Sample data format of finance data as recevied from SEC Data API
![Image Info](./source/etl/image.png)

## Database Design 
![Image Info](./design/Database_Design.png)

## ETL

### Extract

* The CIK IDs for S&P 500 companies are obtained by web scraping WikiPedia page 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'. This is handled by notebook kept under "source/SP500". The company data is saved under 'data/input/SP500.csv'

* The finance data is extracted from SEC Website https://data.sec.gov/api/xbrl/companyfacts/ for each CIK IDs in the S&P500 Index. 

* SEC allows automated download of data from the API only if the following header is setup in the HTTP request

headers = {
    'User-Agent' : email_id,
    'Host' : 'data.sec.gov'
}

### Transform

The data for the following forms are considered for transformation:
* 8K, 10Q, 10K, 10Q/A, 10K/A 

There are multiple filings found in the data for the same reporting period. The latest filings are only kept to reflect the most recently updated information. The reporting period is extracted based on 'start' and 'end' period provided in each filing

### Load
The JSON data is constructed based on the database design. The data is loaded into MongoDB database using 'mongoimport' command

## References:
* https://www.sec.gov/edgar/sec-api-documentation


