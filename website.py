import streamlit as st
import pandas as pd
import random

# Set page configuration
st.set_page_config(page_title="🎓 Student Data Generator", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: 800;
            color: #4A7EBB;
            text-align: center;
        }
        .sub-text {
            text-align: center;
            color: #555;
            margin-bottom: 40px;
        }
        .css-1aumxhk {
            background-color: #f9f9f9;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="main-title">🎓 Student CSV File Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Generate random student data and download it as a CSV file</div>', unsafe_allow_html=True)

# Data generation logic
names = ["Ali", "Ahmed", "Behram", "Beenish", "Esha", "Farah", "Soha", "Saad", "Sarmad", "Hira", "Hammad", "Haider", "Zara", "Zain", "Neha"]
grades = ["A", "B", "C", "D", "E", "F"]

students = []
for i in range(1, 16):
    student = {
        "ID": i,
        "NAME": random.choice(names),
        "AGE": random.randint(18, 25),
        "GRADE": random.choice(grades),
        "MARKS": random.randint(40, 100)
    }
    students.append(student)

# Convert to DataFrame
df = pd.DataFrame(students)

# Display DataFrame with custom styles (white text, black background)
st.subheader("📋 Generated Student Data")
st.dataframe(df.style.set_properties(
    **{
        'color': 'white',
        'background-color': 'black',
        'border-color': 'white',
        'text-align': 'center'
    }
))

# CSV download
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download CSV File",
    data=csv,
    file_name='student_data.csv',
    mime='text/csv',
    help="Click to download the generated student data"
)
