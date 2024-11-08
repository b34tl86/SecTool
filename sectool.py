import os
from colorama import Fore, Style, init

# Check if colorama is installed, if not, install it
try:
    from colorama import Fore, Style, init
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, Style, init

# Initialize colorama
init()

def install_package(package_name):
    os.system(f"sudo apt-get install {package_name}")

def clear_screen():
    os.system("clear")

def display_menu(menu_options, menu_name):
    clear_screen()
    print_banner()

    print(f"\n{Fore.RED}{Style.BRIGHT}{menu_name} Menu:{Style.RESET_ALL}")
    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")

    choice = input("\nEnter your choice (q to quit, b to go back): ")
    return choice

def print_banner():
    banner = f"""
    {Fore.RED}{Style.BRIGHT}███████ ▓█████  ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
    ░ ▓██▄   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
    ▒██████▒▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒ Ver.2.1
    ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒       ░      ░  ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
    ░  ░  ░     ░   ░          ░      ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
          ░     ░  ░░ ░                   ░ ░      ░ ░      ░  
                    ░                                          
                                    Made with ❤️️ by s1lv3r{Style.RESET_ALL}
    """

    print(banner)

def clone_repo(repo_url, repo_name, install_path="/opt/"):
    full_path = os.path.join(install_path, repo_name)
    if os.path.exists(full_path):
        os.system(f"sudo rm -rf {full_path}")

    os.system(f"sudo git clone {repo_url} {full_path}")

def install_utility_tools():
    utility_tools_menu = [
        "chromium-browser",
        "geany",
        "gedit",
        "synaptic",
        "Install All",
        "Back to Main Menu"
    ]

    while True:
        choice = display_menu(utility_tools_menu, "Utility Tools")

        if choice == 'q':
            break
        elif choice == 'b':
            return  # Go back to the main menu
        elif choice.isdigit() and 1 <= int(choice) <= len(utility_tools_menu):
            if int(choice) == len(utility_tools_menu) - 1:
                # Install all utility tools
                for tool in utility_tools_menu[:-2]:
                    os.system(f"sudo apt-get purge -y {tool} && sudo apt-get autoremove -y && sudo apt-get install -y {tool}")
                print_banner()
            elif int(choice) == len(utility_tools_menu):
                return  # Go back to the main menu
            else:
                os.system(f"sudo apt-get purge -y {utility_tools_menu[int(choice) - 1]} && sudo apt-get autoremove -y && sudo apt-get install -y {utility_tools_menu[int(choice) - 1]}")
                print_banner()
        else:
            print("Invalid choice. Please try again.")
def install_security_tools():
    security_tools_menu = [
        "AutoRecon (https://github.com/Tib3rius/AutoRecon.git)",
        "Ghauri (https://github.com/r0oth3x49/ghauri.git)",
        "GooFuzz (https://github.com/m3n0sd0n4ld/GooFuzz.git)",
        "ParamSpider (https://github.com/devanshbatham/paramspider)",
        "PhoneSploit-Pro (https://github.com/AzeemIdrisi/PhoneSploit-Pro.git)",
        "BirDuster (https://www.github.com/ytisf/BirDuster)",
        "NucleiScanner (https://github.com/0xKayala/NucleiScanner.git)",
        "Install All",
        "Back to Main Menu"
    ]

    def install_tool_by_choice(choice):
        """Install a specific tool based on menu choice number."""
        if choice == 1:
            clone_repo("https://github.com/Tib3rius/AutoRecon.git", "AutoRecon")
            os.system("cd /opt/AutoRecon && python3 -m pip install -r requirements.txt")  
        elif choice == 2:
            clone_repo("https://github.com/r0oth3x49/ghauri.git", "ghauri")
            os.system("cd /opt/ghauri && python3 -m pip install --upgrade -r requirements.txt && python3 -m pip install -e")
        elif choice == 3:
            clone_repo("https://github.com/m3n0sd0n4ld/GooFuzz.git", "GooFuzz")
            os.system("cd /opt/GooFuzz && sudo chmod +x GooFuzz")
        elif choice == 4:
            clone_repo("https://github.com/devanshbatham/paramspider", "paramspider")
            os.system("cd /opt/paramspider && sudo pip install .")
        elif choice == 5:
            clone_repo("https://github.com/AzeemIdrisi/PhoneSploit-Pro.git", "PhoneSploit-Pro")
            os.system("cd /opt/PhoneSploit-Pro && sudo pip install -r requirements.txt")
        elif choice == 6:
            clone_repo("https://www.github.com/ytisf/BirDuster", "BirDuster")
            os.system("cd /opt/BirDuster && sudo pip3 install --user -r requirements.txt")
        elif choice == 7:
            clone_repo("https://github.com/0xKayala/NucleiScanner.git", "NucleiScanner")
            os.system("cd /opt/NucleiScanner && cd NucleiScanner && sudo chmod +x install.sh && ./install.sh && ns -h && cd ..")
        print_banner()

    while True:
        choice = display_menu(security_tools_menu, "Security Tools")

        if choice == 'q':
            break
        elif choice == 'b':
            return  # Go back to the main menu
        elif choice.isdigit() and 1 <= int(choice) <= len(security_tools_menu):
            choice = int(choice)
            if choice == len(security_tools_menu) - 1:
                # Install all security tools
                for i in range(1, len(security_tools_menu) - 1):
                    install_tool_by_choice(i)
            elif choice == len(security_tools_menu):
                return  # Go back to the main menu
            else:
                install_tool_by_choice(choice)
        else:
            print("Invalid choice. Please try again.")


def install_osint_tools():
    osint_tools_menu = [
        "BlackBird (https://github.com/p1ngul1n0/blackbird)",
        "Mr. Holmes (https://github.com/Lucksi/Mr.Holmes)",
        "SIGIT (https://github.com/termuxhackers-id/SIGIT.git)",
        "Alfred (https://github.com/alfredredbird/alfred)",
        "Back to Main Menu"
    ]

    while True:
        choice = display_menu(osint_tools_menu, "OSINT Tools")

        if choice == 'q':
            break
        elif choice == 'b':
            return  # Go back to the main menu
        elif choice.isdigit() and 1 <= int(choice) <= len(osint_tools_menu):
            if int(choice) == 1:
                # Install BlackBird
                repo_url = "https://github.com/p1ngul1n0/blackbird"
                repo_name = repo_url.split("/")[-1]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && pip install -r requirements.txt")
                print_banner()
            elif int(choice) == 2:
                # Install Mr. Holmes
                repo_url = "https://github.com/Lucksi/Mr.Holmes"
                repo_name = repo_url.split("/")[-1]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && sudo chmod +x install.sh && sudo bash install.sh")
                print_banner()
            elif int(choice) == 3:
                # Install SIGIT
                repo_url = "https://github.com/termuxhackers-id/SIGIT.git"
                repo_name = "SIGIT"
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && bash installkali.sh")
                print_banner()
            elif int(choice) == 4:
                # Install Alfred
                repo_url = "https://github.com/alfredredbird/alfred"
                repo_name = repo_url.split("/")[-1]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && sudo pip3 install -r requirements.txt")
                print_banner()
            elif int(choice) == 5:
                return  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")

def remove_projectdiscovery_tools():
    # List of common ProjectDiscovery tools to remove
    projectdiscovery_tools = [
        "nuclei",
        "httpx",
        "naabu",
        "subfinder",
        "dnsx",
        "pdtm"
    ]

    for tool in projectdiscovery_tools:
        os.system(f"sudo rm -f /usr/local/bin/{tool}")  # Remove tool from common install paths
        os.system(f"sudo apt-get remove --purge -y {tool}")  # Remove if installed through package manager
        os.system("sudo apt-get autoremove -y")

    print("All ProjectDiscovery tools have been removed.")

def install_other_tools():
    other_tools_menu = [
        "PDTM (github.com/projectdiscovery/pdtm)",
        "Webcopilot (github.com/h4r5h1t/webcopilot)",
        "FatRat (https://github.com/Screetsec/TheFatRat.git)",
        "Nucleimonst3r (https://github.com/blackhatethicalhacking/Nucleimonst3r.git)",
        "CyberPhish (https://github.com/Cyber-Dioxide/CyberPhish)",
        "Back to Main Menu"
    ]

    def install_cyberphish():
        """Install CyberPhish tool to /opt."""
        # Step 1: Install colorama dependency if not already installed
        os.system("pip install colorama")

        # Step 2: Clone CyberPhish repository to /opt
        repo_url = "https://github.com/Cyber-Dioxide/CyberPhish"
        repo_name = "CyberPhish"
        full_path = os.path.join("/opt", repo_name)

        if os.path.exists(full_path):
            os.system(f"sudo rm -rf {full_path}")

        os.system(f"sudo git clone {repo_url} {full_path}")
        
        # Step 3: Install requirements
        os.system(f"cd {full_path} && sudo pip install -r requirements.txt")
        print_banner()

    while True:
        choice = display_menu(other_tools_menu, "Other Tools")

        if choice == 'q':
            break
        elif choice == 'b':
            return  # Go back to the main menu
        elif choice.isdigit() and 1 <= int(choice) <= len(other_tools_menu):
            choice = int(choice)
            if choice == 1:
                # Install PDTM
                os.system("go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest")
                os.system("source ~/.zshrc")  # Source the zshrc file
                os.system("~/go/bin/pdtm -ia")  # Run pdtm -ia
                print_banner()
            elif choice == 2:
                # Install Webcopilot
                repo_url = "https://github.com/h4r5h1t/webcopilot"
                repo_name = repo_url.split("/")[-1]
                full_path = os.path.join("/opt", repo_name)

                if os.path.exists(full_path):
                    os.system(f"sudo rm -rf {full_path}")

                os.system(f"sudo git clone {repo_url} {full_path}")
                os.system(f"cd {full_path} && sudo chmod +x webcopilot install.sh && sudo mv webcopilot /usr/bin/ && sudo ./install.sh")
                print_banner()
            elif choice == 3:
                # Install TheFatRat
                repo_url = "https://github.com/Screetsec/TheFatRat.git"
                repo_name = repo_url.split("/")[-1]
                full_path = os.path.join("/opt", repo_name)

                if os.path.exists(full_path):
                    os.system(f"sudo rm -rf {full_path}")

                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && sudo chmod +x setup.sh && sudo ./setup.sh")
                print_banner()
            elif choice == 4:
                # Install Nucleimonst3r
                install_nucleimonst3r()
            elif choice == 5:
                # Install CyberPhish
                install_cyberphish()
            elif choice == len(other_tools_menu):
                return  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")



def main_menu():
    main_menu_options = ["Utility Tools", "Security Tools", "OSINT Tools", "Other Tools"]

    while True:
        choice = display_menu(main_menu_options, "Main")

        if choice == 'q':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(main_menu_options):
            if int(choice) == 1:
                install_utility_tools()
            elif int(choice) == 2:
                install_security_tools()
            elif int(choice) == 3:
                install_osint_tools()
            elif int(choice) == 4:
                install_other_tools()  # Add the new option for "Other Tools"
            # Add more options for other menus if needed
            else:
                pass
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
