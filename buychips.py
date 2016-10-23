'''
Author : Bhishan Bhandari
bbhishan@gmail.com

The program uses following modules

selenium 	to interact and control the browser

time 		to create pause in the program to behave like we are human

pyautogui 	to find the location of buy chips button in the game to click

time is a default module in python which comes installed when installing python.

pyautogui and selenium can be installed as follows. 

In command prompt/terminal type the following and hit enter to install selenium 
pip install selenium 

In command prompt/terminal type the following and hit enter to install pyautogui 
pip install pyautogui

'''

from selenium import webdriver 
import time 
from selenium.webdriver.common.keys import Keys
import pyautogui 

def main(username, password):
    try:
        browser = webdriver.Chrome()
    except:
        print "requirement not satisfied."

    
    browser.maximize_window()
    try:
        browser.get("http://www.codeshareonline.com/doubledown.html")
        time.sleep(10)
        codes_paragraph = browser.find_element_by_class_name("paragraph")
        all_codes = codes_paragraph.find_elements_by_tag_name("a")
        count = 0
        final_codes = []
        for codes in all_codes:
            if "facebook" in codes.get_attribute("href"):
                print codes.text
                final_codes.append(codes.text)
                count += 1
    

        print "Total coupon codes collected : ", count

    except:
        print "Could not get coupon codes. "

    
    browser.get("https://facebook.com")
    time.sleep(15)
    email_field = browser.find_element_by_id("email")
    password_field = browser.find_element_by_id("pass")
    email_field.send_keys(username)
    time.sleep(3)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(20)
    web_body = browser.find_element_by_tag_name('body')
    web_body.send_keys(Keys.ESCAPE)
    for i in range(5):
        web_body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    for i in range(10):
        web_body.send_keys(Keys.PAGE_UP)
        time.sleep(2)
    browser.get("https://apps.facebook.com/doubledowncasino")
    time.sleep(50)
    web_body = browser.find_element_by_tag_name('body')
    web_body.send_keys(Keys.ESCAPE)
    stat = 0
    for i in range(3000):
        try:
            time.sleep(5)
            buy_chips = pyautogui.locateOnScreen("/home/bhishan/bhishanworks/programmingblog/fiverr/facebookgame/buychips.png")
            button7x, button7y = pyautogui.center(buy_chips)
            pyautogui.click(button7x, button7y)
            print "found and clicked"
            stat = 1
        except:
            print "could not find image of buy chips to click"

        if stat == 1:
            break

    time.sleep(5)
    for each_code in final_codes:
        promo_entry = browser.find_element_by_id("package_promo_input")
        promo_entry.send_keys(each_code)
        promo_button = browser.find_element_by_id("package_promo_button")
        promo_button.click()


if __name__ == '__main__':
    main("bbhishan@gmail.com", "password")
