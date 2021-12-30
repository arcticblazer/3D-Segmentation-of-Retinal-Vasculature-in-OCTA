import cv2
import numpy as np
from PIL import Image
import imageio
import matplotlib.pyplot as plt

def localAdaptiveThreshold2D(img):
#     img = cv2.GaussianBlur(img, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 0)
    return thresh

for image_num in range(10352, 10501):
    image_path = "./Data/Filtered/" + str(image_num) + ".bmp"
    img = imageio.imread(image_path)
    print(str(image_num) + " Image read")

    image_volume = []
    for frame_no in range(304):
        image_frame = img[frame_no*640 : (frame_no+1)*640]
    #     plt.imshow(image_frame)
        image_volume.append(image_frame)

    image_volume = np.array(image_volume)

    threshold_vol = np.zeros([304,640,304], dtype = np.uint8)

    for frame_no in range(640):
        image_frame = image_volume[:,frame_no,:]
        # threshold_vol.append(localAdaptiveThreshold2D(image_frame))
        threshold_vol[:,frame_no,:] = localAdaptiveThreshold2D(image_frame)

    threshold_vol = np.array(threshold_vol)

    output_image = []
    for frame_no in range(304):
        frame = threshold_vol[frame_no,:,:]
        for row in range(640):
            output_image.append(frame[row,:])
    # print("Volume converted to 2D array")
      
    output_image = np.array(output_image)
    output_image = Image.fromarray((output_image).astype(np.uint8))
    output_image.save("./Data/LAT/" + str(image_num) + ".bmp")
    print("Done")