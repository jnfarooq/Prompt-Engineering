'''
Code generated with ChatGPT. 
Enter a website address, and the code generates a QR code. 
'''

import tkinter as tk
# from tkinter import filedialog # ChatGPT imported this but is not being used. 
from qrcode import QRCode, constants

from PIL import ImageTk

def generate_qr():
    website = entry.get()
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(website)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as a PNG file
    img.save("qr_code.png")

    # Convert PIL image to PhotoImage
    img = ImageTk.PhotoImage(img)

    # Show the QR code in the UI
    qr_label.config(image=img)
    qr_label.image = img


root = tk.Tk()
root.title("QR Code Generator")

label = tk.Label(root, text="Enter website link:")
label.pack()

entry = tk.Entry(root)
entry.pack()

qr_label = tk.Label(root)
qr_label.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

root.mainloop()