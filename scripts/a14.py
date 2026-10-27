#!/usr/bin/env python

# Black formatter: shift + alt + F


"""For the given topology (Figure 1), write a Python script that takes input from the user and logs into R1 and configures an IP address on the Fa1/0 interface and creates and configures an IP address on a loopback interface.
The input from the user should be the following:
•	IP address of the router you want to configure
•	SSH login Username
•	SSH login Password
•	Interface description and IP address (that you want to configure on the router—fa1/0 in our example)
•	Loopback interface description and IP address
"""

import argparse
from netmiko import ConnectHandler


def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will automate the configuration process for a new switch"
    )
    parser.add_argument(
        "R_IP_address",
        action="store",
        help="Enter IP address of router you want to configure",
    )
    parser.add_argument("--version", action="version", version="2.1")
    args = parser.parse_args()
    return args


def main():
    args = ArgParse_slides()
    rIP = args.R_IP_address

    # credientials
    user = input(f"Username: ")
    passw = input(f"Password: ")

    try:
        net_connect = ConnectHandler(
            device_type="cisco_ios_telnet", host=rIP, username=user, password=passw
        )
        print("connection established")
    except:
        print("connection not established")
    interfaceDescription = input("Enter interface name: ")
    interfaceIPAddress = input("Enter new IP address for interface: ")
    loopbackInterface = input("Enter Loopback interface name: ")
    loopbackIPAddress = input("Enter Loopback IP address: ")
    config_lst = [
        f"interface {interfaceDescription}",
        f"ip address {interfaceIPAddress} 255.255.255.0",
        "exit",
        f"interface {loopbackInterface}",
        f"ip address {loopbackIPAddress}",
    ]
    net_connect.send_config_set(config_lst)
    net_connect.save_config()


if __name__ == "__main__":
    main()
