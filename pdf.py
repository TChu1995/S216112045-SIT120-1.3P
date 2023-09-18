import os
from PIL import Image
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from tqdm import tqdm


def convert_folder_to_pdf(folder_path):
    # Get the folder name for the PDF title
    folder_name = os.path.basename(folder_path)

    # Create a PDF canvas with portrait orientation
    pdf_file_path = f"{folder_name}.pdf"
    c = canvas.Canvas(pdf_file_path, pagesize=portrait)

    # Get a list of picture files in the folder
    jpeg_files = [
        f
        for f in os.listdir(folder_path)
        if f.lower().endswith(".jpeg")
        or f.lower().endswith(".jpg")
        or f.lower().endswith(".png")
    ]

    # Sort the files by name
    jpeg_files.sort()

    # Initialize chapter count
    chapter_count = 1

    # Create a progress bar
    with tqdm(
        total=len(jpeg_files), desc=f"Converting {folder_name}", unit="image"
    ) as pbar:
        for jpeg_file in jpeg_files:
            image_path = os.path.join(folder_path, jpeg_file)

            # Open the image and get its size
            img = Image.open(image_path)
            img_width, img_height = img.size

            # Set the page size to match the image size
            c.setPageSize((img_width, img_height))

            # Add the image to the PDF
            c.drawImage(image_path, 0, 0, width=img_width, height=img_height)

            # Add a new page for the next image
            c.showPage()

            # Increment chapter count and format it as "0001", "0002", etc.
            chapter_count += 1

            pbar.update(1)  # Update the progress bar

    # Save the PDF
    c.save()


def main():
    # Specify the directory containing folders with JPEG images
    root_directory = "E:\Comics\OP"

    # Get a list of subdirectories (folders) in the root directory
    subdirectories = [
        f
        for f in os.listdir(root_directory)
        if os.path.isdir(os.path.join(root_directory, f))
    ]

    # Process each folder and convert images to PDF with progress tracking
    for folder in subdirectories:
        folder_path = os.path.join(root_directory, folder)
        convert_folder_to_pdf(folder_path)


if __name__ == "__main__":
    main()
