#Webscrapes and stores team information for NCAA D1
#packages
from bs4 import BeautifulSoup
import requests
import urllib.request
#gets school url
#uses this webpage to get url https://www.ncaa.com/schools-index/
# @TODO: Find string in html and extract the respective url for the school
# returns urls of schools
def get_url_list(page):
    url = 'https://www.ncaa.com/stats/basketball-men/d1/current/team/145/p{}'.format(page)
    accessed = False
    while accessed == False:
        try:
            response = requests.get(url)
            print(response)
            accessed = True
        except:
            accesssed = False
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return [soup.table.find_all('tr')[i].find_all('td')[1].find('a',href=True)['href'] for i in range(1,len(soup.table.find_all('tr')))] # puts result into array
    else: 
        return [] 
# gets all urls
i = 1
url_arr = get_url_list(1) # holds urls for teams
while len(get_url_list(i)) > 0:
    i+=1
    url_arr_temp = get_url_list(i) # holds page urls for teams
    url_arr = url_arr + url_arr_temp
print(len(url_arr))
    