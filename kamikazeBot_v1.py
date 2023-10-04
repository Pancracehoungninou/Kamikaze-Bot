import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

# Utilisez ChromeDriverManager pour gérer le WebDriver Chrome
driver = webdriver.Chrome()

def connect_to_discord(mail, password):
    # Ouvrez le site web avec le formulaire
    driver.get("https://discord.com/login")

    # Attendre quelques secondes (facultatif)
    time.sleep(1)

    # Remplissez le formulaire avec les données
    email_input = driver.find_element(By.NAME, "email")  
    password_input = driver.find_element(By.NAME, "password")  
    email_input.send_keys(mail)
    password_input.send_keys(password)

    # Capture d'écran (facultatif)
    driver.save_screenshot("discord_SpamBOT.png")

    # Envoyez le formulaire (peut varier en fonction de la page)
    connect_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    connect_btn.click()
    time.sleep(1)

# Fonction pour se connecter à Discord et envoyer des messages
def spamMessages(mail, password, channel_id, salon_id, gif_list):
    
    connect_to_discord(mail, password)
    
    # Naviguez vers la page du salon avec l'ID
    driver.get(f"https://discord.com/channels/{channel_id}/{salon_id}")
    time.sleep(3)

    msg_input = driver.find_element(By.CSS_SELECTOR, '[role="textbox"]')

    # Mélangez la liste de manière aléatoire
    random.shuffle(gif_list)

    for i, gif_url in enumerate(gif_list):
        msg_input.send_keys(gif_url)
        pyautogui.press('ENTER')
        print(f"Message #{i + 1} envoyé !")

    time.sleep(3)

    # Fermez le navigateur
    driver.quit()

# Vos données d'authentification et de cible
mail_account = "enzolezozo74@gmail.com"
password_account = "Spambot0."
channel_id = "1159060146085974046"
salon_id = "1159060683770576917"

# Liste de GIFs horribles à utiliser pour spammer le jour J
horribleGIFs = [
    "https://media.discordapp.net/attachments/804052933074747423/1061772410136838184/023A4127-D2C9-495D-A9A6-E5D6D189AEB2.gif?ex=6516a5dd&is=6515545d&hm=8d7c7e19b6238f0502a25144ef264dbeebc251dc8d220479c14b0d4d94fcbaf0&",
    "https://media.discordapp.net/attachments/988862412260274176/1006469577917616128/rek-2.gif",
    "https://media.giphy.com/media/QU3qqW1s5CG9OfLVm4/giphy.gif",
    "https://media.discordapp.net/attachments/1051496462602743828/1101771781712388096/speech_hunnypaint.gif",
    "https://media.discordapp.net/attachments/940874052313157673/952619369521893386/Di_Drone_Strike.gif",
    "https://cdn.discordapp.com/attachments/947311594793234465/1128894439205638184/give_me_some_pushups.gif", 
    "https://media.discordapp.net/attachments/616545188441096214/616755424154091723/17274551.gif",
    "https://media.discordapp.net/attachments/878431660822110238/1079244777620512868/ezgif.com-video-to-gif.gif",
    "https://media.giphy.com/media/ndTwJoUxnpdtuB9Fqx/giphy.gif",
    "https://media.discordapp.net/attachments/1019605363240218714/1022979671220035604/c87d_X.gif",
    "https://media.discordapp.net/attachments/697632190162534400/811758015085936650/doublepica.gif",
    "https://media.discordapp.net/attachments/824586860834586628/1057500911406166098/rJghnPFB.gif",
    "https://media.discordapp.net/attachments/884554983104729109/1013121391488409730/C4F5E6BD-74F8-426B-A45D-85D17ADB5ACF-2.gif",
    "https://giphy.com/gifs/EooFElWfrBWMO05mIi",
    "https://media.discordapp.net/attachments/589796596749828117/982348833872818176/ckUslmZH.gif",
    "https://media.discordapp.net/attachments/873232945299742783/1043619539780370442/Panic_speechbubble.gif",
    "https://cdn.discordapp.com/attachments/622853505383661604/988048547255554048/image0-6.gif",
    "https://media.discordapp.net/attachments/804052933074747423/1022568205664911410/image0.gif",
    "https://media.discordapp.net/attachments/547047227080835072/893164025469366302/image0.gif",
    "https://media.discordapp.net/attachments/997058853390798888/1023733875349913691/giphy_1.gif",
    "https://media.discordapp.net/attachments/873232945299742783/1053234338663243776/gn.gif",
    "https://media.discordapp.net/attachments/915662777375391814/998912194563538984/ezgif.com-gif-maker.gif",
    "https://media.discordapp.net/attachments/1048298408194089051/1057214325191884810/cryaboutit.gif"
]

# Liste de GIFs à utiliser pour tester le bot (des gifs normaux)
testGIFs = [
    "https://media.discordapp.net/attachments/466373431231905793/1009953158279221278/caption.gif",
    "https://tenor.com/view/cat-blink-cat-blinking-cat-funny-cat-funny-cat-blinking-gif-27202865",
    "https://tenor.com/view/on-my-way-cat-run-cat-on-my-way-cat-cat-on-my-way-gif-26471384",
    "https://tenor.com/view/shocked-surprised-gasp-what-cat-shock-gif-635629308990545194",
    "https://tenor.com/view/kitty-cat-sandwich-cats-sandwich-gif-26112528",
    "https://tenor.com/view/crazy-cat-insane-cat-help-my-cat-is-insane-help-my-cat-cat-gif-21688581"
]

# Nombre d'instances que vous souhaitez créer
num_instances = ["1159060683770576917"]  # Par exemple, créez 3 instances

# Créez les instances
for saloon_id in num_instances:
    spamMessages(mail_account, password_account, channel_id, saloon_id, testGIFs)