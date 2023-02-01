from PIL import Image
import numpy as np
import art_image

img = art_image.Gradient()

Image.fromarray(np.uint8(img.image((2048, 1080), (0, 0, 255), (255, 255, 0)))).save('gradient.jpg', quality=100)