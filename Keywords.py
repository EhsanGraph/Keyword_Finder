import requests_html
from bs4 import BeautifulSoup

keywords = []
longtail = []


session = requests_html.HTMLSession()
req = session.get("https://www.google.com/search?q=Afghan+Nobel+Music&ei=2lRwZInHEKrnsAf4pKTQCQ&ved=0ahUKEwiJnP7VsJL_AhWqM-wKHXgSCZoQ4dUDCA8&uact=5&oq=Afghan+Nobel+Music&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABOgoIABBHENYEELADSgQIQRgAUMwDWMwDYKsFaANwAXgAgAF0iAF0kgEDMC4xmAEAoAECoAEBwAEByAEI&sclient=gws-wiz-serp")

soup = BeautifulSoup(req.content, 'html.parser')

for i in soup.find_all('div',{'class':'s75CSd'}):
    keywords.append(i.text)

for w in keywords:
    session2 = session.get(f'https://www.google.com/search?q={w}&ei=2lRwZInHEKrnsAf4pKTQCQ&ved=0ahUKEwiJnP7VsJL_AhWqM-wKHXgSCZoQ4dUDCA8&uact=5&oq=Afghan+Nobel+Music&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABOgoIABBHENYEELADSgQIQRgAUMwDWMwDYKsFaANwAXgAgAF0iAF0kgEDMC4xmAEAoAECoAEBwAEByAEI&sclient=gws-wiz-serp')
    soup2 = BeautifulSoup(session2.content, 'html.parser')
    for words in soup2.find_all('div',{'class':'s75CSd'}):
        longtail.append(words.text)
        

print(keywords)
print('------------------------------------------------------------')
print(longtail)