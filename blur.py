from PIL import Image, ImageFilter
# blur an image
before = Image.open("pic.JPG")
after = before.filter(ImageFilter.BLUR)
after.save("out.jpg")
