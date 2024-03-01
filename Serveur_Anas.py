# Anas : https://lvdneng.rosselcdn.net/sites/default/files/dpistyles_v2/vdn_864w/2022/12/16/node_1267557/55798445/public/2022/12/16/B9732927551Z.1_20221216095912_000%2BGMRLS4N21.2-0.jpg?itok=QUtHl2bf1671273463
# photo sur site web pour context : https://www.lavoixdunord.fr/1267557/article/2022-12-16/le-rappeur-anas-benturquia-des-tours-de-villeneuve-d-ascq-celles-de-dubai


import socket

age = 21
port = 50000 + age

while True:
    try:
        # Instancie un socket d'écoute
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Lie le socket à l'adresse locale et au port
        server_socket.bind(('localhost', port))
        
        # Active le mode d'écoute du socket
        server_socket.listen(1)
        
        print(f"Le serveur écoute sur le port {port}...")
        
        # Accepte la connexion du client
        client_socket, client_address = server_socket.accept()
        print(f"Client connecté depuis {client_address}")
        
        # Attend de recevoir un message du client
        message = client_socket.recv(1024).decode()
        print(f"Message reçu du client : {message}")
        
        # Renvoie le message au client avec le texte supplémentaire
        response = message + "\nJe suis là !"
        client_socket.send(response.encode())
        
        if message == "je sui a laeropor bisouuuu je manvol" :
            # Ferme la connexion
            client_socket.close()
            server_socket.close()
            break
        
    except OSError:
        # Si le port est déjà occupé, augmentez-le de 100
        port += 100