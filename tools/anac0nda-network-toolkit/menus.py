def show_main_options():
    print("Select an option:\n")
    print("BUILDING")
    print("\t1- Set tool parameters")
    print("\t2- Build packet")
    print("\t3- Send packet")
    print("\t4- Reset packet")
    print("NETWORK PROBING")
    print("\t5- Discover hosts")
    print("\t6- UDP traceroute")
    print("ATTACKING")
    print("\t7- TCP SYN flood")
    print("MISCELANOUS")
    print("\t8- Reset toolkit data")
    print("\t0- Sair")

def run_main_option(option):
    match option:
        case "1":
            set_tool_parameters()
            break
        case "2":
            build_packet()
            break
        case "3":
            send_packet()
            break
        case "4":
            reset_packet()
            break
        case "5":
            discover_hosts()
            break
        case "6":
            udp_traceroute()
            break
        case "7":
            tcp_syn_flood()
            # tcp_conn_flood("127.0.0.1", "192.168.1.1")
            # tcp_conn_flood("192.168.1.254", "192.168.1.4")
            break
        case "8":
            reset_toolkit_data()
            break
        case "0":
            print("\n3000")
            break
        case _:
            option = -1
            print("Opcao invalida")

def main_menu():
    option = -1
    print("Anac0nda's Network tool")

    while option != 0:
        show_main_options()
        run_main_option(input("> "))

def show_set_tool_parameters():
    print("Select an option:\n")
    print("1- Set source host")
    print("2- Set destination host")
    print("3- Set source network")
    print("4- Set destination network")

def show_build_packet_menu():
    print("Select an option:\n")
    print("1- Add packet layer")
    print("2- Set source host")
    print("3- Set destination host")
