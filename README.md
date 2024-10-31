# TDS
1. I used the GitHub API to pull data on Bangalore-based users with 100+ followers, including their repository details, to better understand their work.
2. One surprising trend: Many popular developers focus on data science, and Python is by far the favorite programming language.
3. To gain more followers, developers should focus on well-documented projects and consider Python or other widely-used languages.

## About This Project
This project involved gathering and analyzing data on GitHub users located in Bangalore with a following of over 100. By using the GitHub REST API, I was able to collect details about each user and up to 500 of their most recent public repositories. 
The data is saved in two CSV files:
1. **users.csv**: Key details about each user like their name, company, bio, and follower count.
2. **repositories.csv**: Details about each user’s public repositories, including the number of stars, programming language, and license type.

## How I Collected the Data:
With the GitHub API, I filtered for users based in Bangalore who had 100 or more followers. For each user, I then fetched information about their public repositories, capturing everything from the repository name and programming language to the star count and license type.

## My Insights:
### After looking over the data, some interesting trends stood out:
Many highly-followed developers in Bangalore are working in data science, and Python seems to be the language of choice.
Documentation Matters: Repositories with detailed README files and documentation tend to have more stars and followers.
Recommendations for Developers

### Based on these findings, developers looking to build their following might benefit from:

Good documentation makes projects more approachable, which can lead to more stars and engagement. Since Python is already well-loved in Bangalore’s developer community, using it (or similarly popular languages) may increase project visibility.

## Project Files
**users.csv**: Information on users in Bangalore with 100+ followers, including their bio, company, and follower count.
**repositories.csv**: Information on their repositories, like stars, language, and license.
**README.md**: This file, giving an overview of the project, findings, and recommendations.

## Running the Code
To fetch and save this data, you’ll need Python installed on your system. Run the script (TDS_Project_1.py) after installing the requests library to pull data from GitHub and generate the CSV files.


