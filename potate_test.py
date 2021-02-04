import streamlit as st
import numpy as np
from PIL import Image
import cv2


def macth_image(image, template):  # マッチした位置、スケール、一致度を返す
    height = template.shape[0]
    width = template.shape[1]
    g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # グレースケール加工
    scale = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25,
             1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8,2,2.4,2.8,3,3.5,4,4.5,5,5.5,6,7,8,9,10,11,12,13,14,15,17
             ]
    rank = []
    for i in scale:  # scaleのパターンだけ縮小→拡大し、最もマッチする値を選ぶ
        g_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        g_template = cv2.resize(g_template, (int(width * i), int(height * i)))  # 縮小拡大
        w, h = g_template.shape[1::-1]
        result = cv2.matchTemplate(g_image, g_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        rank.append(max_val)

    best_scale = scale[np.argmax(rank)]
    g_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    g_template = cv2.resize(g_template, (int(width * best_scale), int(height * best_scale)))  # 縮小拡大
    w, h = g_template.shape[1::-1]
    result = cv2.matchTemplate(g_image, g_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return (min_val, max_val, min_loc, max_loc,g_template,best_scale)



def four_patern_test(image, template):  # 0度、90度、180度、270度回転の4パターンから最もマッチするものを出力
    image1 = image
    image2 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image3 = cv2.rotate(image, cv2.ROTATE_180)
    image4 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img_list = [image1, image2, image3, image4]
    res1 = macth_image(image1, tmp)[1]
    res2 = macth_image(image2, tmp)[1]
    res3 = macth_image(image3, tmp)[1]
    res4 = macth_image(image4, tmp)[1]
    res_list = [res1, res2, res3, res4]
    return img_list[np.argmax(res_list)]


if __name__ == '__main__':
    st.title("じゃがいも野郎を探すぜ！")

    uploaded_file = st.file_uploader("ここから画像を入れてね", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = np.array(image.convert("RGB"))
        image = cv2.cvtColor(image, 1)
        tmp = cv2.imread("potato_boy8.jpg")

        image = four_patern_test(image,tmp)

        result = macth_image(image, tmp)
        w, h = result[4].shape[1::-1]
        top_left = result[3]
        btm_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(image, top_left, btm_right, 255, 2)

        st.image(image, caption=f"一致度：{result[1]},縮尺：{result[5]}", use_column_width=True)

