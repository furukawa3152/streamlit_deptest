import streamlit as st
import numpy as np
from PIL import Image
import cv2

def macth_image(image,template):
    height = template.shape[0]
    width = template.shape[1]
    g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    scale=[0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1,1.05,1.1,1.15,1.2,1.25,
           1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8]
    rank = []
    for i in scale:
        g_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        g_template = cv2.resize(g_template,(int(width*i),int(height*i)))#縮小拡大
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
    top_left = max_loc
    btm_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(image, top_left, btm_right, 255, 2)
    return image

if __name__ == '__main__':
    st.title("じゃがいも野郎を探すぜ！")

    uploaded_file = st.file_uploader("ここから画像を入れてね",type="jpg")


    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = np.array(image.convert("RGB"))
        image = cv2.cvtColor(image,1)
        tmp = cv2.imread("potato_boy8.jpg")
        result = macth_image(image,tmp)
        st.image(result,caption="itaruchann",use_column_width=True)