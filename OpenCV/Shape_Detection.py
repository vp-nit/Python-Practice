import cv2 as cv
import numpy as np

# ----- DETECTING SIMPLE GEOMETRICAL SHAPES ----- #

img = cv.imread('resources/shapes.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(img_gray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, epsilon=0.01 * cv.arcLength(contour, closed=True), closed=True)
    # epsilon defines approximation accuracy
    cv.drawContours(img, [approx], 0, (0, 0, 0), 3)

    # writing the name of the shape
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        (x, y, w, h) = cv.boundingRect(approx)
        aspect_ratio = float(w) / h
        # print(aspect_ratio)
        if 0.95 <= aspect_ratio <= 1.05:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "Rectangle", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))  # (y-10) just to show
            # that we can adjust the position of text.

    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 6:
        cv.putText(img, "Hexagon", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 7:
        cv.putText(img, "Heptagon", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 8:
        cv.putText(img, "Octagon", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        # Use circularity formula to differentiate between ellipse and circle
        # circularity = 4*pi*Area/perimeter^2 =1 For circle and between 0 and one for ellipse
        circularity = 4 * np.pi * cv.contourArea(contour) / (cv.arcLength(contour, True) ** 2)
        # print(circularity)
        if 1.10 >= circularity >= 0.90:
            cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        elif 0.90 > circularity > 0:
            cv.putText(img, "Ellipse", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "Unknown Shape", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv.imshow('Shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()
