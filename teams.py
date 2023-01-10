#Webscrapes and stores team information for NCAA D1
#packages
from bs4 import BeautifulSoup
import requests
import urllib.request
#gets school url
#uses this webpage to get url https://www.ncaa.com/schools-index/
# @TODO: Find string in html and extract the respective url for the school
def get_team_url(name):
# create request
#url = 'https://www.ncaa.com/schools/{}'
#school_url ='ohio-st'
    base_url  = 'https://www.ncaa.com/schools-index/'
    accessed = False
    while accessed == False:
        try:
            response = requests.get(base_url)#.format(school_url))
            print(response)
            accessed = True
        except:
            accesssed = False
    page = 0
    not_found = True
    while response.status_code != 404 and not_found:
        page+=1 
        url = base_url.format(page)
        # reinforces integrity of the data collection
        accessed = False
        # check for access
        while accessed == False:
            try:
                response = requests.get(url)#.format(school_url))
                print(response)
                accessed = True
            except:
                accesssed = False
        print(response.text)
        not_found = False

url = get_team_url("Ohio St.")