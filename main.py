#!/usr/bin/env python

import sys

# Gets the current Python version
cur_M_version = sys.version_info[0]
cur_m_version = sys.version_info[1]
print ("Current Python version: " + str(cur_M_version) +"."+ str(cur_m_version))

# RBI's source URL, required to download the raw data
src_url = "https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009"

# Function takes RBI's URL as input and scraps all the xls links on the page
def scrape_url (src_url):
    
