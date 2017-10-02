# How I turned my raspi into a wireless access point

For starters I installed the packages hostapd and isc-dhcp-server
In the setup.py I have some basic copy commands that copy the basic configuration.

Further on there are some more things to be done:

1) sudo nano /etc/rc.local and add the line "bash /etc/iptables.sh"
2) sudo nano /etc/sysctl.conf and uncomment the net.ipv4.ip_forward=1 line
3) Go to /etc/network/interfaces and add the following:
iface wlan0 inet static  
    address 172.24.1.1
    netmask 255.255.255.0
    network 172.24.1.0
    broadcast 172.24.1.255
4) Provide a wpa_pass in the hostapd.conf file
5) restart services
	ifdown wlan0; ifup wlan0
	service isc-dhcp-server restart
	service hostapd restart
	service networking restart
6) And make them 'permanent' with sudo update-rc.d hostapd enable 
and sudo update-rc.d isc-dhcp-server enable
