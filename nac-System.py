# Importiere die erforderlichen Bibliotheken
import socket
import json

# Definiere die Funktion zum Überprüfen der IP-Adresse
def check_ip_address(ip_address):
    # Überprüfe, ob die IP-Adresse in der Liste der zugelassenen IP-Adressen enthalten ist
    allowed_ips = ["192.168.1.1", "192.168.1.2"]
    if ip_address in allowed_ips:
        return True

    return False

# Starte den Server
while True:
    # Empfange eine Verbindung
    connection, address = socket.accept()

    # Überprüfe die IP-Adresse
    if not check_ip_address(address[0]):
        # Verweigere den Zugriff
        connection.sendall(b"Access denied")
        connection.close()
        continue

    # Erlaube den Zugriff
    connection.sendall(b"Access granted")
    connection.close()
