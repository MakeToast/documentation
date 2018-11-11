import numpy as np
import cv2

def contour() :
    img = cv2.imread('src/color_origin.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 125, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)

    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)

def moment() :
    img = cv2.imread('src/image1.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour = contours[0]
    mmt = cv2.moments(contour)

    for key, val in mmt.items() :
        print('%s:\t%.5f' %(key, val))

    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    print(cx, cy)

def contour_area() :
    img = cv2.imread('src/image1.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[164]
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)

    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)
    # cv2.drawContours(img, contours, 164, (255, 255, 0), 1)
    print('contour 면적 : ', area)
    print('contour 길이 : ', perimeter)
    
    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def contour_approx() :
    img = cv2.imread('src/color_origin.jpg')
    
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img2= img1= thr

    cnt = contours[8]
    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)
    '''
    for i in range(len(contours)) :
        cnt = contours[i]
        cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)
        cv2.imshow('contour', img)
        cv2.waitKey(0)
    '''
    
    epsilon1 = 0.01 * cv2.arcLength(cnt, True)
    epsilon2 = 0.1 * cv2.arcLength(cnt, True)

    approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
    approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

    cv2.drawContours(img, [approx1], 0, (0, 255, 0), 3)
    cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3)

    
    
    cv2.imshow('Approx1', img)
    cv2.imshow('Approx2', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()   

def contour_iteration() :
    img = cv2.imread('src/color_origin.jpg')
    
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
    max = 0
    val = 0
    for i in range(len(contours)) :
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        print('contour 면적 : ', area)
        print('contour 길이 : ', perimeter)
        if max < area :
            max = area
            val = i
        #cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)
        #cv2.imshow('contour', img)
        #cv2.waitKey(0)
    print(max, val)
    cnt = contours[val]
    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)
    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
contour_iteration()