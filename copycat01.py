#!/usr/bin/env python3

# Import modules
import shutil
import os

def main():

     # Change directories
     os.chdir("/home/student/mycode/")

     # Make a copy
     shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

     #Copy the whole subdir
     os.system("rm -rf /home/student/mycode/5g_research_backup/")
     shutil.copytree("5g_research/", "5g_research_backup/")


if __name__ == "__main__":
    main()
