import streamlit as st
import pandas as pd

# Load the dataset
file_path = 'dataset.csv'  # Ensure this CSV file is in the same folder as the Python script
data = pd.read_csv("dataset.csv")


# Set the title of the app
st.title('Disease Cases Over Time')

# Display the raw data (optional)
if st.checkbox('Show raw data'):
    st.write(data)

# Filter by disease
disease = st.selectbox('Select a disease', data['disease'].unique())

# Filter data by the selected disease
filtered_data = data[data['disease'] == disease]

# Select a region to filter by
region = st.selectbox('Select a region', filtered_data['refArea'].unique())

# Filter the data based on selected region
region_data = filtered_data[filtered_data['refArea'] == region]

# Display a line chart for number of cases over time
st.line_chart(region_data[['refPeriod', 'Number of cases']].set_index('refPeriod'))

# Add more interactive features if needed
st.write(f"Selected disease: {disease} in {region}")


