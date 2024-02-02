import cv2

img = cv2.imread("./solar-system.jpg")

cv2.putText(img,"Sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Mercurio",(100,195),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"Venus",(200,175),cv2.FONT_HERSHEY_COMPLEX,0.5,(5,122,240))
cv2.putText(img,"Terra",(300,165),cv2.FONT_HERSHEY_COMPLEX,0.5,(29,46,194))
cv2.putText(img,"Marte",(400,175),cv2.FONT_HERSHEY_COMPLEX,0.5,(46,29,194))
cv2.putText(img,"Jupiter",(500,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(5,122,240))
cv2.putText(img,"Saturno",(800,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(5,122,240))
cv2.putText(img,"Urano",(1000,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Netuno",(1100,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))


cv2.imshow("imagem", img)
cv2.waitKey(0)
