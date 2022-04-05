class CalcIpv4:
    def __init__(self, ip, mascara=None, cidr=None):
        self.ip = ip
        self.mascara = mascara
        self.cidr = cidr

    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, ip):
        self._ip = ip

    @property
    def mascara(self):
        return self._mascara

    @mascara.setter
    def mascara(self, mascara):
        self._mascara = mascara

    @property
    def cidr(self):
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        self._cidr = cidr
    