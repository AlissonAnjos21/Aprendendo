class CalcIpv4:
    def __init__(self, ip, mascara=None, cidr=None):
        self.ip = ip
        self.mascara = mascara
        self.cidr = cidr
        print(self.ip)

    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, ip):
        ip = ip.split('.')
        self._ip = ip
