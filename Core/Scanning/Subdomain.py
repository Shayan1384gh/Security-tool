import socket
from urllib.parse import urlparse
from tqdm import tqdm


COMMON_SUBDOMAINS = [
    # Common
    "www", "api", "app", "admin", "portal", "dashboard",

    # Mail
    "mail", "webmail", "smtp", "imap", "pop", "mx",

    # Development
    "dev", "test", "staging", "stage", "beta", "alpha",
    "demo", "uat", "qa", "preprod", "prod",

    # Infrastructure
    "vpn", "gateway", "proxy", "remote", "access",
    "firewall", "dns", "ns1", "ns2", "ns3",

    # Hosting
    "cpanel", "whm", "plesk", "host", "server",

    # Storage
    "cdn", "static", "media", "assets", "files",
    "download", "uploads", "backup", "storage",

    # Web Apps
    "blog", "shop", "store", "forum", "wiki",
    "support", "help", "docs", "kb",

    # Monitoring
    "monitor", "status", "uptime", "health",
    "grafana", "kibana", "elk",

    # Databases
    "db", "mysql", "mongo", "redis",
    "postgres", "pgadmin",

    # CI/CD
    "git", "github", "gitlab",
    "jenkins", "ci", "cd", "build",

    # Cloud
    "cloud", "aws", "azure", "gcp",
    "s3", "bucket", "object",

    # Security
    "auth", "login", "sso", "identity",
    "secure", "security",

    # Internal
    "internal", "intranet", "corp",
    "office", "staff", "employee",

    # Network
    "router", "switch", "network",
    "vpn", "gw",

    # Mobile
    "m", "mobile", "api-mobile",

    # Misc
    "search", "news", "img",
    "video", "cdn1", "cdn2"
]


def get_domain(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc:
        return parsed_url.netloc
    return parsed_url.path

def check_subdomain(subdomain):
    try:
        ip = socket.gethostbyname(subdomain)
        return ip
    except:
        return None

def run_subdomain(target):
    domain = get_domain(target)
    print(f"\n🎯 Target: {domain}")
    print(f"🔍 Testing {len(COMMON_SUBDOMAINS)} subdomains")
    print("=" * 60)

    found = []
    for word in tqdm(COMMON_SUBDOMAINS, desc = "🌐 Scanning" , unit = "subdomain" ):
        subdomain = f"{word}.{domain}"
        ip = check_subdomain(subdomain)
    if ip:
        found.append((subdomain, ip))
        tqdm.write(
            f"✅ FOUND -> {subdomain} | IP: {ip}"
        )

    print("\n" + "=" * 60)
    if found:
        print(f"🎉 Found {len(found)} subdomains:\n")

        for subdomain, ip in found:
            print(f"🌐 {subdomain}")
            print(f"📍 {ip}")
            print("-" * 40)

    else:
        print("❌ No subdomains found")

    print("=" * 60)

    return found

target = input("🎯 Enter Domain: ")

run_subdomain(target)



