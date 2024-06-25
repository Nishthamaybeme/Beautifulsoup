from bs4 import BeautifulSoup
import requests

html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
# print(html_text)
#200 means requests accepted
soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date=job.find('span',class_ = 'sim-posted').text
    if "2" in published_date:
         company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
         skills=job.find('span',class_='srp-skills').text.replace(' ','')


         print(f'''
Company name:{company_name}
Required skills: {skills}
         ''' )
    
         print('')
   

