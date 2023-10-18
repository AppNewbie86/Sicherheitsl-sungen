# Importiere die erforderlichen Bibliotheken
import json

# Definiere die Rollen
roles = {
    "user": {
        "permissions": ["read", "write"]
    },
    "admin": {
        "permissions": ["read", "write", "delete"]
    }
}

# Definiere die Funktion zum Autorisieren einer Aktion
def authorize_action(user_role, action):
    # Finde die Rolle des Benutzers
    role = roles.get(user_role)
    if role is None:
        return False

    # Überprüfe, ob die Aktion in den Berechtigungen der Rolle enthalten ist
    return action in role["permissions"]
