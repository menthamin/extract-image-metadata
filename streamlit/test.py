import streamlit as st
from PIL import Image
import importlib.util
import sys

spec = importlib.util.spec_from_file_location(
    "extract_image_metadata",
    "/Users/jmjeon/PycharmProjects/extract-image-metadata/streamlit/functions/extract_image_metadata.py",
)
module = importlib.util.module_from_spec(spec)
sys.modules["extract_image_metadata"] = module
spec.loader.exec_module(module)

from extract_image_metadata import get_image_metadata


def load_image(image_file):
    img = Image.open(image_file)
    return img


def main():
    st.title("Extract Image metadata")

    st.subheader("Image")
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

    if image_file is not None:
        # To See details
        file_details = {
            "filename": image_file.name,
            "filetype": image_file.type,
            "filesize": image_file.size,
        }

        img = Image.open(image_file)
        metadata = get_image_metadata(img)

        st.write(file_details)
        st.write("Metadata info")
        st.write(metadata)

        # To View Uploaded Image
        st.image(load_image(image_file), width=250)


main()
