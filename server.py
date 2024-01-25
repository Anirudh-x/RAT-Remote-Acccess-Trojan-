import socket 

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket using IPv4 address and TCP protocol

    ip_to_listen = "0.0.0.0" # IP address to listen incoming connections, By 0.0.0.0 we can accept connections from all the user in a network
    port = 8788

    my_socket_address = (ip_to_listen, port)
    server_socket.bind(my_socket_address) # Bind the server socket to the specified IP address and port number

    server_socket.listen(5)  # Start listening for incoming connections with a maximum backlog of 5 connections

    print("Listening for all incoming client connections...")

    client_socket,client_address = server_socket.accept() # Accept an incoming connection from a client and return a new socket object and the address of the client

    print(f"NEW CONNECTION : {client_address}:{port}")

    while True:
        command = input("Enter Command to Execute on Client (or 'exit' to quit)")

        client_socket.send(command.encode()) # Send the command to the client after encoding it to bytes

        if command.lower() == 'exit': # If the command is "exit", terminate the loop
            break

        respone = client_socket.recv(1024).decode() # Receive the output of the command from the client and decode it from bytes to a string
        print(f"Output from client Command Line : \n {respone}") # Print the output of the command on the server console

    client_socket.close() # Close the connection to the client
    server_socket.close() # Close the server socket