with open('photo.jpg', 'ab') as f:
    f.write(b"hello world")

with open('photo.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset+2)
    print(f.read())

import PIL.Image
import io

img = PIL.Image.open('photo2.jpg')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

with open('photo2.jpg', 'ab') as f:
    f.write(byte_arr.getvalue())

with open('photo2.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)
    new_img = PIL.Image.open(io.BytesIO(f.read()))
    new_img.save("new_image.png")
