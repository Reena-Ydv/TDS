# TDS
1. I gathered data on GitHub users in Bangalore with 100+ followers, including their public repositories, using the GitHub API.
2. Many top developers in Bangalore are heavily focused on data science, with Python as the dominant language.
3. To gain more followers, developers should focus on well-documented projects and consider Python or other widely-used languages.

## About This Project
This project aims to explore GitHub users in Bangalore who have gained a significant following. Using the GitHub REST API, I pulled information about each user, their follower count, and details on their most recent public repositories. 

The collected data is organized into two files:
1. **users.csv**: Key details about each user like their name, company, bio, and follower count.
2. **repositories.csv**: Details about each user’s public repositories, including the number of stars, programming language, and license type.

## How I Collected the Data:
With the GitHub API, I filtered for users based in Bangalore who had 100 or more followers. For each user, I then fetched information about their public repositories upto 500, capturing everything from the repository name and programming language to the star count and license type.

## My Insights:
### After looking over the data, some interesting patterns stood out:
1. Many popular developers in Bangalore are working in data science, with Python as their primary language.
2. Repositories with detailed README files and documentation tend to attract more stars and followers.

## Recommendations for Developers:
Based on these findings, developers looking to build their following might benefit from:

1. Good documentation makes projects more approachable, which can lead to more stars and engagement. 
2. Since Python is already well-loved in Bangalore’s developer community, using it (or similarly popular languages) may increase project visibility.

## File Descriptions:
**users.csv**: Information on users in Bangalore with 100+ followers, including their bio, company, and follower count.
**repositories.csv**: Information on their repositories, like stars, language, and license.
**README.md**: This file, giving an overview of the project, findings, and recommendations.

## Running the Code
To fetch and save this data, you’ll need Python installed on your system. Run the script (TDS_Project_1.py) after installing the requests library to pull data from GitHub and generate the CSV files.


