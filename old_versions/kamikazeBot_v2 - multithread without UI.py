import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import threading

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
    time.sleep(2)

    msg_input = driver.find_element(By.CSS_SELECTOR, '[role="textbox"]')

    # Mélangez la liste de manière aléatoire
    random.shuffle(gif_list)

    for i, gif_url in enumerate(gif_list):
        msg_input.send_keys(gif_url)
        pyautogui.press('ENTER')
        print(f"Message #{i + 1} envoyé !")

    time.sleep(1)

    # Fermez le navigateur
    driver.quit()



# Vos données d'authentification et de cible
mail_account = "<votre_adresse_mail>"
password_account = "<votre_mdp>"
channel_id = "1159060496185974146"
saloon_ids = ["115906654837706917", "1159104389448656"]  # Liste des salons à cibler


# Liste de GIFs à utiliser pour tester le bot (des gifs normaux)
testGIFs = [
    "https://media.discordapp.net/attachments/466373431231905793/1009953158279221278/caption.gif",
    "https://tenor.com/view/cat-blink-cat-blinking-cat-funny-cat-funny-cat-blinking-gif-27202865",
    "https://tenor.com/view/on-my-way-cat-run-cat-on-my-way-cat-cat-on-my-way-gif-26471384",
    "https://tenor.com/view/shocked-surprised-gasp-what-cat-shock-gif-635629308990545194",
    "https://tenor.com/view/kitty-cat-sandwich-cats-sandwich-gif-26112528",
    "https://tenor.com/view/crazy-cat-insane-cat-help-my-cat-is-insane-help-my-cat-cat-gif-21688581"
]

# Créez une liste de threads pour exécuter plusieurs instances en parallèle
threads = []

# Créez une instance pour chaque salon
for saloon_id in saloon_ids:
    thread = threading.Thread(target=spamMessages, args=(mail_account, password_account, channel_id, saloon_id, testGIFs))
    threads.append(thread)

# Lancez toutes les instances en même temps
for thread in threads:
    thread.start()

# Attendez que toutes les instances se terminent
for thread in threads:
    thread.join()
