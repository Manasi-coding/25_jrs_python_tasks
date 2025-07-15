import cv2 as cv
import os

class Image_Utility:

    def __init__(self):
        self.image=None
        self.path=''

    def get_path(self):
        self.path=input('Enter the image path: ').strip()
        if not os.path.exists(self.path):
            print('File not found!')
            return False
        self.image=cv.imread(self.path)
        return True
    
    def Resize(self):
        w=int(input('Enter width: '))
        h=int(input('Enter height: '))
        self.image=cv.resize(self.image,(w,h))
        cv.imshow('Resized Image', self.image)
        cv.waitKey(0)

    def Rotate(self):
        self.image=cv.rotate(self.image, cv.ROTATE_90_CLOCKWISE)
        cv.imshow('Rotated Image', self.image)
        cv.waitKey(0)

    def Gray(self):
        self.image=cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        cv.imshow('Grayscaled Image', self.image)
        cv.waitKey(0)

    def Blur(self):
        try:
            k=int(input('Enter kernel size (odd): '))
            self.image=cv.GaussianBlur(self.image,(k,k),0)
            cv.imshow('Blurred Image', self.image)
            cv.waitKey(0)
        except:
            print('Invalid kernel size!')

    def Threshold(self):
        try:
            val = int(input('Enter threshold value (0-255): '))
            gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
            _, self.image = cv.threshold(gray, val, 255, cv.THRESH_BINARY)
            cv.imshow('Thresholded Image', self.image)
            cv.waitKey(0)
        except:
            print('Invalid threshold value!')

    def Canny(self):
        low=int(input('Enter lower threshold value:'))
        high=int(input('Enter higher threshold value:'))
        self.image=cv.Canny(self.image,low,high)
        cv.imshow('Canny-Edge Image', self.image)
        cv.waitKey(0)

    def Contour(self):
        gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        edged = cv.Canny(gray, 30, 200)        #to highlight the edges
        contours, hierarchy = cv.findContours(edged,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)      #find contours
        self.image = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
        cv.drawContours(self.image, contours, -1, (255,0,0), 2)         #-1: draws all contours in blue colour of border thickness 2
        cv.imshow('Contoured Image', self.image)
        cv.waitKey(0)

    def Dilate(self):
        try:
            gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
            _, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
            k = int(input('Enter kernel size (odd): '))
            kernel = cv.getStructuringElement(cv.MORPH_RECT, (k, k))
            self.image = cv.dilate(thresh, kernel, iterations=1)
            cv.imshow('Dilated Image', self.image)
            cv.waitKey(0)
        except:
            print('Dilation failed!')

    def Erode(self):
        try:
            gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
            _, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
            k = int(input('Enter kernel size (odd): '))
            kernel = cv.getStructuringElement(cv.MORPH_RECT, (k, k))
            self.image = cv.erode(thresh, kernel, iterations=1)
            cv.imshow('Eroded Image', self.image)
            cv.waitKey(0)
        except:
            print('Erosion failed!')


    def Rect(self):
        print('Enter top-left coordinates:')
        x1=int(input())
        y1=int(input())
        print('Enter bottom-right coordinates:')
        x2=int(input())
        y2=int(input())
        c=(255,0,0)     #blue colour
        t=-1             #thickness of the border (to fill completely)
        self.image=cv.rectangle(self.image,(x1,y1),(x2,y2),c,t)
        cv.imshow('After Drawing', self.image)
        cv.waitKey(0)


def main():
    data=Image_Utility()
    action=None
    if not data.get_path():
        return
    
    while True:
        print('\n1.Resize, 2.Rotate, 3.Convert to gray, 4.Blur, 5.Threshold, 6.Canny Edges, 7.Contour, 8.Dilate, 9.Erode, 10.Draw a Rectangle, 11.EXIT')
        try:
            ch = int(input('Enter your choice (1-11): '))
        except:
            print("Invalid input.")
            continue

        match ch:
            case 1: action=data.Resize()
            case 2: action=data.Rotate()
            case 3: action=data.Gray()
            case 4: action=data.Blur()
            case 5: action=data.Threshold()
            case 6: action=data.Canny()
            case 7: action=data.Contour()
            case 8: action=data.Dilate()
            case 9: action=data.Erode()
            case 10: action=data.Rect()
            case 11: break

if __name__ == "__main__":
    main()

