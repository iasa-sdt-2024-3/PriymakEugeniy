import zmq
import threading
from tkinter import *
import pickle
from PIL import Image, ImageTk
from encryptor import generate_keypair, encrypt, decrypt

name = input("Enter your name: ")

# Generate RSA keys for the server
public_key, private_key = generate_keypair(1024)

# Initialize ZeroMQ context
context = zmq.Context()

# Define server setup function
def setup_server(ip, port):
    socket = context.socket(zmq.PAIR)
    socket.bind(f"tcp://{ip}:{port}")
    return socket

# Function to send messages
def send_message():
    if edit_text.get().strip():
        message = edit_text.get().strip()
        encrypted_message = encrypt(message, client_public_key)  # Encrypt the message
        server_socket.send(pickle.dumps(encrypted_message))  # Send encrypted message
        listbox.insert(END, f"{name}: {message}")
        edit_text.delete(0, END)

# Function to receive messages
def receive_messages():
    while True:
        try:
            encrypted_message = pickle.loads(server_socket.recv())
            decrypted_message = decrypt(encrypted_message, private_key)  # Decrypt the message
            listbox.insert(END, f"{client_name}: {decrypted_message}")
        except Exception as e:
            listbox.insert(END, f"Error receiving message: {e}")

# GUI to input server details
input_root = Tk()
input_root.title("Server Setup")
input_root.geometry("400x200")

Label(input_root, text="Enter IP:").pack()
ip_entry = Entry(input_root)
ip_entry.pack()

Label(input_root, text="Enter Port:").pack()
port_entry = Entry(input_root)
port_entry.pack()

def start_server():
    global server_socket, client_name, client_public_key
    ip = ip_entry.get()
    port = port_entry.get()
    server_socket = setup_server(ip, port)
    input_root.destroy()
    # Exchange public keys and names
    client_name, client_public_key = pickle.loads(server_socket.recv())  # Receive client name and public key
    server_socket.send(pickle.dumps((name, public_key)))  # Send server name and public key

Button(input_root, text="Start Server", command=start_server).pack()
input_root.mainloop()

# Main chat GUI
root = Tk()
image = Image.open("images/server_image.jpg")
bgimage3 = ImageTk.PhotoImage(image)
root.bgimage3 = bgimage3

bg_label = Label(root, image=bgimage3)
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