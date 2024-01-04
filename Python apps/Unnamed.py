import winapps 
import os
for app in winapps.search_installed('chrome'): 
    print(app.install_location)
    os.startfile(os.path.join(str(app.install_location), "chrome.exe"))
