
import streamlit as st
from PIL import Image
import requests

st.markdown(
    """
    <style>
    /* Set overall body styling */
    body {
        background-color: #ffffff;
        color: #000000;
        font-family: 'Poppins', sans-serif;
    }

    /* Add shadow and border-radius to sections */
    .section {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        border-radius: 8px;
        background-color: white;
        margin-bottom: 20px;
    }

    /* Hover effects for buttons and links */
    a:hover {
        color: #457B9D !important;
    }
    .button:hover {
        transform: scale(1.05);
        transition: transform 0.2s ease;
    }

    /* Sidebar customization */
    .sidebar-icons img:hover {
        transform: scale(1.1);
        transition: transform 0.3s ease;
    }

    /* Adjust column widths and image sizes based on screen size */
    @media (max-width: 768px) {
        .profile-image {
            width: 100px !important;
        }
    }
    @media (min-width: 769px) {
        .profile-image {
            width: 150px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Sidebar for navigation with hyperlinks
st.sidebar.title("Kushal Gowda G V")
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
    <div style="display: flex; justify-content: space-evenly; align-items: center;">
        <a href="https://github.com/kushalgowdagv" target="_blank">
            <img src="{github_icon}" width="30">
        </a>
        <a href="mailto:kushalgowdagv@gmail.com" target="_blank">
            <img src="{email_icon}" width="30">
        </a>
        <a href="https://www.linkedin.com/in/kushalgowdagv/" target="_blank">
            <img src="{linkedin_icon}" width="30">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


# About Me Section
def about_me():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.title("About Kushal Gowda", anchor="about-me")
    
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

        st.subheader("Badges")



        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <a href="https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/90rm512v.png" target="_blank">
                    <img src="https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/90rm512v.png" width="100" style="margin: 0 10px;">
                </a>
                <a href="https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/wa41bvjd.png" target="_blank">
                    <img src="https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/wa41bvjd.png" width="100" style="margin: 0 10px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )


# Resume Download Button
        st.subheader("Resume")
        resume_url = "https://drive.google.com/file/d/1JOnG4jDvGrL7CskoO7C3PJcAvDn8U0QI/view?usp=sharing"
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-top: 10px;">
                <a href="{resume_url}" target="_blank" style="
                    padding: 10px 20px;
                    font-size: 16px;
                    color: white;
                    background-color: #4CAF50;
                    text-decoration: none;
                    border-radius: 5px;
                    display: inline-block;
                    ">
                    Download Resume
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    

    with col2:

        # st.markdown(
        #     """
        #     **Kushal Gowda** is a **Quantitative Researcher** and **Developer** with hands-on expertise in **quantitative trading**, **algorithmic strategies**, and **risk management**. 
        #     He brings a solid background in **statistical arbitrage**, **NLP sentiment analysis**, and **market risk modeling** from his recent work as a **Quantitative Research Intern** .

        #     Kushal is currently pursuing a **Master’s in Financial Engineering** at **Lehigh University** and **Chartered Financial Analyst (CFA)** Level III Candidate, specializing in **derivatives pricing**, **stochastic processes**, and **portfolio optimization**.
        #     His professional journey includes notable roles at institutions like **HTTS - High Tech Trading System Fund** and **Finominal**, focusing on **equity portfolio optimization**, **dynamic VaR implementations**, 
        #     and the development of **volatility-optimized tools**.

        #     Beyond finance, Kushal holds certifications in **algorithmic trading**, **data science**, and **machine learning**. His educational background in **Computer Science** from 
        #     **Dr. Ambedkar Institute of Technology** further supports his diverse technical capabilities. Eager to innovate in the quantitative finance domain, 
        #     Kushal combines his passion for **technology** with an **analytical approach** to deliver impactful solutions.
        #     """,
        #     unsafe_allow_html=True
        # )
    #     st.title("Education", anchor="education")
    
    # # Lehigh University
    #     st.write("### Lehigh University, United States")
    #     lehigh_logo_url = "https://collegeaim.org/wp-content/uploads/2021/08/Lehigh-University-logo.png"
    #     st.markdown(
    #         f"""
    #         <div style="display: flex; align-items: center;">
    #             <img src="{lehigh_logo_url}" width="50" style="margin-right: 10px;">
    #             <span><strong>MS Financial Engineering</strong> (Aug 2023 - May 2025)</span>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    # # CFA 
    #     st.write("### Chartered Financial Analyst Society(CFA), USA")
    #     cfa_url = "https://higherlogicdownload.s3.amazonaws.com/CFAI/bdc5586b-297b-4536-bd76-5bfa158a0b36/UploadedImages/CFA_Institute_Logo_RGB.png"
    #     st.markdown(
    #         f"""
    #         <div style="display: flex; align-items: center;">
    #             <img src="{cfa_url}" width="50" style="margin-right: 10px;">
    #             <span><strong>CFA Level 1 and Level 2 passed with abouve 90th percentile</strong> (Aug 2016 - Sept 2020)</span>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    # # Dr. Ambedkar Institute of Technology
    #     st.write("### Dr. Ambedkar Institute of Technology, India")
    #     ambedkar_logo_url = "https://www.getmycollege.com/image-upload/new-uploads/college/logo/dr-ambedkar-institute-of-technology-logo-406.jpg"
    #     st.markdown(
    #         f"""
    #         <div style="display: flex; align-items: center;">
    #             <img src="{ambedkar_logo_url}" width="50" style="margin-right: 10px;">
    #             <span><strong>Bachelor of Engineering in Computer Science</strong> (Aug 2016 - Sept 2020)</span>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
        st.title("Education", anchor="education")
    
    # Lehigh University
        st.markdown(
            """
            ### <u>Lehigh University, United States</u>
            **MS Financial Engineering**  
            *Aug 2023 - May 2025*
            """, unsafe_allow_html=True
        )
    
    # Chartered Financial Analyst (CFA)
        st.markdown(
            """
            ### <u>Chartered Financial Analyst Society (CFA), USA</u>
            **CFA Level 1 and Level 2 passed with above 90th percentile**  
            *2016 - 2020*
            """, unsafe_allow_html=True
        )
        st.markdown(
            """
            ### <u>Dr. Ambedkar Institute of Technology, India</u>
            **Bachelor of Engineering in Computer Science**  
            *Aug 2016 - Sept 2020*
            """, unsafe_allow_html=True
        )
# Skills Section with Organized Headings and Icons
    st.subheader("Technical Skills")
# Big Data and Analytics
    st.write("**Big Data and Analytics:**")
    st.markdown(
        """
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 20px;">
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg" width="50">
            <p>Apache Spark</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Kubernetes_logo_without_workmark.svg/926px-Kubernetes_logo_without_workmark.svg.png" width="50">
            <p>Kubernetes</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Hadoop_logo_new.svg" width="50">
            <p>Hadoop</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Cassandra_logo.svg" width="50">
            <p>Apache Cassandra</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Machine Learning and AI
    st.write("**Machine Learning and AI:**")
    st.markdown(
            """
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 20px;">
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Keras_logo.svg" width="50">
            <p>Keras</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/TensorFlow_logo.svg" width="50">
            <p>TensorFlow</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="50">
            <p>Scikit-Learn</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg" width="50">
            <p>PyTorch</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Databases and Data Engineering
    st.write("**Databases and Data Engineering:**")
    st.markdown(
        """
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 20px;">
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/en/d/dd/MySQL_logo.svg" width="50">
            <p>MySQL</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" width="50">
            <p>Snowflake</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/Sql_data_base_with_logo.svg" width="50">
            <p>SQL</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )

# Financial Terminals
    st.write("**Financial Terminals:**")
    st.markdown(
        """
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 20px;">
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Bloomberg_logo.svg" width="50">
            <p>Bloomberg Terminal</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/67/Morningstar_Logo.svg" width="50">
            <p>Morning Star</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/Refintiv_Logo.svg" width="50">
            <p>Refinitiv</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Polygon_Blockchain_Matic_Logo.svg" width="50">
            <p>Polygon</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )

# Programming Languages
    st.write("**Programming Languages:**")
    st.markdown(
        """
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 20px;">
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="50">
            <p>Python</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/18/C_Programming_Language.svg" width="50">
            <p>C++</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg" width="50">
            <p>R</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" width="50">
            <p>MATLAB</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Java_Logo.svg" width="50">
            <p>Java</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )

# Cloud Computing
    st.write("**Cloud Computing:**")
    st.markdown(
        """
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 20px;">
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" width="50">
            <p>AWS</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/Microsoft_Azure_Logo.svg" width="50">
            <p>Microsoft Azure</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Docker_%28container_engine%29_logo.svg" width="50">
            <p>Docker</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )


def education():
    st.title("Education", anchor="education")
    
    # Lehigh University
    st.write("### Lehigh University, United States")
    lehigh_logo_url = "https://collegeaim.org/wp-content/uploads/2021/08/Lehigh-University-logo.png"
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <img src="{lehigh_logo_url}" width="50" style="margin-right: 10px;">
            <span><strong>MS Financial Engineering</strong> (Aug 2023 - May 2025)</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


    # Dr. Ambedkar Institute of Technology
    st.write("### Dr. Ambedkar Institute of Technology, India")
    ambedkar_logo_url = "https://www.getmycollege.com/image-upload/new-uploads/college/logo/dr-ambedkar-institute-of-technology-logo-406.jpg"
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <img src="{ambedkar_logo_url}" width="50" style="margin-right: 10px;">
            <span><strong>Bachelor of Engineering in Computer Science</strong> (Aug 2016 - Sept 2020)</span>
        </div>
        """,
        unsafe_allow_html=True,
    )



def professional_experience():
    st.title("Professional Experience", anchor="professional-experience")
    
    with st.expander("Trade Terminal, San Jose, \n United States"):
        st.write("**Quantitative Research Intern**  \n_May 2024 - Present_")
        st.write("- Engineered a real-time NLP model for Reddit sentiment analysis to predict Binance listings using random classification and K-Means clustering, tracking 4000 crypto pairs across 70 exchanges by analyzing volume, market cap, and key metrics.")
        st.write("- Implemented and managed cross-asset volatility arbitrage strategies on perpetual and expiry futures contracts by conducting regression and detailed statistical analysis, generating trading signals on a minute-by-minute timeframe with a hit ratio of 67%.")
        st.write("- Analyzed order book structure and market microstructure using Kalman-Filtering to improve order execution in different liquidity environments, achieving 15% better trade settlement, reducing execution costs and slippage.")
        st.write("- Prototyped, optimized, and executed trading strategy over $200K in order volume, enhancing profitability with walk-forward & Bayesian techniques.")

    with st.expander("Lehigh University, United States"):
        st.write("**Graduate Research Assistant**  \n_Jan 2024 - Present_")
        st.write("- Designed and implemented Vasicek and CIR models focusing on their stochastic process assumption and mean-reverting process using Python, conducting MLE-based parameter estimation, sensitivity analysis, and stress-testing for robust predictive power.")
        st.write("- Extracted, transformed, loaded (ETL) 30 years of FED Federal Open Market Committee (FOMC) data using Ray Dalio’s framework, employing ChatGPT API and advanced prompt engineering to classify data into regimes and assign sentiment scores based on market impact.")
        st.write("- Quantified FOMC sentiment with weighted scores, evaluating policy influence on sectors to drive portfolio adjustments, optimize allocation, and improve risk management.")

    with st.expander("HTTS - High Tech Trading System Fund, Switzerland and India"):
        st.write("**Quantitative Research Analyst**  \n_Aug 2022 - Aug 2023_")
        st.write("- Developed multi-threaded data ingestion pipelines for 5,000+ equity assets, achieving 5x faster database updates. Automated daily reporting and built a visualization dashboard for 21 KPIs, aiding portfolio analysis and decision-making.")
        st.write("- Collaborated with portfolio managers to develop risk management frameworks, and implemented dynamic Value at Risk (VaR), reducing attributed capital by 4% across confidence intervals (95%, 99%) and time horizons (1-day, 10-day).")
        st.write("- Contributed to the development of in-house backtesting platform and trading infrastructure, debugging critical features supporting live trading operations.")
        st.write("- Applied Monte Carlo simulations and hierarchical risk parity for return forecasts to develop diversified portfolios, surpassing the S&P 500’s quarterly performance by 2% without relying on mean-variance optimization.")

    with st.expander("Algorithma, Bangalore, India"):
        st.write("**Quantitative Research Analyst**  \n_Aug 2022 - Aug 2023_")
        st.write("- Developed Python-based FIX protocol and AWS ELT data pipelines to enhance order flow and automate data management.")
        st.write("- Designed and backtested 0-DTE algorithmic trading strategies on major Indian equity indices using position sizing, technical indicators, and stop-loss strategies, reducing capital exposure by 30% and boosting profitability by 15%.")
        st.write("- Engineered a real-time monitoring system using statistical analysis of unusual volume spikes, momentum shifts, and price patterns. Reduced drawdowns by 20% through optimized strike price selection and refined entry timing.")

    with st.expander("Finominal, London (FinTech, Investment Research Tools)"):
        st.write("**Quantitative Research Analyst**  \n_Aug 2022 - Aug 2023_")
        st.write("- Communicated closely with the stakeholders performing Market Research to conduct a peer review analysis on novel ETFs and Mutual Funds in the market based on the FAMA-French model and 11 different metrics.")
        st.write("- Developed a Volatility Optimizer tool that generates optimal portfolio weights based on targeted volatility and Sharpe ratio using mean-variance optimization, used to manage over 14 portfolios, improving risk management.")
        st.write("- Formulated an Inflation Hedger tool using Thiel-Sen and OLS models to identify high inflation-beta assets among 20,000 tickers, optimizing portfolio exposure to inflation and enhancing risk-adjusted returns while reducing volatility.")


# Projects Section

def projects():
    st.title("Latest Works", anchor="projects")
    
    # Project 1
    st.markdown("#### Visualisation and evaluation of Pricing Models")
    col1, col2 = st.columns([2, 1])  # Adjust column ratios as needed
    
    with col1:
        st.write("""
This project is designed to provide an interactive web application for option pricing, option Greek visualization, 
and asset price simulation. The platform leverages various option pricing models, including Black-Scholes, Monte Carlo Simulation, and Binomial Tree methods, to simulate and price financial derivatives like options.

The application also provides a dynamic and interactive visualization of option Greeks, enabling users to understand how key 
parameters like Delta, Gamma, Theta, Vega, and others evolve with respect to changes in underlying asset prices.
        """)
        st.markdown(
            """
            <a href="https://github.com/kushalgowdagv/Pricing_Models" target="_blank" style="
                display: inline-block;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                color: #E63946;
                border: 2px solid #E63946;
                border-radius: 25px;
                text-decoration: none;
            ">GitHub</a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <a href="https://kushalgowdagv-pricing-models-streamlit-app-ucutms.streamlit.app/" target="_blank" style="
                display: inline-block;
                margin-top: 10px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                color: #457B9D;
                border: 2px solid #457B9D;
                border-radius: 25px;
                text-decoration: none;
            ">Visit Website</a>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        # Replace 'image_path' with your image file or a placeholder URL
        image_path = "https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/Binomial_tree_Forecasting.jpg"  # Ensure the file is correctly referenced in your directory
        st.image(image_path, use_column_width=True)

    # Add spacing for better readability
    st.markdown("<br>", unsafe_allow_html=True)

    # Project 2
    st.markdown("#### FAMA French Modelling")
    col1, col2 = st.columns([2, 1])  # Adjust column ratios as needed
    
    with col1:
        st.write("""
This project develops a fundamental factor model using ten factors:
 20-Day ADV, Growth, Volatility, Profitability, Dividend Yield, Value, Market Sensitivity, Medium-Term Momentum, Short-Term Momentum, and Liquidity.
 The model aims to capture changing market conditions and improve portfolio efficiency.
        """)
        st.markdown(
            """
            <a href="https://github.com/kushalgowdagv/FAMA_Factors_modelling" target="_blank" style="
                display: inline-block;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                color: #E63946;
                border: 2px solid #E63946;
                border-radius: 25px;
                text-decoration: none;
            ">GitHub</a>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        # Replace 'image_path' with your image file or a placeholder URL
        image_path = "https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/Fama_french_model.jpg"  # Ensure the file is correctly referenced in your directory
        st.image(image_path, use_column_width=True)

    # Add spacing for better readability
    st.markdown("<br>", unsafe_allow_html=True)
   
    # Project 3
    st.markdown("#### FedGPT - LLM Based Analysis of FOMC Releases")
    col1, col2 = st.columns([2, 1])  # Adjust column ratios as needed
    
    with col1:
        st.write("""
This project, titled "Fed-GPT: Translating Fedspeak," focuses on analyzing Federal Reserve communications through sentiment scoring and advanced language model techniques.
 It provides insights into economic indicators, sentiment correlations, and actionable strategies for financial analysis.
        """)
        st.markdown(
            """
            <a href="https://github.com/kushalgowdagv/FedGPT---LLM-Based-Analysis-of-FOMC-Releases/blob/main/FedGPT.pptx" target="_blank" style="
                display: inline-block;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                color: #E63946;
                border: 2px solid #E63946;
                border-radius: 25px;
                text-decoration: none;
            ">GitHub</a>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        # Replace 'image_path' with your image file or a placeholder URL
        image_path = "https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/Fama_french_model.jpg"  # Ensure the file is correctly referenced in your directory
        st.image(image_path, use_column_width=True)

    # Add spacing for better readability
    st.markdown("<br>", unsafe_allow_html=True)

    # Project 4
    st.markdown("#### Portfolio Optimization")
    col1, col2 = st.columns([2, 1])  # Adjust column ratios as needed
    
    with col1:
        st.write("""
This Project provides a comprehensive guide to download historical stock data, analyze trends, and optimize investment portfolios using Python. Key features include data visualization, statistical analysis, and portfolio optimization with efficient frontier, Sharpe Ratio, and VaR.
 Fully customizable for tickers and date ranges, it's ideal for financial research and decision-making.
        """)
        st.markdown(
            """
            <a href="https://github.com/kushalgowdagv/Portfolio_Optimization" target="_blank" style="
                display: inline-block;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                color: #E63946;
                border: 2px solid #E63946;
                border-radius: 25px;
                text-decoration: none;
            ">GitHub</a>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        # Replace 'image_path' with your image file or a placeholder URL
        image_path = "https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/Portfolio_Oprimization.jpg"  # Ensure the file is correctly referenced in your directory
        st.image(image_path, use_column_width=True)

    # Add spacing for better readability
    st.markdown("<br>", unsafe_allow_html=True)




# Certifications Section
def certifications():
    st.title("Certifications", anchor="certifications")
    st.markdown(
        """
        - [Chartered Financial Analyst (CFA) Level 2](https://www.cfainstitute.org/en/programs/cfa)
        - [EPAT (Algo Trading) from QuantInsti](https://certificates.quantinsti.com/530928df-d2b8-4d54-a012-6fe3e88d1620?key=987f968a891148f7255b6a0c7c53238d592b9e0387af1c1880d607a1d453b6af)
        - [Machine Learning Scientist from DataCamp](https://www.datacamp.com/statement-of-accomplishment/track/8f59e3375605cd06e0e0696942bfd90e0d208467?raw=1)
        - [Data Scientist from DataCamp](https://www.datacamp.com/statement-of-accomplishment/track/5ced062426634ec74621ea03b54bd94a7b7a8329?raw=1)
        - [Applied Finance](https://www.datacamp.com/completed/statement-of-accomplishment/track/cb86389e8984562d8c92f1435d0bc09e8bb23d22)
        - [Options 101 from Akuna Capital](https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/download.jpeg)
        - [Options 201 from Akuna Capital](https://raw.githubusercontent.com/kushalgowdagv/Kushal_Portfolio/main/images/1701212815179.jpg)
        - [Financial markets from Yale University](https://www.coursera.org/account/accomplishments/verify/GSBJPGB8QP2U?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course)
        - [Bloomberg Market Concepts](https://portal.bloombergforeducation.com/certificates/NstRvdswhPocLdynjmR5jfNp)
        """,
        unsafe_allow_html=True
    )


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

def contact_me():
    st.markdown(
        """
        <h1 style="text-align: center; margin-top: 20px;">Contact Me</h1>

        <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
            <a href="https://github.com/kushalgowdagv" target="_blank" style="margin-right: 15px;">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" title="GitHub">
            </a>
            <a href="mailto:kushalgowdagv@gmail.com" target="_blank" style="margin-right: 15px;">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="40" title="Email">
            </a>
            <a href="https://www.linkedin.com/in/kushalgowdagv/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40" title="LinkedIn">
            </a>
        </div>
        <p style="text-align: center; font-size: 16px; margin-top: 10px;">Feel free to connect with me on any of the platforms above!</p>
        """,
        unsafe_allow_html=True
    )

# Call the Contact Me Section at the end of your app



# Display the sections based on anchor
about_me()
education()
professional_experience()
projects()
certifications()
extracurricular()
contact_me()


# Contact Me Section

