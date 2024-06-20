from time import sleep
from win11toast import toast

i = 1
while True:
    sleep(1)
    toast(
        "Your Nabee",
        "Hey Hubby! Computer theke utho na!",
        icon=r"E:\Cartoon\Alcatraz\IMG-20240325-WA0022.jpg",
        audio="ms-winsoundevent:Notification.Looping.Alarm",
        button="Dismiss",
        image=r"E:\Cartoon\Alcatraz\WhatsApp Image 2024-04-11 at 10.24.16 AM (2).jpeg",
    )
    i += 1
    if i == 3:
        break
