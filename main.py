
# script to make readme files in all the folders
import os 

for i in os.listdir():
    if i in [".git", "readme.md", "main.py"]:
        pass
    else:
        os.chdir(i)
        with open("readme.md", "x") as file:
            file.write("")
            os.chdir("..")

print("done")