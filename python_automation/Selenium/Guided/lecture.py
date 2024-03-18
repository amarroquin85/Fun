from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
service = Service('C:\\Users\\alexm\\OneDrive\\Desktop\\ITprojects\\Projects\\Fun\\python_automation\\Selenium\\chromedriver.exe')

def get_driver():
    #set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches',['enable-logging'])
    driver= webdriver.Chrome(service=service,options=options)
    return driver
def clean_text(text):
    """Extract only the temperature from the text"""
    output = float(text.split(":")[1])
    return output
def main():
    driver = get_driver()
    driver.get("http://automated.pythonanywhere.com/login/")
    time.sleep(3)
    driver.find_element(by="id",value="id_username").send_keys("automated")
    driver.find_element(by="id",value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    text = driver.find_element(by="id",value="displaytimer").text
    
    print(text)
    print(clean_text(text))
main()
    