#!/bin/bash

IPTABLES="/sbin/iptables"

$IPTABLES -t nat -A POSTROUTING -o eth0 -j MASQUERADE
$IPTABLES -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
$IPTABLES -A FORWARD -i wlan0 -o eth0 -j ACCEPT
