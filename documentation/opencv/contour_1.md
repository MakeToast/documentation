# Contour
- Image Contour
    * 같은 값을 가진 곳을 연결한 선 (ex. 등고선, 등압선 등)
    * 동일한 색 또는 동일한 색상 강도(Color intensity)를 가진 부분의 가장 자리 경계를 연결한 선
    * 이미지에 있는 물체의 모양 분석이나 객체 인식 등에 유용하게 활용되는 도구
    * 바이너리 이미지 사용(보다 정확한 이미지 Contour 확보하기 위해) - threshold나 canny edge detection 적용하는 것이 좋다.
    * cv2.findContours() : Suzuki85 알고리즘 이용하여 이미지의 Contour를 찾는 함수
    * OpenCV에서 Contour 찾기 = 검정색 배경에서 흰색 물체(Contour를 찾고자 하는 대상) 찾기

- Example Code
```
import numpy as np
import cv2

def contour() :
    img = cv2.imread('image/to/path')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
> imgray : Gray 스케일로 변환시킨 이미지.<br>
> thresh : imgray를 thresholding한 값<br>

- cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    - return value: thr, 이미지에서 찾은 contour, contour들 간의 게층 구조
    - thresh: contour 찾기를 할 소스 이미지. **thresholding을 통해 변환된 바이너리 이미지**
    - cv2.RETR_TREE : contour추출 모드. 2번째 리턴값인 hierarchy의 값에 영향을 줌
        - cv2.RETR_EXTERNAL : 이미지의 가장 바깥쪽의 contour를 추출
        - cv2.RETR_LIST : contour 간 계층구조 상관관계를 고려하지 않고 contour 추출
        - cv2.RETR_CCOMP : 이미지에서 모든 contour를 추출한 후, 2단계 contour 계층 구조로 구성함. 
            - 1단계 계층 - 외곽 경계 부분
            - 2단계 계층 - 구멍의 경계 부분 나타내는 contour
        - cv2.RETR_TREE : 이미지에서 모든 contour를 추출하고 contour들간의 상관관계 추출
    - cv2.CHAIN_APPROX_SIMPLE : contour 근사 방법
        - cv2.CHAIN_APPROX_NONE : contour를 구성하는 모든 점을 저장
        - cv2.CHAIN_APPROX_SIMPLE : contour의 수평, 수직, 대각선 방향의 점은 모두 버리고 끝 점만 남겨둠 ( 에를 들어 똑바로 세워진 직사각형의 경우 4개의 모서리점만 남기고 다 버림 )
        - cv2.CHAIN_APPROX_TC89__1 : Teh-Chin 연결 근사 알고리즘 적용

- cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    - findContours로 찾은 contour를 실제로 그리는 함수
    - img : contour를 나타낼 대상 이미지
    - contours: img에 그릴 contour. 이 값은 cv2.findContours()함수의 2번째 리턴 값으로 리스트형 자료이다. i 번째 contour의 첫 번째 픽셀 좌표는 contours[i][0]과 같이 접근 가능
    - -1 : img에 실제로 그릴 contour 인덱스 파라미터. 이 값이 음수이면 모든 contour를 그림
    - 1 : contour 선의 두께

- cv2.CHAIN_APPROX_SIMPLE과 cv2.CHAIN_APPROX_NONE 차이
    - cv2.CHAIN_APPROX_SIMPLE : contour의 수평, 수직, 대각선 방향의 직전상에 놓은 점들을 모두 버리고 끝 점들만 취한다.
    - cv2.CHAIN_APPROX_NONE : contour 상의 모든 점을 취한다

[reference](http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220516697251&parentCategoryNo=&categoryNo=66&viewDate=&isShowPopularPosts=false&from=postView)