# Contour

### Matching Shape(모양 비교하기)
- OpenCV의 cv2.matchShapes() 함수는 두 도형 또는 두 Contour를 비교하여 닮은 정도를 수치로 리턴한다.
- 리턴한 값이 작으면 닮은 정도가 높은 것이고 값이 크면 닮은 정도가 낮습니다.
    - 만약 두 도형이 완전히 닮은 꼴이면 0 리턴
- cv2.matchShape()함수는 Hu Moments를 이용해 두 도형의 닮음 정도를 계산한다.
- cv2.matchShape(cnt1, cnt2, method, parameter)
    - cnt1, cnt2 : 비교할 두 도형 또는 Contour
    - method : 비교 방법, 3가지 종류 있고 Hu Moment를 이용해 계산
        - cv2.CONTOURS_MATCH_L1(현재 버전에서 이 상수가 정의되어 있지 않아 1로 정의해서 사용)
        - cv2.CONTOURS_MATCH_L2(현재 버전에서 이 상수가 정의되어 있지 않아 2로 정의해서 사용)
        - cv2.CONTOURS_MATCH_L3(현재 버전에서 이 상수가 정의되어 있지 않아 3으로 정의해서 사용)
        - parameter : 현재 지원하지 않은 인자. 0.0 값으로 입력함
    - example
        - cv2.matchShape(cnt1, cnt2, 1, 0,0)

[reference](http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220524551089&parentCategoryNo=&categoryNo=66&viewDate=&isShowPopularPosts=false&from=postView)