from selenium import webdriver
from time import sleep

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')
    
    # def crop(self):
    #     image = 
    
    def navigate(self):
        self.driver.get('')
        button = self.driver.find_element_by_xpath('//button[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_small item-phone-button_header js-item-phone-button_header"]')
        button.click()
        sleep(3)
        self.take_screenshot()

        image = self.driver.find_element_by_xpath('//div[@class"item-phone-big-number js-item-phone-big-number"]//*')
        location = image.location
        size = image.size 
        self.crop(location, size)

def main():
    b = Bot()

if __name__ == '__main__':
    main()
