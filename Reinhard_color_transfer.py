import cv2
import numpy as np
import os

input_dir = r"E:\CV_projects\input_dir"
output_dir = r"E:\CV_projects\output_dir"

def get_mean_and_std(x):
    x_mean, x_std = cv2.meanStdDev(x)
    x_mean = np.hstack(np.around(x_mean, 2))
    x_std = np.hstack(np.around(x_std, 2))
    return x_mean, x_std

template_img = cv2.imread(r"E:\CV_projects\template.jfif")  # source img
template_img_lab = cv2.cvtColor(template_img, cv2.COLOR_BGR2LAB)
template_mean, template_std = get_mean_and_std(template_img_lab)

input_img_list = os.listdir(input_dir)

for input_img_name in input_img_list:
    input_img_path = os.path.join(input_dir, input_img_name)
    print(input_img_name)
    
    input_img = cv2.imread(input_img_path)
    input_img_lab = cv2.cvtColor(input_img, cv2.COLOR_BGR2LAB)
    img_mean, img_std = get_mean_and_std(input_img_lab)

    height, width, channel = input_img_lab.shape
    for i in range(0, height):
        for j in range(0, width):
            for k in range(0, channel):
                x = input_img_lab[i, j, k]
                x = (x - img_mean[k]) * (template_std[k] / img_std[k]) + template_mean[k]
                x = round(x)
                x = 0 if x < 0 else x
                x = 255 if x > 255 else x
                input_img_lab[i, j, k] = x

    modified_img = cv2.cvtColor(input_img_lab, cv2.COLOR_Lab2BGR)
    output_path = os.path.join(output_dir, "modified_" + os.path.splitext(input_img_name)[0] + ".jpg")
    cv2.imwrite(output_path, modified_img)

