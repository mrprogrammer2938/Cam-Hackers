#!/usr/bin/bash
# This cdoe write by (ms.nope)
#       ╋╋╋╋╋╋╋╋╋╋┏┓╋┏┓╋╋╋╋╋┏┓
#       ╋╋╋╋╋╋╋╋╋╋┃┃╋┃┃╋╋╋╋╋┃┃
#       ┏━━┳━━┳┓┏┓┃┗━┛┣━━┳━━┫┃┏┳━━┳━┳━━┓
#       ┃┏━┫┏┓┃┗┛┃┃┏━┓┃┏┓┃┏━┫┗┛┫┃━┫┏┫━━┫
#       ┃┗━┫┏┓┃┃┃┃┃┃╋┃┃┏┓┃┗━┫┏┓┫┃━┫┃┣━━┃
#       ┗━━┻┛┗┻┻┻┛┗┛╋┗┻┛┗┻━━┻┛┗┻━━┻┛┗━━┛
#            version 2.0
#            (Cam Hackers)
if [[ "$(id -u)" -ne 0 ]];
then
  echo "
  Please, Run This Programm as Root!"
  exit 1
fi
function main() {
    printf '\033]2;Cam-Hackers-Installing\a'
    clear
    echo "
Installing... "
    sleep 2
    chmod +x camhackers.py
    echo "──────────╔╗─╔╗─────╔╗"
    echo "──────────║║─║║─────║║"
    echo "╔══╦══╦╗╔╗║╚═╝╠══╦══╣║╔╦══╦═╦══╗"
    echo "║╔═╣╔╗║╚╝║║╔═╗║╔╗║╔═╣╚╝╣║═╣╔╣══╣"
    echo "║╚═╣╔╗║║║║║║─║║╔╗║╚═╣╔╗╣║═╣║╠══║"
    echo "╚══╩╝╚╩╩╩╝╚╝─╚╩╝╚╩══╩╝╚╩══╩╝╚══╝"
    echo "v2.0"
    apt install python3
    apt install python
    apt install firefox
    chmod +x camhackers.py
    echo "
Finish!

Usage:
     python3 camhackers.py 
"
    exit 1

}
main
