import qrcode

# Function to generate and save QR code
def generate_qr(link, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size of the QR code
    )
    
    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Example usage
link = "https://example.com"
file_name = "qrcode_example.png"
generate_qr(link, file_name)
