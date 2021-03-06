#!/usr/bin/python
# coding=utf-8
import struct
from StringIO import StringIO

from base.decorators import bigworld_packet, g_Packets, g_SubPackets
from base.packets.PacketData import PacketDataBase
from base.packets.types.BinaryIStream import BinaryIStream

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x7)
class EntityProperty(PacketDataBase):
    def __init__(self, stream):
        self.objectID, = struct.unpack('I', stream.read(4))
        self.messageId, = struct.unpack('I', stream.read(4))
        self.data = BinaryIStream(stream)
