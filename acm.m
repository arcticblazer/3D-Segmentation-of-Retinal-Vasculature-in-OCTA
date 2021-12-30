image_x = 640;
image_y = 304;
no_of_frames = 304;
image = zeros(no_of_frames,image_x,image_y);

for image_num = 10413:10500
    full_image = imread("./Data/Preprocessed/" + string(image_num) + ".bmp");

    for frame_no = 1:no_of_frames
        slice = full_image((frame_no-1)*640 +1:(frame_no)*640, :);
        image(frame_no,:,:) = slice;
    end

    % imshow(reshape(image(:,280,:),304,304), [0,255])

    seed_level = 280;
    seed_value = 150;
    seed = image(:,seed_level,:) > seed_value;
    mask = zeros(size(image));
    mask(:,280,:) = seed;

    bw = activecontour(image,mask,100);

    final_image = zeros(no_of_frames*image_x, image_y);

    for frame_no = 1:no_of_frames
       final_image((frame_no-1)*640 + 1:frame_no*640, : ) = reshape(bw(frame_no,:,:), image_x, image_y);
    end

    final_image = uint8(final_image*255);
    imwrite(final_image, "./Data/ACM/" + string(image_num) + ".bmp");
end