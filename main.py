from time import sleep
import requests
from datetime import datetime
import smtplib

my_email = "👇put your email here"
my_password = "👇you need to open the service from your email account to get a new password"


MY_LAT = 32.006183 # Your latitude
MY_LONG = 34.787529 # Your longitude

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT <= iss_latitude + 5) and (MY_LAT <= iss_latitude - 5) and (MY_LONG <= iss_longitude + 5) and (
            MY_LONG <= iss_longitude - 5) :
        return True





#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunrise and sunset <= time_now:
        return True

while True:
    sleep(60)
    if is_night() and is_iss_close():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="👇put your email here", msg=f"Subject:iss over here!\n\nlook up to sky now")
        connection.close()




