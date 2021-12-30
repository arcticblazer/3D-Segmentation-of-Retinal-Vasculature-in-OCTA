import mclahe
import cv2
import numpy as np
from PIL import Image
import imageio
import matplotlib.pyplot as plt

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
    # print("Volume acquired")
    # print(image_volume.shape)

    preprocessed_image = mclahe.mclahe(image_volume)
    # print("Preprocessing Complete")

    output_image = []
    for frame_no in range(304):
        frame = preprocessed_image[frame_no,:,:]
        for row in range(640):
            output_image.append(frame[row,:])
    # print("Volume converted to 2D array")
      
    output_image = np.array(output_image)
    output_image = Image.fromarray((output_image*255).astype(np.uint8))
    output_image.save("./Data/Preprocessed/" + str(image_num) + ".bmp")
    # print("Done")
        