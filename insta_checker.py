
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
import time

def check_instagram(username, password, specific_user):
    # Set up Chrome options
    options = Options()
    options.add_argument("--incognito")

    # Set up driver
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.instagram.com')

    # Log in
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button/div[text()="Log in"]'))).click()

    # Click 'Not Now' for notifications

    # Go to messages
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Messages"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not Now"]'))).click()
    # Check messages from specific user
    while True:
        try:
            # Find the chat with the specific user
            chat = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//a[@href="/direct/t/{specific_user}/"]')))
            # Check if there's a 'New message' badge
            if chat.find_element_by_xpath('.//div[text()="New message"]'):
                print('New message received')
                playsound('sound.mp3')
                break
        except Exception as e:
            print('No new message yet')
        time.sleep(5)  # Wait before checking again

    driver.quit()

check_instagram('goldarmgang69', '@Opboy64', 'prianajain')
