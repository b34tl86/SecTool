import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init()

def is_valid_choice(choice, menu_length):
    """Check if the input choice is valid."""
    return choice.isdigit() and 1 <= int(choice) <= menu_length

def check_permissions():
    """Ensure the script is run as root."""
    if os.geteuid() != 0:
        print("This script must be run as root (use sudo).")
        exit(1)

def install_package(package_name):
    """Install a package using apt-get and handle errors."""
    try:
        subprocess.run(["sudo", "apt-get", "install", "-y", package_name], check=True)
    except subprocess.CalledProcessError:
        print(f"Error installing package: {package_name}")

def clear_screen():
    """Clear the terminal screen."""
    os.system("clear")

def display_menu(menu_options, menu_name):
    """Display the menu options and handle input."""
    clear_screen()
    print_banner()

    print(f"\n{Fore.RED}{Style.BRIGHT}{menu_name} Menu:{Style.RESET_ALL}")
    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")

    # Add "A" for Install All and "B" for Back to Main Menu
    print(f"\nA. Install All\nB. Back to Main Menu\nq. Quit")
    choice = input("\nEnter your choice (q to quit, B to go back to main menu): ")
    return choice

def print_banner():
    """Print the banner."""
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
    """Clone a git repository and install it."""
    full_path = os.path.join(install_path, repo_name)
    if os.path.exists(full_path):
        subprocess.run(["sudo", "rm", "-rf", full_path])

    subprocess.run(["sudo", "git", "clone", repo_url, full_path])

def install_git_repo(repo_url, repo_name, install_script="install.sh"):
    """Clone a repository and run the install script."""
    clone_repo(repo_url, repo_name)
    repo_path = os.path.join("/opt", repo_name)
    subprocess.run(["sudo", "chmod", "+x", install_script], cwd=repo_path)
    subprocess.run([f"sudo ./install.sh"], cwd=repo_path)

def install_other_tools():
    """Install other tools from the menu."""
    other_tools_menu = [
        "PDTM (github.com/projectdiscovery/pdtm)",
        "Webcopilot (github.com/h4r5h1t/webcopilot)",
        "FatRat (https://github.com/Screetsec/TheFatRat.git)",
        "Nucleimonst3r (https://github.com/blackhatethicalhacking/Nucleimonst3r.git)",
        "CyberPhish (https://github.com/Cyber-Dioxide/CyberPhish)"
    ]

    while True:
        choice = display_menu(other_tools_menu, "Other Tools")

        if choice == 'q':
            break
        elif choice.lower() == 'a':
            # Install all other tools
            for i in range(0, len(other_tools_menu)):
                install_git_repo(other_tools_menu[i], other_tools_menu[i].split()[0])
            print("All other tools installed.")
        elif choice.lower() == 'b':
            # Go back to the main menu
            break
        elif is_valid_choice(choice, len(other_tools_menu)):
            install_git_repo(other_tools_menu[int(choice) - 1], other_tools_menu[int(choice) - 1].split()[0])
        else:
            print("Invalid choice. Please try again.")

def install_utility_tools():
    """Install utility tools from the menu."""
    utility_tools_menu = [
        "chromium-browser",
        "geany",
        "gedit",
        "synaptic"
    ]

    while True:
        choice = display_menu(utility_tools_menu, "Utility Tools")

        if choice == 'q':
            break
        elif choice.lower() == 'a':
            # Install all utility tools
            for tool in utility_tools_menu:
                install_package(tool)
            print("All utility tools installed.")
        elif choice.lower() == 'b':
            # Go back to the main menu
            break
        elif is_valid_choice(choice, len(utility_tools_menu)):
            install_package(utility_tools_menu[int(choice) - 1])
        else:
            print("Invalid choice. Please try again.")

def install_security_tools():
    """Install security tools from the menu."""
    security_tools_menu = [
        ("AutoRecon", "https://github.com/Tib3rius/AutoRecon.git"),
        ("Ghauri", "https://github.com/r0oth3x49/ghauri.git"),
        ("GooFuzz", "https://github.com/m3n0sd0n4ld/GooFuzz.git"),
        ("ParamSpider", "https://github.com/devanshbatham/paramspider"),
        ("PhoneSploit-Pro", "https://github.com/AzeemIdrisi/PhoneSploit-Pro.git"),
        ("BirDuster", "https://www.github.com/ytisf/BirDuster"),
        ("NucleiScanner", "https://github.com/0xKayala/NucleiScanner.git")
    ]

    while True:
        choice = display_menu([tool[0] for tool in security_tools_menu], "Security Tools")

        if choice == 'q':
            break
        elif choice.lower() == 'a':
            # Install all security tools
            for tool in security_tools_menu:
                install_git_repo(tool[1], tool[0])
            print("All security tools installed.")
        elif choice.lower() == 'b':
            # Go back to the main menu
            break
        elif is_valid_choice(choice, len(security_tools_menu)):
            selected_tool = security_tools_menu[int(choice) - 1]
            install_git_repo(selected_tool[1], selected_tool[0])
        else:
            print("Invalid choice. Please try again.")

def install_osint_tools():
    """Install OSINT tools from the menu."""
    osint_tools_menu = [
        ("BlackBird", "https://github.com/p1ngul1n0/blackbird"),
        ("Mr. Holmes", "https://github.com/Lucksi/Mr.Holmes"),
        ("SIGIT", "https://github.com/termuxhackers-id/SIGIT.git"),
        ("Alfred", "https://github.com/alfredredbird/alfred")
    ]

    while True:
        choice = display_menu([tool[0] for tool in osint_tools_menu], "OSINT Tools")

        if choice == 'q':
            break
        elif choice.lower() == 'a':
            # Install all OSINT tools
            for tool in osint_tools_menu:
                install_git_repo(tool[1], tool[0])
            print("All OSINT tools installed.")
        elif choice.lower() == 'b':
            # Go back to the main menu
            break
        elif is_valid_choice(choice, len(osint_tools_menu)):
            selected_tool = osint_tools_menu[int(choice) - 1]
            install_git_repo(selected_tool[1], selected_tool[0])
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    """Display the main menu."""
    menu_options = [
        "Utility Tools",
        "Security Tools",
        "OSINT Tools",
        "Other Tools"
    ]

    while True:
        choice = display_menu(menu_options, "Main")

        if choice == 'q':
            break
        elif is_valid_choice(choice, len(menu_options)):
            if int(choice) == 1:
                install_utility_tools()
            elif int(choice) == 2:
                install_security_tools()
            elif int(choice) == 3:
                install_osint_tools()
            elif int(choice) == 4:
                install_other_tools()

        else:
            print("Invalid choice. Please try again.")

# Main execution
if __name__ == "__main__":
    check_permissions()
    main_menu()
