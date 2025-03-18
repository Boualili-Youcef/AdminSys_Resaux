import psutil
import ipaddress
import subprocess
import re

def get_network_info():
    """Récupère l'adresse IP et le masque de l'interface eth0"""
    try:
        result = subprocess.run(["sudo", "ifconfig", "eth0"], capture_output=True, text=True, check=True)
        ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', result.stdout)
        mask_match = re.search(r'netmask (\d+\.\d+\.\d+\.\d+)', result.stdout)

        if ip_match and mask_match:
            ip_addr = ip_match.group(1)
            netmask = mask_match.group(1) 
            netmask_cidr = sum(bin(int(octet)).count('1') for octet in netmask.split('.'))

            network = ipaddress.IPv4Network(f"{ip_addr}/{netmask_cidr}", strict=False)
            return network
        else:
            raise RuntimeError("Impossible de récupérer l'adresse IP et le masque.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError("Erreur lors de l'exécution de ifconfig. Essaye avec `sudo`.") from e

def get_external_tcp_connections(local_network):
    """Liste les connexions TCP vers des adresses hors du sous-réseau"""
    connections = psutil.net_connections(kind="tcp")
    external_connections = []

    print("\n Toutes les connexions TCP détectées :")
    for conn in connections:
        if conn.raddr:
            remote_ip = conn.raddr.ip
            remote_port = conn.raddr.port
            state = conn.status

            print(f" {remote_ip}:{remote_port} - {state}")  

            if not ipaddress.IPv4Address(remote_ip) in local_network:
                external_connections.append((remote_ip, remote_port, state))

    return external_connections


if __name__ == "__main__":
    try:
        local_network = get_network_info()
        external_conns = get_external_tcp_connections(local_network)

        print("Connexions TCP vers l'extérieur :")
        for ip, port, state in external_conns:
            print(f"Adresse distante: {ip}, Port: {port}, État: {state}")

    except Exception as e:
        print("Erreur:", e)
