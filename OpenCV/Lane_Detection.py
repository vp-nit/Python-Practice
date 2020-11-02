import cv2 as cv
import numpy as np

# ----- LANE DETECTION CONCEPT ON LIVE VIDEO FEED ----- #

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image


def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0, 255, 255), 3)

    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def process(image):
    height = image.shape[0]
    width = image.shape[1]
    # print(f'height: {height}\nwidth :{width}')

    region_of_interest_vertices = [
        (width/7, height),
        (2*width / 5, 3/5*height),
        (3/5 * width, 3/5*height),
        (width, height)
    ]

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    canny_image = cv.Canny(gray_image, 100, 120)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

    lines = cv.HoughLinesP(cropped_image,
                           rho=6,
                           theta=np.pi / 60,
                           threshold=160,
                           lines=np.array([]),
                           minLineLength=40,
                           maxLineGap=50)

    image_with_lines = draw_the_lines(image, lines)
    return image_with_lines


cap = cv.VideoCapture('resources/solidYellowLeft.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv.putText(frame, 'Press "Q" to quit', (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 205, 205), 3)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
