import pywhatkit as kit #installpywhatkit
import os
kit.sendwhatmsg("Enter your friends phone no. and add country code","Enter Your Message",24,00) #at the end enter time in 24 hours format
os.system("taskkill /im chrome.exe /f") #it will close the browser
os.system("shutdown /s /t 1") #it will shutdown the pc
