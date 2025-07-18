# Run these in a Linux terminal with sudo privileges

# 1. Flush existing rules
sudo iptables -F
sudo iptables -X

# 2. Default policy: deny all
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# 3. Allow loopback
sudo iptables -A INPUT -i lo -j ACCEPT

# 4. Allow SSH
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

# 5. Allow HTTP/HTTPS
sudo iptables -A INPUT -p tcp -m multiport --dports 80,443 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m multiport --sports 80,443 -m state --state ESTABLISHED -j ACCEPT

# 6. Allow established connections
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 7. Save rules (Debian/Ubuntu)
sudo iptables-save | sudo tee /etc/iptables/rules.v4 > /dev/null
