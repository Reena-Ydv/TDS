import requests
import csv
from time import sleep

# doing Authentication
GITHUB_TOKEN = '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'
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Fetching users from Bangalore with over 100 followers
def get_users_in_bangalore():
    users = []
    page = 1
    while True:
        url = f"https://api.github.com/search/users?q=location:Bangalore+followers:>100&per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print("Error fetching users:", response.json())
            break
        
        items = response.json().get("items", [])
        if not items:
            break
        
        users.extend(items)
        page += 1
        sleep(1)  # To avoid hitting rate limits
    
    return users

# Fetching repositories for each user
def get_user_repositories(user_login):
    repositories = []
    page = 1
    while len(repositories) < 500:
        url = f"https://api.github.com/users/{user_login}/repos?per_page=100&page={page}&sort=pushed"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error fetching repos for {user_login}:", response.json())
            break
        
        repo_items = response.json()
        if not repo_items:
            break
        
        # Only fetching up to 500 repositories
        for repo in repo_items:
            repo_data = {
                "login": user_login,
                "full_name": repo.get("full_name", ""),
                "created_at": repo.get("created_at", ""),
                "stargazers_count": repo.get("stargazers_count", 0),
                "watchers_count": repo.get("watchers_count", 0),
                "language": repo.get("language", ""),
                "has_projects": str(repo.get("has_projects", False)).lower(),
                "has_wiki": str(repo.get("has_wiki", False)).lower(),
                "license_name": repo.get("license")["key"] if repo.get("license") else ""
            }
            repositories.append(repo_data)
        
        page += 1
        sleep(1)  # To avoid hitting rate limits
    
    return repositories

# Gathering all data and save to CSV through Main function
def main():
    # Step 1: Fetching from get_users_in_bangalore function
    users = get_users_in_bangalore()
    
    # Step 2: Open repositories.csv and write headers
    with open("repositories.csv", "w", newline="", encoding="utf-8") as repo_file:
        repo_writer = csv.DictWriter(repo_file, fieldnames=[
            "login", "full_name", "created_at", "stargazers_count", 
            "watchers_count", "language", "has_projects", 
            "has_wiki", "license_name"
        ])
        repo_writer.writeheader()
        
        # Step 3: For each user, fetching repositories and write to CSV
        for user in users:
            user_login = user['login']
            repositories = get_user_repositories(user_login)
            
            for repo in repositories:
                repo_writer.writerow(repo)

    print("Data saved to repositories.csv")

# Run the main function
if __name__ == "__main__":
    main()








































'''

import requests 
import csv

GITHUB_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjEwMDE5ODFAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.yVytEJB5w0iOk2ijlLKbx2ieRlIbmzuC_QYl2c4EAuU'
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_users_in_bangalore(headers):
    users = []
    page = 1
    while True:
        response = requests.get(f"https://api.github.com/search/users?q=location:Bangalore+followers:>100&per_page=100&page={page}", headers=headers)
        print(response.status_code, response.json())
        if response.status_code != 200:
            break
        items = response.json().get("items", [])
        if not items:
            break
        users.extend(items)
        page += 1
    return users

def get_user_details(username, headers):
    response = requests.get(f"https://api.github.com/users/{username}", headers=headers)
    return response.json() if response.status_code == 200 else None

def get_repos_of_user(username, headers):
    repos = []
    page = 1
    while True:
        response = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100&page={page}", headers=headers)
        if response.status_code != 200:
            break
        items = response.json()
        if not items:
            break
        repos.extend(items)
        page += 1
    return repos

def clean_company_name(name):
    if name:
        return name.strip().lstrip('@').upper()
    return ''

def save_users_to_csv(users):
    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'name', 'company', 'location', 'email', 'hireable', 'bio', 'public_repos', 'followers', 'following', 'created_at'])
        for user in users:
            details = get_user_details(user['login'], HEADERS)
            if details:
                writer.writerow([
                    details['login'],
                    details.get('name', ''),
                    clean_company_name(details.get('company', '')),
                    details.get('location', ''),
                    details.get('email', ''),
                    details.get('hireable', ''),
                    details.get('bio', ''),
                    details.get('public_repos', ''),
                    details.get('followers', ''),
                    details.get('following', ''),
                    details.get('created_at', '')
                ])

def save_repos_to_csv(user_repos):
    with open('repositories.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name'])
        for user in user_repos:
            for repo in user['repos']:
                writer.writerow([
                    user['login'],
                    repo.get('full_name', ''),
                    repo.get('created_at', ''),
                    repo.get('stargazers_count', ''),
                    repo.get('watchers_count', ''),
                    repo.get('language', ''),
                    repo.get('has_projects', ''),
                    repo.get('has_wiki', ''),
                    repo['license']['name'] if repo.get('license') else ''
                ])

def main():
    users = get_users_in_bangalore(HEADERS)
    user_repos = [{'login': user['login'], 'repos': get_repos_of_user(user['login'], HEADERS)} for user in users]
    
    save_users_to_csv(users)
    save_repos_to_csv(user_repos)
    
    with open('README.md', 'w') as file:
        file.write("# GitHub Users and Repositories from Bangalore\n")
        file.write("This repository contains users from Bangalore with more than 100 followers and their repositories.\n")

if __name__ == "__main__":
    main()

'''