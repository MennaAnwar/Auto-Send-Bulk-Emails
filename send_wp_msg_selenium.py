from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace with your own message and phone number
message = "Hello, world!"
number = "+201014742409"  # Don't forget to include the country code

# Start up a new Chrome browser
browser = webdriver.Chrome()

# Load WhatsApp web
browser.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code
input("Scan the QR code and press Enter to continue...")

# Search for the user or group by phone number
search_box = browser.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
search_box.send_keys(number + Keys.RETURN)

# Wait for the chat to load
time.sleep(5)

# Find the message input box and type the message
message_box = browser.find_element(By.XPATH,'//div[@class="_3FRCZ copyable-text selectable-text"][@data-tab="1"]')
message_box.send_keys(message + Keys.RETURN)

# Wait for the message to send
time.sleep(5)

# Close the browser
browser.quit()

print("Message sent successfully!")