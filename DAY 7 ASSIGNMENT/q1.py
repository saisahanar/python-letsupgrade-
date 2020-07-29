# Use the dictionary,
# port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"},
# and make a new dictionary in which keys become values and values become keys,
# as shown: Port2 = {“FTP":21, "SSH":22, “telnet":23,"http": 80}

port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
port2={}
for key,values in port1.items():
    port2[values]=key
print(port2)    