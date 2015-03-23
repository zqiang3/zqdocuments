drive_list = [
{'uid': 20085399, 'drive_id': 1034, 'use': True, 'expire': False, 'end_time': 200000},
{'uid': 20085399, 'drive_id': 1035, 'use': False, 'expire': False, 'end_time': 300000},
{'uid': 20085399, 'drive_id': 1036, 'use': True, 'expire': True, 'end_time': 400000},
{'uid': 20085399, 'drive_id': 1037, 'use': True, 'expire': True, 'end_time': 600000},

]


drive_list = sorted(drive_list, key=lambda x: (x['use'], x['expire'], x['end_time']), reverse=True)
print drive_list