# Importing the OpenCV library
import cv2

# Reading the image using imread() function
image = cv2.imread("road.jpg")

# Extracting the height and width of an image
height, width = image.shape[:2]

# Displaying the height and width
print("Image dimensions:")
print(f"Height = {height} \nWidth = {width}")


# Extracting RGB values from a random pixel
(B, G, R) = image[100, 100]

# Displaying pixel values
print("\nRGB values at pixel [100, 100]:")
print(f"R: {R} \nG: {G} \nB: {B}")


# Extracting region of interest by slicing pixels
roi = image[100 : 500, 200 : 700]

roi_success = cv2.imwrite("roi.jpg", roi)
print("\nRegion of interest extracted.") if roi_success else print("\nExtraction failed.")


# Calculating aspect ratio
ratio = width / height

# Resizing the image
dim = (800, int(800 * (1 / ratio)))
resize = cv2.resize(image, dim)

resize_success = cv2.imwrite("resize.jpg", resize)
print("\nImage resized successfully.") if resize_success else print("\nResize failed.")


# Calculating center of image
center = (width // 2, height // 2)

# Generating rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)

# Performing affine transformation
rotated = cv2.warpAffine(image, matrix, (width, height))

rotate_success = cv2.imwrite("rotated.jpg", rotated)
print("\nRotation of image successful.") if rotate_success else print("\nRotation failed.")


# Copying image
output = image.copy()

# Using rectangle() to create a rectangle
rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (255, 0, 0), 2)

rectangle_success = cv2.imwrite("rectangle.jpg", output)
print("\nRectangle creation successful.") if rectangle_success else print("\nRectangle creation failed.")


# Copying image
output = image.copy()

# Adding text using putText()
text = cv2.putText(output, "OpenCV Demo", (500, 550), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

text_success = cv2.imwrite("text.jpg", output)
print("\nText creation success.") if text_success else print("\nText creation failed.")
