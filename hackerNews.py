import time
import random
import requests

def fetch(url,delay=(1,3)):
    """
    Simulate human random clicking 1..3 seconds then fetch URL.
    Returns the actual page source fetched and the beautiful soup object.
    """
    import bs4 as soup
    header = {'User-Agent':'not me'}
    url = requests.get(url=url,headers=header)
    time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
    html_string = url.text
    print(html_string)
    soup = soup.BeautifulSoup(html_string, 'html.parser')
    return (html_string,soup)

html, soup = fetch('https://www.reddit.com/r/all')
for tag in soup.find_all('a',{'data-click-id':'comments'}):
    tag['href']
    print(tag['href'])