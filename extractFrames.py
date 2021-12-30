from pydicom import dcmread
from pydicom.data import get_testdata_file
# from scipy import misc
from PIL import Image
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os

for image_num in range(10352, 10501):
    images_path = "./Data/Raw/" + str(image_num) + "/"
    images = os.listdir(images_path)
    images = sorted(images, key = lambda num : int(num[:-4]))
    print(len(images))

    volume = []

    for image in images:
        print(image)
        img = imageio.imread(os.path.join(images_path, image))
        
        #img = Image.open(os.path.join(images_path, image)).convert('L')
        #img = np.array(img.getdata()).reshape(img.size[0], img.size[1])
        #img = img.transpose()
        
        #gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
        #grey = gray(img).astype(np.uint8)

        for row in range(img.shape[0]):
            volume.append(img[row])

    vol = np.array(volume)
    print(vol.shape)
    result = Image.fromarray(vol.astype(np.uint8))
    # result = result.transpose()
    print(result.size)
    result.save("./data/Compiled/" + str(image_num) + ".bmp")





