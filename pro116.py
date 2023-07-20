import cv2

img = cv2.imread("solar-system.jpg")


cv2.imshow("resultado",img)
cv2.waitKey(1)
cv2.putText(img,"Sol", 
            (100,80), 
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,"Mercurio", 
            (100,180), 
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0,0,255)
            )

cv2.putText(img,"Venus", 
            (190,260), 
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0,0,255)
            )

cv2.putText(img,"Terra", 
            (270,170), 
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0,0,255)
            )

cv2.putText(img,"Marte", 
            (370,260), 
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0,0,255)
            )

cv2.putText(img,"Jupiter", 
            (500,80), 
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0,0,255)
            )

cv2.putText(img,"Saturno", 
            (770,130), 
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0,0,255)
            )

cv2.putText(img,"Urano", 
            (950,130), 
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0,0,255)
            )

cv2.putText(img,"Netuno", 
            (1100,130), 
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0,0,255)
            )

cv2.imwrite("Solar_systemwithname.jpg",img)
