#!/usr/bin/env python3
"""
Convert a square icon to a circular icon with transparent background
"""
from PIL import Image, ImageDraw
import os

def make_circular(input_path, output_path):
    """Create a circular version of the image"""
    # Open the image
    img = Image.open(input_path).convert("RGBA")

    # Get dimensions
    width, height = img.size

    # Create a new image with transparency
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)

    # Draw a white circle (this will be the visible area)
    draw.ellipse((0, 0, width, height), fill=255)

    # Create output image
    output = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    output.paste(img, (0, 0))
    output.putalpha(mask)

    # Save the result
    output.save(output_path, 'PNG')
    print(f"✓ Created circular icon: {output_path}")
    print(f"  Size: {width}x{height}")

if __name__ == "__main__":
    input_file = "assets/img/android-chrome-512x512.png"
    output_file = "assets/img/android-chrome-512x512.png"

    # Backup the original
    if os.path.exists(input_file):
        backup_file = "assets/img/android-chrome-512x512_backup.png"
        Image.open(input_file).save(backup_file)
        print(f"✓ Backed up original to: {backup_file}")

    # Create circular version
    make_circular(input_file, output_file)
    print("\n✓ Done! Refresh your browser to see the circular icon.")
