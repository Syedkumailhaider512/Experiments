import requests , webbrowser
from bs4 import BeautifulSoup
import httplib2

'''

search = webbrowser.open("https://www.google.com/search?q=" + query)
pdf_data = requests.get("https://www.google.com/search?q=filetype%3Apdf " + query)
search_data = requests.get("https://www.google.com/search?q=filetype%3Apdf " + query)
pdf_soup = BeautifulSoup(pdf_data.text, 'html.parser')
search_soup = BeautifulSoup(search_data.text, 'html.parser')


#print(pdf_soup.prettify())
print(search_soup.prettify())
'''
query = input("Enter any word: ")
url = "https://www.google.com/search?q=" + query
pdf = webbrowser.open(url)

http = httplib2.Http(url)

response , content = http.request(url)

links = []

for link in BeautifulSoup(content).find_all('a', href = True):
    links.append(link['href'])

for link in links:
    print(link)