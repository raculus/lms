from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LMS():
    driver = ''

    def __init__(self):
        #Chromedriver Options
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        #options.add_argument('disable-gpu')

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)

        self.driver.get(url='https://lms.namhae.ac.kr')

    def login(self,id, pw):
        self.driver.find_element(By.ID, 'input-username').send_keys(id)
        self.driver.find_element(By.ID, 'input-password').send_keys(pw)
        self.driver.find_element(By.ID, 'input-password').send_keys(Keys.ENTER)
    def courseList(self):
        list = []
        aList = self.driver.find_elements(By.CSS_SELECTOR, 'div.course_lists > ul > li > div > a')
        titleList = self.driver.find_elements(By.CSS_SELECTOR, 'div.course-name > div.course-title > h3')
        for a, title in zip(aList, titleList):
            a = a.get_attribute('href')
            title = title.text
            list.append([a, title])
        return list
            

##todo: remove
lms = LMS()
lms.login('21901029', '000208')
lms.courseList()
