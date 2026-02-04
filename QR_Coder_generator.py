import qrcode

print("QR Code Generator")

data = input("Enter text or URL to generate QR code: ").strip()

if data =='':
    print("Error: No text entered. QR code not generated.")
    
else:
    qr = qrcode.make(data)
    file_name = "qrcode.png"
    qr.save(file_name)
    print(f"QR Code generated and saved as {file_name}")
    