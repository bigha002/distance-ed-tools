import webbrowser
from datetime import datetime, time
from time import sleep

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

foundationsLink = 'https://meet.google.com/nzi-sbzt-wek'
urls = ['https://meet.google.com/udh-mkir-tjh', 'https://meet.google.com/eyw-rttk-pxm', 'https://meet.google.com/cvt-zuwj-dww', 'https://meet.google.com/twc-enzn-khz',
        'https://meet.google.com/nzi-sbzt-wek', 'https://meet.google.com/owi-effs-hws']
urls2 = ['https://meet.google.com/udh-mkir-tjh', 'https://meet.google.com/eyw-rttk-pxm', 'https://meet.google.com/cvt-zuwj-dww', 'https://meet.google.com/ygp-nxaf-jpu',
         'https://meet.google.com/nzi-sbzt-wek', 'https://meet.google.com/owi-effs-hws']

def act(x):
    return x+10

def wait_start(runTime, action):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
        sleep(1)# you can change 1 sec interval to any other
    return action

weekday = datetime.today().weekday()
dayOfMonth = datetime.today().day

# weekday = datetime(2020, 12, 15).weekday()
# dayOfMonth = datetime(2020, 12, 15).day

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
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361474902/materials')

    wait_start('8:23', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[1])
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLScVf_JIluCDSRZ99em5DkyCWztXLyxtl-GcP53Mi1_OnXZB9Q/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361482598/materials')

    wait_start('9:17', lambda: act(100))
    webbrowser.get(chrome_path).open(foundationsLink)
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLSccrV5dP678OFz_1qkd2wbQ4sIIm0CULmpG7utUBcB9-LejTw/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361475970/materials')

    wait_start('9:47', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[2])
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLSccrV5dP678OFz_1qkd2wbQ4sIIm0CULmpG7utUBcB9-LejTw/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361474029/materials')

    wait_start('10:41', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[3])
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLSegh1MarrgnhucGAfg_8lK0yBtTarim3NVyTa76UQ1YVY2v6A/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361484314/materials')

    wait_start('12:16', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[4])
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLSegh1MarrgnhucGAfg_8lK0yBtTarim3NVyTa76UQ1YVY2v6A/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361477199/materials')

    wait_start('13:10', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[5])
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361473018/materials')
else:
    print("Running code for regular schedule")

    linksToUse = urls
    if weekday == 1 or weekday == 3:
        print("Day is tuesday or thursday")
        linksToUse = urls2

    wait_start('7:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[0])
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361474902/materials')

    wait_start('8:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[1])
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLScVf_JIluCDSRZ99em5DkyCWztXLyxtl-GcP53Mi1_OnXZB9Q/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361482598/materials')

    wait_start('9:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[2])
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLSccrV5dP678OFz_1qkd2wbQ4sIIm0CULmpG7utUBcB9-LejTw/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361474029/materials')

    wait_start('10:29', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[3])
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLSegh1MarrgnhucGAfg_8lK0yBtTarim3NVyTa76UQ1YVY2v6A/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361484314/materials')

    wait_start('12:04', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[4])
    webbrowser.get(chrome_path).open('https://docs.google.com/forms/d/e/1FAIpQLSegh1MarrgnhucGAfg_8lK0yBtTarim3NVyTa76UQ1YVY2v6A/viewform')
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361477199/materials')

    wait_start('13:04', lambda: act(100))
    webbrowser.get(chrome_path).open(linksToUse[5])
    webbrowser.get(chrome_path).open('https://osseo.schoology.com/course/3361473018/materials')