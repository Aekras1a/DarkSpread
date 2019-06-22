
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



emails = []

def readMails():
    with open("emails.txt", "r") as ins:
        for line in ins:
            emails.append(line)

def initBrowser():
    browser = False
    options = webdriver.ChromeOptions() 
    options.add_argument("--user-data-dir=assets\\Browsers\\Chrome\\User Data")
    browser = webdriver.Chrome(executable_path="assets\\webdriver\\chromedriver.exe",chrome_options=options)
    browser.get('https://mail.google.com')
    return browser

def gmail(browser,email,config):
            if("mail.google.com" not in browser.current_url ):
                print("Bot is waiting for Login or Gmail Tab is not Active")
                time.sleep(5)
            else:
                #print("We are on Gmail, wait a bit")
                time.sleep(10)
                browser.find_element_by_xpath("//div[@gh='cm']").click()
                mailto = browser.find_element_by_xpath("//textarea[@role='combobox']")
                mailto.clear()
                mailto.send_keys(email)
                time.sleep(5)
                subjectBox = browser.find_element_by_xpath("//input[@name='subjectbox']")
                subjectBox.clear()
                subjectBox.send_keys(config["botconfig"]["subject"])
                time.sleep(5)
                maintext = browser.find_element_by_xpath("//div[@role='textbox']")
                maintext.clear()
                with open(config["botconfig"]["mailbodyFile"], 'r') as myfile:
                     html = myfile.read()
                maintext.send_keys(html.strip(' \t\n\r'))
                time.sleep(5)
                browser.find_element_by_xpath("//tr[@class='btC']/td[1]").click()
                print("Mail Send to "+ email)


if __name__ == "__main__":

    spider = """
______           _    _____                          _ 
|  _  \         | |  /  ___|                        | |
| | | |__ _ _ __| | _\ `--. _ __  _ __ ___  __ _  __| |
| | | / _` | '__| |/ /`--. \ '_ \| '__/ _ \/ _` |/ _` |
| |/ / (_| | |  |   </\__/ / |_) | | |  __/ (_| | (_| |
|___/ \__,_|_|  |_|\_\____/| .__/|_|  \___|\__,_|\__,_|
                           | |                         
                           |_|                          v1.0    
    """
    print(spider)
    with open('config.ini') as data_file:
            config = json.load(data_file)

    print("Reading Emails...")
    readMails()
    print("Start Browser...")
    browser = initBrowser()

    if(browser == False):
        print("Failed to Start Web Browser\n")
        exit()

    while(1):
        print("Start Work...")
        for email in emails:
            print("Current: "+email.strip(' \t\n\r'))
            gmail(browser,email.strip(' \t\n\r'),config)
                