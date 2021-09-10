
How Its Useful:Since we cant transfer current chrome tabs from a local to a remote system unless its connected to the same network,so we can use this tool.Also there is another way to transfer tabs that is by saving all tabs in bookmarks and then reloading them from remote system but this method is very time consuming whereas this tool can automate the whole process within a few clicks.


Prerequisites:Python3 installed in your system,stable internet connection,pendrive or any another storage device,Chromedriver,selenium packages installed in both Local and target systems.

To Download Chromedriver:https://chromedriver.chromium.org/downloads

Step1:In Terminal/CMD:type->pip install selenium

Step2:Add chromedriver & google chrome to path(System environment variables)

Step3:Open CMD/Terminal and type->
chrome.exe --remote-debugging-port=9222
--user-data-dir="C:\selenum\ChromeProfile"

Note:The path in above command C:\selenum\ChromeProfile is a folder in which we will store the contents like cache etc of the chromedriver.You can give your custom path depending on your OS(Windows/Linux) and choice.

Now on running the command a new chromedriver window will be opened so you can work in it as you wish by opening new tabs!
-----------------------------------------------------
After you are done working in that window and want to transfer the countless tabs you opened to another remote system follow the steps below:

Step1:Run file.py file in your editor or in CMD/Terminal.

Step2:In the same directory as chrome_save.py is stored you can find a text file called tab.txt.Copy tab.txt,chrome_load_final.py to a pendrive or upload the files to google drive and pull down from there to your remote system

Step3:In your Remote System have the above mentioned files in same directory and then run chrome_load_final.py in editor or CMD/Terminal.

Now the chromedriver will open all the saved tabs in your target machine.
(also ensure cookies are allowed in chromedriver).
---------------------------------------------------------------
Continue your work from where you stopped!!
ENJOY!!
