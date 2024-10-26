import streamlit as st
from PIL import Image
import requests

# Sidebar for navigation with hyperlinks
st.sidebar.title("Kushal Gowda")
st.sidebar.markdown("[About Me](#about-me)")
st.sidebar.markdown("[Education](#education)")
st.sidebar.markdown("[Professional Experience](#professional-experience)")
st.sidebar.markdown("[Projects](#projects)")
st.sidebar.markdown("[Certifications](#certifications)")
st.sidebar.markdown("[Extracurricular & Competitions](#extracurricular)")

# Sidebar information
st.sidebar.title("Profile Sections")
st.sidebar.write("Navigate to each section by clicking the links above")

# About Me Section
def about_me():
    st.title("About Kushal Gowda Guruvinamata Venugopal", anchor="about-me")
    
    # Creating two columns for layout
    col1, col2 = st.columns([1, 2])
    
    # Left Column - Profile Image and Contact Email
    with col1:
        # Profile image
        profile_image = Image.open(r"C:\\Users\\sagar\\OneDrive\\Documents\\GitHub\\Kushal_Portfolio\\assets\\images\\kush-profile-image.jpg")
        st.image(profile_image, caption="Kushal Gowda", width=150)
        
        # Contact Information
        st.subheader("Contact")
        st.write("**Email:** kushalgowdagv@gmail.com")
    
    # Right Column - Certifications, Education, Skills
    with col2:
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

# Education Section
def education():
    st.title("Education", anchor="education")
    st.write("### Lehigh University, United States")
    st.write("**MS Financial Engineering** (Aug 2023 - May 2025)")
    st.write("- Financial Derivatives, Financial Engineering Practicum, Quantitative Risk Management, etc.")
    
    st.write("### Dr. Ambedkar Institute of Technology, India")
    st.write("**Bachelor of Engineering in Computer Science** (Aug 2016 - Sept 2020)")
    st.write("Certifications: CFA Level 2, Algo Trading (EPAT), Data Scientist (DataCamp), Options 101/201, Bloomberg Market Concepts")

# Professional Experience Section
def professional_experience():
    st.title("Professional Experience", anchor="professional-experience")
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
def projects():
    st.title("Projects", anchor="projects")
    st.write("### Volatility Optimizer Tool")
    st.write("- Developed a tool to generate optimal portfolio weights based on targeted volatility.")
    st.write("### Real-time NLP Model")
    st.write("- Engineered a model for Reddit sentiment analysis to predict Binance listings.")

# Certifications Section
def certifications():
    st.title("Certifications", anchor="certifications")
    st.write("- Chartered Financial Analyst (CFA) Level 2")
    st.write("- EPAT (Algo Trading) from QuantInsti")
    st.write("- Data Scientist and Machine Learning Scientist from DataCamp")
    st.write("- Options 101 and 201 from Akuna Capital")
    st.write("- Bloomberg Market Concepts")

# Extracurricular and Competitions Section
def extracurricular():
    st.title("Extracurricular & Competitions", anchor="extracurricular")
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

# Display the sections based on anchor
about_me()
education()
professional_experience()
projects()
certifications()
extracurricular()

# Display GitHub Profile
username = 'kushalgowdagv'  # Replace with GitHub username
display_github_profile(username)

# Cloud Deployment Note
st.write("This app is designed to be deployed on cloud platforms like Heroku, Streamlit Cloud, or AWS for easy access and demonstration.")
