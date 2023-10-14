from PyQt5 import QtCore, QtGui, QtWidgets
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pyautogui



class Ui_KamikazeBOT(object):


    ## -------------------- Fonction pour importer les données d'authentification à partir du fichier credentials.txt -------------------- ##
    def import_credentials(self):
        import os

        # Obtenez le répertoire du script actuel
        script_directory = os.path.dirname(__file__)

        # Construisez le chemin complet du fichier credentials.txt
        file_path = os.path.join(script_directory, 'datas', 'credentials.txt')

        # Vérifiez si le fichier existe
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    mail = lines[0].strip()
                    password = lines[1].strip()
                    return mail, password
        else:
            print(f"Le fichier {file_path} n'a pas été trouvé.")
            return None, None
        

    ## -------------------- Fonction pour importer les messages à spammer à partir du fichier spams_to_send.txt -------------------- ##
    def import_spam_messages(self):
        import os

        # Obtenez le répertoire du script actuel
        script_directory = os.path.dirname(__file__)

        # Construisez le chemin complet du fichier spams_to_send.txt
        file_path = os.path.join(script_directory, 'datas', 'spams_to_send.txt')

        # Créez une liste pour stocker les messages
        messages = []

        # Vérifiez si le fichier existe
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    # Supprimez les espaces inutiles et ajoutez la ligne à la liste
                    message = line.strip()
                    if message:
                        messages.append(message)
            return messages
        else:
            print(f"Le fichier {file_path} n'a pas été trouvé.")
            return None


    ## -------------------- Fonction pour activer l'anti-captcha -------------------- ##
    def active_anti_capcha(self, driver):

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


    ## -------------------- Fonction pour se connecter à Discord -------------------- ##
    def connect_to_discord(self, driver, mail, password):
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

    
    ## -------------------- Fonction pour spammer de messages un salon d'un channel Discord -------------------- ##
    def spamMessages(self, mail, password, channel_id, salon_id, gif_list, anti_capcha_is_active = False):
        driver = webdriver.Chrome()

        if anti_capcha_is_active:
            self.active_anti_capcha(driver)

        self.connect_to_discord(driver, mail, password)
        
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



    ## -------------------- Fonction appeler lors de l'appui sur le bouton pour lancer le bot -------------------- ##
    def start_bot(self):

        email, password = self.import_credentials()
        tab_spam_messages = self.import_spam_messages()
        

        # Récupère l'URL du serveur Discord
        input_text = self.lineEdit.text()

        # Récupère l'état de la checkbox
        anti_capcha_is_active = self.checkBox.isChecked()

        # Sépare l'URL en utilisant le caractère '/'
        url_parts = input_text.split('/')

        # Recherche de la partie "channels" dans l'URL
        channel_index = url_parts.index("channels")

        # Extraire channel_id et salon_id de l'url de type https://discord.com/channels/<id_channel>/<id_saloon>
        if len(url_parts) > channel_index + 2:
            channel_id = url_parts[channel_index + 1]           # <id_channel>
            saloon_id = url_parts[channel_index + 2]             # <id_saloon>
            
            self.spamMessages(email, password, channel_id, saloon_id, tab_spam_messages, anti_capcha_is_active)

        else:
            print("URL invalide, veuillez fournir un lien Discord valide.")



    def setupUi(self, KamikazeBOT):
        KamikazeBOT.setObjectName("KamikazeBOT")
        KamikazeBOT.resize(489, 597)
        self.centralwidget = QtWidgets.QWidget(KamikazeBOT)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 467, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold")
        font.setPointSize(30)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.checkBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setIconSize(QtCore.QSize(16, 16))
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox, 0, QtCore.Qt.AlignHCenter)



        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.start_bot)

        KamikazeBOT.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(KamikazeBOT)
        self.statusbar.setObjectName("statusbar")
        KamikazeBOT.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(KamikazeBOT)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 22))
        self.menubar.setObjectName("menubar")
        KamikazeBOT.setMenuBar(self.menubar)

        self.retranslateUi(KamikazeBOT)
        QtCore.QMetaObject.connectSlotsByName(KamikazeBOT)

    def retranslateUi(self, KamikazeBOT):
        _translate = QtCore.QCoreApplication.translate
        KamikazeBOT.setWindowTitle(_translate("KamikazeBOT", "Kamikaze BOT"))
        self.label_2.setText(_translate("KamikazeBOT", "Kamikaze BOT"))
        self.label.setText(_translate("KamikazeBOT", "Server Discord URL"))
        self.checkBox.setText(_translate("KamikazeBOT", "Anti Captcha"))
        self.pushButton.setText(_translate("KamikazeBOT", "Start BOT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KamikazeBOT = QtWidgets.QMainWindow()
    ui = Ui_KamikazeBOT()
    ui.setupUi(KamikazeBOT)
    KamikazeBOT.show()
    sys.exit(app.exec_())
