# Importing

import requests
import time
import random
import os
from colored import fg, bg, attr

# Colors

color = input('Enter Your Color:').strip()
color1 = fg(color)
red = fg(1)
blue = fg(50)
gg = fg(33)

# Save Folder By Name

try:
    os.mkdir('photo')
except:
    pass

# The Art

print(color1+ """    ___         __           ____             _____ __        ____  _     
   /   | __  __/ /_____     / __ \_________  / __(_) /__     / __ \(_)____
  / /| |/ / / / __/ __ \   / /_/ / ___/ __ \/ /_/ / / _ \   / /_/ / / ___/
 / ___ / /_/ / /_/ /_/ /  / ____/ /  / /_/ / __/ / /  __/  / ____/ / /__  
/_/  |_\__,_/\__/\____/  /_/   /_/   \____/_/ /_/_/\___/  /_/   /_/\___/  
                                                                            - by @1xm0d Tyizo , Dont Sell it !""")

s = requests.session()

# Instagram username

user = str(input(gg+'Put your username: '))

# Instagram password user

password = str(input(gg+'Put your password: '))

# Sleep => Secends

mySleep = int(input(gg+'Sleep (sec) : '))

url_ig = 'https://www.instagram.com/accounts/login/ajax/'
ig = s.get('https://www.instagram.com').cookies['csrftoken']
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
s.headers = {'user-agent': user_agent}
s.headers.update({'referer': 'https://www.instagram.com'})
s.headers.update({'x-csrftoken': ig})
payload = {"username": user, 'enc_password': '#PWD_INSTAGRAM_BROWSER:0:' + str(int(time.time())) + ':' + password}
r = s.post(url_ig, data=payload)
if r.json()["authenticated"]:
    print(f"Login Done ✔ @{user}")
else:
    print("Somthing went wrong !")
    input('Enter to exit ... ')
    exit()
s.headers.update({'x-csrftoken': r.cookies['csrftoken']})
profile_picture = 'https://www.instagram.com/accounts/web_change_profile_picture/'
print('\n')
while True:
    path = os.getcwd()
    photo = os.listdir('photo')
    r = random.choice(photo)
    x = (r'{}\photo\{}'.format(path, r))
    p_pic = x
    p_pic_s = os.path.getsize(x)
    files = {'profile_pic': open(p_pic, 'rb')}
    s.headers.update({"Content-Length": str(p_pic_s)})
    payload2 = {"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg",
    "Content-Type": "image/jpeg"}
    try:
        change_profile_picture = s.post(profile_picture, data=payload2, files=files)
        status = change_profile_picture.json()['status']
        print(color1+'Profile Picture Changed', status)
    except:
        print(color1+'Error , Try Again .. ', f'({r})')
    time.sleep(mySleep)