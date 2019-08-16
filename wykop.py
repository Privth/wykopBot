from selenium import webdriver
from selenium.webdriver.common import keys
import time

class WykopBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.wykop.pl/mikroblog/')
        time.sleep(1)

        logInButton = bot.find_element_by_class_name('dropdown-show')
        logInButton.click()

        login = bot.find_element_by_id('newregister-login')
        password = bot.find_element_by_id('newregister-pass')
        submit = bot.find_element_by_xpath('/html/body/div[1]/div/ul[2]/li[4]/div/div/ul/li[1]/form/fieldset/p/input')

        login.clear()
        password.clear()

        login.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

    def plusbot(self):
        bot = self.bot
        bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        while True:
            pluses = bot.find_elements_by_class_name('mikro')
            for plus in pluses:
                plus.click()

test = WykopBot('yourUserName', 'yourPassword')
test.login()
test.plusbot()
