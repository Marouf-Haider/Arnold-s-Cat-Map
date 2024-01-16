def apply_arnold_cat_map(image_path, iterations):
    
    # Load image in grayscale mode
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if image was loaded successfully
    if image is None:
        raise ValueError("Image could not be read. Check the file path.")
 
    # Check if image is square
    if image.shape[0] != image.shape[1]:
        raise ValueError("Image must be square (same width and height).")   
    
    # Get image size (assumes square image)
    N = image.shape[0]

    # Initialize empty image of same shape
    encoded_image = np.zeros_like(image)

    # Iterate through each pixel coordinate
    for x in range(N):
        for y in range(N):
            # Start with current pixel position
            x_new, y_new = x, y

            # Apply ACM transformation 'iterations' times
            for i in range(iterations):
                x_new, y_new = (x_new + y_new) % N, (x_new + 2 * y_new) % N

            # Place pixel in new position
            encoded_image[x_new, y_new] = image[x, y]
            
    # Return the encoded image
    return encoded_image