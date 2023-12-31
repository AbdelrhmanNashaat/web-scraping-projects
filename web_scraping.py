# -*- coding: utf-8 -*-
"""Web Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17KdkMKFkyICkt07-TnCYP2f1xDOApfoh
"""

# Number one Import Modules that I will Use
import requests # used to call the page that i will scrap it
from bs4 import BeautifulSoup # used to parse html code and extract data from page
import csv

# Number one Import Modules that I will Use
import requests  # used to call the page that i will scrap it
from bs4 import BeautifulSoup  # used to parse html code and extract data from page
import csv
from itertools import zip_longest

print('This Project Get all Matches in A selected Day from YallaKoora')
date = input('Enter Date in the Following way MM/DD/YYY :')
page = requests.get(
    f'https://www.yallakora.com/match-center/%d9%85%d8%b1%d9%83%d8%b2-%d8%a7%d9%84%d9%85%d8%a8%d8%a7%d8%b1%d9%8a%d8%a7%d8%aa?date={date}')


def main(page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    championship_title_list = []
    match_week_list = []
    team_A_list = []
    team_B_list = []
    match_time_list = []
    score_list = []
    match_details = []
    championships = soup.find_all('div', {'class': 'matchCard'})

    def get_match_info(championships):
        # get championship title
        championship_title = championships.contents[1].find('h2').text.strip()

        # get list of html has all matches data
        all_matches = championships.contents[3].find_all('li')

        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            # get match week

            match_week = all_matches[i].find('div', {'class': 'date'}).text.strip()

            # team A name
            team_A = all_matches[i].find('div', {'class': 'teamA'}).text.strip()

            # team B name
            team_B = all_matches[i].find('div', {'class': 'teamB'}).text.strip()

            # get score
            match_result = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            # get match time
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()

            # add match data to the list
            championship_title_list.append(championship_title)
            match_week_list.append(match_week)
            team_A_list.append(team_A)
            team_B_list.append(team_B)
            score_list.append(score)
            match_time_list.append(match_time)

    for i in range(len(championships)):
        get_match_info(championships[i])

    file_list = [championship_title_list, match_week_list, team_A_list, team_B_list, score_list, match_time_list]
    exported = zip_longest(*file_list)

    with open('D:\web scraping\YallKoora Scrap\matches_details.csv', 'w', encoding="utf-8-sig") as output_file:
        wr = csv.writer(output_file)
        wr.writerow(['championship Title', 'Match Week', 'Team A', 'Team B', 'Score', 'Time'])
        wr.writerows(exported)
        print('File Created')


main(page)

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
soup = BeautifulSoup(src, 'lxml')
jop_titles = soup.find_all('h2', {'class': 'css-m604qf'})
company_names = soup.find_all('a', {'class': 'css-17s97q8'})
locations = soup.find_all('span', {'class': 'css-5wys0k'})
jop_type = soup.find_all('span', {'class': 'css-1ve4b75'})
jop_skills = soup.find_all('div', {'class': 'css-y4udm8'})

for i in range(len(jop_titles)):
    jop_titles_list.append(jop_titles[i].text)
    company_names_list.append(company_names[i].text)
    locations_list.append(locations[i].text)
    jop_type_list.append(jop_type[i].text)
    jop_skills_list.append(jop_skills[i].text)

file_list = [jop_titles_list, company_names_list, locations_list, jop_type_list, jop_skills_list]
exported = zip_longest(*file_list)
with open('D:\web scraping\wuzzuf Scrap\jops_details.csv', 'w') as output_file:
    wr = csv.writer(output_file)
    wr.writerow(['Jop Titles', 'Company Name', 'Location', 'Jop Type', 'Jop Skills'])
    wr.writerows(exported)
    print('File Created')

# download any vedio from youtube
from pytube import YouTube
link = input('Enter Youtube Video Url :')
video = YouTube(link)
stream = video.streams.get_highest_resolution()
print("Downloading:", stream.title)
stream.download()
print('Download Done')

# download any vedio from any site
import requests


def download_video(url):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open('video.mp4', "wb") as file:
            for chunk in response.iter_content(chunk_size=4096):
                file.write(chunk)

        print("Download complete!")
    else:
        print("Failed to download the video.")


video_url = input('Enter Video Url : ')


download_video(video_url)