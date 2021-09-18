import json
import os
import sys

from PIL import Image, ImageFilter


def get_input(local=False):
    if local:
        print("Reading local file lena.png.")

        return 'lena.png'

    dids = os.getenv('DIDS', None)

    if not dids:
        print("No DIDs found in environment. Aborting.")
        return

    dids = json.loads(dids)

    for did in dids:
        filename = f'data/inputs/{did}/0'  # 0 for metadata service
        print(f"Reading asset file {filename}.")

        return filename


def run_blur(local=False):
    filename = get_input(local)
    if not filename:
        print("Could not retrieve filename.")
        return

    img = Image.open(filename)
    img = img.filter(ImageFilter.BLUR)

    result_filename = 'output/grayscale.png' if local else '/data/outputs/result'
    img.save(result_filename)


if __name__ == "__main__":
    local = (len(sys.argv) == 2 and sys.argv[1] == "local")
    run_blur(local)
