import random
import threading
import time

from classes import ServerHost, ConnectedClient

FILLER_BAR = "#-------------------#"

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
