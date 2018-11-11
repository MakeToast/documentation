# Contour

### Contour Hierarchy
- cv2.findContours() : 이미지에서 찾은 contour와 이 contour들의 hierarchy 리턴
    - _, contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

- Contour Hierarchy (Contour 계층)
    - Contour을 찾다보면 각각 독립적으로 Contour가 존재하는 경우도 있고 Contour 내부에 Contour가 존재하는 경우도 있다.
    - 각각 동일한 레벨에서 Contour가 존재하는 경우 같은 계층에 존재한다고 하며 Contour 내부에 또다른 Contour가 존재하는 경우, Contour를 포함하고 있는 Contour를 부모계층, 어떤 Contour 안에 들어가 있는 Contour를 자식계층이라 한다.

    - cv2.findContours() 함수의 두번째 리턴값은 Contour들간의 관계를 나타내는 값이다. 
        - [Next, Previous, First Child, Parent]
            - Next : 동일레벨의 다음 Contour 인덱스. 동일레벨의 다음 Contour가 없으면 -1
            - Previous : 동일레벨의 이전 Contour 인덱스. 동일레벨의 이전 Contour가 없으면 -1
            - First Child : 최초의 자식 Contour 인덱스. 자식 Contour가 없으면 -1
            - Parent : 부모 Contour 인덱스. 부모 Contour가 없으면 -1
        - 두 번째 들어가는 parameter는 Contour Hierarchy 값의 결과에 영향을 주는 인자이다.
            - cv2.RETR_LIST : 이미지에서 발견한 모든 Contour들을 계층에 상관하지 말고 나열하는 것
            - cv2.RETR_TREE : 모든 Contour들의 관계를 명확히 해서 리턴하는 인자
            - cv2.RETR_EXTERNAL
            - cv2.RETR_CCOMP
[reference](http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220534805843&parentCategoryNo=&categoryNo=66&viewDate=&isShowPopularPosts=false&from=postView)