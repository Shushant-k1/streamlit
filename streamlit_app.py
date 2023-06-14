import streamlit as st
import easyocr
import cv2
from PIL import Image
def fun(image):
  reader = easyocr.Reader(['en']) 
  result = reader.readtext(image)
  #image = cv2.imread(image)
  res = reader.readtext(image) 
  z = ""
  for (bbox, text, prob) in res: 
    # unpack the bounding box/
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    cv2.rectangle(image, tl, br, (255, 0,0), 2)
    z = z + text
  return z
img = st.file_uploader("Choose a Image", accept_multiple_files=False)
if img is not None :
    image = Image.open(img)
    st.image(image, caption='Sunrise by the mountains')
    #img = cv2.imread(image)
    final = fun(image)
    st.write(final)
