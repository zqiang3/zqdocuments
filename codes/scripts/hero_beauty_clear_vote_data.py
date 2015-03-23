# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import redis
import sys
import traceback
from datetime import datetime


def get_mongo_conn():
    config = get_app_config()
    host = config.get('mongo_host')
    port = config.get('mongo_port')
    db = config.get('db')
    user = config.get('user')
    password = config.get('password')

    try:
        client = pymongo.MongoClient(host, port)
        db = client[db]
        db.authenticate(user, password)
        return db
    except:
        print traceback.format_exc()


def get_redis_conn():
    config = get_app_config()
    host, port = config.get('redis_host'), config.get('redis_port')
    if not host or not port:
        return None

    redis_cli = redis.StrictRedis(host, port)
    return redis_cli




def get_app_config():
    args = sys.argv
    if len(args) < 2:
        print 'must have 2 arguments'
        sys.exit(-1)

    cmd = args[1]
    if cmd == 'online':
        config = {}
        config['mongo_host'] = '127.0.0.1'
        config['mongo_port'] = 30000
        config['db'] = 'cc_pt_app'
        config['user'] = 'pt_app_online'
        config['password'] = 'pt_app_online'
        config['redis_host'] = '10.120.200.87'
        config['redis_port'] = 6379
        return config
    elif cmd == '88':
        config = {}
        config['mongo_host'] = '192.168.229.88'
        config['mongo_port'] = 27017
        config['db'] = 'gamble'
        config['user'] = 'gamble'
        config['password'] = 'gamblepwd'
        config['redis_host'] = '192.168.11.42'
        config['redis_port'] = 6379
        return config
    elif cmd == '42':
        config = {}
        config['mongo_host'] = '192.168.11.42'
        config['mongo_port'] = 27017
        config['db'] = 'gamble'
        config['user'] = 'gamble'
        config['password'] = 'gamblepwd'
        config['redis_host'] = '192.168.11.42'
        config['redis_port'] = 6379
        return config
    else:
        print 'args invalid'
        sys.exit(-2)


def main():
    mongo_db = get_mongo_conn()
    redis_cli = get_redis_conn()
    if not mongo_db:
        print 'no mongo conn'
        return

    try:
        table_name = 'herochl_anchor_info_test'
        backup_table = table_name + '_' + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        res = mongo_db[table_name].find()
        count = res.count()
        for item in res:
            item.pop('_id')
            mongo_db[backup_table].save(item)
        statement = {'$set': {'votes': 0}}
        res = mongo_db[table_name].update({}, statement, multi=True, upsert=False)
        print 'updated: {0}'.format(count)

        keys = redis_cli.keys()
        prefix = 'hero_anchor_ticket_info_'
        for key in keys:
            if key.startswith(prefix):
                redis_cli.delete(key)
                print 'delete redis key: %s' % key
        print 'clear cache finished'
    except Exception, ex:
        print traceback.format_exc()


if __name__ == '__main__':
    main()
    print 'all finished'
