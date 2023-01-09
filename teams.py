#Webscrapes and stores team information for NCAA D1
#packages
from bs4 import BeautifulSoup
import requests
import urllib.request

# create request
url = 'https://www.ncaa.com/schools/{}'
school_url ='ohio-st'
# reinforces integrity of the data collection
accessed = False
while accessed == False:
    try:
        response = requests.get(url.format(school_url))
        print(response)
        accessed = True
    except:
        accesssed = False