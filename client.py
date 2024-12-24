from tkinter import *
import zmq
import threading
import pickle
from PIL import Image, ImageTk
from encryptor import generate_keypair, encrypt, decrypt

name = input("Enter your name: ")

# Generate RSA keys for the client
public_key, private_key = generate_keypair(1024)

# Initialize ZeroMQ context
context = zmq.Context()

def setup_client(ip, port):
    socket = context.socket(zmq.PAIR)
    socket.connect(f"tcp://{ip}:{port}")
    return socket

def send_message():
    if edit_text.get().strip():
        message = edit_text.get().strip()
        encrypted_message = encrypt(message, server_public_key)  # Encrypt the message
        client_socket.send(pickle.dumps(encrypted_message))  # Send encrypted message
        listbox.insert(END, f"{name}: {message}")
        edit_text.delete(0, END)

def receive_messages():
    while True:
        try:
            encrypted_message = pickle.loads(client_socket.recv())
            decrypted_message = decrypt(encrypted_message, private_key)  # Decrypt the message
            listbox.insert(END, f"{server_name}: {decrypted_message}")
        except Exception as e:
            listbox.insert(END, f"Error receiving message: {e}")

input_root = Tk()
input_root.title("Client Setup")
input_root.geometry("400x200")

Label(input_root, text="Enter Server IP:").pack()
ip_entry = Entry(input_root)
ip_entry.pack()

Label(input_root, text="Enter Server Port:").pack()
port_entry = Entry(input_root)
port_entry.pack()

def connect_to_server():
    global client_socket, server_name, server_public_key
    ip = ip_entry.get()
    port = port_entry.get()
    client_socket = setup_client(ip, port)
    input_root.destroy()
    # Exchange public keys and names
    client_socket.send(pickle.dumps((name, public_key)))  # Send client name and public key
    server_name, server_public_key = pickle.loads(client_socket.recv())  # Receive server name and public key

Button(input_root, text="Connect", command=connect_to_server).pack()
input_root.mainloop()

root = Tk()
image = Image.open("images/client_image.jpg")
bgimage1 = ImageTk.PhotoImage(image)
root.bgimage1 = bgimage1

bg_label = Label(root, image=bgimage1)
bg_label.place(relwidth=1, relheight=1)

root.title(name)
root.geometry("400x700")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(fill=BOTH, expand=True)

scrollbar.config(command=listbox.yview)

Button(root, text="Send", command=send_message).pack(fill=X, side=BOTTOM)

edit_text = Entry(root)
edit_text.pack(fill=X, side=BOTTOM)

threading.Thread(target=receive_messages, daemon=True).start()
root.mainloop()