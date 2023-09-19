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
            match_time_list.append(match_time)
            score_list.append(score)

    for i in range(len(championships)):
        get_match_info(championships[i])

    file_list = [championship_title_list, match_week_list, team_A_list, team_B_list, match_time_list, score_list]
    exported = zip_longest(*file_list)

    with open('D:\web scraping\YallKoora Scrap\matches_details.csv', 'w', encoding="utf-8") as output_file:
        wr = csv.writer(output_file)
        wr.writerow(['championship Title, Match Week , Team A, Team B, Time, Score'])
        wr.writerows(exported)
        output_file.close()
        print('File Created')

main(page)
