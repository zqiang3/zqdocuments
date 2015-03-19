#!/usr/bin/env python
# -*- coding:utf-8 -*-

import CommonPath
import time
import sys
import json
from QuickNet import AsyncCore
from logger import logging
import threading


class Client(threading.Thread):
    def __init__(self, ip, port):
        super(Client, self).__init__()
        self.ip = ip
        self.port = port
        self.hid = None
        self.status = True
        self.con_mgr = AsyncCore()

    def connect(self):
        connect_hid = self.con_mgr.new_connect(self.ip, self.port)
        logging.info('connect_hid: %s' % connect_hid)
        if connect_hid < 0:
            logging.info('connect server error, hid: %s' % connect_hid)
        else:
            self.hid = connect_hid
            logging.info('connect server success, hid: %s' % connect_hid)

    def close(self):
        self.con_mgr.close(self.hid)
        self.hid = None

    def exit(self):
        self.close()
        time.sleep(0.5)
        self.status = False

    def send_data(self, data):
        if not self.hid:
            return
        res = self.con_mgr.send(self.hid, data)
        print res

    def test(self):
        data = {
            'sid': 40967,
            'cid': 33
        }
        self.send_data(json.dumps(data))

    def run(self):
        while True:
            if self.status is False:
                break
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
    client.start()
    client.connect()
    while True:
        time.sleep(0.1)
        command = raw_input('please input data: ')
        if command == 'test':
            print 'test'
            client.test()
        elif command == 'close':
            client.close()
        elif command == 'reconnect':
            client.connect()
        elif command == 'exit':
            client.exit()
            sys.exit(0)
