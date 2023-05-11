import qrcode
img = qrcode.make("https://github.com/ChristianAlameda/Resume")
img.save("ResumeQRCode.jpg")