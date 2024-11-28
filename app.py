import os
import pandas as pd
import streamlit as st
from predictFromModel import Prediction  # Ensure this module is in the same directory

# Configure Streamlit app
st.set_page_config(page_title="🌟 Thyroid Detection System", layout="wide")

# CSS for Custom Styling
st.markdown(
    """
    <style>
    .stDownloadButton, .stFileUploader { margin-top: 15px; }
    .block-container { padding-top: 2rem; }
    .stDataFrame { margin-top: 10px; max-height: 200px; } /* Limit height of data preview */
    .center-step { text-align: center; margin-top: 30px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# File directories
CSV_FILE_DIR = "Prediction_Output_File/"
SAMPLE_FILE_DIR = "Prediction_SampleFile/"
INPUT_FILE_DIR = "Prediction_InputFileFromUser/"
os.makedirs(CSV_FILE_DIR, exist_ok=True)
os.makedirs(SAMPLE_FILE_DIR, exist_ok=True)
os.makedirs(INPUT_FILE_DIR, exist_ok=True)


# Utility function to get the first file from a directory
def get_first_file(directory):
    files = os.listdir(directory)
    return os.path.join(directory, files[0]) if files else None

# Header and Introduction
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
st.title("🌟 Thyroid Detection System")
st.subheader("Your AI-Powered Assistant for Thyroid Prediction 🚀")
st.markdown("Analyze your data and get predictions in three easy steps!")
st.markdown('</div>', unsafe_allow_html=True)

# Horizontal Layout for Steps 1 and 2
col1, col2 = st.columns([1, 1], gap="large")

# Step 1: Download the sample file
with col1:
    st.markdown("### 📂 Step 1: Download the Sample File")
    sample_file_path = get_first_file(SAMPLE_FILE_DIR)
    if sample_file_path and os.path.exists(sample_file_path):
        with open(sample_file_path, "rb") as sample_file:
            st.download_button(
                label="📥 Download Sample File",
                data=sample_file,
                file_name="Sample.csv",
                mime="text/csv",
                help="Click to download a sample CSV file for reference."
            )
    else:
        st.warning("⚠️ No sample file found. Please add one to the `Prediction_SampleFile/` directory.")

# Step 2: Upload the file for prediction
with col2:
    st.markdown("### 📤 Step 2: Upload Your File")
    uploaded_file = st.file_uploader(
        "🔼 Upload a CSV file for prediction",
        type=["csv"],
        help="Upload your CSV file in the same format as the sample file."
    )
    if uploaded_file:
        st.success("✅ File uploaded successfully!")
        try:
            # Show only a snippet of the uploaded file
            df = pd.read_csv(uploaded_file, index_col=0)
            st.write("📊 **Preview (First 5 Rows):**")
            st.dataframe(df.head(5), height=200)  # Limit preview height to 200px
        except Exception as e:
            st.error(f"⚠️ Unable to preview the file: {e}")

# Step 3: Download prediction results - Centered Below
st.markdown('<div class="center-step">', unsafe_allow_html=True)
st.markdown("### 🎯 Step 3: Download Results")
if uploaded_file:
    try:
        # Save the uploaded file for processing
        input_file_path = os.path.join(INPUT_FILE_DIR, "InputFile.csv")
        df.to_csv(input_file_path)

        # Run prediction
        with st.spinner("🔄 Running prediction... This might take a few seconds ⏳"):
            pred = Prediction()  # Initialize prediction class
            pred.predictionFromModel()

        # Provide download button for results
        result_file_path = get_first_file(CSV_FILE_DIR)
        if result_file_path and os.path.exists(result_file_path):
            with open(result_file_path, "rb") as result_file:
                st.download_button(
                    label="📥 Download Results File",
                    data=result_file,
                    file_name="Prediction.csv",
                    mime="text/csv",
                    help="Click to download the prediction results."
                )
            st.balloons()
            st.success("🎉 Prediction completed successfully! Download your results above.")
        else:
            st.error("❌ Prediction failed. Please check your input or model configuration.")
    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction: {e}")
else:
    st.info("🔹 Please upload a file to proceed with the prediction.")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.info("💡 **Tip:** Ensure your data matches the sample file format for accurate predictions.")
st.markdown("© 2024 Thyroid Detection System | Powered by AI 🌟")
