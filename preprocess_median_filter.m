image_x = 640;
image_y = 304;
no_of_frames = 304;
image = zeros(no_of_frames,image_x,image_y);

for image_num = 10352:10500
    full_image = imread("./Data/Compiled/" + string(image_num) + ".bmp");

    for frame_no = 1:no_of_frames
        slice = full_image((frame_no-1)*640 +1:(frame_no)*640, :);
        image(frame_no,:,:) = slice;
    end

    filtered_image = medfilt3(image);
    final_image = zeros(no_of_frames*image_x, image_y);

    for frame_no = 1:no_of_frames
       final_image((frame_no-1)*640 + 1:frame_no*640, : ) = reshape(filtered_image(frame_no,:,:), image_x, image_y);
    end

    final_image = uint8(final_image);
    imwrite(final_image, "./Data/Filtered/" + string(image_num) + ".bmp");
end    


