import cv2
import numpy as np
from PIL import Image
import imageio
import matplotlib.pyplot as plt

def extract_volume(image_path):
    img = imageio.imread(image_path)
    image_volume = []
    for frame_no in range(304):
        image_frame = img[frame_no*640 : (frame_no+1)*640]
    #     plt.imshow(image_frame)
        image_volume.append(image_frame)
        
    image_volume = np.array(image_volume)
    
    return image_volume
    
def dice(seg, gt):
    k = 255
    seg = seg[:, 260:305, :]
    gt = gt[:, 260:305, :]
    return np.sum(seg[gt==k])*2.0 / (np.sum(seg) + np.sum(gt))
    
f = open("results.csv", "w")
print("File Read")
for image_num in range(10302,10501):
    f.write(str(image_num) + ",")
    print(image_num)
    oof = extract_volume("./Data/OOF/" + str(image_num) + ".bmp")
    acm = extract_volume("./Data/ACM/" + str(image_num) + ".bmp")
    lat = extract_volume("./Data/LAT/" + str(image_num) + ".bmp")

    models = {"ACM" : acm, "Local Adaptive Threshold" : lat, "OOF" : oof}

    for model1name in models:
        for model2name in models:
            # print("DICE Coeff between " + model1name + " and " + model2name + " = " + str(dice(models[model1name], models[model2name])))
            f.write(str(dice(models[model1name], models[model2name])) + ",")
        
    f.write("\n")
