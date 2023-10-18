# Importiere die erforderlichen Bibliotheken
import os
import json

# Definiere die Benutzerdaten
users = [
    {
        "username": "johndoe",
        "password": "password",
        "roles": ["user", "admin"]
    },
    {
        "username": "janedoe",
        "password": "password",
        "roles": ["user"]
    }
]

# Definiere die Funktion zum Autorisieren eines Benutzers
def authorize_user(username, password):
    # Finde den Benutzer
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user["roles"]

    return []

# Definiere die Funktion zum Erstellen eines Tokens
def create_token(username, roles):
    # Erzeuge ein zufälliges Token
    token = os.urandom(32).hex()

    # Speichere das Token in einer Datei
    with open("token.txt", "w") as f:
        f.write(token)

    return token

# Starte den Server
while True:
    # Empfange eine Anfrage
    request = input()

    # Analysiere die Anfrage
    if request == "login":
        # Autorisiere den Benutzer
        roles = authorize_user(input("Benutzername: "), input("Passwort: "))

        # Erstelle ein Token
        token = create_token(input("Benutzername: "), roles)

        # Sende das Token zurück
        print("Token: " + token)

    elif request == "logout":
        # Lösche das Token
        os.remove("token.txt")

        # Gebe eine Erfolgsmeldung zurück
        print("Logout erfolgreich")

    else:
        # Gebe eine Fehlermeldung zurück
        print("Unbekannte Anfrage")
