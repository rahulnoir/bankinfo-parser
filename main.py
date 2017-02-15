#!/usr/bin/env python

import sys
import requests
import re

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
    
    if DEBUG == 1:
        print ("DEBUG_MSG: Inside scrape_url() function.\nDEBUG_MSG: url = " + url)
    
    # Scraping the xls links from the `url` variable
    get_data = requests.get(url)

    if DEBUG == 1:
        print ("DEBUG_MSG: " + str(get_data.status_code))

    if get_data.status_code == 200:
        if DEBUG == 1:
            print ("DEBUG_MSG: Success! Status returned = " + str(get_data.status_code))
        xls_urls = re.findall(b"(https?:\/\/(.+?)\.xls)", get_data.content)
        for xls in xls_urls:
            print (xls[0])
## TODO: check if string, element greater than 1 to check if there is data in the list/array
    else:
        print("\nDEBUG_MSG: Invalid response received or link unreachable.\nDEBUG_MSG: Status returned: " + str(get_data.status_code))

scrape_url(src_url)
