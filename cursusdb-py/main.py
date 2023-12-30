#
# CursusDB
# Python Native Client Module
# ******************************************************************
# Copyright (C) 2023 CursusDB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import base64
import socket

# CursusDB Cluster Client Class
class Client:
    def __init__(self, host, port, username, password, tls):
        self.sock = None
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.tls = tls

    # Instance method
    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        auth_str = f"{self.username}\\0{self.password}".encode("utf8")

        encoded_auth_str = base64.b64encode(auth_str)

        self.sock.sendall(b"Authentication: " + encoded_auth_str + b"\r\n")

        auth_response = self.sock.recv(2048)

        if auth_response.decode("utf-8").startswith("0"):
            return "Connected to cluster successfully."
        else:
            return auth_response

    def query(self, q):
        query_str = f"{q}\r\n".encode("utf8")
        self.sock.sendall(query_str)
        query_response = self.sock.recv(2097152)
        return query_response.decode("utf-8")

    def close(self):
        self.sock.close()
