import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\nUSER DETAILS")
        print("Name:", data.get("name"))
        print("Username:", data.get("login"))
        print("Followers:", data.get("followers"))
        print("Following:", data.get("following"))
        print("Public Repos:", data.get("public_repos"))
    elif response.status_code == 404:
        print("User not found.")
    else:
        print("Error:", response.status_code)


def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        print("\nREPOSITORIES:")
        for repo in repos[:5]:
            print(f"- {repo['name']} ⭐ {repo['stargazers_count']}")
    else:
        print("Error fetching repos:", response.status_code)


if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    get_user_info(username)
    get_repositories(username)
