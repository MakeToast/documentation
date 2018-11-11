# Contour
- 폐곡선 : 원, 타원의 둘레와 같이 닫혀 있는 곡선
### Image Moments
- 객체의 무게중심, 객체의 면적 등과 같은 특성을 계산할 때 유용
    - 모멘트 종류는 3가지고 총 24개의 값을 가진다.
        - Spatial Moments(공간 모멘트) : m00, m10, m01, m20, m11, m02, m30, m21, m12, m03
        - Central Moments(중심 모멘트) : mu20, mu11, mu02, mu30, mu21, mu12, mu03
        - Central Normalized Moments(평준화된 중심 모멘트) : nu20, nu11, nu02, nu30, nu21, nu03
- cv2.moments()
    - parameter : 1xN 또는 Nx1 크기의 Numpy array
    - return value : 이미지에서 contour를 찾은 리스트형 자료(하나의 contour : 1xN크기의 Numpy array)
    - cv2.findContours() : 이미지 contour들을 찾음
    - 찾은 contour에서 이미지 모멘트를 구하고자 하는 contour 1개를 정함
    - 이 contour를 cv2.moments() 함수의 인자로 전달하여 이미지 모멘트 구함
- Example Code
```
import numpy as np
import cv2

def moment() :
    img = cv2.imread('path/to/image')
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
```
> contour = cv2.contours[0]<br>
> mmt = cv2.moments(contour)<br>
    >> cv2.findContour() 함수로 찾은 contours 중 첫번째 contour에 대한 이미지 모멘트를 구한다.
> cx = int(mmt['m10']/mmt['m00'])<br>
> cy = int(mmt['m01']/mmt['m00'])<br>
    >> 무게중심의 x좌표와 y좌표를 구하는 식

- Contour Area : 폐곡선 형태의 Contour로 둘러싸인 면적
    - cv2.contourArea()
    - Contour Area = cv2.moments()로 얻은 'm00'
- Contour Perimeter : Contour 호의 길이
    - cv2.arcLength()
        - 두 번째 인자값은 폐곡선인지 양끝이 열려 있는 호인지 나타내는 boolean값 (True : Contour 폐곡선 / False : Contour 열려있는 호)

- Example Code
```
import numpy as np
import cv2

def contour() :
    img = cv2.imread('path/to/image')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[164]
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)

    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)

    print('contour 면적 : ', area)
    print('contour 길이 : ', perimeter)

    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
> cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)<br>
    >> cnt = contours[164], 즉 165번째 Contour의 모든 픽셀을 두께1, 하늘색 선으로 img위에 드로잉 해라.<br>
    >> == cv2.drawContours(img, contours, 164, (255, 255, 0), 1)

- Contour Approximation(Contour 근사법)
    - 이미지 프로세싱을 하다보면 도형 외곽선을 꼭지점수가 원래보다 적은 다른 모양으로 바꿀 필요성이 생길 때가 있다.
    - **Couglas-Peucker** 알고리즘을 적용하여 꼭지점 줄이기 근사를 수행

- Example Code
```
import numpy as np
import cv2

def contour() :
    img = cv2.imread('path/to/image')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)

    epsilon1 = 0.01 * cv2.arcLength(cnt, True)
    epsilon2 = 0.1 * cv2.arcLength(cnt, True)

    approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
    approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

    cv2.drawContours(img1, [approx1], 0, (0, 255, 0), 3)
    cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3)

    cv2.imshow('contour', img)
    cv2.imshow('Approx1', img1)
    cv2.imshow('Approx2', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
> epsilon1 = 0.01*cv2.arcLength(cnt, True)<br>
> epsilon2 = 0.1*cv2.arcLength(cnt, True)<br>
> approx1 = cv2.approxPolyDP(cnt, epsilon1, True)<br>
> approx2 = cv2.approxPolyDP(cnt, epsilon2, True)<br>

- cv2.approxPolyDP()
    - 인자로 주어진 곡선 또는 다각형을 epsilon 값에 따라 꼭지점수를 줄여 새로운 곡선이 다각형을 생성하여 리턴한다.
- cv2.approxPolyDP()
    - cnt : Numpy Array 형식의 곡선 또는 다각형.
    - epsilon : 근사 정확도를 위한 값. 이 값은 오리지널 커브와 근사 커브간 거리의 최대값으로 사용
    - True : 세 번째 인자가 True이면 폐곡선, False이면 양끝이 열려있는 곡선 임을 의미
    - __epsilon의 크기에 따라 근사되는 결과가 다르게 나온다.__
        - epsilon 값이 작으면 오리지널 Contour과 비슷한 결과 도출, 크면 오리지널 Contour와 차이가 있는 결과 나옴. 도형의 꼭지점의 개수가 epsilon의 크기가 크면 줄어든다.

[reference](http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220516822775&parentCategoryNo=&categoryNo=66&viewDate=&isShowPopularPosts=false&from=postView)