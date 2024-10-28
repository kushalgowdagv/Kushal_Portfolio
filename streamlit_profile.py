
import streamlit as st
from PIL import Image
import requests
st.markdown(
    """
    <style>
    /* Adjust column widths and image sizes based on screen size */
    @media (max-width: 768px) {
        .profile-image {
            width: 100px !important;
        }
        .sidebar-icons img {
            width: 20px !important;
        }
    }
    @media (min-width: 769px) {
        .profile-image {
            width: 150px !important;
        }
        .sidebar-icons img {
            width: 30px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Sidebar for navigation with hyperlinks
st.sidebar.title("Kushal Gowda")
st.sidebar.markdown("[About Me](#about-me)")
st.sidebar.markdown("[Education](#education)")
st.sidebar.markdown("[Professional Experience](#professional-experience)")
st.sidebar.markdown("[Projects](#projects)")
st.sidebar.markdown("[Certifications](#certifications)")
st.sidebar.markdown("[Extracurricular & Competitions](#extracurricular)")

# Sidebar information with icons for GitHub, email, and LinkedIn
st.sidebar.title("Connect with Me")
github_icon = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
linkedin_icon = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
email_icon = "https://cdn-icons-png.flaticon.com/512/732/732200.png"

# Using st.markdown with HTML to include hyperlinks with images
st.sidebar.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <a href="https://github.com/kushalgowdagv" target="_blank">
            <img src="{github_icon}" width="30" style="margin: 0 10px;">
        </a>
        <a href="mailto:kushalgowdagv@gmail.com" target="_blank">
            <img src="{email_icon}" width="30" style="margin: 0 10px;">
        </a>
        <a href="https://www.linkedin.com/in/kushalgowdagv/" target="_blank">
            <img src="{linkedin_icon}" width="30" style="margin: 0 10px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

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



# Skills Section with Organized Headings and Icons
        st.subheader("Technical Skills")

# Big Data and Analytics
        st.write("**Big Data and Analytics:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg" width="30" style="margin: 0 10px;"> Big Data Analytics
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Kubernetes_logo_without_workmark.svg" width="30" style="margin: 0 10px;"> Kubernetes
                <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Hadoop_logo_new.svg" width="30" style="margin: 0 10px;"> Hadoop
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Apache_Cassandra_logo.svg" width="30" style="margin: 0 10px;"> Apache Cassandra
            </div>
            """,
            unsafe_allow_html=True
        )

# High Performance Computing (HPC) and Quantification
        st.write("**High Performance Computing (HPC) and Quantification:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/Intel_HPC_logo.svg" width="30" style="margin: 0 10px;"> HPC
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/Quantitative_analysis_icon.svg" width="30" style="margin: 0 10px;"> Quantification
            </div>
            """,
            unsafe_allow_html=True
        )

# Machine Learning and AI
        st.write("**Machine Learning and AI:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Keras_logo.svg" width="30" style="margin: 0 10px;"> Keras
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/TensorFlow_logo.svg" width="30" style="margin: 0 10px;"> TensorFlow
                <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="30" style="margin: 0 10px;"> Scikit-Learn
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/PyTorch_logo_icon.svg" width="30" style="margin: 0 10px;"> PyTorch
            </div>
            """,
            unsafe_allow_html=True
        )

# Databases and Data Engineering
        st.write("**Databases and Data Engineering:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/en/d/dd/MySQL_logo.svg" width="30" style="margin: 0 10px;"> MySQL
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/68/MariaDB_logo.svg" width="30" style="margin: 0 10px;"> MariaDB
                <img src="https://upload.wikimedia.org/wikipedia/en/2/23/Snowflake_Logo.svg" width="30" style="margin: 0 10px;"> Snowflake
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/SQL_logo.svg" width="30" style="margin: 0 10px;"> SQL
            </div>
            """,
            unsafe_allow_html=True
        )

# Quantitative Finance and Financial Modeling
        st.write("**Quantitative Finance and Financial Modeling:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/e/e6/Bloomberg_logo.svg" width="30" style="margin: 0 10px;"> Bloomberg Terminal
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" width="30" style="margin: 0 10px;"> MATLAB
                <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Excel_logo.svg" width="30" style="margin: 0 10px;"> Microsoft Excel
            </div>
            """,
            unsafe_allow_html=True
        )

    # Programming Languages
        st.write("**Programming Languages:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="30" style="margin: 0 10px;"> Python
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/18/C_Programming_Language.svg" width="30" style="margin: 0 10px;"> C++
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg" width="30" style="margin: 0 10px;"> R
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Java_Logo.svg" width="30" style="margin: 0 10px;"> Java
            </div>
            """,
            unsafe_allow_html=True
        )

# Cloud Computing
        st.write("**Cloud Computing:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" width="30" style="margin: 0 10px;"> AWS
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/Microsoft_Azure_Logo.svg" width="30" style="margin: 0 10px;"> Azure
            </div>
            """,
            unsafe_allow_html=True
        )


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
