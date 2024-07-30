#https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from PIL import Image, ImageFilter, ImageEnhance

# Define file paths
original_image_path = r"C:\Users\Alshuruq Company\Desktop\PythonProblems\image_pillow.jpg"
brightened_image_path = r"C:\Users\Alshuruq Company\Desktop\PythonProblems\image_brightened.jpg"
greyscale_image_path = r"C:\Users\Alshuruq Company\Desktop\PythonProblems\image_greyscale.jpg"
filtered_image_path = r"C:\Users\Alshuruq Company\Desktop\PythonProblems\image_filtered.jpg"

# Open image
myImage = Image.open(original_image_path)
myImage.show()

# Increase brightness
enhancer = ImageEnhance.Brightness(myImage)
brightened_image = enhancer.enhance(1.5)  # Adjust the factor as needed (1.5 means 50% brighter)
brightened_image.show()

# Save brightened image to avoid overriding
brightened_image.save(brightened_image_path)

# Convert image to greyscale
converted_image = brightened_image.convert("L")
converted_image.show()

# Save greyscale image to avoid overriding
converted_image.save(greyscale_image_path)

# Apply filter to the greyscale image
out_filter = converted_image.filter(ImageFilter.DETAIL)
out_filter.show()

# Save filtered image
out_filter.save(filtered_image_path)
