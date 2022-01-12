# importing the module
import cv2

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (0, 0, 255), 2)
		cv2.imshow('image', img)


# driver function
if __name__=="__main__":



   img = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Code/Examen/MyImage.png')

   cv2.imshow('image', img)
   cv2.setMouseCallback('image', click_event)
   cv2.waitKey(0)

