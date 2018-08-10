from time import sleep

import random
import socket
import threading
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
        self.listener: socket = None
        self.clients: List[ConnectedClient] = []

    def setup_listening_socket(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind((self.host, self.port))
        listener.listen(self.maximum_connections)

        self.listener = listener

    def start_listening(self):
        try:
            while True:
                conn, addr = self.listener.accept()
                print('Establishing connection with: ', conn.getpeername())

                new_client = ConnectedClient(conn)

                # TODO: Add debug if client does not exists in the server_host's client list
                if new_client not in self.clients:
                    self.clients.append(new_client)
                    new_client.serving_thread = spawn_serving_thread(self, new_client)
                sleep(0.5)
        except KeyboardInterrupt:
            self.listener.close()

            print("Closing listening thread.")


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


def spawn_serving_thread(server_host: ServerHost, connection_client: ConnectedClient):
    """
        Create a new thread to connect to new client.
        :param connection_client:
        :param server_host:

        """
    spawned_thread = threading.Thread(target=start_serving_thread, args=(server_host, connection_client))
    spawned_thread.daemon = True
    spawned_thread.start()

    return spawned_thread


def start_serving_thread(server_host: ServerHost, connected_client: ConnectedClient):
    """
    # ===##===##===##===##===##===##===##===#
    # INDIVIDUAL THREAD OPERATION
    # ===##===##===##===##===##===##===##===#

    """

    client_socket = connected_client.socket_conn
    requested_name = client_socket.recv(1024).decode('utf-8')

    print(f"RECEIVED: {requested_name}")

    # TODO: Inform user that username is taken. Currently, adding random int if already exists
    if requested_name in server_host.get_client_usernames():
        requested_name += random.randint(1000, 3000)
    connected_client.username = requested_name

    print(f"""
        {FILLER_BAR} \ 
        Connection established. \
        Username added:  {requested_name} \
        Clients: {server_host.clients} \
        {FILLER_BAR} \
        """)

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if data == '':
            print(f"Removing {connected_client.username} from client list")
            server_host.remove_client(connected_client)
        else:
            print(f"RECEIVED DATA: '{data}'")
            splat = data.split('::')
            print('Received data: from {}'.format(splat[0]) + '\nAt ' + time.ctime(time.time()) + '::', splat[1])
            if 'Quit' in str(splat[1]):
                break
            if 'Finish' in str(splat[1]):
                print('Shutting Down.....\nPlease Wait a Moment')
                server_host.listener.close()
                break
            server_host.broadcast_message(data)
    connected_client.close()
