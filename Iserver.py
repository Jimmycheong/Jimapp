"""Iserver.py

This file contains code to create a server.

"""

import argparse

from classes import ServerHost
from methods import FILLER_BAR


def main(host: str, port: int):
    global server_host
    server_host = ServerHost(host, port, 3)
    server_host.setup_listening_socket()
    print(f"""
    {FILLER_BAR} \n
    Server has started
    Hosting on: {server_host.address}\n
    
    Ready to serve.....
    {FILLER_BAR}
    """)

    try:
        server_host.start_listening()

    except (SystemExit):
        print("Shutting down server host...")

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
