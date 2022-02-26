import cv2
import glob

images=glob.glob("/Users/vojtechoravec/Documents/VisualStudio/Python/imgs*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    if not cv2.imwrite("resized_"+image,re):
        raise Exception("no img")
    cv2.destroyAllWindows()
    
    