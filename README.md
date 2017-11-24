#### RBI IFSC code scraper (*discontinued...*)  
  
![Build-State](https://travis-ci.org/rn4ir/bankinfo-parser.svg?branch=master)  
  
A simple scraper made to download relevant branch-related information for various banks in India.  
  
*Notes:*
- The scraper downloads the data from the Reserve Bank of India's website.
- [The URL that is scraped.](https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009)
- The internal Spreadsheet links are downloaded to a directory (called `xls/`) created in the present working directory.
- The Spreadsheets are converted and saved as CSV files in a new directory (called `csv/`) created in the present working directory.
- These CSV files can later be used to process the data as per your requirement.
