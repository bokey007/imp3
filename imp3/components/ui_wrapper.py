import cv2
import streamlit as st

def opencv_ui_decorator(func):
    def wrapper(*args, **kwargs):
        # Create a Streamlit column layout
        col1, col2 = st.columns(2)

        # Display the input image in the first column
        with col1:
            st.image(args[0], channels="BGR")
            st.write(f"Resolution: {args[0].shape}")

        # Call the OpenCV function and display the output image in the second column
        output_img = func(*args, **kwargs)
        with col2:
            st.image(output_img, channels="BGR")
            st.write(f"Resolution: {output_img.shape}")

        # Add UI elements to control the function's parameters and update the output image
        with st.sidebar:
            st.subheader("Controls")
            threshold1 = st.slider("Threshold 1", 0, 255, 50)
            threshold2 = st.slider("Threshold 2", 0, 255, 100)
            apertureSize = st.slider("Aperture Size", 3, 7, 3)
            output_img = func(*args, threshold1=threshold1, threshold2=threshold2, apertureSize=apertureSize)

        return output_img

    return wrapper

# Example usage
@opencv_ui_decorator
def canny(img, threshold1, threshold2, apertureSize):
    return cv2.Canny(img, threshold1, threshold2, apertureSize)

im = cv2.imread("input.jpg")
canny(im)
