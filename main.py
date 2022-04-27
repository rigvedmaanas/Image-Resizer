from PIL import Image

Original_File = "Images/NormalImage.jpeg"
Destination = "Images/ResizedImage.jpeg"

im = Image.open(Original_File)
px = im.load()

pixels = list(im.getdata())
new_pixel = []
buffer = []
count = 1
for x in pixels:
    new_pixel.append(x)
    buffer.append(x)
    if count == im.width:
        for i in buffer:
            new_pixel.append(i)
        buffer = []
        count = 0
    count += 1
correct_pixels = []

for y in new_pixel:
    correct_pixels.append(y)
    correct_pixels.append(y)

img = Image.new(im.mode, (im.width*2,im.height*2), (0,0,0))
img.putdata(correct_pixels)
img.save(Destination)

