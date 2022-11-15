from playwright.sync_api import sync_playwright
import time
import random
import string
import json

numbers = string.digits
letters = string.ascii_lowercase

def walmartgen():
    options = open('C:/Users/andre/PycharmProjects/walmartAccountGen/options/walmartGenOptions.json')
    jsonoptions = json.load(options)
    y = 0
    accounts = 1
    while y < int(jsonoptions['accounts']):
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.walmart.ca/create-account")
            result_email1 = ''.join(random.choice(letters) for i in range(8))
            result_email2 = ''.join(random.choice(numbers) for i in range(9))
            result_email = result_email2 + result_email1
            phone_number = ''.join(random.choice(numbers) for i in range(4))
            email = result_email + jsonoptions['catchall']
            file1 = open('C:/Users/andre/PycharmProjects/walmartAccountGen/createdaccounts.txt', 'a')
            file1.write(email + ":" + jsonoptions['password'] + "\n")
            print(email + ":" + jsonoptions['password'])
            file1.close()
            page.wait_for_selector('#firstName')
            random_firstname = random.choice(open("C:/Users/andre/PycharmProjects/walmartAccountGen/firstnames.txt").readlines())
            random_lastname = random.choice(open("C:/Users/andre/PycharmProjects/walmartAccountGen/lastnames.txt").readlines())
            page.fill('#firstName', random_firstname)
            page.fill('#lastName', random_lastname)
            page.fill('#phoneNumber', "647225" + phone_number)
            page.fill('#email', email)
            page.fill('#password', jsonoptions['password'])
            page.click('#TAndC')
            page.click('xpath=/html/body/div[1]/div/div[1]/div/form/div/div[10]/button')
            page.wait_for_selector('#accounts-home-page > div:nth-child(2) > div > div > div > div.css-15d3kon.e1lo459p5 > h1')
            time.sleep(1)
            page.wait_for_selector('xpath=/html/body/div[1]/div/div[3]/div[3]/div[2]/div[1]/div[4]/div[2]/a/div')
            time.sleep(1)
            page.click('xpath=/html/body/div[1]/div/div[3]/div[3]/div[2]/div[1]/div[4]/div[2]/a/div')
            time.sleep(1)
            page.wait_for_selector('.e1xsuuhf8')
            page.click('.e1xsuuhf8')
            page.wait_for_selector('xpath=//*[@id="address1"]')
            page.fill('xpath=//*[@id="address1"]', jsonoptions['address'])
            page.fill('xpath=//*[@id="city"]', jsonoptions['city'])
            page.fill('xpath=//*[@id="postalCode"]', jsonoptions['postalcode'])
            page.fill('xpath=//*[@id="phoneNumber"]', "647703" + phone_number)
            page.select_option('#province', jsonoptions['province'])
            page.click('.css-vfxkzw')
            page.wait_for_selector('.e1iabzgi4')
            page.click('.e1iabzgi4')
            page.wait_for_load_state('domcontentloaded')
            page.dblclick('xpath=/html/body/div[1]/div/div[3]/div[1]/div/div[2]/section/section/div/div[1]/ul/li[10]/div/a', force=True)
            page.wait_for_selector('.css-kk5hrw')
            page.click('.css-kk5hrw')
            page.wait_for_selector('#firstName')
            page.dblclick('#firstName')
            page.fill('#firstName', "Michael")
            page.dblclick('#lastName')
            page.fill('#lastName', "Andreucci")
            page.fill('#cardNumber', jsonoptions['CCnumber'])
            page.fill('#securityCode', jsonoptions['CVV'])
            page.select_option('#expiryMonth', jsonoptions['expiryMonth'])
            page.select_option('#expiryYear', jsonoptions['expiryYear'])
            page.wait_for_selector('.css-127t9hs > svg:nth-child(1) > circle:nth-child(1)')
            page.click('.css-q7lffx', force=True)
            page.check('#primaryCardCheckbox')
            page.click('.e1srjxbw7')
            page.wait_for_selector('.css-wckgdq')
            y += 1

#asyncio.run(walmartgen())