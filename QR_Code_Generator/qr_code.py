import qrcode

qr_generator = "https://classroom.google.com/c/NjQ4NjA0Mzg2NDU1"  
filename = "qr_code.png"  

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(qr_generator)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save(filename)
print(f"QR code saved as {filename}")