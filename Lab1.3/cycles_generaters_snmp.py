"""Useful info for HELP"""

from pysnmp.hlapi import *

snmp_1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.107', 161)),
                ContextData(),
                ObjectType(snmp_1))

result2 = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.107', 161)),
                ContextData(),
                ObjectType(snmp_2),
                 lexicographicMode=False)


print('Type of SNMP1 object: ' + str(type(result)))         #get generator
print('Type of SNMP2 object: ' + str(type(result2)))

print('\nInfo from generator SNMP1: ')
for item in result:
    for info in item[3]:                                    #get useful data from 3nd filed
        print(info)

print('\nInfo from generator SNMP2: ')
for item in result2:
    for info in item[3]:
        print(info)
