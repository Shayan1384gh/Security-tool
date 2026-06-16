import ipaddress
import requests

ip = input("Enter your IP address: ")
api_key = "at_BwGqTBqQtngIZiitgZbzSR73iKOjJ"

def ip_check():
    try:
        ip_address = ipaddress.ip_address(ip)

        print("\n" + "═" * 50)
        print("🔎 IP VALIDATION")
        print("═" * 50)

        if ip_address.is_private:
            print(f"🔒 Type : Private IP")
        else:
            print(f"🌐 Type : Public IP")

        print(f"📌 Address : {ip_address}")

        print("═" * 50)

    except ValueError:
        print(f"❌ Invalid IP Address: {ip}")

def ip_lookup():
    try:
        response = requests.get(
            f"https://geo.ipify.org/api/v2/country,city,vpn?apiKey={api_key}&ipAddress={ip}",
            timeout=5
        )

        if (response.status_code== 200):
            data = response.json()
            location = data.get("location", {})

            print("\n" + "═" * 50)
            print("🌍 IP LOOKUP RESULT")
            print("═" * 50)

            print(f"📌 IP Address : {data.get('ip')}")
            print(f"🌎 Country    : {location.get('country')}")
            print(f"🏙️ City       : {location.get('city')}")
            print(f"🗺️ Region     : {location.get('region')}")
            print(f"📮 PostalCode : {location.get('postalCode')}")
            print(f"🕒 Timezone   : {location.get('timezone')}")
            print(f"📍 Latitude   : {location.get('lat')}")
            print(f"📍 Longitude  : {location.get('lng')}")

            print("═" * 50)

        else:
            print(f"❌ Request Failed ({response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")


ip_check()
ip_lookup()