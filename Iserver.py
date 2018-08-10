"""Iserver.py

This file contains code to create a server.

"""
import argparse
from time import sleep

from classes import ServerHost, ConnectedClient
from methods import FILLER_BAR, spawn_serving_thread


def main(host: str, port: int):
    global server_host
    server_host = ServerHost(host, port, 3)
    server_host.setup_listening_thread()
    print('Waiting for connection.....')

    print(f"""
    {FILLER_BAR} \n
    Server has started
    Hosting on: {server_host.address}\n
    {FILLER_BAR}
    """)

    while True:
        try:
            conn, addr = server_host.listener.accept()
            print('Establishing connection with: ', conn.getpeername())

            new_client = ConnectedClient(conn)

            # TODO: Add debug if client does not exists in the server_host's client list
            if new_client not in server_host.clients:
                server_host.clients.append(new_client)
                new_client.serving_thread = spawn_serving_thread(server_host, new_client)

        except (KeyboardInterrupt, SystemExit):
            server_host.listener.close()
        sleep(0.5)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--p", help="Port number")
    parser.add_argument("--a", help="Address number")
    args = parser.parse_args()

    try:
        port = int(args.p)
    except:
        port = 5000

    try:
        address = str(args.a)
    except:
        address = '127.0.0.1'

    main(address, port)
