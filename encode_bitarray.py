import argparse
import json

import pyqrcode

def create_qr_data(data):
    qr = pyqrcode.create(data)
    return qr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reads image print qr data')
    parser.add_argument('data', type=str,
                        help='Any string data')
    parser.add_argument('out_file', type=str,
                        help='Out json file')
    args = parser.parse_args()

    res = create_qr_data(args.data)
    with open(args.out_file, 'w') as file:
        json.dump(res.code, file, indent=2, sort_keys=True, ensure_ascii=False)
