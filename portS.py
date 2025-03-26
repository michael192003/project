import socket
import re
from common_ports import ports_and_services 

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    
    # Validate if target is IP or domain
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", target):
            return "Error: Invalid IP address"
        return "Error: Invalid hostname"

    # Scan ports
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)

    if not verbose:
        return open_ports

    # Generate verbose output
    hostname = target if target != ip else None
    result = f"Open ports for {hostname} ({ip})\nPORT     SERVICE"
    for port in open_ports:
        service = ports_and_services.get(port, "unknown")
        result += f"\n{port:<8} {service}"

    return result

scanner= input("put the ip or site here: ")
print(get_open_ports(scanner, [20, 80], True))
