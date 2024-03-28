import csv
import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

def send_whatsapp_message(msg: str):
    try:
       with open("whatsapp.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, PhoneNumber in reader:
            
            pywhatkit.sendwhatmsg_instantly(phone_no=PhoneNumber, message=msg,tab_close=False)
            time.sleep(10)
            pyautogui.click()
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')
            print("Message sent!")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    send_whatsapp_message(msg="hello , This is a test msg for a project^^.sry for disturbance")