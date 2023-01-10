#Webscrapes and stores team information for NCAA D1
#packages
from bs4 import BeautifulSoup
import requests
import urllib.request
#gets school url
#uses this webpage to get url https://www.ncaa.com/schools-index/
def get_team_url(name):
# create request
#url = 'https://www.ncaa.com/schools/{}'
#school_url ='ohio-st'
    url = 'https://www.ncaa.com/schools-index/'
    # reinforces integrity of the data collection
    accessed = False
    while accessed == False:
        try:
            response = requests.get(url)#.format(school_url))
            print(response)
            accessed = True
        except:
            accesssed = False

url = get_team_url("Ohio St.")