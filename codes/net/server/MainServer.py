#!/usr/bin/env python
# -*- coding:utf-8 -

import sys
import time
import CommonPath
from QuickNet import AsyncCore
from logger import logging
import threading


class MainServer(threading.Thread):
    def __init__(self, port):
        super(MainServer, self).__init__()
        self.port = port
        self.hid = None
        self.con_mgr = None
        self.init()

    def init(self):
        self.con_mgr = AsyncCore()

    def listen(self):
        listen_hid = self.con_mgr.new_listen(ip=None, port=self.port, reuse=True)
        if listen_hid < 0:
            logging.info('listen failure, port: %s' % self.port)
            self.port += 1
            return False
        else:
            self.hid = listen_hid
            logging.info('listen port success, port: %s' % self.port)
            return True

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
    server = MainServer(10005)
    server.start()
    server.listen()