#!/usr/bin/env python
# -*- coding:utf-8 -*-

import CommonPath
import time
import sys
from QuickNet import AsyncCore
from logger import logging
import threading


class Client(threading.Thread):
    def __init__(self, ip, port):
        super(Client, self).__init__()
        self.ip = ip
        self.port = port
        self.hid = None
        self.con_mgr = AsyncCore()

    def connect(self):
        connect_hid = self.con_mgr.new_connect(self.ip, self.port)
        if connect_hid < 0:
            logging.info('connect server error, hid: %s' % connect_hid)
        else:
            self.hid = connect_hid
            logging.info('connect server success, hid: %s' % connect_hid)

    def send_data(self, data):
        res = self.con_mgr.send(self.hid, data)

    def run(self):
        while True:
            time.sleep(0.01)
            self.con_mgr.wait(0)
            while True:
                event, wparam, lparam, data = self.con_mgr.read()
                if event is None:
                    break
                else:
                    print event, wparam, lparam, data



if __name__ == '__main__':
    client = Client('127.0.0.1', 10005)
    client.setDaemon(True)
    client.start()
    client.connect()
    while True:
        time.sleep(0.1)
        command = raw_input('please input data: ')
        if command != 'end':
            print '%s sended' % command
            client.send_data(command)
        elif command == 'end':
            sys.exit(0)
