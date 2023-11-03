import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

import time
load_dotenv()

ACCOUNT_EMAIL = os.environ.get('ACCOUNT_EMAIL')
ACCOUNT_PASSWORD = os.environ.get('ACCOUNT_PASSWORD')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')

def exit_application():
    # Click Close Button
    close_button = driver.find_element(By.CLASS_NAME, value="artdeco-button__icon")
    close_button.click()

    time.sleep(2)
    #Click Discard Button
    #discard_button = driver.find_element(By.CLASS_NAME, value="artdeco-button__text")
    discard_button = driver.find_element(by=By.LINK_TEXT, value="Discard")
    discard_button.click()


# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("detach", True)

# Create new driver
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.linkedin.com/jobs/search/?currentJobId=3744776625&distance=25&f_WT=2&geoId=103644278&keywords=Entry%20Level%20Python%20Developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true"
# Navigate to a webpage
driver.get(url)

# Click Reject Cookies Button
# time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# # Find the login element using CSS selector
# login = driver.find_element(By.CSS_SELECTOR, value="a.nav__button-secondary")
# # Get the href attribute of the login element
# href = login.get_attribute("href")
# # Click on the login button
# login.click()
time.sleep(5)
# Find the email input field using its ID
email = driver.find_element(By.ID, value="username")
# Check if the email input field is empty
if not email.get_attribute("value"):
    email.send_keys(ACCOUNT_EMAIL)

# Find the password input field using its ID
password = driver.find_element(By.ID, value="password")
# Check if the password input field is empty
if not password.get_attribute("value"):
    password.send_keys(ACCOUNT_PASSWORD)

# Get the Sign In button
sign_in = driver.find_element(By.CSS_SELECTOR, value="button.btn__primary--large.from__button--floating")
# Click on the Sign In button
sign_in.click()

# CAPTCHA - Solve the Puzzle Manually
#input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container")


# Find the save button and save the job posting for later
# save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button span")
# save_button.click()

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)

    try:
        # Click Apply Button
        easy_apply = driver.find_element(by=By.LINK_TEXT, value="Easy Apply")
        easy_apply.click() 

        # Find the phone number input field using its ID
        time.sleep(5)
        phone_number = driver.find_element(By.ID, value="input[id*=phoneNumber]")
        # Check if the password input field is empty
        if not phone_number.get_attribute("value"):
            phone_number.send_keys(PHONE_NUMBER)

        #Submit the application
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            exit_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        exit_application()
        print("No application button, skipped.")
        continue

#Find Easy Apply
# easy_apply = driver.find_element(by=By.LINK_TEXT, value="Easy Apply")
# easy_apply.click()

# # Find the phone number input field using its ID
# phone_number = driver.find_element(By.ID, value="input[id*=phoneNumber]")
# # Check if the password input field is empty
# if not phone_number.get_attribute("value"):
#     phone_number.send_keys(PHONE_NUMBER)

# #Submit the application
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
# submit_button.click()

time.sleep(5)
driver.quit()
