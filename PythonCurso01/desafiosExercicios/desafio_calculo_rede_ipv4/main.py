from calcipv4 import CalcIpv4

calcipv4 = CalcIpv4('192.168.0.25', '255.255.255.192', 26)

print(f'IP: {calcipv4.format_decimal(calcipv4.ip, calcipv4.prefix)}')
print(f'Mask: {calcipv4.format_decimal(calcipv4.mask_value, calcipv4.prefix)}')
print(f'Web: {calcipv4.format_decimal(calcipv4.decimal_web_ip, calcipv4.prefix)}')
print(f'Broadcast: {calcipv4.format_decimal(calcipv4.decimal_broadcast_ip, calcipv4.prefix)}')
print(f'Prefix: {calcipv4.prefix}')
print(f'Number of Web IPs: {calcipv4.number_of_ips}')
