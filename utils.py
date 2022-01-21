
from PIL import Image, ImageDraw

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def mask_regular_hexagon(pil_img):
  img_width, img_height = pil_img.size
  img_rgba = pil_img.copy()


  mask = Image.new("L", pil_img.size, 0)
  draw = ImageDraw.Draw(mask)
  draw.regular_polygon((img_width // 2, img_height // 2, img_height // 2), 6, rotation=0, fill=255)
  img_rgba.putalpha(mask)
  return img_rgba

def pixellate(pil_img):
  # Resize smoothly down to pixels
  imgSmall = pil_img.resize((32,32),resample=Image.BILINEAR)

  # Scale back up using NEAREST to original size
  result = imgSmall.resize(pil_img.size,Image.NEAREST)
  return result


def cut_nft_pfp(source_image, shouldPixellate=False):
  square_image = crop_max_square(source_image)
  if shouldPixellate:
    square_image = pixellate(square_image)
  masked_image = mask_regular_hexagon(square_image)

  return masked_image

