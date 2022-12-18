# Network-Scanner-Project

In this project, code will take three command line arguments:


&ensp (1) ip_range: the range of IP addresses to scan (e.g. 192.168.1.0/24)



&ensp (2) scan_type: the type of scan to perform (e.g. sP for a ping scan, sT for a TCP connect scan)



&ensp (3) port_range: the range of ports to scan (e.g. 1-1000 to scan ports 1 through 1000)






Ex.     python network_scanner.py 192.168.1.0/24 sP 1-1000




This will perform a TCP connect scan (-sT) on the IP range 192.168.1.0/24, scanning the ports in the range 1-1000.
