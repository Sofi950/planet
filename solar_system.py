import cv2 

img = cv2.imread("solar-system.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)

cv2.putText(
    img, "Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.putText(
    img, "Mercurio", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.putText(
    img, "Venus", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.putText(
    img, "Tierra", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.putText(
    img, "Marte", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.putText(
    img, "Mercurio", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.putText(
    img, "Saturno", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.putText(
    img, "Urano", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.putText(
    img, "Neptuno", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) 
)

cv2.imwrite("Solar_systemwithname.jpg", img)