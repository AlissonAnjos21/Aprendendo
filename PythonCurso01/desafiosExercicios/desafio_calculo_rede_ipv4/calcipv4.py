class CalcIpv4:
    def __init__(self, ip, mascara=None, cidr=None):
        self.ip = ip
        self.mascara = mascara
        self.cidr = cidr
        # print(self.ip)
        # print(self.convert_to_binary(self.ip))

    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, ip):
        ip = ip.split('.')
        for i, j in enumerate(ip):
            ip[i] = int(j)
        self._ip = ip

    def convert_to_binary(self, ip):
        values = [128, 64, 32, 16, 8, 4, 2, 1]
        bin_values = []
        for i in ip:
            bin_individual_value = []
            for j in values:
                if i >= j:
                    bin_individual_value.append(1)
                    i = i - j
                else:
                    bin_individual_value.append(0)
            bin_values.append(bin_individual_value)
        return bin_values
