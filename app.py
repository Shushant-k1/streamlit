import streamlit as st
import easyocr
import os
#from google.colab.patches import cv2_imshow
def fun(image):
  reader = easyocr.Reader(['en']) 
  result = reader.readtext(image)
  #image = cv2.imread(image)
  res = reader.readtext(image) 
  z = ""
  for (bbox, text, prob) in res: 
    # unpack the bounding box/
    # (tl, tr, br, bl) = bbox
    # tl = (int(tl[0]), int(tl[1]))
    # tr = (int(tr[0]), int(tr[1]))
    # br = (int(br[0]), int(br[1]))
    # bl = (int(bl[0]), int(bl[1]))
    # cv2.rectangle(image, tl, br, (255, 0,0), 2)
    # cv2.putText(image, text, (tl[0], tl[1] - 10),
    #   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    z = z + text
  return z

img = "A_Desk-Book_of_Errors_in_English.djvu.jpg"

print(fun(img))
