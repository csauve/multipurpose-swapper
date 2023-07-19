import os, sys
import glob
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("mode", help="The target channel order", choices=["gbx", "xbox"])
parser.add_argument("src", help="The directory containing source tiffs")
parser.add_argument("dst", help="The directory where converted tiffs will be written to")
args = parser.parse_args()

src_glob = os.path.join(args.src, "**/*multi*.tif*")
for input_file in glob.glob(src_glob, recursive=True):
  rel_path = os.path.relpath(input_file, args.src)
  dst_path = os.path.join(args.dst, rel_path)
  print("Converting " + rel_path)
  with Image.open(input_file) as img:
    for x in range(img.width):
      for y in range(img.height):
        (r, g, b, a) = img.getpixel((x, y))
        output = (a, g, r, b) # mcc/xbox to gbx
        if args.mode == "xbox":
          output = (b, g, a, r)
        img.putpixel((x, y), output)
    img.save(dst_path)