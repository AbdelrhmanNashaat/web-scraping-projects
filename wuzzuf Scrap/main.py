import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


jop_titles_list = []
company_names_list = []
locations_list = []
jop_type_list = []
jop_skills_list = []

page = requests.get('https://wuzzuf.net/search/jobs/?q=python&a=hpb')
src = page.content
soup = BeautifulSoup(src,'lxml')
jop_titles = soup.find_all('h2',{'class' : 'css-m604qf'})
company_names = soup.find_all('a',{'class' : 'css-17s97q8'})
locations = soup.find_all('span',{'class' : 'css-5wys0k'})
jop_type = soup.find_all('span',{'class' : 'css-1ve4b75'})
jop_skills = soup.find_all('div',{'class' : 'css-y4udm8'})

for i in range(len(jop_titles)):
  jop_titles_list.append(jop_titles[i].text)
  company_names_list.append(company_names[i].text)
  locations_list.append(locations[i].text)
  jop_type_list.append(jop_type[i].text)
  jop_skills_list.append(jop_skills[i].text)
file_list = [jop_titles_list,company_names_list,locations_list,jop_type_list,jop_skills_list]
exported = zip_longest(*file_list)
with open('D:\web scraping\wuzzuf Scrap\jops_details.csv','w') as output_file:
  wr = csv.writer(output_file)
  wr.writerow(['Jop Titles','Company Name' , 'Location' , 'Jop Type', 'Jop Skills'])
  wr.writerows(exported)
  print('File Created')