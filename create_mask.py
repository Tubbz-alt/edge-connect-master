from src.utils import create_mask
from PIL import Image
import numpy as np
import random
for i in range(10):
    x = random.randint(-10,30)
    y = random.randint(-10,10)
    mask = create_mask(256, 256, 120+x, 40+y)*255
    mask  =np.expand_dims(mask,-1)
    mask = np.tile(mask,(1,1,3))
    Image.fromarray(mask.astype(np.uint8)).save('./ww_data/ww_mask{}.png'.format(i))