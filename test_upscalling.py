# Test of different resizing and upscaling techniques.
from PIL import Image

# Open the input image
input_image = Image.open("output/crop1_2_centered.png")

# Upscale the image to 2x resolution using bicubic interpolation
upscaled_image = input_image.resize((input_image.width * 4, input_image.height * 4), resample=Image.BICUBIC)

# Save the upscaled image
upscaled_image.save("output/1bicubic.jpg")

# Upscale the image to 2x resolution using bilinear interpolation
upscaled_image = input_image.resize((input_image.width * 4, input_image.height * 4), resample=Image.BILINEAR)

# Save the upscaled image
upscaled_image.save("output/2bilinear.jpg")

# Upscale the image to 2x resolution using Lanczos interpolation
upscaled_image = input_image.resize((input_image.width * 4, input_image.height * 4), resample=Image.LANCZOS)

# Save the upscaled image
upscaled_image.save("output/3lanczos.jpg")

# Upscale the image to 2x resolution using nearest neighbor interpolation
upscaled_image = input_image.resize((input_image.width * 4, input_image.height * 4), resample=Image.NEAREST)

# Save the upscaled image
upscaled_image.save("output/4nearest.jpg")

