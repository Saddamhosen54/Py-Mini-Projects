# install rembg, PIL, tkinter using pip

from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def remove_background(input_path, output_path):
    # Open the input image
    with open(input_path, "rb") as input_file:
        input_image = input_file.read()

    # Remove the background
    output_image = remove(input_image)

    # Save the output image
    with open(output_path, "wb") as output_file:
        output_file.write(output_image)

def select_files():
    # Open file dialog to select an input file
    input_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )
    
    if input_path:
        # Set default output path
        default_output_path = os.path.splitext(input_path)[0] + "_no_bg.png"
        
        # Open file dialog to select where to save the output file
        output_path = filedialog.asksaveasfilename(
            title="Save the output image",
            defaultextension=".png",
            initialfile=default_output_path,
            filetypes=[("PNG files", "*.png")]
        )
        
        if output_path:
            # Remove the background
            remove_background(input_path, output_path)
            print(f"Background removed successfully! Output saved at: {output_path}")

if __name__ == "__main__":
    # Create a Tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Call the select_files function to start the process
    select_files()
