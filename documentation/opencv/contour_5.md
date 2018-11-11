# Contour
    - 이미지상의 객체들에 대한 주요 속성들을 도출하는 방법

1. Aspect Ratio
    - 주어진 Contour의 외접하는 직사각형(Bounding Rect)을 구한 후 이 직사각형의 폭과 높이를 이용해서 Aspect Ratio의 값을 구합니다.
    - Aspect Ratio = Width / Height
    ```
    x, y, w, h = cv2.boundingRect(cnt)
    aspect_ratio = float(w) / h
    ```

2. Extent
    - Contour의 넓이와 Contour의 외접 직사각형 넓이의 비로 구할 수 있다.
    - Extend = Object Area / Bounding Rectangle Area
    ```
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    rect_area = w*h
    extent = float(area) / rect_area
    ```

3. Solidity
    - Contour의 넓이와 이 Contour의 Convex Hull 넓이의 비로 구할 수 있다.
    - Solidity = Contour Area / Convex Hull Area
    ```
    area = cv2.contourArea(cnt)
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(bull)
    solidity = float(area) / hull_area 
    ```

5. Equivalent Diameter
    - Contour의 넓이와 동일한 럽이를 가진 원의 지름
    ```
    area = cv2.contourArea(cnt)
    equivalent_diameter = np.sqrt(4*area/np.pi)
    ```

6. Orientation
    - 객체가 향하고 있는 방향
    - Contour의 최적 타원의 기울어진 각도로 구한다.
    ```
    (x, y), (MajorAxis, MinorAxis), angle = cv2.fitEllipse(cnt)
    ```

7. Mask & Pixel Points
    - 가끔 객체를 구성하는 모든 점들, 다시 말하면 모든 픽셀들의 좌표를 추출할 필요가 있을 때 cv2.findNonZero() 함수를 이용한다.
    ```
    mask = np.zeros(imgray.shape, np.uint8)
    cv2.drawContours(mask, [cnt], 0, 255, -1)
    pixels = cv2.findNonZero(mask)
    ```

8. Mean Color / Mean Intensity
    - Contour내의 평균 색상, Gray Scale 이미지일 경우 평균 intensity 값을 찾기 위해 cv2.mean() 함수를 활용하면 된다.
    ```
    mask = np.zeros(imgray.shape, np.uint8)
    mean_value = cv2.mean(img, mask = mask)
    ```
9. Extreme Points
    - Contour의 가장 왼쪽점, 가장 오른쪽점, 가장 윗점, 가장 아랫점
    ```
    leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
    rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
    topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
    bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
    ```
[reference](http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220517848698&parentCategoryNo=&categoryNo=66&viewDate=&isShowPopularPosts=false&from=postView)