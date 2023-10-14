# Kamikaze-Bot 🤖
Spam BOT discord (se connecte automatiquement et envoie des GIFs dans les salons du channel choisi)
Fait en Python avec Selenium et Pyautogui

<br>


# Bot avec UI / Interface 📱

![alt text](https://github.com/alexiglnt/Kamikaze-Bot/blob/main/images/demo-ui.png?raw=true)

## Configuration du bot
- Lancer le fichier **`install_requirements.cmd`**, ce fichier va installer les modules Python nécessaires au fonctionnement du bot
- dans **`datas/credentials.txt`** : mettez votre adresse mail et votre mot de passe Discord l'un en dessous de l'autre en respectant ce format :


    **Exemple :** 

    ```
    johndoe@gmail.com
    password123
    ```

    Vos identifiants de connection ne seront utilisés que pour permettre au BOT de se connecter à Discord, ils ne seront pas stockés ou utilisés pour autre chose. 
    
- dans **`datas/spams_to_send.txt`** : mettez les messages/GIFs que vous voulez spammer dans les salon du channel Discord choisi. Mettez les messages/GIFs les uns en dessous des autres en respectant ce format : 

    **Exemple 1 (messages) :** 

    ```
    Ceci est un spam
    Booouuuuhh je t'ai eu
    hahahahahahahah
    Message automatique 😱
    I'm the boss 😎
    Envoie de messages
    Ceci est un bot de spam
    Je peux t'envoyer autant de messages que je veux dans ce channel 😈 
    ```
    **Exemple 2 (GIFs Discord) :** 

    ```
    https://media.discordapp.net/attachments/466373431231905793/1009953158279221278/caption.gif
    https://tenor.com/view/cat-blink-cat-blinking-cat-funny-cat-funny-cat-blinking-gif-27202865
    https://tenor.com/view/on-my-way-cat-run-cat-on-my-way-cat-cat-on-my-way-gif-26471384
    https://tenor.com/view/shocked-surprised-gasp-what-cat-shock-gif-635629308990545194
    https://tenor.com/view/kitty-cat-sandwich-cats-sandwich-gif-26112528
    https://tenor.com/view/crazy-cat-insane-cat-help-my-cat-is-insane-help-my-cat-cat-gif-21688581
    ```


## Prérequis
- Pour pouvoir spammer un salon Discord il faut évidemment que vous soyez dans le channel
- Il vous faut un compte Discord avec **IP vérifiée** pour éviter le **captcha** lors de la connexion à Discord 

    Si vous lancez le bot sur un réseaux sur lequel vous n'avez jamais été connecté à **Discord Web** auparavant, alors allez sur https://discord/login et connectez vous une première fois, à la main, pour que Discord vérifie votre IP. Un mail va vous être envoyé par Discord pour vérifier votre connexion, cliquez sur le lien et vous pourrez lancer le bot sans problème.

    Si le captcha s'active quand même après avoir fait ceci, vous devrez cocher l'option **`Anti Captcha`** lors du lancement du bot (case à cocher dans l'interface). Le bot sera un peu plus lent, du au fait qu'il devra activer l'anti-captcha au démarrage, mais cela fonctionnera quand même.


<br>

## Lancement du bot

- Lancez le fichier **`RUN_BOT.cmd`** : ce fichier va lancer le bot et l'interface graphique s'ouvrira 
- Sur Discord Web, allez sur le channel, puis dans le salon (par exemple #general) dans lequel vous voulez spammer
- Copier l'URL entier de la page (par exemple https://discord.com/channels/176373431231905793/15373431231905795)
- Dans l'interface graphique, coller l'URL que vous venez de copier dans le champ **`Server Discord URL`**
- Cocher la case **`Anti Captcha`** si vous avez un captcha qui s'active lors de la connexion à Discord (voir ci-dessus dans ***Configuration du bot, étape 3***)
- Cliquez sur **`Start BOT`** et admirez le résultat 😈

<br>

![alt text](https://github.com/alexiglnt/Kamikaze-Bot/blob/main/images/video-demo.png?raw=true)

<br><br><br>


# Anciennes Versions du BOT 🤖 :

## V1 :
- se connecte automatiquement à Discord
- se rend sur le channel souhaité puis dans le salon souhaité 
- spam de GIFs (stockés dans un tableau)

## V2 (en cours) :
- se connecte automatiquement à Discord
- se rend sur le channel souhaité puis dans le salon souhaité 
- spam de GIFs (stockés dans un tableau)
- **multithreading --> pour pouvoir créer plusieurs instances de Selenium et donc raid plusieurs salons en même temps**
