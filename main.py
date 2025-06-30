# main.py
import qrcode
import os
import argparse
from datetime import datetime


def generate_qr(url, output_dir="qr_codes"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.join(
        output_dir, f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )
    img = qrcode.make(url)
    img.save(filename)
    print(f"[✔] QR Code saved to: {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code for a URL")
    parser.add_argument(
        "--url",
        type=str,
        required=False,
        default="https://github.com/kaw393939",
        help="URL to encode in QR code",
    )
    args = parser.parse_args()

    generate_qr(args.url)
