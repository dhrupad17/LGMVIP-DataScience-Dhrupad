import cv2
#to take image input (RGB format)
image=cv2.imread("ben10.jpg")
cv2.imwrite("1_original.jpg",image)

#to convert it to Grayscale Image
g_f= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite("2_grayscale.jpg",g_f)

#to invert the colors of grayscaled imange
i=cv2.bitwise_not(g_f)
cv2.imwrite("3_invert.jpg",i)

#to make blur image from grayscaled and inverted image
b=cv2.GaussianBlur(i,(21,21),0)
cv2.imwrite("4_blur.jpg",b)

#to combine inverterd and blurred image
ib=cv2.bitwise_not(b)
cv2.imwrite("5_invertedblurry.jpg",ib)

#to make Final Sketch
sketch= cv2.divide(g_f,ib,scale=256.0)
cv2.imwrite("6_sketch.jpg",sketch)#output