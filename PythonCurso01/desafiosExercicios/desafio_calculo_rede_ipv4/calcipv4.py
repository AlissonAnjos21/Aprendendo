class CalcIpv4:

    values = [128, 64, 32, 16, 8, 4, 2, 1]

    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix
        
        self.binary_ip = self.convert_ip_to_binary(self.ip)
        self.binary_mask = self.generate_binary_mask_from_prefix()
        self.decimal_mask = self.convert_binary_ip_to_decimal(self.binary_mask)
        self.binary_broadcast_ip = self.generate_broadcast_ip()
        self.binary_web_ip = self.generate_web_ip()
        self.decimal_broadcast_ip = self.convert_binary_ip_to_decimal(self.binary_broadcast_ip)
        self.decimal_web_ip = self.convert_binary_ip_to_decimal(self.binary_web_ip)
        self.number_of_ips = self.generate_number_of_ips()
        self.binary_mask_from_mask = self.convert_ip_to_binary(self.mask)
        self.prefix = self.generate_prefix_from_binary_mask()
        # print(self.ip)
        # print(self.mask)
        # print(self.binary_ip)
        # print(self.binary_mask)
        # print(self.decimal_mask)
        # print(self.binary_broadcast_ip)
        # print(self.binary_web_ip)
        # print(self.decimal_broadcast_ip)
        # print(self.decimal_web_ip)
        # print(self.number_of_ips)
        # print(self.binary_mask_from_mask)
        # print(self.prefix)

    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, ip):
        ip = ip.split('.')
        for i, j in enumerate(ip):
            ip[i] = int(j)
        self._ip = ip

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, mask):
        if mask:
            mask = mask.split('.')
            for i, j in enumerate(mask):
                mask[i] = int(j)
            self._mask = mask
        else:
            self._mask = None

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        if prefix:
            self._prefix = prefix
        else:
            self._prefix = None

    def convert_ip_to_binary(self, ip):
        bin_values = []
        for i in ip:
            bin_individual_value = []
            for j in self.values:
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

    def generate_prefix_from_binary_mask(self):
        prefix = 0
        for i in self.binary_mask_from_mask:
            for j in i:
                if j == 1:
                    prefix+=1
        return prefix

                
    def convert_binary_ip_to_decimal(self, binary):
        decimal_value = []
        for i in binary:
            aux = 0
            for j, k in enumerate(i):
                if k == 1:
                    aux += self.values[j]
            decimal_value.append(aux)
        return decimal_value

    def generate_broadcast_ip(self):
        aux = 0
        broadcast_ip = []
        for i in self.binary_ip:
            ip_value = []
            for j in i:
                if aux < self.prefix:
                    ip_value.append(j)
                    aux+=1
                else:
                    ip_value.append(1)
            broadcast_ip.append(ip_value)
        return broadcast_ip


    def generate_web_ip(self):
        aux = 0
        web_ip = []
        for i in self.binary_ip:
            ip_value = []
            for j in i:
                if aux < self.prefix:
                    ip_value.append(j)
                    aux+=1
                else:
                    ip_value.append(0)
            web_ip.append(ip_value)
        return web_ip

    def generate_number_of_ips(self):
        return (2 ** (32 - self.prefix)) - 2
