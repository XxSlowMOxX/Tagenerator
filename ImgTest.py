from PIL import Image, ImageDraw

img = Image.new('RGB', (100, 30), color = (73, 109, 137))
d = ImageDraw.Draw(img)
d.text((10, 10), "Test", fill=(255,255,0))

img.save("test_red.png")