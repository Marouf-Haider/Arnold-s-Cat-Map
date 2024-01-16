import numpy as np
import cv2
from numpy import ones as o
from numpy import lcm as l

def apply_arnold_cat_map(image_path, iterations):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image could not be read. Check the file path.")
    if image.shape[0] != image.shape[1]:
        raise ValueError("Image must be square (same width and height).")
    N = image.shape[0]
    encoded_image = np.zeros_like(image)
    for x in range(N):
        for y in range(N):
            x_new, y_new = x, y
            for i in range(iterations):
                x_new, y_new = (x_new + y_new) % N, (x_new + 2 * y_new) % N
            encoded_image[x_new, y_new] = image[x, y]
    return encoded_image

def minimal_period(n):
    p = 1
    li = o([n, n])
    for i in range(n):
        for j in range(n):
            if int(li[i][j]) == 1:
                c = 1
                i_1 = i
                j_1 = j
                while ((2 * i_1 + j_1) % n) != i or ((i_1 + j_1) % n) != j:
                    a = i_1
                    i_1 = (2 * i_1 + j_1) % n
                    j_1 = (a + j_1) % n
                    c += 1
                    li[i_1][j_1] = 0
                p = l(p, c)
    return p

def retrieve(encoded_image_path, iterations):
    encoded_image = cv2.imread(encoded_image_path, cv2.IMREAD_GRAYSCALE)
    if encoded_image is None:
        raise ValueError("Image could not be read. Check the file path.")
    if encoded_image.shape[0] != encoded_image.shape[1]:
        raise ValueError("Image must be square (same width and height).")
    N = encoded_image.shape[0]
    period = minimal_period(N)
    reverse_iterations = period - (iterations % period)
    return apply_arnold_cat_map(encoded_image_path, reverse_iterations)

if __name__ == "__main__":
    input_image_path = 'assets/test_image.jpg'
    iterations = 10

    # Encode image
    encoded_image = apply_arnold_cat_map(input_image_path, iterations)
    cv2.imwrite('outputs/encoded_image.jpg', encoded_image)
    print("Encoded image saved to outputs/encoded_image.jpg")

    # Retrieve original image
    original_image = retrieve('outputs/encoded_image.jpg', iterations)
    cv2.imwrite('outputs/retrieved_image.jpg', original_image)
    print("Retrieved image saved to outputs/retrieved_image.jpg")