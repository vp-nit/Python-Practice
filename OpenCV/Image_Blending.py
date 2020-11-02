import cv2 as cv
import numpy as np

# ----- IMAGE BLENDING USING IMAGE PYRAMIDS ----- #

# Step 1: Read the images
apple_r = cv.imread('resources/apple_r.jpg')
apple_g = cv.imread('resources/apple_g.jpg')
print(apple_r.shape)
print(apple_g.shape)

# step 2: generate gaussian pyramids
apple_r_copy = apple_r.copy()
gp_apple_r = [apple_r_copy]
for i in range(6):
    apple_r_copy = cv.pyrDown(apple_r_copy)
    gp_apple_r.append(apple_r_copy)

apple_g_copy = apple_g.copy()
gp_apple_g = [apple_g_copy]
for i in range(6):
    apple_g_copy = cv.pyrDown(apple_g_copy)
    gp_apple_g.append(apple_g_copy)

# step 3: generate laplacian pyramids
apple_r_copy = gp_apple_r[5]
lp_apple_r = [apple_r_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_apple_r[i])
    laplacian = cv.subtract(gp_apple_r[i-1], gaussian_expanded)
    lp_apple_r.append(laplacian)

apple_g_copy = gp_apple_g[5]
lp_apple_g = [apple_g_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_apple_g[i])
    laplacian = cv.subtract(gp_apple_g[i - 1], gaussian_expanded)
    lp_apple_g.append(laplacian)

# Step 4: Add both halves
apple_r_g_pyramid = []
n = 0
for apple_r_lap, apple_g_lap in zip(lp_apple_r, lp_apple_g):
    n += 1
    cols, rows, ch = apple_r_lap.shape
    laplacian = np.hstack((apple_r_lap[:, :int(cols / 2)], apple_g_lap[:, int(cols / 2):]))
    apple_r_g_pyramid.append(laplacian)

# step 5: reconstruct image
apple_r_g_reconstruct = apple_r_g_pyramid[0]
for i in range(1,6):
    apple_r_g_reconstruct = cv.pyrUp(apple_r_g_reconstruct)
    apple_r_g_reconstruct = cv.add(apple_r_g_pyramid[i], apple_r_g_reconstruct)

cv.imshow('Apple', apple_r)
cv.imshow('Orange', apple_g)
cv.imshow('Apple_Gr_Red_Reconstruct', apple_r_g_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()