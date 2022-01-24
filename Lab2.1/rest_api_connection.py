import pprint
import requests

host_url = '10.31.70.210'
r = requests.post(host_url + '/api/v1/auth/token-services', auth=("restapi", "j0sg1280-7@"), verify=False)
token = r.json()[‘token-id’]

header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get(host_url + '/api/v1/interfaces', headers=header, verify=False)
pprint.pprint(r.json())

{'items': [{'description': '',
            'icmp-redirects': True,
            'icmp-unreachable': True,
            'if-name': 'VirtualPortGroup1',
            'ip-address': '10.31.70.209',
