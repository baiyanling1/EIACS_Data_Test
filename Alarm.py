from pysnmp.hlapi import *

# 设置 SNMP 目标地址和端口
target = '10.18.40.20'
port = 30000

# 设置 SNMP 社区名和 OID
community = 'public'
oid = '1.3.6.1.4.1.12345.1'

# 创建 SNMP 消息
errorIndication, errorStatus, errorIndex, varBinds = next(
    sendNotification(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((target, port)),
        ContextData(),
        'trap',
        NotificationType(
            ObjectIdentity(oid).addAsn1MibSource('file:///usr/share/snmp/mibs'),
            (OctetString('test'),)
        ).loadMibs()
    )
)

# 检查是否有错误
if errorIndication:
    print('SNMP error: %s' % errorIndication)
else:
    print('SNMP trap sent successfully')
