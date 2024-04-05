import os
import customtkinter
from customtkinter import *
from tkinter import *
from tkinter import filedialog, simpledialog
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import re
from PIL import Image

root = CTk()
root.geometry("1000x500")
root.title("Image Cryptor")
root.iconbitmap("shield.ico")

ascii_art = """

██╗███╗░░░███╗░█████╗░░██████╗░███████╗  ░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░██████╗░
██║████╗░████║██╔══██╗██╔════╝░██╔════╝  ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║██╔████╔██║███████║██║░░██╗░█████╗░░  ██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║██████╔╝
██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░  ██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║██╔══██╗
██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗  ╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝██║░░██║
╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝  ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
"""

title_label = CTkLabel(root, text=ascii_art, font=("Fire Font-k",14,"bold"), text_color="#EC1422" )
title_label.place(relx=0.5, rely=0.1, anchor="center")

def is_strong_password(password):
    if len(password) not in [16,24,32]:
        return False
    
    if not re.search(r"[A-Z]",password):
        return False
    if not re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?`~]", password):
        return False
    return True

def encrypt_image():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        key = simpledialog.askstring("AES Key", "Enter AES Key:",show="*")

        if not key:
            print("AES key not provided")

        if not is_strong_password(key):
            print("Encryption Key must be 16, 24, or 32 bytes in length.\n"
                  "\nand should contain at least one capital letter, one digit and one special character from the set !@#$%^&*()_+-=[];':\"\\|,.<>/?`~"
                  )
            return

        try:
            with open(file_path, "rb") as f:
                image_data = f.read()

            padded_image_data = pad(image_data, AES.block_size)

            cipher = AES.new(key.encode(), AES.MODE_ECB)
            encrypted_image_data = cipher.encrypt(padded_image_data)

            with open(file_path, "wb") as f:
                f.write(encrypted_image_data)

            print("Image encrypted successfully!")
        except TypeError as e:
            print("Encryption Key must be 16, 24, or 32 bytes in length ."
                  "And should contain at least one capital letter, "
                  "one digit and "
                  "one special character from the set !@#$%^&*()_+-=[];':\"\\|,.<>/?`~"
                )
        except Exception as e:
            print(f"Error: {e}")

def decrypt_image():
    file_path = filedialog.askopenfilename(filetypes = [("PNG files","*.png")])
    if file_path:
        key = simpledialog.askstring("AES Key","Enter AES Key:",show="*")

        if not key:
            print("AES key not provided.")
        
        if not is_strong_password(key):
            print("Encryption Key must be 16, 24, or 32 bytes in length."
                  "and should contain at least one capital letter, one digit and one special character from the set !@#$%^&*()_+-=[];':\"\\|,.<>/?`~"
                )
            return
        try:
            with open(file_path, "rb") as f:
                encrypted_image_data = f.read()

            cipher = AES.new(key.encode(), AES.MODE_ECB)
            decrypted_image_data = cipher.decrypt(encrypted_image_data)

            unpadded_decrypted_image_data = unpad(decrypted_image_data, AES.block_size)

            with open(file_path, "wb") as f:
                f.write(unpadded_decrypted_image_data)

            print("Image decrypted successfully!")
        except TypeError as e:
            print("Encryption Key must be 16, 24, or 32 bytes in length .\n"
                  "And should contain at least one capital letter,\n "
                  "one digit and \n"
                  "one special character from the set !@#$%^&*()_+-=[];':\"\\|,.<>/?`~\n"
                )
        except Exception as e:
            print(f"Error: {e}")


img1 = Image.open("lock.png")
img2 = Image.open('unlock.png')
b1 = CTkButton(master=root, text="Encrypt Image", text_color="#000000", command=encrypt_image,corner_radius =32, fg_color = "#EC1422",
               hover_color= "#F0FFFF", border_color = "#000000", border_width =2, image = CTkImage(dark_image = img1 , light_image = img1))
b1.place(relx=0.5, rely=0.5, anchor="center")

b2 = CTkButton(root, text="Decrypt Image",text_color="#000000", command=decrypt_image,corner_radius =32, fg_color = "#EC1422",
               hover_color= "#F0FFFF", border_color = "#000000", border_width =2, image = CTkImage(dark_image = img2 , light_image = img2))
b2.place(relx=0.5, rely=0.7, anchor="center")

def project_info():
    p_info = Toplevel(root)
    p_info.title("Project Info")
    p_info.geometry("1000x500")
    p_info.config(bg="black")

    p_info_text = """
    Project : Image Encryptor/Decryptor
    -------------------------------------------------------
    Developer: Brian Biju 
    -------------------------------------------------------
    Descripton: As part of the Supraja Technologies internship program, this project aims to develop an Image Encryptor/Decryptor program. 
    The program utilizes AES (Advanced Encryption Standard) encryption to encrypt and decrypt images securely. 
    The encryption process ensures that the images remain confidential and protected from unauthorized access.
    -------------------------------------------------------
    Features:
    1. Image Encryption: Securely encrypt images to protect sensitive information.
    2. Image Decryption: Decrypt encrypted images to restore them to their original state.
    3. AES Encryption: Utilizes AES encryption algorithm for robust security.
    4. User-friendly Interface: Intuitive graphical interface for easy usage.
    5. File Selection: Allows users to select PNG images for encryption and decryption.
    -------------------------------------------------------
    Usage:
    1. To encrypt an image, click on the "Encrypt Image" button and select the PNG file you want to encrypt. Enter the AES key when prompted.
    2. To decrypt an image, click on the "Decrypt Image" button and select the encrypted PNG file. Enter the AES key used for encryption.
    3. Ensure to use a strong AES key with a length of 16, 24, or 32 bytes for optimal security.
    4. The program provides feedback on successful encryption or decryption operations and alerts users in case of errors.

    """
    p_info_label = CTkLabel(p_info, text = p_info_text, font = ("Courier New", 12), justify="left")
    p_info_label.pack(padx = 20, pady = 20)

b3 = CTkButton(master=root, text="Project Info", text_color="#000000", command=project_info,corner_radius =32, fg_color = "#EC1422",
               hover_color= "#F0FFFF", border_color = "#000000", border_width =2)
b3.place(relx = 0.5, rely=0.3, anchor="center")


image_path1 = os.path.join(os.path.dirname(__file__), 'encryption3.png')
image_path2 = os.path.join(os.path.dirname(__file__), 'secured1.png')

left_image = customtkinter.CTkImage(light_image= Image.open(image_path1), size = (150,150))
left_image_label = customtkinter.CTkLabel(root , image = left_image, text = '')
left_image_label.place(relx=0.2, rely=0.5, anchor="center")

right_image = customtkinter.CTkImage(light_image= Image.open(image_path2), size = (150,150))
right_image_label = customtkinter.CTkLabel(root , image = right_image, text = '')
right_image_label.place(relx=0.8, rely=0.5, anchor="center")


binary_data = "0101010101010101"

digit_width = 12

for i, digit in enumerate(binary_data):
    color = "#EC1422" if i % 2 == 0 else "#F0FFFF"
    label = CTkLabel(root, text=digit, font=("Courier Prime", 20), text_color=color)
    label.place(relx=0.1 + i * (digit_width / root.winfo_width()), rely=0.9, anchor="w")



root.mainloop()
