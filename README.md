# multipurpose-swapper
This utility swaps RGBA channels of tiff files between Gearbox and Xbox [multipurpose map formats][1].

Installation:
```sh
pip3 install pillow
```

Usage examples:
```
python3 convert.py -h
python3 convert.py gbx input_dir output_dir
python3 convert.py xbox input_dir output_dir
```

All .tiff/tif files with "multi" in their name under the input directory will be converted to new files at the same relative paths in the output directory.

[1]: https://c20.reclaimers.net/h1/tags/shader/shader_model/#multipurpose-map
