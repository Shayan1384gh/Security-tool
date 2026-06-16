import threading
import requests

username = input("Enter the username you are looking for: ")

sites = {
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "DevTo": "https://dev.to/{}",
    "Medium": "https://medium.com/@{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "CodePen": "https://codepen.io/{}",
    "Replit": "https://replit.com/@{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "LeetCode": "https://leetcode.com/{}",
    "Codeforces": "https://codeforces.com/profile/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "DockerHub": "https://hub.docker.com/u/{}",
    "PyPI": "https://pypi.org/user/{}",
    "Giters": "https://giters.com/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Gravatar": "https://gravatar.com/{}",
    "Keybase": "https://keybase.io/{}",
    "BuyMeACoffee": "https://www.buymeacoffee.com/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "Patreon": "https://www.patreon.com/{}"
}

results = []
lock = threading.Lock()

def user_checker(site, url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers = headers, timeout=6)
        if response.status_code == 200:
            print(f"found on {site}")
            with lock:
                results.append({"site": site,"url": url, "status": "found"})
        else:
            print(f"not found on {site}")
    except requests.RequestException:
        print(f"error on {site}")

threads = []

for site, pattern in sites.items():
    profile_url = pattern.format(username)
    t = threading.Thread(target=user_checker, args=(site, profile_url))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nFinal Results:")
print(results)
