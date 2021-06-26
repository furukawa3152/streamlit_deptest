import streamlit as st
import numpy as np
from PIL import Image
import cv2

# image = cv2.imread("jagaimoyarou.jpg")
# template = cv2.imread("potato_boy8.jpg")
# (hight, width, color) = template.shape
# result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
# print(result)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# cv2.rectangle(image, max_loc, (max_loc[0] + width, max_loc[1] + hight), 255, 2)
# cv2.imshow("test", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(cv2.minMaxLoc(result))

def macth_image(image, template):  # マッチした位置、スケール、一致度を返す
    height = template.shape[0]
    width = template.shape[1]
    g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # グレースケール加工
    scale = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15,
             1.2, 1.25,
             1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 2, 2.3, 2.6, 2.8, 3, 3.2, 3.5]
    rank = []
    for i in scale:  # scaleのパターンだけ縮小→拡大し、最もマッチする値を選ぶ
        g_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        g_template = cv2.resize(g_template, (int(width * i), int(height * i)))  # 縮小拡大
        # w, h = g_template.shape[1::-1]
        result = cv2.matchTemplate(g_image, g_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        rank.append(max_val)

    best_scale = scale[np.argmax(rank)]
    g_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    g_template = cv2.resize(g_template, (int(width * best_scale), int(height * best_scale)))  # 縮小拡大
    result = cv2.matchTemplate(g_image, g_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return (min_val, max_val, min_loc, max_loc, g_template, best_scale)

if __name__ == '__main__':
    # image = Image.open("jagaimoyarou.jpg")
    # image = np.array(image.convert("RGB"))
    # image = cv2.cvtColor(image, 1)
    # template = Image.open("potato_boy8.jpg")
    # tmp_arg = np.array(template.convert("RGB"))
    # tmp_arg = cv2.cvtColor(tmp_arg, 1)
    image = cv2.imread("furukawa.jpg")
    template = cv2.imread("potato_boy8.jpg")
    print(macth_image(image, template))

