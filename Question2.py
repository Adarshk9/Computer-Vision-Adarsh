import cv2

def grayscale(image):
  """Converts an image to grayscale."""
  return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def invert(image):
  """Inverts the colors of an image."""
  return cv2.bitwise_not(image)

# Load an image
image = cv2.imread("image.jpg")

# Convert the image to grayscale
grayscale_image = grayscale(image)

# Invert the image
inverted_image = invert(grayscale_image)

# Show the original and processed images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", grayscale_image)
cv2.imshow("Inverted Image", inverted_image)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()