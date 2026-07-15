import subprocess
import sys
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_banner():
    banner = """
    ╔══════════════════════════════════════════╗
    ║      🔥   - Security Tools -             ║
    ║         Version Control - Pro +          ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)


def show_menu():
    menu = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                     🛡️  Pentest Tool                         ║
    ║              Recon • OSINT • Web Security Tools              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║                                                              ║
    ║  [ 1 ] 🔍  Recon Scanner                                     ║
    ║  [ 2 ] 🚪  Port Scanner                                      ║
    ║  [ 3 ] 📁  Directory Scanner                                 ║
    ║  [ 4 ] 💥  DDoS Tester                                       ║
    ║  [ 5 ] 🕸️  XSS Scanner                                       ║
    ║  [ 6 ] 👤  Username Finder                                   ║
    ║  [ 7 ] 🌐  Subdomain Finder                                  ║
    ║  [ 8 ] 📍  IP Lookup                                         ║
    ║                                                              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  [ 0 ] ❌  Exit                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(menu)


def run_tool(tool_name):
    print(f"\n▶️  Running {tool_name}...\n")

    if tool_name == "Recon":
        subprocess.run([sys.executable, "Core/Scanning/Recon.py"])


    elif tool_name == "Port_scanner":

        subprocess.run([sys.executable, "Core/Scanning/Port_scanner.py"])


    elif tool_name == "Dir_scanner":

        subprocess.run([sys.executable, "Core/Scanning/Dir_scanner.py"])


    elif tool_name == "DDos":

        subprocess.run([sys.executable, "Core/Web-Attack/DDos.py"])


    elif tool_name == "Xss":

        subprocess.run([sys.executable, "Core/Web-Attack/Xss.py"])


    elif tool_name == "UsernameFounder":

        subprocess.run([sys.executable, "Core/OSINT/UsernameFounder.py"])


    elif tool_name == "Subdomain":

        subprocess.run([sys.executable, "Core/Scanning/Subdomain.py"])


    elif tool_name == "Ip_lookup":

        subprocess.run([sys.executable, "Core/OSINT/Ip_lookup.py"])

    print("\n✅ Tool execution completed!")
    input("\nPress Enter to continue...")


def main():
    while True:
        clear_screen()
        show_banner()
        show_menu()

        choice = input("\n⚡ Enter your choice (0-8): ").strip()

        if choice == "1":
            run_tool("Recon")
        elif choice == "2":
            run_tool("Port_scanner")
        elif choice == "3":
            run_tool("Dir_scanner")
        elif choice == "4":
            run_tool("DDos")
        elif choice == "5":
            run_tool("Xss")
        elif choice == "6":
            run_tool("UsernameFounder")
        elif choice == "7":
            run_tool("Subdomain")
        elif choice == "8":
            run_tool("Ip_lookup")
        elif choice == "0":
            print("\n👋 Goodbye from PsychoTeam!")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice! Please try again.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
