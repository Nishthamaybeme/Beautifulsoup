# import requests
# from bs4 import BeautifulSoup

# html_text= requests.get('https://www.google.com/localservices/prolist?g2lbs=AOHF13mhCuAXcZ-IhKfSPUoPmErjrfNo0MzeOU8PaZA9p44EI_ft1IDMi_BiecNtsoTP8-LnGw_7aZ86IcjMCzGoWdVGZBt_pdCsMSrHjaUK7GKpDF8QDOk%3D&hl=en-IN&gl=in&ssta=1&q=all%20interior%20design%20business%20list&oq=all%20interior%20design%20business%20list&slp=MgBSAggCYACSAaQCCg0vZy8xMWpiNGtrY3JjCg0vZy8xMWdoNDhqMm5oCgwvZy8xaG00ODN2NXIKDS9nLzExdDBzdF9yNmIKCy9nLzF0cGxucWsyCg0vZy8xMWg2bTBtYzJmCg0vZy8xMWdnNjR2bmpfCg0vZy8xMWZ4ZHl2eGQ1Cg0vZy8xMWgxMGQwdHk0CgsvZy8xdHBiOWN6YwoML2cvMXE2OW53azM0Cg0vZy8xMXJmOWZrMnB6Cg0vZy8xMXZ4NHcyNWxjCg0vZy8xMXNuXzNuZDVoCg0vZy8xMW10ZnJic3puCgwvZy8xMWd6OHFfd3YKDS9nLzExcWgxYngyazUKDS9nLzExbnkzZl9sM3kKDS9nLzExdmpmbjZ2X3cKDC9nLzFxNjlyeHIyY5oBBgoCFxkQAA%3D%3D&src=2&serdesk=1&sa=X&ved=2ahUKEwiSv5jZ2umGAxUTb2wGHeUtAPUQjGp6BAhYEAE&scp=ChZnY2lkOmludGVyaW9yX2Rlc2lnbmVyEmASEglvo1-e_Xl0ORE2zB_hXJLqFBoSCdlBL3yFDXQ5EUI7Uqk470p4Ih5EYXlhbEJhZ2gsIEFncmEsIFV0dGFyIFByYWRlc2gqFA20lDgQFWLfey4dkrs9ECVbn4AuMAEaIWFsbCBpbnRlcmlvciBkZXNpZ24gYnVzaW5lc3MgbGlzdCIhYWxsIGludGVyaW9yIGRlc2lnbiBidXNpbmVzcyBsaXN0KhFJbnRlcmlvciBkZXNpZ25lcg%3D%3D').text

# # print(html_text)
# # r= requests.get(html_text,headers=headers)
# soup=BeautifulSoup(html_text,'lxml')
# designers=soup.find_all('div',class_='I9iumb')
# # print(designers)
# for job in designers:
#     company_name=job.find('div',class_='rgnuSb xYjf2e')
#     print(company_name)
#     rating=job.find('div',class_='rGaJuf')
#     print(rating)
#     experience=job.find('span',class_='FjZRNe hGz87c')
#     print(experience)
#     print(f'''
# Company name:{company_name}
# Ratings out of 5: {rating}
# Experience:{experience}
#          ''' )
#     print('')
import requests
import pandas as pd
from bs4 import BeautifulSoup
print("LIST OF INTERIOR DESIGNER BUSINESS IN AGRA")

# Fetch the HTML content of the webpage
url = 'https://www.google.com/localservices/prolist?g2lbs=AOHF13mhCuAXcZ-IhKfSPUoPmErjrfNo0MzeOU8PaZA9p44EI_ft1IDMi_BiecNtsoTP8-LnGw_7aZ86IcjMCzGoWdVGZBt_pdCsMSrHjaUK7GKpDF8QDOk%3D&hl=en-IN&gl=in&ssta=1&q=all%20interior%20design%20business%20list&oq=all%20interior%20design%20business%20list&slp=MgBSAggCYACSAaQCCg0vZy8xMWpiNGtrY3JjCg0vZy8xMWdoNDhqMm5oCgwvZy8xaG00ODN2NXIKDS9nLzExdDBzdF9yNmIKCy9nLzF0cGxucWsyCg0vZy8xMWg2bTBtYzJmCg0vZy8xMWdnNjR2bmpfCg0vZy8xMWZ4ZHl2eGQ1Cg0vZy8xMWgxMGQwdHk0CgsvZy8xdHBiOWN6YwoML2cvMXE2OW53azM0Cg0vZy8xMXJmOWZrMnB6Cg0vZy8xMXZ4NHcyNWxjCg0vZy8xMXNuXzNuZDVoCg0vZy8xMW10ZnJic3puCgwvZy8xMWd6OHFfd3YKDS9nLzExcWgxYngyazUKDS9nLzExbnkzZl9sM3kKDS9nLzExdmpmbjZ2X3cKDC9nLzFxNjlyeHIyY5oBBgoCFxkQAA%3D%3D&src=2&serdesk=1&sa=X&ved=2ahUKEwiSv5jZ2umGAxUTb2wGHeUtAPUQjGp6BAhYEAE&scp=ChZnY2lkOmludGVyaW9yX2Rlc2lnbmVyEmASEglvo1-e_Xl0ORE2zB_hXJLqFBoSCdlBL3yFDXQ5EUI7Uqk470p4Ih5EYXlhbEJhZ2gsIEFncmEsIFV0dGFyIFByYWRlc2gqFA20lDgQFWLfey4dkrs9ECVbn4AuMAEaIWFsbCBpbnRlcmlvciBkZXNpZ24gYnVzaW5lc3MgbGlzdCIhYWxsIGludGVyaW9yIGRlc2lnbiBidXNpbmVzcyBsaXN0KhFJbnRlcmlvciBkZXNpZ25lcg%3D%3D'
response = requests.get(url)
html_text = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_text, 'lxml')


designers = soup.find_all('div', {'jscontroller': 'xkZ6Lb'})
data = []
for job in designers:
  company_name = job.find('div', class_='rgnuSb xYjf2e')
  rating = job.find('div', class_='rGaJuf')
  experience = job.find('span', class_='FjZRNe hGz87c')


company_name_text = company_name.text if company_name else 'N/A'
rating_text = rating.text if rating else 'N/A'
experience_text = experience.text if experience else 'N/A'

data.append({
    'Company Name': company_name_text,
    'Rating': rating_text,
    'Experience': experience_text,
   
})
df = pd.DataFrame(data)


df.to_excel('interioragra.xlsx', index=False)

print("Data has been written to interior_designers_in_agra.xlsx")