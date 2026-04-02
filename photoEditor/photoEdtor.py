# PhotoEditor Project using Pillow
# --------------------------------
# This script demonstrates how to use Pillow (PIL) to:
# 1. Open an image
# 2. Resize it
# 3. Apply filters (grayscale, blur, sharpen)
# 4. Add text on top
# 5. Save the edited image

from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance

# Step 1: Open an image
# Replace 'input.jpg' with the path to your image file
img = Image.open("keyboard.jpg")

# Step 2: Resize the image
# Resize to 400x400 pixels while keeping aspect ratio
img_resized = img.resize((400, 400))

# Step 3: Apply filters

# Create an enhancer object for contrast
enhancer = ImageEnhance.Contrast(img_resized)
# Apply enhancement (factor > 1 increases contrast, < 1 decreases)
img_contrast = enhancer.enhance(1.5)

img_gray = img_resized.convert("L")  # Convert to grayscale
img_blur = img_resized.filter(ImageFilter.BLUR)  # Apply blur
img_sharp = img_resized.filter(ImageFilter.SHARPEN)  # Sharpen image

# Step 4: Add text on top
# Create a copy so we don’t overwrite the original
img_text = img_resized.copy()
draw = ImageDraw.Draw(img_text)

# Load a font (default if you don’t have a .ttf file)
# You can replace with a font file: ImageFont.truetype("arial.ttf", 30)
font = ImageFont.load_default()

# Add text at position (10, 10)
draw.text((10, 10), "Hello Pillow!", font=font, fill=(255, 0, 0))

# Step 5: Save the edited images
img_contrast.save("output_contrast.jpg")
img_resized.save("output_resized.jpg")
img_gray.save("output_gray.jpg")
img_blur.save("output_blur.jpg")
img_sharp.save("output_sharp.jpg")
img_text.save("output_text.jpg")

print("✅ Photo editing complete! Check your output images.")
