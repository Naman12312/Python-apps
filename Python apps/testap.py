import winapps
import subprocess
import os
a = input("Enter the name of the application")
def getPossibleExePaths(appPath):
    if not appPath:
        raise Exception("App Path cannot be None")
    pattern = appPath + ":*exe"
    try:
        returned = subprocess.check_output(['where', pattern]).decode('utf-8')
        listOfPaths = filter(None, returned.split(os.linesep))
        return [i.strip() for i in list(listOfPaths)]
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error getting path for '{appPath}'")
def g(appo):
    for i in winapps.search_installed(appo):
        ab = str(i.install_location)
        if ab and ab != "None":
            return ab
        return None
if __name__ == "__main__":
    os.startfile(getPossibleExePaths(g(a))[0])