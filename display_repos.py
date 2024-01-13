import requests
import getpass

def get_repos(user, token):
    url = f"https://api.github.com/users/{user}/repos"
    headers = {"Authorization": f"Token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_repos(user, token):
    repos = get_repos(user, token)
    if repos is not None:
        for repo in repos:
            print(f"Name: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Stars: {repo['stargazers_count']}")
            print()
    else:
        print("Error retrieving repositories")

if __name__ == "__main__":
    user = input("Enter GitHub username: ")
    token = getpass.getpass(prompt="Enter personal access token: ")
    display_repos(user, token)
