#!/usr/bin/env python

import sys
import requests
import re
import os
import shutil

DEBUG = 1

# Gets the current Python version
if DEBUG == 1:
    cur_M_version = sys.version_info[0]
    cur_m_version = sys.version_info[1]
    print ("DEBUG_MSG: Current Python version: " + str(cur_M_version) +"."+ str(cur_m_version))

# RBI's source URL, required to download the raw data
src_url = "https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009"

# Function takes RBI's URL as input and scraps all the xls links on the page
def scrape_url (url):
    main_xls_urls = []
    if DEBUG == 1:
        print ("DEBUG_MSG: Inside scrape_url() function.\nDEBUG_MSG: url = " + url)
    
    # Scraping the xls links from the `url` variable
    get_data = requests.get(url)
    if get_data is None:
        print ("No data was received, or unable to scrape the page.")
        if DEBUG == 1:
            print ("\nDEBUG_MSG: check 'requests' section under scrape_url()")

    if DEBUG == 1:
        print ("DEBUG_MSG: " + str(get_data.status_code))

    if get_data.status_code == 200:
        main_xls_urls = get_xls_links(get_data)
        main_xls_urls = [url.replace("http:", "https:") for url in main_xls_urls]
        create_xlsdir()
        download_xls(main_xls_urls)
    else:
        print("\nDEBUG_MSG: Invalid response received or link unreachable.\nDEBUG_MSG: Status returned: " + str(get_data.status_code))

def get_xls_links (scraped_data):
    xls_links = []
    if DEBUG == 1:
        print ("DEBUG_MSG: Success! Status returned = " + str(scraped_data.status_code))
    xls_urls = re.findall(r'(https?:\/\/(.+?)\.xls)', scraped_data.text)
    if len(xls_urls) == 0:
       print ("Empty list/No XLS file URLs")
       if DEBUG == 1:
           print ("\nDEBUG_MSG: Function name = scrape_url(), under sorting regex")
    for xls in xls_urls:
        xls_links.append(xls[0])
    return (xls_links)

def create_xlsdir():
    xls_filepath = "xls/"
    if not os.path.isdir(xls_filepath):
        if DEBUG == 1:
            print ("\nDEBUG_MSG: DIR 'xls/' doesn't exist.")
        os.makedirs(xls_filepath, exist_ok=True)
    else:
        if DEBUG == 1:
            print ("\nDEBUG_MSG: DIR 'xls/' exists.")
            print ("\nDEBUG_MSG: Deleting 'xls/' DIR.")
        shutil.rmtree(xls_filepath, ignore_errors=True)
        os.makedirs(xls_filepath, exist_ok=True)

def download_xls(xls_urls):
    for xls_url in xls_urls:
        path = 'xls' + '/' + xls_url.split("/")[-1]
        try:
            req_url = requests.get(xls_url, stream=True)
            if req_url.status_code == 200:
                with open(path, 'wb') as f:
                    for chunk in req_url.iter_content(1024):
                        f.write(chunk)
        except Exception as excp:
            raise Exception("Cannot download the XLS link:\n", req_url, "\n", str(excp))
## TODO: Add try/except to raise Exception; then add section to keep track of new XLS changes

scrape_url(src_url)
