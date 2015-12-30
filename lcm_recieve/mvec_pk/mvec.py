"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class mvec(object):
    __slots__ = ["title", "len", "vec"]

    def __init__(self):
        self.title = ""
        self.len = 0
        self.vec = []

    def encode(self):
        buf = BytesIO()
        buf.write(mvec._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        __title_encoded = self.title.encode('utf-8')
        buf.write(struct.pack('>I', len(__title_encoded)+1))
        buf.write(__title_encoded)
        buf.write(b"\0")
        buf.write(struct.pack(">q", self.len))
        buf.write(struct.pack('>%dd' % self.len, *self.vec[:self.len]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != mvec._get_packed_fingerprint():
            raise ValueError("Decode error")
        return mvec._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = mvec()
        __title_len = struct.unpack('>I', buf.read(4))[0]
        self.title = buf.read(__title_len)[:-1].decode('utf-8', 'replace')
        self.len = struct.unpack(">q", buf.read(8))[0]
        self.vec = struct.unpack('>%dd' % self.len, buf.read(self.len * 8))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if mvec in parents: return 0
        tmphash = (0x985810bdf8586e3) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if mvec._packed_fingerprint is None:
            mvec._packed_fingerprint = struct.pack(">Q", mvec._get_hash_recursive([]))
        return mvec._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
