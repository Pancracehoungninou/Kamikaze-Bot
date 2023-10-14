import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pyautogui

# Utilisez ChromeDriverManager pour gérer le WebDriver Chrome
driver = webdriver.Chrome()


def active_anti_capcha():

    driver.get("https://chrome.google.com/webstore/detail/nopecha-captcha-solver/dknlfmjaanfblgfdfebhijalfmhmjjjo?hl=fr")
    driver.maximize_window()
    
    # ouvrir le navigateur en plein écran
    print(f"SIze : {driver.get_window_size()}")

    time.sleep(0.5)

    # Cliquez sur le bouton "Ajouter à Chrome"
    add_to_chrome_btn = driver.find_element(By.CSS_SELECTOR, '[aria-label="Ajouter à Chrome"]')
    add_to_chrome_btn.click()
    time.sleep(5)

    # voir le click sur le bouton 
    # click a unen certaine position
    # pyautogui.click(822, 116)

    time.sleep(5)




    # # Créez une instance de WebDriverWait en utilisant le driver
    # wait = WebDriverWait(driver, 10)

    # # Wait for the alert to be displayed and store it in a variable
    # alert = wait.until(EC.alert_is_present())

    # # Store the alert text in a variable
    # text = alert.text

    # # Press the OK button
    # alert.accept()

    # # try:
    # #     WebDriverWait(driver, 10).until(EC.alert_is_present())
    # #     alert = driver.switch_to.alert
    # #     print("Alert exists in the page")
    # #     alert.accept()
    # # except Exception as e:
    # #     print(f"An error occurred: {str(e)}")


    # time.sleep(2)

    # alert = driver.switch_to.alert

    # time.sleep(3)

    # Utilisation de XPath pour trouver l'élément "Ajouter l’extension"
    # add_extension_btn = driver.find_element(By.XPATH, '//*[@aria-label="Ajouter l’extension"]')
    # add_extension_btn.click()


    # Cliquez sur le bouton "Ajouter l'extension"
    # add_extension_btn = driver.find_element(By.CSS_SELECTOR, '[aria-label="Ajouter l’extension"]')
    # add_extension_btn.click()

    # # Revenez au contexte par défaut
    # driver.switch_to.default_content()

    # time.sleep(3)

    # # Fermez le navigateur
    # driver.quit()


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
def spamMessages(mail, password, channel_id, salon_id, gif_list, anti_capcha_is_active = False):
    
    
    if anti_capcha_is_active:
        active_anti_capcha()

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
mail_account = "<votre_adresse_mail>"
password_account = "<votre_mdp>"
channel_id = "1159060496185974146"


# Liste de GIFs à utiliser pour tester le bot (des gifs normaux)
testGIFs = [
    "https://media.discordapp.net/attachments/466373431231905793/1009953158279221278/caption.gif",
    "https://tenor.com/view/cat-blink-cat-blinking-cat-funny-cat-funny-cat-blinking-gif-27202865",
    "https://tenor.com/view/on-my-way-cat-run-cat-on-my-way-cat-cat-on-my-way-gif-26471384",
    "https://tenor.com/view/shocked-surprised-gasp-what-cat-shock-gif-635629308990545194",
    "https://tenor.com/view/kitty-cat-sandwich-cats-sandwich-gif-26112528",
    "https://tenor.com/view/crazy-cat-insane-cat-help-my-cat-is-insane-help-my-cat-cat-gif-21688581"
]

# Nombre d'instances que vous souhaitez créer (l'id des salons)
num_instances = ["1159694274770576917"]  # Par exemple, créez 3 instances

# Créez les instances
for saloon_id in num_instances:
    spamMessages(mail_account, password_account, channel_id, saloon_id, testGIFs, False)