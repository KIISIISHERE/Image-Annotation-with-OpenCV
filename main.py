import cv2
#global variables-accessed by all the functions in the code
drawing=False
#initialize the starting point
ix,iy=-1,-1
image=None
clone=None #copy of the image will be saved
#function-draw a shape around an object using a mouse
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,image
    #lest mouse button
    if event==cv2.EVENT_LBUTTONDOWN:
        #start drawing
        drawing=True
        #set the starting point of the mouse
        ix,iy=x,y
    #moving the mouse:
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing:
            #copy the image
            temp=clone.copy()
            #draw a rectangle according to the mouse movement
            cv2.rectangle(temp,(ix,iy),(x,y),(255,255,255),4)
            #show the preview
            cv2.imshow("Annotated image",temp)
    #mouse release
    elif event==cv2.EVENT_LBUTTONUP:
        #stop drawing
        drawing=False
        cv2.rectangle(image,(ix,iy),(x,y),(255,255,255),4)
        #Add a label to the annotated point
        label="Highlighted section"
        cv2.putText(image,label,(ix,iy-10),cv2.FONT_ITALIC,0.7,(0,0,0),2)
        cv2.imshow("Annotated image",image)
#load image
image=cv2.imread("image.png")
#chekc if image exists
if image is None:
    print("Error: Image not found.")
    exit()
#make a copy of the original image
clone=image.copy()
#create a resizable window
cv2.namedWindow("Annotated image")
#link the mouse to the events
cv2.setMouseCallback("Annotated image",draw_rectangle )
print("Instructions")
print("1. Click and hold the left mouse button to start drawing a rectangle.")
print("-press 'q' to quit.")
print("-press 'r' to reset the image.")
#while loop
while True:
    #display the current image
    cv2.imshow("Current image",image)
    #wait for keypress
    key=cv2.waitKey(1) & 0xFF
    #if user presser r
    if key==ord("r"):
        #clear any drawings on the image
        image=clone.copy()
    #user presses q
    elif key==ord("q"):
        break
#clear the windows
cv2.destroyAllWindows()
#save the annotated image
cv2.imwrite("annotated_image.png",image)
