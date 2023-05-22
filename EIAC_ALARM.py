from pysnmp.hlapi import *

# 设置 SNMP 目标地址和端口
target = '10.18.40.20'
port = 30000

# 设置 SNMP 社区名和 OID
community = 'public'
trap_oid = '1.3.6.1.4.1.31648.3.16.7'

# 设置告警信息
alarm_id = 'ALM-DEVICE-1003'
alarm_name = 'XXXXX'
severity = 3
alarm_type = 5
clear_type = 1
clear_trap_oid = '1.3.6.1.4.1.31648.3.16.8'
trap_event_params = [
    '1.3.6.1.4.1.31648.3.15.11.1.1',
    '1.3.6.1.4.1.31648.3.15.11.1.2',
    '1.3.6.1.4.1.31648.3.15.11.1.3',
    '1.3.6.1.4.1.31648.3.15.1',
    '1.3.6.1.4.1.31648.3.15.2',
    '1.3.6.1.4.1.31648.3.15.3',
    '1.3.6.1.4.1.31648.3.15.4',
    '1.3.6.1.4.1.31648.3.15.5',
    '1.3.6.1.4.1.31648.3.15.6',
    '1.3.6.1.4.1.31648.3.15.7',
    '1.3.6.1.4.1.31648.3.15.8',
    '1.3.6.1.4.1.31648.3.15.9',
    '1.3.6.1.4.1.31648.3.15.10',
    '1.3.6.1.4.1.31648.3.15.11',
    '1.3.6.1.4.1.31648.3.15.12',
    '1.3.6.1.4.1.31648.3.15.13',
    '1.3.6.1.4.1.31648.3.15.14',
    '1.3.6.1.4.1.31648.3.1',
    '1.3.6.1.4.1.31648.3.2',
    '1.3.6.1.4.1.31648.3.3',
    '1.3.6.1.4.1.31648.3.4',
    '1.3.6.1.4.1.31648.3.5',
    '1.3.6.1.4.1.31648.3.6',
    '1.3.6.1.4.1.31648.3.7',
    '1.3.6.1.4.1.31648.3.8',
    '1.3.6.1.4.1.31648.3.9',
    '1.3.6.1.4.1.31648.3.10',
    '1.3.6.1.4.1.31648.3.11',
    '1.3.6.1.4.1.31648.3.12',
    '1.3.6.1.4.1.31648.3.13',
    '1.3.6.1.4.1.31648.3.14'
]

# 创建 SNMP 消息
errorIndication, errorStatus, errorIndex, varBinds = next(
    sendNotification(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((target, port)),
        ContextData(),
        'trap',
        NotificationType(
            ObjectIdentity(trap_oid).addAsn1MibSource('file:///usr/share/snmp/mibs'),
            (OctetString(alarm_id),
             OctetString(alarm_name),
             Integer(severity),
             Integer(alarm_type),
             Integer(clear_type),
             ObjectIdentity(trap_oid),
             ObjectIdentity(clear_trap_oid),
             Null(),
             [OctetString(x) for x in trap_event_params])
        ).loadMibs()
    )
)

# 检查是否有错误
if errorIndication:
    print('SNMP error: %s' % errorIndication)
else:
    print('SNMP trap sent successfully')