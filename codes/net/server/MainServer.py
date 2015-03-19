#!/usr/bin/env python
# -*- coding:utf-8 -

import sys
import time
import json
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
        self.client_event_handler = {}
        self.init()

    def init(self):
        self.con_mgr = AsyncCore()

    def add_event_handler(self, sid, cid, func):
        service = self.client_event_handler.get(sid, None)
        if service is None:
            self.client_event_handler[sid] = {}
        self.client_event_handler[sid][cid] = func

    def send_game_ready(self):
        print 'game ready'

    def listen(self):
        listen_hid = self.con_mgr.new_listen(ip=None, port=self.port, reuse=True)
        logging.info('listen_hid: %s' % listen_hid)
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
                    if event == 3:  # data
                        json_data = json.loads(data)
                        sid = int(json_data.get('sid'))
                        cid = int(json_data.get('cid'))
                        if self.client_event_handler.get(sid) and self.client_event_handler[sid].get(cid):
                            func = self.client_event_handler[sid][cid]
                            func()


if __name__ == '__main__':
    server = MainServer(10005)
    server.add_event_handler(40967, 33, server.send_game_ready)
    server.start()
    server.listen()