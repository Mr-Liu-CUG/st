import streamlit as st
from PIL import Image

st.title("老金的CUG时光")

st.subheader("小福在这里👇")
img1 = Image.open("./xf/1.jpg")
st.image(img1, caption="中国地质大学（武汉）七十周年校庆🧨🧨")
img2 = Image.open("./xf/2.jpg")
st.image(img2, caption="我们毕业啦🥂🥂")
img3 = Image.open("./xf/3.jpg")
st.image(img3, caption="艰苦朴素 求真务实⛰⛰")

st.subheader("老金在这里👇")
img4 = Image.open("./lj/2022.06.09主楼-谢.jpg")
st.image(img4, caption="好兄弟在这里👆")