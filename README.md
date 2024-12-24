# Secure Data Exchange System Using RSA Encryption
### Project for CN_2024 (Priymak Eugeniy KA-13)

## Project Description
This project implements a client-server system for secure message exchange. The core feature is the use of RSA asymmetric encryption to ensure data confidentiality and security during communication between the client and server.

## Objectives
The goal of this project is to develop a program that facilitates secure client-server communication using RSA encryption. Key objectives include:
- Establishing a reliable client-server connection.
- Encrypting messages to protect them from interception or unauthorized access.
- Ensuring smooth and efficient communication with a user-friendly graphical interface.

## Key Components

### Client-Server Interaction (Chat)
The client-server model is a structured approach where the client (user application) interacts with a centralized server to exchange data. In this chat context:
1. The **server binds** to an IP address and a port (scanned for availability).
2. The **client connects** to the server via the specified IP and port.
3. **Message exchange** occurs, where the server processes and relays messages.
4. The session ends when the client disconnects.

### Development Tools

#### 1. Python Programming Language
Python's flexibility and extensive library support make it ideal for this project. Key libraries include:
- **tkinter**: For building the graphical user interface (GUI).
- **pickle**: For serializing and deserializing data.
- **threading**: To handle multi-threaded communication.
- **zmq**: To implement client-server interaction.

#### 2. ZeroMQ (zmq) Library
ZeroMQ is a high-performance library for message passing. It simplifies network communication with features like:
- Support for multiple interaction models, such as `PAIR`, `REQ-REP`, and `PUB-SUB`.
- Asynchronous messaging, enabling non-blocking operations.
- Easy integration with Python.

In this project, `zmq` is used to establish a bidirectional connection between the client and server using `PAIR` sockets.

#### 3. RSA Encryption Algorithm
RSA ensures data confidentiality and authenticity. Its key principles include:
- **Key generation**: A pair of keys (public and private) is created.
- **Encryption**: Messages are encrypted with the recipient's public key.
- **Decryption**: The private key decrypts the received message.

The RSA functionality is implemented in the `encryptor.py` module, which handles key generation, encryption, and decryption.

## Installation Instructions

Before running the project, ensure you have Python (version 3.11 or higher) and the necessary libraries installed. Use the following commands:

1. Install **ZeroMQ** for client-server communication:
   ```bash
   pip install pyzmq
   
2. Install Pillow for image handling in the GUI:
   ```bash
    pip install pillow

3. Install Tkinter (usually included with Python):
- On Debian/Ubuntu:
    ```bash
   sudo apt-get install python3-tk

- On macOS: Tkinter is bundled with Python installations.
- On Windows: Use the official Python installer from ***python.org***.

### Running the Program
- **Scan Ports**: Launch `open_port_scanner.py` to find an available port (default is 127.0.0.1 for demonstration). Specify a custom IP and port range if needed.

Example output: 


Found open port: 5555
- **Start the Server**: Run `server.py` and provide the server name. Input the IP and the open port found earlier to bind the server.

- **Start the Client**: Run `client.py` (with the server running) and connect using the same IP and port.

- **Communicate**: 
After connecting, both client and server will have chat windows. Enter messages and press Send to communicate securely.

- **End the Session**: Close the chat windows for both the client and server to terminate the connection.