
import requests

# Paste your access token here
access_token = "EAAR0ZAhPwkuEBRCX7gwZBGym9kNLuZCZBhlxhLPoZAWk2ng8MPTSRq5HPSH846FHakCHeZCfKZBOB2O21mjIM5KlWf1ZC9SmzgGAMDWOQzvOfc8VQXYwnGErUCG9OIJteV6KSDZAZA5Qbt1Lrkmvi5qfrJQdIqYRYZCOC7kVGZCQyZAZABeTsKfZAKGbdZBaQXJyDMawdUy5mvwrvyYglTC6cskv78LXbHDOMJPa2MZBVzUMM88bEAka0ZCA4ZAFxacwnVmSGKR8T72fqUw1ajYZA4VxZCeunh19klXueNp9XByVL15phZBgFnC2w5rdbPoqsdZB2dyUB1v4KMcPMd4ZBep3IXuIsgZDZD"

# Get basic profile data
url = "https://graph.facebook.com/me?access_token=" + access_token

response = requests.get(url)
data = response.json()

# Print output
print("Name:", data["name"])
print("ID:", data["id"])
