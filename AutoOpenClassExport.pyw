import webbrowser
from datetime import datetime, time
from time import sleep

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# PUT THE LINK TO THE GOOGLE MEET WHEREVER THERE IS A SPACE

foundationsLink = ' ' # Foundations google meet link

urls = ['[PUT URLS HERE FOR EVER HOUR]', # First hour
        ' ', # Second hour
        ' ', # Third hour
        ' ', # Fourth hour
        ' ', # Fifth hour
        ' '] # Sixth hour

# URLS2 IS FOR ANY CLASSES THAT CHANGE MEET LINKS FOR TUESDAYS AND THURSDAYS. IF THE LINK DOESN'T CHANGE, PASTE IT IN HERE ANYWAYS

urls2 = [' ', # First hour
         ' ', # Second hour
         ' ', # Third hour
         ' ', # Fourth hour
         ' ', # Fifth hour
         ' '] # Sixth hour

def act(x):
    return x+10

def wait_start(runTime, action):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time():
        sleep(1)
    return action

weekday = datetime.today().weekday()
dayOfMonth = datetime.today().day

firstOfMonth = True
for i in range(1, dayOfMonth):
    countingDate = datetime(datetime.today().year, datetime.today().month, i)
    if countingDate.weekday() == weekday:
        print("Not the first day of the month")
        firstOfMonth = False
        break

if firstOfMonth == True:
    print("Running code for foundations schedule")

    linksToUse = urls
    if weekday == 1 or weekday == 3:
        print("Day is tuesday or thursday")
        linksToUse = urls2

    wait_start('7:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[0])

    wait_start('8:23', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[1])

    wait_start('9:17', lambda: act(100))
    webbrowser.get(chrome_path).open(foundationsLink)

    wait_start('9:47', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[2])

    wait_start('10:41', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[3])

    wait_start('12:16', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[4])

    wait_start('13:10', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[5])
else:
    print("Running code for regular schedule")

    linksToUse = urls
    if weekday == 1 or weekday == 3:
        print("Day is tuesday or thursday")
        linksToUse = urls2

    wait_start('7:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[0])

    wait_start('8:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[1])

    wait_start('9:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[2])

    wait_start('10:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[3])

    wait_start('12:04', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[4])

    wait_start('13:04', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[5])