#!/bin/bash

# Function to generate a random color
generate_color() {
    echo -e "\e[38;5;$((RANDOM % 256))m"
}

# Function to generate a random Figlet banner
generate_custom_banner() {
    echo -e "      ██████ ▓█████  ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    "
    echo -e "    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    "
    echo -e "    ░ ▓██▄   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    "
    echo -e "      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░  " 
    echo -e "    ▒██████▒▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒$(generate_color)ver.2.1\n\e[0m]"
    echo -e "    ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░"
    echo -e "    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒       ░      ░  ▒░   ░ ▒ ▒░ ░ ░ ▒  ░"
    echo -e "    ░  ░  ░     ░   ░          ░      ░ ░ ▒  ░ ░ ░ ▒    ░ ░   "
    echo -e "          ░     ░  ░░ ░                   ░ ░      ░ ░      ░  "
    echo -e "                    ░                                       "
    echo -e "                                             	Made with ❤️️ by $(generate_color)s1lv3r\n\e[0m]"
}

# Function to create symbolic links
create_symbolic_links() {
    tool_name=$1
    symlink_path="/usr/local/bin/$tool_name"
    sudo ln -sf "/opt/$tool_name/$tool_name" "$symlink_path"
    echo "   Symbolic link for $tool_name created at $symlink_path"
}

# Function to clear screen and display banner
clear_screen() {
    clear
    generate_custom_banner
}

# Utility Tools

install_google_chrome() {
    sudo apt update
    sudo apt install google-chrome-stable -y
    create_symbolic_links "google-chrome-stable"
    echo "   1.1. Google Chrome installation complete."
}

install_gedit() {
    sudo apt install gedit -y
    create_symbolic_links "gedit"
    echo "   1.2. gedit installation complete."
}

install_synaptic() {
    sudo apt install synaptic -y
    create_symbolic_links "synaptic"
    echo "   1.3. Synaptic installation complete."
}

install_utility_tools() {
    echo "Installing Utility Tools..."
    install_google_chrome
    install_gedit
    install_synaptic
}

# Security Tools

install_autorecon() {
    pipx install git+https://github.com/Tib3rius/AutoRecon.git
    sudo env "PATH=$PATH" autorecon [OPTIONS]
    sudo "$(which autorecon)" [OPTIONS]
    create_symbolic_links "autorecon"
    echo "   2.1. AutoRecon installation complete."
}

install_ghauri() {
    sudo rm -rf /opt/ghauri
    sudo git clone https://github.com/r0oth3x49/ghauri.git /opt/ghauri
    cd /opt/ghauri
    sudo python3 -m pip install --upgrade -r requirements.txt
    sudo python3 setup.py install
    create_symbolic_links "ghauri"
    cd /
    echo "   2.2. Ghauri installation complete."
}

install_goofuzz() {
    sudo rm -rf /opt/GooFuzz
    sudo git clone https://github.com/m3n0sd0n4ld/GooFuzz.git /opt/GooFuzz
    cd /opt/GooFuzz
    sudo chmod +x GooFuzz
    sudo ./GooFuzz -h
    create_symbolic_links "GooFuzz"
    cd /
    echo "    2.3. GooFuzz installation complete."
}

install_hakrawler() {
    sudo rm -rf /opt/hakrawler
    sudo git clone https://github.com/hakluke/hakrawler.git /opt/hakrawler
    cd /opt/hakrawler
    sudo go build .
    sudo mv hakrawler /usr/local/bin/
    create_symbolic_links "hakrawler"
    cd /
    echo "   2.4. Hakrawler installation complete."
}

install_security_tools() {
    echo "Installing Security Tools..."
    install_autorecon
    install_ghauri
    install_goofuzz
    install_hakrawler
}

# Password Recovery Tools

install_zydra() {
    sudo rm -rf /opt/zydra
    sudo git clone https://github.com/hamedA2/Zydra.git /opt/zydra
    cd /opt/zydra
    sudo chmod +x install.sh
    sudo bash install.sh
    create_symbolic_links "zydra"
    cd /
    echo "   3.1. Zydra installation complete."
}

install_hashcat_launcher() {
    sudo rm -rf /opt/hashcat-launcher
    sudo git clone https://github.com/s77rt/hashcat.launcher.git /opt/hashcat-launcher
    cd /opt/hashcat-launcher
    sudo make
    create_symbolic_links "hashcat-launcher"
    cd /
    echo "   3.2. Hashcat Launcher installation complete."
}

install_password_recovery_tools() {
    echo "Installing Password Recovery Tools..."
    install_zydra
    install_hashcat_launcher
}

# OSINT Tools

install_blackbird() {
    sudo rm -rf /opt/blackbird
    sudo git clone https://github.com/p1ngul1n0/blackbird.git /opt/blackbird
    cd /opt/blackbird
    sudo python3 -m pip install -r requirements.txt
    create_symbolic_links "blackbird"
    cd /
    echo "   4.1. BlackBird installation complete."
}

install_mrholmes() {
    sudo rm -rf /opt/mrholmes
    sudo git clone https://github.com/Lucksi/Mr.Holmes.git /opt/mrholmes
    cd /opt/mrholmes
    sudo apt-get update
    sudo chmod +x install.sh
    sudo bash install.sh
    create_symbolic_links "mrholmes"
    cd /
    echo "   4.2. Mr. Holmes installation complete."
}

install_sigit() {
    pkg install wget -y
    wget https://raw.githubusercontent.com/termuxhackers-id/SIGIT/main/install.sh
    bash install.sh
    create_symbolic_links "sigit"
    echo "   4.3. SIGIT installation complete."
}

install_osint_tools() {
    echo "Installing OSINT Tools..."
    install_blackbird
    install_mrholmes
    install_sigit
}

# OTHERS Tools

install_pdtm() {
    go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest
    create_symbolic_links "pdtm"
    echo "   5.1. PDTMAutorecon installation complete."
}

install_others_tools() {
    echo "Installing OTHERS Tools..."
    install_pdtm
}

# Main menu

while true; do
    clear_screen

    echo "Please choose the category to install:"
    echo "1. Utility Tools"
    echo "2. Security Tools"
    echo "3. Password Recovery Tools"
    echo "4. OSINT Tools"
    echo "5. OTHERS Tools"
    echo "6. Exit"

    read -p "Enter your choice (1-6): " main_choice

    case $main_choice in
        1)
            echo "Please choose the utility tool to install:"
            echo "1. Google Chrome"
            echo "2. gedit"
            echo "3. Synaptic"
            echo "4. Install All"
            read -p "Enter your choice (1-4): " utility_choice
            case $utility_choice in
                1)
                    install_google_chrome
                    ;;
                2)
                    install_gedit
                    ;;
                3)
                    install_synaptic
                    ;;
                4)
                    install_utility_tools
                    ;;
                *)
                    echo "Invalid choice. Exiting..."
                    exit 1
                    ;;
            esac
            ;;
        2)
            echo "Please choose the security tool to install:"
            echo "1. AutoRecon"
            echo "2. Ghauri"
            echo "3. GooFuzz"
            echo "4. Hakrawler"
            echo "5. Install All"
            read -p "Enter your choice (1-5): " security_choice
            case $security_choice in
                1)
                    install_autorecon
                    ;;
                2)
                    install_ghauri
                    ;;
                3)
                    install_goofuzz
                    ;;
                4)
                    install_hakrawler
                    ;;
                5)
                    install_security_tools
                    ;;
                *)
                    echo "Invalid choice. Exiting..."
                    exit 1
                    ;;
            esac
            ;;
        3)
            echo "Please choose the password recovery tool to install:"
            echo "1. Zydra"
            echo "2. Hashcat Launcher"
            echo "3. Install All"
            read -p "Enter your choice (1-3): " password_choice
            case $password_choice in
                1)
                    install_zydra
                    ;;
                2)
                    install_hashcat_launcher
                    ;;
                3)
                    install_password_recovery_tools
                    ;;
                *)
                    echo "Invalid choice. Exiting..."
                    exit 1
                    ;;
            esac
            ;;
        4)
            echo "Please choose the OSINT tool to install:"
            echo "1. BlackBird"
            echo "2. Mr. Holmes"
            echo "3. SIGIT"
            echo "4. Install All"
            read -p "Enter your choice (1-4): " osint_choice
            case $osint_choice in
                1)
                    install_blackbird
                    ;;
                2)
                    install_mrholmes
                    ;;
                3)
                    install_sigit
                    ;;
                4)
                    install_osint_tools
                    ;;
                *)
                    echo "Invalid choice. Exiting..."
                    exit 1
                    ;;
            esac
            ;;
        5)
            echo "Please choose the OTHERS tool to install:"
            echo "1. PDTMAutorecon"
            echo "2. Install All"
            read -p "Enter your choice (1-2): " others_choice
            case $others_choice in
                1)
                    install_pdtm
                    ;;
                2)
                    install_others_tools
                    ;;
                *)
                    echo "Invalid choice. Exiting..."
                    exit 1
                    ;;
            esac
            ;;
        6)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Exiting..."
            exit 1
            ;;
    esac

    read -p "Press Enter to continue..."
done
