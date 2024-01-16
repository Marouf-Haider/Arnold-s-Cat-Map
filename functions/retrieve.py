def retrieve(encoded_image_path, iterations):
    # Read encoded image
    encoded_image = cv2.imread(encoded_image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if encoded image was loaded successfully
    if encoded_image is None:
        raise ValueError("Image could not be read. Check the file path.")
 
    # Check if image is square
    if encoded_image.shape[0] != encoded_image.shape[1]:
        raise ValueError("Image must be square (same width and height).")  
     
    # Extract image size from encoded image (assumes global variable or previously loaded)
    N = encoded_image.shape[0]

    # Compute minimal period for this image size
    period = minimal_period(N)

    # Compute how many more iterations are needed to restore the image
    reverse_iterations = period - (iterations % period)

    # Apply inverse transformation using the remaining iterations
    return apply_arnold_cat_map(encoded_image_path, reverse_iterations)