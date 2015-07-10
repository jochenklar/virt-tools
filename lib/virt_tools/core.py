import libvirt
import virtinst
import xml.etree.ElementTree as ET

class Domain:

    def __init__(self, name):
        self.name  = name

    def connect(self):
        self.conn = libvirt.open('qemu:///system')
        if self.conn == None:
            raise RuntimeError('Failed to connect.')

    def vnc(self):
        self.connect()
        dom = self.conn.lookupByName(self.name)
        xml = ET.fromstring(dom.XMLDesc(0))
        return xml.find('devices').find('graphics').get('port')

    def mac(self):
        self.connect()
        dom = self.conn.lookupByName(self.name)
        xml = ET.fromstring(dom.XMLDesc(0))
        return xml.find('devices').find('interface').find('mac').get('address')

    def xml(self):
        self.connect()
        dom = self.conn.lookupByName(self.name)
        return dom.XMLDesc(0)

    def dhcpd(self):
        self.connect()
        dom = self.conn.lookupByName(self.name)
        xml = ET.fromstring(dom.XMLDesc(0))
        mac = xml.find('devices').find('interface').find('mac').get('address')
        return "    host %s {\n      hardware ethernet %s;\n      fixed-address IP;\n    }" % (self.name, mac)
