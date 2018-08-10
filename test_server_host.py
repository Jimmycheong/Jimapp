"""test_server_host.py

"""
from time import sleep

import pytest
import socket
from grappa import should

from classes import ServerHost

HOST = "127.0.0.1"
PORT = 5000
MAX_CONN = 3



@pytest.fixture(scope="module")
def create_server_host():
    server_host = ServerHost(HOST, PORT, MAX_CONN)
    return server_host


class TestServerHost:

    def test_setup_listening_socket(self, create_server_host):

        server_host = create_server_host

        server_host.setup_listening_socket()

        server_host.listener | should.be.a(socket.socket)

        server_host.listener.close()


    # def test_server_can_receive_connections_from_clients(self, create_server_host):
    #     server_host = create_server_host
    #
    #     new_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     new_client.connect((HOST, PORT,))
    #
    #     sleep(1)
    #
    #     server_host.clients | should.contain.item(new_client)
