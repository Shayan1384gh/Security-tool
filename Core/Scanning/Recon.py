import sys
from bs4 import BeautifulSoup
import requests
import socket
from urllib.parse import urlparse


class Recon:
    def __init__(self, url):
        self.url = url
        self.headers = {}
        self.technologies = []
        self.domain_info = {}
        self.result_scan = {
            "domain_info": {},
            "technologies": [],
            "headers": {},
        }

    def run_recon(self):
        print("\n" + "=" * 60)
        print(f"🎯 STARTING RECON SCAN FOR: {self.url}")
        print("=" * 60 + "\n")

        self.domain_info = self._get_domain_info(self.url)
        self.result_scan["domain_info"] = self.domain_info

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
            response = requests.get(self.url, headers=headers, timeout=10)
            response.raise_for_status()
            self.headers = dict(response.headers)
            self.result_scan["headers"] = self.headers
            self._find_technology(response)
        except requests.exceptions.Timeout:
            print(f"❌ Request timed out for {self.url}")

        self._print_results()
        return self.result_scan

    def _get_domain_info(self, url) -> dict:
        domain_info = {"domain": url, "ip_address": None}
        parsed_url = urlparse(url)
        domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path

        if not domain:
            print(f"⚠️ No domain found for {self.url}")
            return domain_info

        try:
            ip_address = socket.gethostbyname(domain)
            domain_info["ip_address"] = ip_address
            print(f"✅ Domain resolved: {domain} → {ip_address}")
        except socket.gaierror:
            print(f"❌ Could not resolve host: {domain}")

        return domain_info

    def _find_technology(self, response: requests.Response):
        if "server" in response.headers:
            server_header = response.headers["server"]
            self.technologies.append(server_header)
            print(f"🔧 Server: {server_header}")

        soup = BeautifulSoup(response.text, "html.parser")

        for script_tag in soup.find_all("script", src=True):
            src_lower = script_tag["src"].lower()

            if "react" in src_lower:
                self.technologies.append("React")
                print(f"📦 JavaScript Framework: React")
            elif "vue" in src_lower:
                self.technologies.append("Vue")
                print(f"📦 JavaScript Framework: Vue")
            elif "angular" in src_lower:
                self.technologies.append("Angular")
                print(f"📦 JavaScript Framework: Angular")

        if soup.find("meta", {"name": "generator"}):
            generator = soup.find("meta", {"name": "generator"})["content"]
            self.technologies.append(generator)
            print(f"⚙️ Generator: {generator}")

        if "/wp-content" in response.text or "/wp-includes" in response.text:
            is_already_added = any("WordPress" in tech for tech in self.technologies)
            if not is_already_added:
                self.technologies.append("WordPress")
                print(f"📝 CMS: WordPress")

        self.technologies = list(set(self.technologies))
        self.result_scan["technologies"] = self.technologies

    def _print_results(self):
        print("\n" + "=" * 60)
        print("📊 RECON RESULTS SUMMARY")
        print("=" * 60)

        print("\n🌐 DOMAIN INFORMATION:")
        print(f"   • URL: {self.result_scan['domain_info'].get('domain', 'N/A')}")
        print(f"   • IP Address: {self.result_scan['domain_info'].get('ip_address', 'N/A')}")

        print("\n🛠️ TECHNOLOGIES FOUND:")
        if self.result_scan['technologies']:
            for tech in self.result_scan['technologies']:
                print(f"   • {tech}")
        else:
            print("   • No technologies detected")
            print("\n📋 HTTP HEADERS:")
        if self.result_scan['headers']:
            for key, value in list(self.result_scan['headers'].items())[:10]:
                print(f"   • {key}: {value[:80]}{'...' if len(value) > 80 else ''}")
            if len(self.result_scan['headers']) > 10:
                print(f"   • ... and {len(self.result_scan['headers']) - 10} more headers")
        else:
            print("   • No headers found")

        print("\n" + "="*60)
        print("✅ SCAN COMPLETED SUCCESSFULLY")
        print("="*60 + "\n")




url = input("🎯 Please enter your URL: ")
scanner = Recon(url)
result = scanner.run_recon()