from flask import Flask, jsonify
import glob
import re

hosts = {}

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    s = 'Welcome in my world'
    return s


@app.route('/configs')
def host_info():
    req = []
    for host in hosts.keys():
        req.append(hosts[host]['name'])
    return jsonify(req)


@app.route('/config/<hostname>')
def ip_info(hostname):
    for host in hosts.keys():
        if hosts[host]['name'] == hostname:
            return jsonify(hosts[host]['addresses'])
    return jsonify("Not found")


if __name__ == '__main__':

    for file_name in glob.glob("C:\\Users\\aa.seleznev\\PycharmProjects\p4ne\\Lab1.5\\config_files\\*.txt"):
        hosts[file_name] = {}
        hosts[file_name]['addresses'] = []

        with open(file_name) as f:
            for read_line in f:
                isMatch = re.match("^hostname (.+)", read_line)
                if isMatch:
                    hosts[file_name]['name'] = isMatch.group(1)
                    continue
                isMatch = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)",
                                   read_line)
                if isMatch:
                    hosts[file_name]['addresses'].append({'ip': isMatch.group(1), 'mask': isMatch.group(2)})


app.run(debug=True)
