import streamlit as st
from PIL import Image, ImageFilter

st.title("Image Processing")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    # Sidebar for selecting filters
    filter_type = st.sidebar.selectbox("Select a filter:", ["None", "Blur", "Sharpen", "Grayscale"])

    # Apply selected filter
    if filter_type == "Blur":
        filtered_image = image.filter(ImageFilter.BLUR)
    elif filter_type == "Sharpen":
        filtered_image = image.filter(ImageFilter.SHARPEN)
    elif filter_type == "Grayscale":
        filtered_image = image.convert("L")
    else:
        filtered_image = image

    # Display the original and filtered images
    st.image([image, filtered_image], caption=["Original Image", "Filtered Image"])