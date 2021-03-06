#!/usr/bin/python
# coding=utf-8
import struct

from base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


class Vector3(PacketDataBase):
    def __init__(self, stream):
        self.x, = struct.unpack('f', stream.read(4))
        self.y, = struct.unpack('f', stream.read(4))
        self.z, = struct.unpack('f', stream.read(4))
