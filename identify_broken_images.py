'''
Removing broken images in the BFM dataset (synface)
'''
from PIL import Image
import os
import os.path as path

IMAGE_PATH = '/root/unsup3d-rep/data/synface/train/image'
DEPTH_PATH = '/root/unsup3d-rep/data/synface/train/depth'


img_list = [name for name in os.listdir(IMAGE_PATH) if path.isfile(path.join(IMAGE_PATH, name))]
depth_list = [name for name in os.listdir(DEPTH_PATH) if path.isfile(path.join(DEPTH_PATH, name))]
img_list.sort()
depth_list.sort()

for depth in depth_list:
    d = Image.open(path.join(DEPTH_PATH, depth))

    if depth.replace('depth', 'image') not in img_list:
        print('not in image!')
        os.remove(path.join(DEPTH_PATH, depth))
        continue

    try:
        d.verify()
    except:
        # print(f'broken file: {depth}')
        os.remove(path.join(DEPTH_PATH, depth))



'''
for img in img_list:
    im = Image.open(path.join(IMAGE_PATH, img))
    print(img)

    try:
        im.verify()
    except:
        print(f'broken file: {img}')
        os.remove(path.join(IMAGE_PATH, img))
'''






