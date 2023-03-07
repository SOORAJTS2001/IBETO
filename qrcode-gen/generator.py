import qrcode
from PIL import Image, ImageDraw, ImageFont

# Generate the QR code
floor1checkpoint = {"kitchen-1st-floor":(138, 23), "bedroom1-1st-floor":(48, 24), "empty-1st-floor":(59, 41), "bath-1st-floor":(31, 44), "stairentry-1st-floor":(106, 45), "bath2-1st-floor":(58, 50), "room-1st-floor":(188, 50),"stairexit-1st-floor":(106, 53),"familyroom-1st-floor":(63, 67), "formaldinnning-1st-floor":(100, 68),"office-1st-floor":(139, 71), "exit-1st-floor":(79, 76)}
floor_lists = list(floor1checkpoint.keys())
for floors in floor_lists:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f'http://127.0.0.1:8000/?from_position={floors}')
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # Add text to the image
    draw = ImageDraw.Draw(img)
    text = "test-"+floors
    font = ImageFont.truetype('arial.ttf', 30)
    textwidth, textheight = draw.textsize(text, font)
    x = (img.size[0] - textwidth) / 2
    y = img.size[1] - textheight - 10
    draw.text((x, y), text, font=font)

    # Save the image
    img.save(f'{floors}.png')
