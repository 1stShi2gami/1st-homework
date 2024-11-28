from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w//2, h//2))

def new_photo_2(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((150, 150))



im = new_photo('profile.png')
im_2 = new_photo_2('light.png')

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('HandWriting.otf', 100)
draw.text((250, 200), 'Hello', font=font, fill=('black'))

im.paste(im_2, (100, 100))
im.show('photo')





