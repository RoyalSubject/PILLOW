from PIL import Image, ImageEnhance, ImageDraw, ImageOps

monki = Image.open("monki.png")

sv_monki = monki.convert("L")

sv_monki.save("sad_monki.png")

with Image.open('sad_monki.png') as img:
    img = ImageOps.flip(img)
    img.save("upponer_monk.png")

# hitte på flagga
PINK = (255, 75, 69)
YELLOW = (255, 227, 154)

im = Image.new("RGB", (160, 100), PINK)

imd = ImageDraw.Draw(im)

# Rita två rektanglar
imd.rectangle([(50, 0), (70, 100)], YELLOW)
imd.rectangle([(0, 40), (160, 60)], YELLOW)

im.save("pinkyyy.png")