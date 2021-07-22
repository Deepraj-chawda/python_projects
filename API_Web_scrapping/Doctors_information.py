
'''
__author__ = 'Deepraj Chawda'
__version__ = '3.8.5'
'''
import requests
import bs4
import pandas as pd

doctors = {
    'Name': [],
    'Specialities': [],
    'Education': [],
    'City': [],
    'Experience': [],
    'Hospital' : []
}

url = "https://www.sehat.com/ujjain/doctors?pre_flt=city&page={}"

for i in range(1,8):
    respone = requests.get(url.format(i))
    soup = bs4.BeautifulSoup(respone.content,'html5lib')
    divs = soup.find_all('div',attrs={'class':'col-md-6 col-xs-6 col-sm-6 padding-left-10'})
    
    for div in divs:
        doctors['Name'].append(div.span.text.strip())
        doctors['Specialities'].append(div.find('p',attrs={'class':'margin-bottom-0 dcommatag'}).text.strip())
        doctors['Education'].append(div.find('p',attrs={'class':'edu margin-bottom-10'}).text.strip())
        details = div.find_all('li',attrs={'class':'mrt20 fw300 col-md-12 co-sm-12'})
        doctors['City'].append(details[0].text.strip())
        experience = False
        hospital = False

        for i in range(1,len(details)):
            if details[i].text.strip().endswith('Experience'):
                doctors['Experience'].append(details[i].text.strip())
                experience = True
            if details[i].text.strip().endswith('Hospital'):
                doctors['Hospital'].append(details[i].text.strip())
                hospital = True
        if not experience:
            doctors['Experience'].append(None)
        if not hospital:
            doctors['Hospital'].append(None)

doctors = pd.DataFrame(doctors)
doctors.to_csv('doctors_from_ujjain.csv',index=False)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(doctors.to_string())


