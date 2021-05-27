def Validate_IPAddress(ip_address):
    ip_address = ip_address.strip()
    ip_address_flag = True

#Check Path of IP Address
    if(not(ip_address.count('.') == 3)):
        ip_address_flag = False
    else:
        ip_address = ip_address.split(".")
        for val in ip_address:
            val = int(val)
            if( not(0 <= val <= 255)):
                ip_address_flag = False
    if(ip_address_flag):
        return  200
    else:
        return  400

ip_address = input("Enter IP Address")
status = Validate_IPAddress(ip_address)
if status == 200:
    print("IP Address is correct")
else:
    print("IP Address is not correct")