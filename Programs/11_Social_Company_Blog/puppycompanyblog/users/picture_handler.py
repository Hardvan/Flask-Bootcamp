import os
from PIL import Image
from flask import url_for, current_app


def add_profile_pic(pic_upload, username):

    filename = pic_upload.filename

    # Grab extension type (.jpg, .png, etc.)
    ext_type = filename.split(".")[-1]

    # Save picture as username.jpg
    storage_filename = str(username) + "." + ext_type

    # Create path to save picture
    filepath = os.path.join(current_app.root_path,
                            "static\profile_pics", storage_filename)

    # Set size of picture
    output_size = (200, 200)

    # Open picture and resize it
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
