import cv2
import numpy as np

# mouse callback function
def draw_mask(event,x,y,flags,param):

    if (event ==  cv2.EVENT_MOUSEMOVE ) & (flags == cv2.EVENT_FLAG_LBUTTON):
    	global imgMask
        global imgInput
        global fileName
        global imgInput_temp 
        cv2.circle(imgInput,(x,y),3,(0,255,255),-1)
        cv2.circle(imgMask,(x,y),3,(255),-1)
        # print [x,y]
    elif (event ==  cv2.EVENT_MOUSEMOVE ) & (flags == cv2.EVENT_FLAG_RBUTTON):
        cv2.circle(imgInput,(x,y),6,(0,0,255),-1)
        cv2.circle(imgMask,(x,y),6,(255),-1)
    elif (event == cv2.EVENT_RBUTTONDBLCLK):
        # kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
        # imgMask_1 = cv2.morphologyEx(imgMask, cv2.MORPH_CLOSE, kernel_2)    
        dst = cv2.inpaint(imgInput_temp,cv2.medianBlur(imgMask,3),5,cv2.INPAINT_TELEA)
    	cv2.imwrite(fileName+'_inpainting_mode_1.jpg',dst)
        cv2.imshow('Original image without any modification...', imgInput_temp)
        cv2.imshow('After inpainting..',dst)
        cv2.waitKey(0)
        # imgInput = dst
        # cv2.setMouseCallback('After inpainting..',draw_mask)
        # while(1):
        #     cv2.imshow('After inpainting..',imgInput_temp)

        #     if cv2.waitKey(20) & 0xFF == 27:
        #         break
        # cv2.destroyAllWindows()  
        
    	

def draw_mask_same_color(event,x,y,flags,param):
    if (event ==  cv2.EVENT_MOUSEMOVE ) & (flags == cv2.EVENT_FLAG_LBUTTON):
        global imgMask
        global imgInput
        global fileName
        cv2.circle(imgInput,(x,y),3,(0,255,0),-1)        
        # print ('The color in location'+[x,y]+' = '+imgInput[x,y])
        kernel_2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        imgMask = (imgInput == imgInput[x,y]).astype(np.uint8)
        imgMask = cv2.dilate(imgMask,kernel_2)
      

    elif (event == cv2.EVENT_RBUTTONDBLCLK):
        dst = cv2.inpaint(imgInput,imgMask,3,cv2.INPAINT_TELEA)
        cv2.imwrite(fileName+'_inpainting_mode_2.jpg',dst)
        cv2.imshow('After inpainting..',dst)

        cv2.waitKey(0) 




# Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
print('####################################################################################################')
print('#################################### Welcome to the inpainting demo ################################')
print('####################################################################################################')
print('##################################     Digital Image Process Course   ##############################')
print('####################################################################################################\n\n')

fileName = raw_input('Please input the file name of target picture: ')
mode = raw_input('Please input the mode: ')
imgInput = cv2.imread(fileName, cv2.CV_LOAD_IMAGE_COLOR)
[m,n,r] = imgInput.shape
imgMask = np.zeros((m,n),np.uint8)
imgInput_temp = imgInput.copy()
if mode == '1':
    cv2.namedWindow('Original image in mode 1..')
    cv2.setMouseCallback('Original image in mode 1..',draw_mask)
    while(1):
        cv2.imshow('Original image in mode 1..',imgInput)
        
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
elif mode == '2':
    cv2.namedWindow('Original image in mode 2..')
    cv2.setMouseCallback('Original image in mode 2..',draw_mask_same_color)
    while(1):
        cv2.imshow('Original image in mode 2..',imgInput)
    
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows() 

