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
    print(f"{yellow}🔄 Installing {tool_name}...{reset}")
    os.system(install_command)
    print(f"{green}✅ {tool_name} Installed Successfully!{reset}\n")
    print(f"{blue}📌 How to Use {tool_name}:{reset}")
    print(f"{description}\n")
    print(f"👉 Run this command: {yellow}{usage_command}{reset}\n")
    input("Press Enter to continue...")

# ---------- Main Menu ---------- #
def main():
    while True:
        clear()
        print(f"""{green}
        🔥 Ultimate Termux Hacking Toolkit 🔥
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
            "Nmap একটি নেটওয়ার্ক স্ক্যানিং টুল। এটি দিয়ে IP, Ports, এবং Vulnerability চেক করা যায়।")
            
        elif choice == "2":
            install_tool("Metasploit", "pkg install unstable-repo && pkg install metasploit -y", "msfconsole", 
            "Metasploit একটি শক্তিশালী Penetration Testing Framework। এটি দিয়ে Exploit চালানো যায়।")

        elif choice == "3":
            install_tool("Sqlmap", "pkg install python && pip install sqlmap", "sqlmap -h", 
            "Sqlmap একটি SQL Injection টুল যা ওয়েবসাইটের Database Hack করতে ব্যবহার করা হয়।")

        elif choice == "4":
            install_tool("Hydra", "pkg install hydra -y", "hydra -h", 
            "Hydra একটি Brute Force Attack টুল যা Username & Password Crack করতে সাহায্য করে।")

        elif choice == "5":
            install_tool("Nikto", "pkg install perl && pkg install nikto -y", "nikto -h", 
            "Nikto একটি Web Vulnerability Scanner, যা ওয়েবসাইটের দুর্বলতা চেক করতে ব্যবহার করা হয়।")

        elif choice == "6":
            install_tool("Aircrack-ng", "pkg install aircrack-ng -y", "airmon-ng", 
            "Aircrack-ng একটি WiFi Hacking টুল, যা WPA & WEP Networks Crack করতে পারে।")

        elif choice == "7":
            install_tool("Wifite", "pkg install wifite -y", "wifite", 
            "Wifite একটি Automated WiFi Hacking টুল যা Aircrack-ng এর সাথে কাজ করে।")

        elif choice == "8":
            install_tool("Slowloris", "git clone https://github.com/gkbrk/slowloris.git && cd slowloris && python3 slowloris.py", 
            "python3 slowloris.py -h", "Slowloris একটি DDoS Attack Tool যা ওয়েবসাইট Down করতে পারে।")

        elif choice == "9":
            install_tool("Hammer", "git clone https://github.com/cyweb/hammer.git && cd hammer && python3 hammer.py", 
            "python3 hammer.py", "Hammer একটি DDoS Attack টুল যা ওয়েবসাইটের সার্ভার Flood করে।")

        elif choice == "10":
            install_tool("SocialFish", "git clone https://github.com/UndeadSec/SocialFish.git && cd SocialFish && python3 SocialFish.py", 
            "python3 SocialFish.py", "SocialFish একটি Phishing Attack টুল যা Facebook, Gmail, Instagram Hack করতে পারে।")

        elif choice == "11":
            install_tool("Zphisher", "git clone https://github.com/htr-tech/zphisher.git && cd zphisher && bash zphisher.sh", 
            "bash zphisher.sh", "Zphisher একটি Advanced Phishing Tool যা বিভিন্ন সাইটের Fake Login Page তৈরি করে।")

        elif choice == "12":
            install_tool("Subfinder", "pkg install subfinder -y", "subfinder -d example.com", 
            "Subfinder একটি Subdomain Finder যা ওয়েবসাইটের Hidden Subdomains খুঁজে বের করে।")

        elif choice == "13":
            install_tool("Tor & Anonsurf", "pkg install tor && pkg install anonsurf -y", "anonsurf start", 
            "Tor & Anonsurf একটি Anonymous Browsing টুল যা তোমাকে অজানা রাখতে সাহায্য করবে।")

        elif choice == "14":
            print(f"{yellow}🔄 Updating All Tools...{reset}")
            os.system("pkg update -y && pkg upgrade -y")
            print(f"{green}✅ All Tools Updated Successfully!{reset}")

        elif choice == "0":
            print(f"{red}Exiting...{reset}")
            break

        else:
            print(f"{red}❌ Invalid choice! Try again.{reset}")

        time.sleep(2)

# ---------- Run the Script ---------- #
if __name__ == "__main__":
    main()
