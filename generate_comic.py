from PIL import Image, ImageDraw, ImageFont
import os

def create_comic_frame(verse_text, frame_number):
    # Define the output path
    output_path = os.path.join(os.getcwd(), f'frame_{frame_number}.png')
    
    # Create a blank white background
    img = Image.new('RGB', (800, 600), color='white')
    d = ImageDraw.Draw(img)
    
    # Load a default font (or a comic-style font if available)
    font = ImageFont.load_default()

    # Add text (Bible verse) in a simple comic-style speech bubble
    d.rectangle([20, 50, 780, 200], outline='black', width=3)
    d.text((40, 60), verse_text, fill='black', font=font)

    # Save the frame as an image file
    img.save(output_path)

# Example of generating comic frames for a Bible verse
verses = [
    "In the beginning God created the heavens and the earth.",
    "And the earth was without form and void...",
    "Let there be light!"
]

for i, verse in enumerate(verses):
    create_comic_frame(verse, i)
