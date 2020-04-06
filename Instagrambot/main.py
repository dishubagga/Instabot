from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys



class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        
    def closeBrowser(self):
        self.driver.close()
            
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(6)
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    
    def follow(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[3]/div[1]/a').click()

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
            time.sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click() #right
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click() #right
        for x in range(50):
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click() #right
            
            
        # hrefs = driver.find_elements_by_tag_name('a')
        # pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        # pic_hrefs = [href for href in pic_hrefs if hashtag in href]    
        # print(hashtag + 'photos:' + str(len(pic_hrefs)))
        
        # for pic_hrefs in pic_hrefs:
        #     driver.get(pic_hrefs)
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     try:
        #         driver.find_element_by_link_text("Like").click()
        #         time.sleep(18)
        #     except Exception as e:
        #         time.sleep(2)
                 
dishuIg = InstagramBot(" ","")
#dishuIg.login()
#dishuIg.like_photo('punjabiquotes')
dishuIg.follow()
# hashtags = ['amazing', 'beautiful', 'adventure']
# [dishuIg.like_photo(tag) for tag in hashtags]