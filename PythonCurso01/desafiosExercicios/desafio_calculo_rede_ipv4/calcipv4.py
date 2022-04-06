class CalcIpv4:
    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix
        
        self.binary_ip = self.convert_ip_to_binary()
        self.binary_mask = self.generate_binary_mask_from_prefix()
        # print(self.ip)
        # print(self.binary_ip)
        # print(self.binary_mask)

    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, ip):
        ip = ip.split('.')
        for i, j in enumerate(ip):
            ip[i] = int(j)
        self._ip = ip

    def convert_ip_to_binary(self):
        values = [128, 64, 32, 16, 8, 4, 2, 1]
        bin_values = []
        for i in self.ip:
            bin_individual_value = []
            for j in values:
                if i >= j:
                    bin_individual_value.append(1)
                    i = i - j
                else:
                    bin_individual_value.append(0)
            bin_values.append(bin_individual_value)
        return bin_values

    def generate_binary_mask_from_prefix(self):
        bin_mask = []
        aux = 0
        for i in self.binary_ip:
            bin_values = []
            for j_ in i:
                if aux < self.prefix:
                    bin_values.append(1)
                    aux+=1
                else:
                    bin_values.append(0)
            bin_mask.append(bin_values)
        return bin_mask
                


