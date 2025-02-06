import os
import time

# ---------- Color Codes ---------- #
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
reset = "\033[0m"

# ---------- Function to Clear Screen ---------- #
def clear():
    os.system("clear")

# ---------- Function to Install Tools with Guide ---------- #
def install_tool(tool_name, install_command, usage_command, description):
    clear()
    print(f"{yellow}ЁЯФД Installing {tool_name}...{reset}")
    os.system(install_command)
    print(f"{green}тЬЕ {tool_name} Installed Successfully!{reset}\n")
    print(f"{blue}ЁЯУМ How to Use {tool_name}:{reset}")
    print(f"{description}\n")
    print(f"ЁЯСЙ Run this command: {yellow}{usage_command}{reset}\n")
    input("Press Enter to continue...")

# ---------- Main Menu ---------- #
def main():
    while True:
        clear()
        print(f"""{green}
        ЁЯФе Ultimate Termux Hacking Toolkit ЁЯФе
        -------------------------------------
        [1] Nmap (Network Scanning)
        [2] Metasploit (Penetration Testing)
        [3] Sqlmap (SQL Injection)
        [4] Hydra (Brute Force Attack)
        [5] Nikto (Web Vulnerability Scanner)
        [6] Aircrack-ng (WiFi Hacking)
        [7] Wifite (Automated WiFi Hacking)
        [8] Slowloris (DDoS Attack)
        [9] Hammer (DDoS Attack)
        [10] SocialFish (Phishing Attack)
        [11] Zphisher (Advanced Phishing)
        [12] Subfinder (Subdomain Finder)
        [13] Tor & Anonsurf (Anonymous Browsing)
        [14] Update All Tools
        [0] Exit
        -------------------------------------{reset}
        """)

        choice = input(f"{yellow}Select an option: {reset}")

        if choice == "1":
            install_tool("Nmap", "pkg install nmap -y", "nmap -h", 
            "Nmap ржПржХржЯрж┐ ржирзЗржЯржУрзЯрж╛рж░рзНржХ рж╕рзНржХрзНржпрж╛ржирж┐ржВ ржЯрзБрж▓ред ржПржЯрж┐ ржжрж┐рзЯрзЗ IP, Ports, ржПржмржВ Vulnerability ржЪрзЗржХ ржХрж░рж╛ ржпрж╛рзЯред")
            
        elif choice == "2":
            install_tool("Metasploit", "pkg install unstable-repo && pkg install metasploit -y", "msfconsole", 
            "Metasploit ржПржХржЯрж┐ рж╢ржХрзНрждрж┐рж╢рж╛рж▓рзА Penetration Testing Frameworkред ржПржЯрж┐ ржжрж┐рзЯрзЗ Exploit ржЪрж╛рж▓рж╛ржирзЛ ржпрж╛рзЯред")

        elif choice == "3":
            install_tool("Sqlmap", "pkg install python && pip install sqlmap", "sqlmap -h", 
            "Sqlmap ржПржХржЯрж┐ SQL Injection ржЯрзБрж▓ ржпрж╛ ржУрзЯрзЗржмрж╕рж╛ржЗржЯрзЗрж░ Database Hack ржХрж░рждрзЗ ржмрзНржпржмрж╣рж╛рж░ ржХрж░рж╛ рж╣рзЯред")

        elif choice == "4":
            install_tool("Hydra", "pkg install hydra -y", "hydra -h", 
            "Hydra ржПржХржЯрж┐ Brute Force Attack ржЯрзБрж▓ ржпрж╛ Username & Password Crack ржХрж░рждрзЗ рж╕рж╛рж╣рж╛ржпрзНржп ржХрж░рзЗред")

        elif choice == "5":
            install_tool("Nikto", "pkg install perl && pkg install nikto -y", "nikto -h", 
            "Nikto ржПржХржЯрж┐ Web Vulnerability Scanner, ржпрж╛ ржУрзЯрзЗржмрж╕рж╛ржЗржЯрзЗрж░ ржжрзБрж░рзНржмрж▓рждрж╛ ржЪрзЗржХ ржХрж░рждрзЗ ржмрзНржпржмрж╣рж╛рж░ ржХрж░рж╛ рж╣рзЯред")

        elif choice == "6":
            install_tool("Aircrack-ng", "pkg install aircrack-ng -y", "airmon-ng", 
            "Aircrack-ng ржПржХржЯрж┐ WiFi Hacking ржЯрзБрж▓, ржпрж╛ WPA & WEP Networks Crack ржХрж░рждрзЗ ржкрж╛рж░рзЗред")

        elif choice == "7":
            install_tool("Wifite", "pkg install wifite -y", "wifite", 
            "Wifite ржПржХржЯрж┐ Automated WiFi Hacking ржЯрзБрж▓ ржпрж╛ Aircrack-ng ржПрж░ рж╕рж╛ржерзЗ ржХрж╛ржЬ ржХрж░рзЗред")

        elif choice == "8":
            install_tool("Slowloris", "git clone https://github.com/gkbrk/slowloris.git && cd slowloris && python3 slowloris.py", 
            "python3 slowloris.py -h", "Slowloris ржПржХржЯрж┐ DDoS Attack Tool ржпрж╛ ржУрзЯрзЗржмрж╕рж╛ржЗржЯ Down ржХрж░рждрзЗ ржкрж╛рж░рзЗред")

        elif choice == "9":
            install_tool("Hammer", "git clone https://github.com/cyweb/hammer.git && cd hammer && python3 hammer.py", 
            "python3 hammer.py", "Hammer ржПржХржЯрж┐ DDoS Attack ржЯрзБрж▓ ржпрж╛ ржУрзЯрзЗржмрж╕рж╛ржЗржЯрзЗрж░ рж╕рж╛рж░рзНржнрж╛рж░ Flood ржХрж░рзЗред")

        elif choice == "10":
            install_tool("SocialFish", "git clone https://github.com/UndeadSec/SocialFish.git && cd SocialFish && python3 SocialFish.py", 
            "python3 SocialFish.py", "SocialFish ржПржХржЯрж┐ Phishing Attack ржЯрзБрж▓ ржпрж╛ Facebook, Gmail, Instagram Hack ржХрж░рждрзЗ ржкрж╛рж░рзЗред")

        elif choice == "11":
            install_tool("Zphisher", "git clone https://github.com/htr-tech/zphisher.git && cd zphisher && bash zphisher.sh", 
            "bash zphisher.sh", "Zphisher ржПржХржЯрж┐ Advanced Phishing Tool ржпрж╛ ржмрж┐ржнрж┐ржирзНржи рж╕рж╛ржЗржЯрзЗрж░ Fake Login Page рждрзИрж░рж┐ ржХрж░рзЗред")

        elif choice == "12":
            install_tool("Subfinder", "pkg install subfinder -y", "subfinder -d example.com", 
            "Subfinder ржПржХржЯрж┐ Subdomain Finder ржпрж╛ ржУрзЯрзЗржмрж╕рж╛ржЗржЯрзЗрж░ Hidden Subdomains ржЦрзБржБржЬрзЗ ржмрзЗрж░ ржХрж░рзЗред")

        elif choice == "13":
            install_tool("Tor & Anonsurf", "pkg install tor && pkg install anonsurf -y", "anonsurf start", 
            "Tor & Anonsurf ржПржХржЯрж┐ Anonymous Browsing ржЯрзБрж▓ ржпрж╛ рждрзЛржорж╛ржХрзЗ ржЕржЬрж╛ржирж╛ рж░рж╛ржЦрждрзЗ рж╕рж╛рж╣рж╛ржпрзНржп ржХрж░ржмрзЗред")

        elif choice == "14":
            print(f"{yellow}ЁЯФД Updating All Tools...{reset}")
            os.system("pkg update -y && pkg upgrade -y")
            print(f"{green}тЬЕ All Tools Updated Successfully!{reset}")

        elif choice == "0":
            print(f"{red}Exiting...{reset}")
            break

        else:
            print(f"{red}тЭМ Invalid choice! Try again.{reset}")

        time.sleep(2)

# ---------- Run the Script ---------- #
if __name__ == "__main__":
    main()
