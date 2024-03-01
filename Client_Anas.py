# Anas : https://lvdneng.rosselcdn.net/sites/default/files/dpistyles_v2/vdn_864w/2022/12/16/node_1267557/55798445/public/2022/12/16/B9732927551Z.1_20221216095912_000%2BGMRLS4N21.2-0.jpg?itok=QUtHl2bf1671273463
# photo sur site web pour context : https://www.lavoixdunord.fr/1267557/article/2022-12-16/le-rappeur-anas-benturquia-des-tours-de-villeneuve-d-ascq-celles-de-dubai


import socket

age = 21
port = 50000 + age

# Adresse et port du serveur
server_address = ('localhost', port)

# Création du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect(server_address)

# Envoi de la requête au serveur, décommenter pour tester : 
request = "Serveur es-tu là, tu vas bien, je m'appelle Anas ?"
# request = "je sui a laeropor bisouuuu je manvol"

# envoi de la requête
client_socket.send(request.encode())

# Réception de la réponse du serveur
response = client_socket.recv(1024).decode()

# Affichage de la réponse
print("Réponse du serveur :", response)

# Fermeture de la connexion lorssoukou il i a lairopoourt
client_socket.close()