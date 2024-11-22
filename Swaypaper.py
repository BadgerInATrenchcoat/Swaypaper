#!/usr/bin/python3

import os
import time
import sys

def changeStatus(status: str):
    status_file = open("/tmp/swaypaper.txt", "w")
    status_file.write(status)
    status_file.close()

def getWallpapers(directory: str) -> None:
    status = "started"
    while (status == "started"):
        available_wallpapers = os.listdir(directory)
        for wallpaper in available_wallpapers: 
            status_file = open("/tmp/swaypaper.txt", "r")
            status = status_file.read().strip()
            status_file.close()
            if (status != "started"):
                return
            wallpaper_path = directory + wallpaper
            os.system(f"swaymsg output '*' bg '{wallpaper_path}' fill")
            time.sleep(300)

def main() -> int:
    if (sys.argv[1] == 'start'):
        changeStatus('start')
    elif (sys.argv[1] == 'stop'):
        changeStatus('stop')
        return 0
    else:
        print("Invalid command line arguments.\nAvailable usage is 'swaypaper.py [start/stop]'.")
        return 1

    wallpapers_dir = input('Input the folder containing the wallpapers you would like to use: ')
    getWallpapers(wallpapers_dir)
    return 1


main()
