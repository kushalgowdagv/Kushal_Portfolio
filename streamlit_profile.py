import streamlit as st
from PIL import Image
import requests

# Sidebar for navigation
st.sidebar.title("Kushal Gowda")
st.sidebar.write("Navigation")
st.sidebar.write("[Personal Website](#)")
st.sidebar.write("[Market Data Dashboard](#)")
st.sidebar.write("[FRED Dashboard](#)")
st.sidebar.write("[About Me](#)")

# Sidebar information
st.sidebar.title("Profile Sections")
sections = ["About", "Education", "Professional Experience", "Projects", "Certifications", "Extracurricular & Competitions"]
selected_section = st.sidebar.radio("Navigate", sections)

# About Me Section
def about_me():
    # Header with profile image
    st.title("About Kushal Gowda Guruvinamata Venugopal")
    
    # Profile image
    profile_image = Image.open("path_to_image")  # Replace with actual image file path
    st.image(profile_image, caption="Kushal Gowda", width=150)
    
    # Contact Information
    st.subheader("Contact")
    st.write("**Email:** kushalgowdagv@gmail.com")
    
    # Certifications
    st.subheader("Certifications")
    st.write("Chartered Financial Analyst (CFA): Level 2 Passed")
    st.write("Certifications in Algo Trading (EPAT), Data Science (DataCamp), and more.")

    # Education Section
    st.subheader("Education")
    st.write("**Lehigh University, United States**")
    st.write("M.S. in Financial Engineering (Aug 2023 - May 2025)")
    
    st.write("**Dr. Ambedkar Institute of Technology, India**")
    st.write("Bachelor of Engineering in Computer Science (Aug 2016 - Sept 2020)")

    # Skills Section
    st.subheader("Technical Skills")
    st.write("**Data Analysis:** Python, R, SPSS")
    st.write("**Databases:** MySQL, MariaDB, Snowflake")
    st.write("**Cloud:** AWS, Azure")
    st.write("**Graphic Design/Data Visualization:** Tableau, Power BI")

# Call the function to display the About Me page
if selected_section == "About":
    about_me()

# Education Section
elif selected_section == "Education":
    st.title("Education")
    st.write("### Lehigh University, United States")
    st.write("**MS Financial Engineering** (Aug 2023 - May 2025)")
    st.write("- Financial Derivatives, Financial Engineering Practicum, Quantitative Risk Management, etc.")
    st.write("")
    st.write("### Dr. Ambedkar Institute of Technology, India")
    st.write("**Bachelor of Engineering in Computer Science** (Aug 2016 - Sept 2020)")
    st.write("Certifications: CFA Level 2, Algo Trading (EPAT), Data Scientist (DataCamp), Options 101/201, Bloomberg Market Concepts")

# Professional Experience Section
elif selected_section == "Professional Experience":
    st.title("Professional Experience")
    st.write("### Trade Terminal, San Jose, United States")
    st.write("**Quantitative Research Intern** (May 2024 - Present)")
    st.write("- Engineered real-time NLP models, conducted trading strategies for crypto pairs, managed cross-asset volatility arbitrage, etc.")
    
    st.write("### Lehigh University, United States")
    st.write("**Graduate Research Assistant** (Jan 2024 - Present)")
    st.write("- Worked on interest rate models, market risk, portfolio optimization using Python, ChatGPT API for FOMC analysis, etc.")

    st.write("### HTTS - High Tech Trading System Fund, Switzerland and India")
    st.write("**Quantitative Research Analyst** (Aug 2022 - Aug 2023)")
    st.write("- Developed data pipelines, automated portfolio management, implemented risk management frameworks.")

# Projects Section
elif selected_section == "Projects":
    st.title("Projects")
    st.write("### Volatility Optimizer Tool")
    st.write("- Developed a tool to generate optimal portfolio weights based on targeted volatility.")
    st.write("### Real-time NLP Model")
    st.write("- Engineered a model for Reddit sentiment analysis to predict Binance listings.")

# Certifications Section
elif selected_section == "Certifications":
    st.title("Certifications")
    st.write("- Chartered Financial Analyst (CFA) Level 2")
    st.write("- EPAT (Algo Trading) from QuantInsti")
    st.write("- Data Scientist and Machine Learning Scientist from DataCamp")
    st.write("- Options 101 and 201 from Akuna Capital")
    st.write("- Bloomberg Market Concepts")

# Extracurricular and Competitions Section
elif selected_section == "Extracurricular & Competitions":
    st.title("Extracurricular & Competitions")
    st.write("Involved in several projects related to financial engineering, algorithmic trading competitions, and data science hackathons.")

# GitHub Integration to Display Profile
def display_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    profile_data = response.json()
    
    st.subheader(f"GitHub Profile: {profile_data['name']}")
    st.write(f"Public Repos: {profile_data['public_repos']}")
    st.write(f"Followers: {profile_data['followers']}")
    st.write(f"Following: {profile_data['following']}")
    st.write(f"Profile: {profile_data['html_url']}")

# Display GitHub Profile
username = 'kushalgowdagv'  # Replace with GitHub username
display_github_profile(username)

# Cloud Deployment Note
st.write("This app is designed to be deployed on cloud platforms like Heroku, Streamlit Cloud, or AWS for easy access and demonstration.")
