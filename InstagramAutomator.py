from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

FILE = input("Enter the pathname of the file: ")
TEXT = input("Enter the caption: ")
'''print("Enter the Instagram caption. When you're done, enter a single period on a line by itself.")
buffer = []
while True:
    print("> ", end="")
    line = input()
    if line == ".":
        break
    buffer.append(line)
multiline_string = "\n".join(buffer)
#print(multiline_string)
TEXT = multiline_string'''

driver = webdriver.Chrome(executable_path=r"/Users/sparshgarg/Downloads/chromedriver") #path of the chromedriver on your device
action = ActionChains(driver)
driver.implicitly_wait(1)

driver.get('https://www.instagram.com/')
sleep(2)

username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")

username_input.send_keys("emaiol@email.com") #your instagram email
password_input.send_keys("passowrd") #your instagram password

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)

post_button = driver.find_element_by_xpath("//button[@class='wpO6b ZQScA ']")
post_button.click()

sleep(3)

upload_btn = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
sleep(2)
upload_btn.send_keys(FILE)

sleep(10)
next_btn = driver.find_element_by_xpath("//button[text()='Next']")
next_btn.click()

sleep(2)
next_btn_2 = driver.find_element_by_xpath("//button[text()='Next']")
next_btn_2.click()

sleep(2)
write = driver.find_element(By.TAG_NAME, 'textarea')
write.click()
write.send_keys(TEXT)

sleep(2)
share_btn = driver.find_element_by_xpath("//button[text()='Share']")
share_btn.click()
