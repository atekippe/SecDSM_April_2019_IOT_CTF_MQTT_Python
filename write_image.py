from PIL import Image, ImageDraw
from PIL import ImageFont

img = Image.new('RGB', (640, 480), color=(0, 0, 0))

d = ImageDraw.Draw(img)

font = ImageFont.truetype("Lato-Black.ttf", 32)
d.text((230, 220), "test", fill=(32, 194, 14),font=font)

img.save('pil_text.png')
img.show()
