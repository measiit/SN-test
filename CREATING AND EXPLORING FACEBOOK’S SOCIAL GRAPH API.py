
import requests

# Paste your access token here
access_token = "EAAR0ZAhPwkuEBRLqFVAMmxelPDMrVZA1IZBugc52ENQcqJ5OxhqWl10yGGkXGqpsS6ZAeOZCZA9VzRfiPIweBb18yNHCGx5bZBLnINCZBlyQZCyZCyv1ZBgrHxi5yWofy4WgNAPZAQZB9q5rAaJLGm4D5FclPteFJQtbg9O2YIZCVThGM2DReNE66A2g2Sbj6nsgF5W8ZBYxqZAlXNBYsB9X16dsLNIFeZB6rg8lgsQ7J6AZAu7ocZD"

# Get basic profile data
url = "https://graph.facebook.com/me?access_token=" + access_token

response = requests.get(url)
data = response.json()

# Print output
print("Name:", data["name"])
print("ID:", data["id"])
