from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from properties import username, password, number

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com/')

        sleep(5)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(2)

        # input email/username
        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input.send_keys(username)
        sleep(0.5)

        # input password
        password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_input.send_keys(password)
        sleep(0.5)

        # commit login
        commit = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        commit.click()
        sleep(2)

        # Switch back to base window
        self.driver.switch_to_window(base_window)
        sleep(2)

        # input number
        # number_input = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        # number_input.send_keys(number)

        # commit_number
        # commit = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        # commin.click()

        # closing popups
        popup_localization = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_localization.click() # accept
        sleep(1)

        popup_notification = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        popup_notification.click() # refuse
        sleep(1)

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()


    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()


    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.dislike()
            except Exception:
                try:
                    print('Closing pop up!')
                    self.close_popup()
                except Exception:
                    print('Out of likes. Closing app.')
                    self.out_of_likes()


    def close_popup(self):
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()

    def close_match(self):
        pass
        # match = self.driver.find_element_by_xpath('')
        # match.click()

    def out_of_likes(self):
        out = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        out.click()
        self.driver.quit()
        sleep(0.5)
        exit()

    def next_photo(self):
        next_ft = self.driver.find_element_by_xpath('//*[@id="Tinder"]')
        next_ft.send_keys(Keys.SPACE)

bot = TinderBot()

try:
    bot.login()
    # bot.auto_swipe()
except Exception as err:
    print(err)
    bot.driver.quit()
    exit(1)
