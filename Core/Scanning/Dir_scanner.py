import requests
import threading
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from tqdm import tqdm
import time

common_directories = [

    "admin", "administrator", "admincp", "adminarea", "backend", "manage",
    "administrator", "webadmin", "sysadmin", "root", "manager", "moderator",

    "backup", "backups", "back", "bak", "old", "backup-old", "backup_old",
    "config", "configuration", "settings", "setup", "install", "conf",

    "api", "v1", "v2", "v3", "api/v1", "api/v2", "rest", "graphql",
    "test", "tests", "testing", "dev", "development", "staging", "stage",
    "beta", "alpha", "demo", "example", "sandbox",

    ".git", ".svn", ".hg", ".env", ".htaccess", ".htpasswd", "cgi-bin",
    "error_log", "logs", "log", "tmp", "temp", "cache", "storage",

    "wp-admin", "wp-content", "wp-includes", "wp-json", "wp-login", "wp-signup",
    "wp-cron", "xmlrpc", "wp-config", "wp-config.php", "wp-content/uploads",
    "wp-content/plugins", "wp-content/themes", "wp-content/cache",

    "administrator", "components", "modules", "plugins", "templates", "cache",
    "logs", "tmp", "images", "media", "language", "includes", "libraries",

    "core", "modules", "profiles", "sites", "themes", "vendor",

    "css", "js", "images", "img", "assets", "static", "public", "dist",
    "uploads", "downloads", "files", "media", "resources", "content",

    "login", "signin", "signup", "register", "auth", "logout", "profile",
    "dashboard", "panel", "controlpanel", "cpanel", "webmail",

    "phpmyadmin", "mysql", "db", "database", "sql", "adminer", "myadmin",
    "pma", "phpPgAdmin", "pgadmin",

    "cgi", "cgi-bin", "fcgi", "php", "asp", "jsp", "node", "python",
    "git", "github", "deploy", "build", "dist", "release"
]

url_web = input("🎯 Enter URL: ")


def directory_scanner(url, directory):
    param = urlparse(url)
    if param.path.endswith('/'):
        new_path = param.path + directory + "/"
    else:
        new_path = param.path + "/" + directory + "/"
    new_url = urlunparse((param.scheme, param.netloc, new_path, param.params, param.query, param.fragment))
    return new_url


def run_scanner(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Directory Scanner)"
    }
    list_directory = []

    print(f"\n🔍 Starting directory scan on: {url}")
    print(f"📁 Directories to test: {len(common_directories)}")
    print("=" * 60)

    for url_direct in tqdm(common_directories, desc="📂 Scanning directories", unit="dir"):
        test_url = directory_scanner(url, url_direct)

        try:
            response = requests.get(test_url, headers=headers, timeout=5)

            if response.status_code == 200:
                list_directory.append((test_url, url_direct))
                tqdm.write(f"\n✅ [FOUND] {url_direct} → Status: {response.status_code}")
                tqdm.write(f"   📍 URL: {test_url}\n")

            elif response.status_code == 403:
                tqdm.write(f"⛔ [FORBIDDEN] {url_direct} → Status: 403 (Access denied)")

            elif response.status_code == 401:
                tqdm.write(f"🔐 [AUTH REQUIRED] {url_direct} → Status: 401")

            elif response.status_code == 404:
                pass

            else:
                tqdm.write(f"⚠️ [UNKNOWN] {url_direct} → Status: {response.status_code}")

        except requests.exceptions.Timeout:
            tqdm.write(f"⏰ [TIMEOUT] {url_direct}")
        except:
            pass

    print("\n" + "=" * 60)
    if list_directory:
        print(f"🎉 Scan completed! Found {len(list_directory)} accessible directories:")
        for url, dir_name in list_directory:
            print(f"   📁 {dir_name} → {url}")
    else:
        print("🔒 No accessible directories found (only showing status 200)")
    print("=" * 60)

    return list_directory


print(run_scanner(url_web))