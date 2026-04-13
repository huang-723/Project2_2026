import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def check_soil():
    if GPIO.input(channel):
        return "Please water your plant"
    else:
        return "Water NOT needed"

from_email_addr = "hyfgg20070723@qq.com"
from_email_pass = "kbumkthigyhfdfhc"
to_email_addr = "20119455@setu.ie"

def send_plant_email(status):
    body = status
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Plant Moisture Report'
    
    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    print('Email sent')
    server.quit()

seconds = time.time()
result = time.localtime(seconds)
print("Current TIME Hour:", result.tm_hour)

startTime = 11
lastValue = startTime
print ("Time to send the FIRST email of the day")

while (True):
    seconds = time.time()
    result = time.localtime(seconds)
    Current_Value = result.tm_hour

    if (lastValue == Current_Value):
        print ("IGNORE")
    else:
        difference = Current_Value - lastValue
        if (difference > 3):
            print ("Time difference > 3. Time to send an email")
            soil_status = check_soil()
            send_plant_email(soil_status)
            lastValue = Current_Value
        else:
            print ("Hour Difference < 4. Do NOT Email")

    time.sleep(1)
