# -*- coding: utf-8 -*-

'''
Created in 12/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os
import art

def functionStories():

    # input for config bot
    os.system('cls') # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    way = str(input('Way: ')) # way to geckodriver
    delay = int(input('Delay (just number): ')) # loading delay time

    # input info for bot 
    os.system('cls') # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    os.system('cls') # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    print('')
    print('Loading...')
    print('')

    # load browser drive in to var and open
    try:
        driver = webdriver.Firefox(executable_path=f'{way}/geckodriver') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
    except:
        try:
            driver = webdriver.Firefox(executable_path=f'{way}\geckodriver')
        except:
            print('\033[0;31mDRIVER ERROR!\033[m Check installed drive or path.')

    # function to access the login page and log in
    def botlogin (user, pwd):
        username = user # your user
        password = pwd # your password

        driver.get('https://www.instagram.com/') # instagram url
        sleep(delay)

        '''
        this page / button was removed by Instagram
        driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button 
        '''
        
        userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
        userelement.clear()
        userelement.send_keys(username) # user insertion in 'user' element

        pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
        pwdelement.clear()
        pwdelement.send_keys(password) # password insertion in 'password' element

        pwdelement.send_keys(Keys.RETURN) # log in to page
        sleep(4)


    # function to view the stories
    def stories():
        try:
            driver.find_element_by_xpath('//button[contains(text(), "Agora não")]').click() # press the notification button that appears most of the time, denying the option
            sleep(delay)
            
        except:
            pass

        try:
            driver.find_element_by_xpath('//button[contains(text(), "Agora não")]').click() # press the notification button that appears most of the time, denying the option
            sleep(delay)
            
        except:
            pass

        driver.find_element_by_class_name('_6q-tv').click() # click on the tab where the stories are
        sleep(delay)

        loadstories = '' # variable to terminate the loop without errors

        while loadstories != 0:

            sleep(delay)

            try:
                driver.find_element_by_class_name('coreSpriteRightChevron').click() # next storie button
                
            except KeyboardInterrupt:
                print('\033[0;33mProgram terminated by the user!\033[m')
                loadstories = 0
                
            except:
                print('\033[0;33mEND! No more stories to view\033[m') 
                loadstories = 0


    # running function for login
    try:
        botlogin(username, password)
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
    except:
        print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')

    # running function to see the stories
    try:
        stories()
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
    except:
        print('\033[0;31mUNEXPECTED ERROR ON STORIES\033[m, please try again and verify your connection!')

    print('')
    print('Finish!')
    print('')

