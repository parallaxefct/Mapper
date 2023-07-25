#for any given webpage, the user has the option of finding all URL // the top 3 words that appear on webpage // eventually map out the webserver and all its links
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#takes HTML, parses through and returns all anchor tags
def parse_url(url):
    all_urls = []
    html = urllib.request.urlopen(url, context=ctx).read() #opens URL
    sifter = BeautifulSoup(html, 'html.parser') #sifts and return one large string
    anchor_list = sifter('a', None) #extracts all anchor tags
    for tag in anchor_list:
        #gets HTML tag as string
        x = tag.get('href', None)
        all_urls.append(x)

    return all_urls

#takes all anchor tags, captures URLs and returns total list of URL

#passes a keyword
#def url_mapper(keyword):



url = input('Enter entire URL: ')
choice = input('I can capture all URLs on a single webpage OR map out all URLs on a web server. Page or Map?: ').lower() #figure out how to add


#decision tree: Page
if choice == 'page':
    page_urls = parse_url(url)
    print(page_urls)

#decision tree: URL MAPPING
#elif choice == 'map':
#else:
