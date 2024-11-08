import os
from colorama import Fore, Style, init

# Check and install colorama if not installed
try:
    from colorama import Fore, Style, init
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, Style, init

# Initialize colorama
init()

# Function to install packages
def install_package(package_name):
    os.system(f"sudo apt-get install {package_name}")

# Function to clear the terminal screen
def clear_screen():
    os.system("clear")

# Function to print banner
def print_banner():
    banner = f"""
    {Fore.RED}{Style.BRIGHT}███████ ▓█████  ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
    ░ ▓██▄   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
    ▒██████▒▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒ Ver.2.1
    ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒       ░      ░      ░ ░ ░ ░    ░ ░   
          ░     ░  ░░ ░                   ░ ░      ░ ░      ░  
                    ░                                          
                                    Made with ❤️️ by s1lv3r{Style.RESET_ALL}
    """
    print(banner)

# Function to clone a repository
def clone_repo(repo_url, repo_name, install_path="/opt/"):
    full_path = os.path.join(install_path, repo_name)
    if os.path.exists(full_path):
        os.system(f"sudo rm -rf {full_path}")
    os.system(f"sudo git clone {repo_url} {full_path}")

# Function to install a tool from a given URL and name
def install_tool(repo_url, install_script=None, post_install_commands=None):
    repo_name = repo_url.split("/")[-1].split(".git")[0]
    clone_repo(repo_url, repo_name)

    # Post-install commands
    if post_install_commands:
        for cmd in post_install_commands:
            os.system(f"cd {os.path.join('/opt', repo_name)} && {cmd}")

# Function to handle menu display and input
def display_menu(menu_options, menu_name):
    clear_screen()
    print_banner()
    print(f"\n{Fore.RED}{Style.BRIGHT}{menu_name} Menu:{Style.RESET_ALL}")
    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")

    print("\n")  # Extra space below options for separation
    choice = input("Enter your choice (A/B/Q): ")
    return choice.upper()

# Function for installing utility tools
def install_utility_tools():
    utility_tools_menu = [
        "chromium-browser",
        "geany",
        "gedit",
        "synaptic\n",
        
        "A - Install All",
        "B - Back to Main Menu",
        "Q - Quit"
    ]
    while True:
        choice = display_menu(utility_tools_menu, "Utility Tools")

        if choice == 'Q':
            break
        elif choice == 'B':
            return
        elif choice == 'A':
            # Install all utility tools
            for tool in utility_tools_menu[:-3]:
                os.system(f"sudo apt-get purge -y {tool} && sudo apt-get autoremove -y && sudo apt-get install -y {tool}")
            print_banner()
        elif choice.isdigit() and 1 <= int(choice) <= len(utility_tools_menu) - 3:
            os.system(f"sudo apt-get purge -y {utility_tools_menu[int(choice) - 1]} && sudo apt-get autoremove -y && sudo apt-get install -y {utility_tools_menu[int(choice) - 1]}")
            print_banner()
        else:
            print("Invalid choice. Please try again.")

# Function for installing security tools
def install_security_tools():
    security_tools_menu = [
        "AutoRecon (https://github.com/Tib3rius/AutoRecon.git)",
        "Ghauri (https://github.com/r0oth3x49/ghauri.git)",
        "GooFuzz (https://github.com/m3n0sd0n4ld/GooFuzz.git)",
        "ParamSpider (https://github.com/devanshbatham/paramspider)",
        "PhoneSploit-Pro (https://github.com/AzeemIdrisi/PhoneSploit-Pro.git)",
        "BirDuster (https://www.github.com/ytisf/BirDuster)\n",
        
        "A - Install All",
        "B - Back to Main Menu",
        "Q - Quit"
    ]
    while True:
        choice = display_menu(security_tools_menu, "Security Tools")

        if choice == 'Q':
            break
        elif choice == 'B':
            return
        elif choice == 'A':
            # Install all security tools
            install_tool("https://github.com/Tib3rius/AutoRecon.git", post_install_commands=["python3 -m pip install -r requirements.txt"])
            install_tool("https://github.com/r0oth3x49/ghauri.git", post_install_commands=["python3 -m pip install --upgrade -r requirements.txt", "python3 -m pip install -e"])
            install_tool("https://github.com/m3n0sd0n4ld/GooFuzz.git", post_install_commands=["sudo chmod +x GooFuzz"])
            install_tool("https://github.com/devanshbatham/paramspider", post_install_commands=["sudo pip install ."])
            install_tool("https://github.com/AzeemIdrisi/PhoneSploit-Pro.git", post_install_commands=["sudo pip install -r requirements.txt"])
            install_tool("https://www.github.com/ytisf/BirDuster", post_install_commands=["sudo pip3 install --user -r requirements.txt"])
            print_banner()
        elif choice == '1':
            # Install Autorecon
                repo_url = "https://github.com/Tib3rius/AutoRecon.git"
                repo_name = repo_url.split("/")[-1].split(".git")[0]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && python3 -m pip install -r requirements.txt")  
                print_banner()
        elif choice == '2':
                # Install Ghauri
                repo_url = "https://github.com/r0oth3x49/ghauri.git"
                repo_name = repo_url.split("/")[-1].split(".git")[0]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && python3 -m pip install --upgrade -r requirements.txt && python3 -m pip install -e")
                print_banner()
        elif int(choice) == 3:
                # Install GooFuzz
                repo_url = "https://github.com/m3n0sd0n4ld/GooFuzz.git"
                repo_name = repo_url.split("/")[-1].split(".git")[0]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && sudo chmod +x GooFuzz")
                print_banner()   
        elif int(choice) == 4:
                # Install ParamSpider
                repo_url = "https://github.com/devanshbatham/paramspider"
                repo_name = repo_url.split("/")[-1].split(".git")[0]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && sudo pip install .")
                print_banner()
        elif int(choice) == 5:
                # Install PhoneSploit-Pro
                repo_url = "https://github.com/AzeemIdrisi/PhoneSploit-Pro.git"
                repo_name = repo_url.split("/")[-1].split(".git")[0]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && sudo pip install -r requirements.txt")
                print_banner() 
        elif int(choice) == 6:
                # Install BirDuster
                repo_url = "https://www.github.com/ytisf/BirDuster"
                repo_name = repo_url.split("/")[-1].split(".git")[0]
                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && sudo pip3 install --user -r requirements.txt")
                print_banner()                                                           
        elif int(choice) == 7:
                return  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")

# Function for installing OSINT tools
def install_osint_tools():
    osint_tools_menu = [
        "BlackBird (https://github.com/p1ngul1n0/blackbird)",
        "Mr. Holmes (https://github.com/Lucksi/Mr.Holmes)",
        "SIGIT (https://github.com/termuxhackers-id/SIGIT.git)",
        "Alfred (https://github.com/alfredredbird/alfred)\n",
        
        "A - Install All",
        "B - Back to Main Menu",
        "Q - Quit"
    ]
    while True:
        choice = display_menu(osint_tools_menu, "OSINT Tools")

        if choice == 'Q':
            break
        elif choice == 'B':
            return
        elif choice == 'A':
            install_tool("https://github.com/alfredredbird/alfred", post_install_commands=["sudo pip3 install -r requirements.txt"])
            install_tool("https://github.com/termuxhackers-id/SIGIT.git", repo_name="SIGIT", post_install_commands=["bash installkali.sh"])
            install_tool("https://github.com/Lucksi/Mr.Holmes", post_install_commands=["sudo chmod +x install.sh", "sudo bash install.sh"])
            install_tool("https://github.com/p1ngul1n0/blackbird", post_install_commands=["pip install -r requirements.txt"])
            print_banner()
        elif int(choice) == 1:
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
        else:
            print("Invalid choice. Please try again.")
    
            
# Function for installing other tools
def install_other_tools():
    other_tools_menu = [
        "PDTM (github.com/projectdiscovery/pdtm)",
        "Webcopilot (github.com/h4r5h1t/webcopilot)",
        "TheFatRat (github.com/Screetsec/TheFatRat)\n",
        
        "A - Install All",
        "B - Back to Main Menu",
        "Q - Quit"
    ]
    while True:
        choice = display_menu(other_tools_menu, "Other Tools")

        if choice == 'Q':
            break
        elif choice == 'B':
            return
        elif choice == 'A':
            install_tool("https://github.com/projectdiscovery/pdtm")
            install_tool("https://github.com/h4r5h1t/webcopilot")
            install_tool("https://github.com/Screetsec/TheFatRat")
            print_banner()
        elif int(choice) == 1:
                # Install PDTM
                os.system("go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest")
                os.system("source ~/.zshrc")  # Source the zshrc file
                os.system("~/go/bin/pdtm -ia")  # Run pdtm -ia
                print_banner()
        elif int(choice) == 2:
                # Install Webcopilot
                repo_url = "https://github.com/h4r5h1t/webcopilot"
                repo_name = repo_url.split("/")[-1]
                full_path = os.path.join("/opt", repo_name)

                if os.path.exists(full_path):
                    os.system(f"sudo rm -rf {full_path}")

                os.system(f"sudo git clone {repo_url} {full_path}")
                os.system(f"cd {full_path}")
                os.system(f"sudo chmod +x webcopilot install.sh && sudo mv webcopilot /usr/bin/ && sudo ./install.sh")
                print_banner()
        elif int(choice) == 3:
                # Install TheFatRat
                repo_url = "https://github.com/Screetsec/TheFatRat.git"
                repo_name = repo_url.split("/")[-1]
                full_path = os.path.join("/opt", repo_name)

                if os.path.exists(full_path):
                    os.system(f"sudo rm -rf {full_path}")

                clone_repo(repo_url, repo_name)
                os.system(f"cd {os.path.join('/opt', repo_name)} && sudo chmod +x setup.sh && sudo ./setup.sh")
                print_banner()
        elif int(choice) == 4:
                return  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")

# Main menu function
def main_menu():
    while True:
        menu_options = [
            "Install Utility Tools",
            "Install Security Tools",
            "Install OSINT Tools",
            "Install Other Tools",

        ]
        choice = display_menu(menu_options, "Main")

        if choice == 'Q':
            break
        elif choice == '1':
            install_utility_tools()
        elif choice == '2':
            install_security_tools()
        elif choice == '3':
            install_osint_tools()
        elif choice == '4':
            install_other_tools()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Start the menu
if __name__ == "__main__":
    main_menu()
