from scapy.all import *

# def clipboard():
    # packet = build_packet('192.99.99.99', '192.168.1.254')
    # send_packet(packet)

def build_packet(src, dest):
    packet = IP(ttl=64)/TCP()
    packet.src = src
    packet.dest = dest
    packet.dport = 443
    # packet.flags = "FPU"
    print('> Packet:')
    print(packet)
    # return packet

    # response = sr1(IP(dst=dest)/TCP(dport=443, flags="FPU"))
    response = sr1(packet)
    response.show()

def send_packet(packet):
    print('> Sending the packet...')
    send(packet)
    # print(send_result)

def discover_hosts():
    ans, unans = sr(IP(dst="192.168.1.1/24",proto=(0,255))/"SCAPY",retry=2)
    ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

def udp_traceroute():
    res, unans = sr(IP(dst="target", ttl=(1,20))/UDP()/DNS(qd=DNSQR(qname="test.com")))
    res.make_table(lambda s,r: (s.dst, s.ttl, r.src))

def menu():
    option = -1
    print("Anac0nda's Network tool")

    while option != 0:
        print("Select an option")
        print("1- Discover hosts")
        print("2- UDP traceroute")
        print("3- Send packet")
        print("0- Sair")

        option = input("> ")
        match option:
            case "1":
                discover_hosts()
                break
            case "2":
                udp_traceroute()
                break
            case "3":
                # packet = build_packet('192.99.99.99', '192.168.1.254')
                # send_packet(packet)
                build_packet('192.99.99.99', '192.168.1.254')
                break
            case "0":
                print("Saindo...")
                break
            case _:
                option = -1
                print("Opcao invalida")

def main():
    menu()

main()