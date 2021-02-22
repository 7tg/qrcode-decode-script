import argparse

import zxing
from PIL import Image
from pyzbar.pyzbar import decode


def read_qr_data(image):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(image)
    return barcode

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reads image print qr data')
    parser.add_argument('image', type=str,
                        help='Image File')
    args = parser.parse_args()

    res = read_qr_data(args.image)
    pass


