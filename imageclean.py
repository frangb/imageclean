from PIL import Image
import numpy
import argparse
parser = argparse.ArgumentParser(description="Elimina metadatos de imagen")

parser.add_argument(
    "-i", "--image", help="archivo con la imagen a eliminar los metadatos", type=str
)

parser.add_argument(
    "-o", "--output", help="archivo de salida con el resultado", type=str, default="image_file_without_exif.jpeg")

args = parser.parse_args()

image = Image.open(args.image)

# Random mask
imarray = numpy.random.rand(image.height, image.width, 3) * 255
mask = Image.fromarray(imarray.astype('uint8')).convert('RGB')

# remove exif data
data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)

# combine both images
final_image = Image.blend(image_without_exif, mask, 0.01)
final_image.save(args.output)
