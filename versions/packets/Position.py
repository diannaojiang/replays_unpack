#!/usr/bin/python
# coding=utf-8
import struct

from base.packets.types.Vector3 import Vector3
from base.decorators import bigworld_packet
from base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=10)
class Position(PacketDataBase):
    def __init__(self, stream):
        self.entityId, = struct.unpack('i', stream.read(4))
        self.spaceID, = struct.unpack('i', stream.read(4))
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        self.positionError = Vector3(stream)
        self.rotation = Vector3(stream)
        self.is_error, = struct.unpack('b', stream.read(1))
