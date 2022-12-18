import argparse
import nmap

# Creating a parser object to parse command line arguments
parser = argparse.ArgumentParser(description='Network scanner using nmap')

# Add arguments for the IP range, scan type, and port range
parser.add_argument('ip_range', help='The IP range to scan')
parser.add_argument('scan_type', help='The type of scan to perform')
parser.add_argument('port_range', help='The range of ports to scan')

# Parse the command line arguments
args = parser.parse_args()

# Create an instance of the nmap.PortScanner class
nm = nmap.PortScanner()

# Set the scan options
arguments = f"-{args.scan_type} -p {args.port_range}"
nm.scan(hosts=args.ip_range, arguments=arguments)

# Get a list of all hosts that were found
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

# Print the list of hosts
for host, status in hosts_list:
    print(f"{host} : {status}")