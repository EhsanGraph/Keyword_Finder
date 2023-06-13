import requests_html
from bs4 import BeautifulSoup

print(Fore.RED + f"""
___________.__                              ________.__            _____             .__ 
\_   _____/|  |__   ___________    ____    /  _____/|  |__ _____ _/ ____\____ _______|__|
 |    __)_ |  |  \ /  ___/\__  \  /    \  /   \  ___|  |  \\__  \\   __\\__  \\_  __ \  |
 |        \|   Y  \\___ \  / __ \|   |  \ \    \_\  \   Y  \/ __ \|  |   / __ \|  | \/  |
/_______  /|___|  /____  >(____  /___|  /  \______  /___|  (____  /__|  (____  /__|  |__|
        \/      \/     \/      \/     \/          \/     \/     \/           \/                                                                                    
         [!] Supports multiple keywords
""")

keywords = []
longtail = []


session = requests_html.HTMLSession()
req = session.get("Google search address")

soup = BeautifulSoup(req.content, 'html.parser')

for i in soup.find_all('div',{'class':'s75CSd'}):
    keywords.append(i.text)

for w in keywords:
    session2 = session.get(f'Google search address')
    soup2 = BeautifulSoup(session2.content, 'html.parser')
    for words in soup2.find_all('div',{'class':'s75CSd'}):
        longtail.append(words.text)
        

print(keywords)
print('------------------------------------------------------------')
print(longtail)
