import cv2 
webcam = cv2.VideoCapture(0)
img_counter =0
while True:
    ret,frame  = webcam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test",frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("press escape to close")
        break
    elif k%256 == 32:
        img_name = f"C:\\Users\\prakash\\OneDrive\\Documents\\my project\\identify_faces\\identify_faces_{img_counter}.png"
        cv2.imwrite(img_name,frame)
        print("face taken")
        img_counter+=1

webcam.release()
webcam.destroyAllWindows()      

