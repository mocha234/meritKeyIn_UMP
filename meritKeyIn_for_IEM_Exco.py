import pip

package = 'selenium==3.141.0'
pass_package = 'stdiomask'
driver_package = 'chromedriver-autoinstaller'

def import_or_install(package):
    try:
        __import__(package)
        print("Selenium Installed") # Version 3.141.0
    except ImportError:
        print("Selenium not installed, installing...")
        pip.main(['install', package])  
        print("Selenium Installed")
        
def pass_package_install(pass_package):
    try:
        __import__(pass_package)
        print("stdiomask Installed") 
    except ImportError:
        print("stdiomask not installed, installing...")
        pip.main(['install', pass_package])  
        print("stdiomask Installed")
        
def driver_package_install(driver_package):
    try:
        __import__(driver_package)
        print("chromeDriver Installed") 
    except ImportError:
        print("chromeDriver not installed, installing...")
        pip.main(['install', driver_package])  
        print("chromeDriver Installed")

import_or_install(package)
pass_package_install(pass_package)
driver_package_install(driver_package)
        
import time
import stdiomask
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import csv
import sys

chromedriver_autoinstaller.install()

# User input Variables
name = ""
pwd = ""
eventLinkinEcomm = ""

# Constants
inputName = '//*[@id="form-username"]'
inputEmailID = '//*[@id="form-password"]'
inputCategory = '//*[@id="lvl"]/option[2]'
submitButton = '//*[@id="js-btn"]'
modalButton = '//*[@id="myModal"]/div/div/div[3]/button'
studentApplication = '//*[@id="leftmenubox"]/table[8]/tbody/tr[96]/td[2]/a'
listing = "//a[@href='//application_activities.jsp?action=UniversityList']"
listing1 = '//a[contains(@href,"/application_activities.jsp?action=UniversityList")]'
addNewMember = 'td.contentBgColor>a'
selectInPopout = "input[onclick^='valbutton(form_post);return false;']"
afterenterStudent = '//*[@id = "designation"]/option[2]'
radioB = '//*[@id="radio"]'
studentID = '//*[@id="studID"]'
radioSelectStudent = '//*[@id="radio2"]'
submitNewMember = "input[onclick^='return ValidateFields()']"

# Load .csv to List
inputStudentID = []
with open('matricIDList.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        inputStudentID.append(row[0])

# Some functions ... For delay purposes


def sleep():
    time.sleep(3)


def sleep1():
    time.sleep(1)


# Start UI
print("\n\t+-----------------------------------------------------------------------------+")
print("\t|            ====     ====  ======  ========    =======  =======              |")
print("\t|            == ==   == ==  ==      ==     ==     ==       ==                 |")
print("\t|            == ==   == ==  ======  ==     ==     ==       ==                 |")
print("\t|            ==  == ==  ==  ==      ==  ===       ==       ==                 |")
print("\t|            ==   ===   ==  ======  ==     ===  =======    ==   KeyInMadeEasy |")
print("\t|                                                                             |")
print("\t| Written by mocha234, for any inquiry, please reach out to me @              |")
print("\t|                   github.com/mocha234                                       |")
print("\t+-----------------------------------------------------------------------------+")
print("\n\t")

name = input("Secretary's Matric ID: ")
pwd = stdiomask.getpass()

# print("\n\tSince there's no error for wrong password checking, please check if it's correct:")
# print("\tSecretary's Matric ID: " + name)
# print("\tPassword: " + pwd)
# isCorrect = input("\n\tProceed? (y/n):")

# if isCorrect != "y":
#     sys.exit(
#         "\n\tNoted! Please refill! (Pro-Tip: Press Up arrow key to call previous line)")

print("\n\tEvent's Merit Fill-In page's link should something like this:")
print("\thttps://std-comm.ump.edu.my/ecommstudent/application_activities.jsp?action=UniversityCommiteeAdd&caa_ref_id=XXXXXX")
print("\n\tEvent's Merit Fill-In page's link:")
eventLinkinEcomm = input("\n\t")
print("\n\tDual check please? :)")
print("\tLink: " + eventLinkinEcomm)
isCorrect = input("\n\tProceed? (y/n):")
if isCorrect != "y":
    sys.exit(
        "\n\tNoted! Please refill! (Pro-Tip: Press Up arrow key to call previous line)")
print("\n\tChecklist:")
print("\n\tPlease ensure these following are ready, to avoid 'stuck'")
print("\n\t ---> 1. Replace the matricID.csv?")
print("\n\t ---> 2. matricID.csv only contain one column starting from row 0")
print("\n\t         with students' matric ID?")
print("\n\t ---> 3. Data preprocessed? Only Local students' in the .csv file")
isCorrect = input("\n\tProceed? (y/n):")
if isCorrect != "y":
    sys.exit(
        "\n\tNoted! Please refill! (Pro-Tip: Press Up arrow key to call previous line)")

# Login sequence
# Driver
# driver = webdriver.Chrome(
#    executable_path="chromedriver.exe")

browser = webdriver.Chrome()
browser.get("https://community.ump.edu.my/ecommstaff/login_eccom/")
browser.find_element_by_xpath(inputName).send_keys(name)
browser.find_element_by_xpath(inputEmailID).send_keys(pwd)
browser.find_element_by_xpath(inputCategory).click()
sleep()
browser.find_element_by_xpath(submitButton).click()
# browser.find_element_by_xpath(modalButton).click()

# Start Looping
noOfParticipants = len(inputStudentID)

i = 0
while i < noOfParticipants:
    print("{matricID} ---> Processing".format(matricID=inputStudentID[i]))
    browser.get(eventLinkinEcomm)
    browser.find_element_by_css_selector(addNewMember).click()
    sleep1()
    browser.find_element_by_xpath(afterenterStudent).click()
    # print(browser.title)
    print("---------------------")
    # print(browser.window_handles)
    popoutName = browser.window_handles[1]
    defaultWindow = browser.window_handles[0]
    print(popoutName)
    browser.switch_to.window(popoutName)
    # print(browser.title)
    browser.find_element_by_xpath(radioB).click()
    browser.find_element_by_xpath(studentID).send_keys(inputStudentID[i][0:7])
    print(inputStudentID[i][0:7])
    browser.find_element_by_css_selector(selectInPopout).click()
    browser.find_element_by_xpath(radioSelectStudent).click()
    sleep1()
   ## browser.switch_to.window(defaultWindow)
    # print(browser.title)
    browser.find_element_by_css_selector(submitNewMember).click()
    print("{matricID} ---> Done".format(matricID=inputStudentID[i]))
    print("Finished {a}/{b}".format(a=i+1, b=noOfParticipants))
    i += 1
    sleep()

print("\n\tAll done key in.")
print("\n\tNumber of Participants: " + noOfParticipants)
