import random
import socket
from typing import List

FILLER_BAR = "#-------------------#"


class ConnectedClient:

    def __init__(self, socket_conn: socket, username: str = "user" + str(random.randint(1, 200))):
        self.username = username
        self.socket_conn = socket_conn
        self.address = socket_conn.getpeername()
        self.serving_thread: socket = None


class ServerHost:

    def __init__(self, host: str, port: int, maximum_no_of_connections: int = 5):
        self.host = host
        self.port = port
        self.maximum_connections = maximum_no_of_connections
        self.address = f"{host}:{port}"
        self.listener = None
        self.clients: List[ConnectedClient] = []

    def setup_listening_thread(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind((self.host, self.port))
        listener.listen(self.maximum_connections)

        self.listener = listener

    def get_IPs(self):
        return list(map(lambda c: c.address, self.clients))

    def get_client_usernames(self):
        return list(map(lambda c: c.username, self.clients))

    def remove_client(self, connected_client: ConnectedClient):
        print(connected_client)
        print(f"My list before removing: {self.clients}")
        return self.clients.remove(connected_client)

    def broadcast_message(self, data):
        """

        Used to broadcast message to all clients

        Params:
            data(str): the message to broadcast

        """

        print(f""" \
        <===SENDING===> \
        LISTEN TO THE CLIENTS: {self.clients} \
        """)

        for client in self.clients:
            client.socket_conn.sendto(str.encode(data), client.address)

        print('<===COMPLETE===>')
