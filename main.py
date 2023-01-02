# Govnocode by Bogdikon with <3
#
#   Purpose: Main executable
#
#
################################
import os

import sys

import requests

import platform

from logger import log

# Checking repos

repos = []
with open("repos") as f:
    f_content = f.read()
    f_lines = f_content.split("\n")
    for i in range(len(f_lines)):
        current_line = f_lines[i]
        try:
            line_first = current_line[0]
        except IndexError:
            pass
        else:
            if line_first == "#":
                pass
            else:
                if current_line[-1] != "/":
                    repos.append(f_lines[i] + "/")
                else:
                    repos.append(f_lines[i])


# End checking repos


def get_app(app_name):
    for repo in range(len(repos)):
        log("info", "Checking " + repos[repo])
        log("info", "Sending request")
        app_exist = requests.get(repos[repo] + app_name + ".zip")
        log("info", "Request sent")
        if app_exist:
            log("ok", "Got 200! Trying to download...")
            #		 log("info", "download.bat " + repos[i] + app_name + ".zip")
            #		if platform.system() == "Linux":
            #			log("info", "Linux detected")
            #			os.system("./download.sh")
            #			log("ok", "File downloaded!")
            #			exit(0)
            if platform.system() == "Windows":
                os.system("download.bat " + repos[repo] + app_name + ".zip" + " " + app_name + ".zip")
                log("ok", "File downloaded!")
                exit(0)
            else:
                log("err", "Unsupported system " + platform.system())
                exit(1)
        else:
            if repo == len(repos) - 1:
                log("err", "Package not found. Can't continue.")
                return exit(1)
            log("warn", f"Got {app_exist.status_code}. Trying with another location...")


def find_app(app_name):
    for repo in range(len(repos)):
        log("info", "Checking " + repos[repo])
        log("info", "Sending request")
        app_exist = requests.get(repos[repo] + app_name + ".zip")
        log("info", "Request sent")
        if app_exist:
            log("ok", "Found package on " + repos[repo])
        else:
            if repo == len(repos) - 1:
                log("err", "Package not found. Can't continue.")
                return exit(1)
            log("warn", f"Got {app_exist.status_code}. Trying with another location...")


def remove_app(app_name):
    log("info", "Trying to find package " + app_name)
    if platform.system() != "Windows":
        log("err", "Not implemented on non-windows os yet :(")
        exit(1)
    if os.system("remover.bat " + app_name) == 1:
        log("err", "Specified package wasn't found!")
    else:
        log("ok", "Found and removed package " + app_name)


def version():
    print("PM v1.0R")
    exit()


def makeapp(app_name, pack_name):
    log("info", "Making an app bundle")
    os.system("appmaker.bat " + app_name + " " + pack_name)


# Checking command line

if platform.system() != "Windows":
    log("err", "Cross-platform currently not supported!")
    exit(1)

if len(sys.argv) <= 1:
    print("Too few arguments")
    exit()
elif len(sys.argv) >= 4:
    print("Too much arguments")
    exit()

if sys.argv[1] == "get":
    get_app(sys.argv[2])
if sys.argv[1] == "version":
    version()
if sys.argv[1] == "remove":
    remove_app(sys.argv[2])
if sys.argv[1] == "find":
    find_app(sys.argv[2])