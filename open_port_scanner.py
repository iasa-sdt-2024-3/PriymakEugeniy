import socket
import sys
import logging

PORT_PROTOCOLS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    119: "NNTP",
    123: "NTP",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    179: "BGP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "Microsoft-DS",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD/LPR",
    587: "SMTP (Submission)",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5555: "Oracle WebCenter Content: Inbound Refinery—Intradoc Socket port",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Proxy",
    8443: "HTTPS (Alt Port)",
    9090: "WebSphere",
    27017: "MongoDB",
}

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class InvalidIPAddressError(Exception):
    #Exception raised when an invalid IPv4 address is entered.
    pass


class InvalidPortRangeError(Exception):
    #Exception raised when an invalid port range is entered.
    pass

# Check if a given string is a valid IPv4 address
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


#Scan a given port on a given IP address to check if it's open.
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False


def get_user_input():
    target = input("Enter the IPv4 address to scan (or 'exit' to quit): ")
    if target.lower() == 'exit':
        sys.exit()

    if not is_valid_ip(target):
        raise InvalidIPAddressError("Invalid IP address format. Please enter a valid IPv4 address.")

    start_port = int(input("Enter the starting port (Min: 1): "))
    end_port = int(input("Enter the ending port (Max: 65535): "))

    if start_port < 1 or end_port < start_port or end_port > 65535:
        raise InvalidPortRangeError("Invalid port range. Please enter port numbers between 1 and 65535.")

    return target, start_port, end_port  #returns a tuple containing target IP, start port, and end port


def display_open_ports(open_ports):
    if open_ports:
        print("\nOpen ports:")
        for port in open_ports:
            protocol = PORT_PROTOCOLS.get(port, "Unknown")
            print(f"Port {port} is open (Protocol: {protocol})")
        print()
    else:
        print("No open ports found in the specified range.")


def main():
    title = "PORT SCANNER"
    print(title)

    while True:
        try:
            target, start_port, end_port = get_user_input()
        except ValueError:
            logger.error("Invalid input. Please enter valid values.")
            continue
        except (InvalidIPAddressError, InvalidPortRangeError) as e:
            logger.error(str(e))
            continue

        open_ports = []

        print(f"Scanning ports from {start_port} to {end_port} on {target}...")

        for port in range(start_port, end_port + 1):
            if scan_port(target, port):
                open_ports.append(port)

        display_open_ports(open_ports)


if __name__ == "__main__":
    main()
