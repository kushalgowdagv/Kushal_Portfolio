
import streamlit as st
from PIL import Image
import requests
st.markdown(
    """
    <style>
    /* Set background color to white */
    body {
        background-color: white;
    }

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
        # st.subheader("Resume")
        # resume_url = "https://drive.google.com/file/d/1JOnG4jDvGrL7CskoO7C3PJcAvDn8U0QI/view?usp=sharing"
        # st.markdown(
        #     f"""
        #     <div style="display: flex; justify-content: center; margin-top: 10px;">
        #         <  a href="{resume_url}" target="_blank">
        #             <button style="padding: 10px 20px; font-size: 16px;">Download Resume</button>
        #         </a>
        #     </div>
        #     """,
        #     unsafe_allow_html=True
        # )


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
    # Certifications
    #     st.subheader("Certifications")
    #     st.write("Chartered Financial Analyst (CFA): Level 2 Passed")
    #     st.write("Certifications in Algo Trading (EPAT), Data Science (DataCamp), and more.")
    
    # # Education Section
    #     st.subheader("Education")
    #     st.write("**Lehigh University, United States**")
    #     st.write("M.S. in Financial Engineering (Aug 2023 - May 2025)")
    
    #     st.write("**Dr. Ambedkar Institute of Technology, India**")
    #     st.write("Bachelor of Engineering in Computer Science (Aug 2016 - Sept 2020)")

        # Updated Certification and Education Content
        st.markdown(
            """
            **Kushal Gowda** is a **Quantitative Researcher** and **Developer** with hands-on expertise in **quantitative trading**, **algorithmic strategies**, and **risk management**. 
            He brings a solid background in **statistical arbitrage**, **NLP sentiment analysis**, and **market risk modeling** from his recent work as a **Quantitative Research Intern** .

            Kushal is currently pursuing a **Master’s in Financial Engineering** at **Lehigh University** and **Chartered Financial Analyst (CFA)** Level III Candidate, specializing in **derivatives pricing**, **stochastic processes**, and **portfolio optimization**.
            His professional journey includes notable roles at institutions like **HTTS - High Tech Trading System Fund** and **Finominal**, focusing on **equity portfolio optimization**, **dynamic VaR implementations**, 
            and the development of **volatility-optimized tools**.

            With a technical foundation in **Python**, **C++**, **SQL**, and various **trading platforms**, he has executed sophisticated **quantitative strategies** and **risk analysis frameworks** to enhance **profitability** 
            and **portfolio resilience**.

            Beyond finance, Kushal holds certifications in **algorithmic trading**, **data science**, and **machine learning**. His educational background in **Computer Science** from 
            **Dr. Ambedkar Institute of Technology** further supports his diverse technical capabilities. Eager to innovate in the quantitative finance domain, 
            Kushal combines his passion for **technology** with an **analytical approach** to deliver impactful solutions.
            """,
            unsafe_allow_html=True
        )

# Skills Section with Organized Headings and Icons
        st.subheader("Technical Skills")

# Big Data and Analytics
        st.write("**Big Data and Analytics:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg" width="50" style="margin: 0 20px;"> Big Data Analytics
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Kubernetes_logo_without_workmark.svg/926px-Kubernetes_logo_without_workmark.svg.png" width="50" style="margin: 0 20px;"> Kubernetes
                <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Hadoop_logo_new.svg" width="50" style="margin: 0 20px;"> Hadoop
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Cassandra_logo.svg" width="50" style="margin: 0 20px;"> Apache Cassandra
            </div>
            """,
            unsafe_allow_html=True
        )

# # High Performance Computing (HPC) and Quantification
#         st.write("**High Performance Computing (HPC) and Quantification:**")
#         st.markdown(
#             """
#             <div style="display: flex; align-items: center;">
#                 <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/Intel_HPC_logo.svg" width="30" style="margin: 0 10px;"> HPC
#                 <img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/Quantitative_analysis_icon.svg" width="30" style="margin: 0 10px;"> Quantification
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# Machine Learning and AI
        st.write("**Machine Learning and AI:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Keras_logo.svg" width="50" style="margin: 0 20px;"> Keras
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/TensorFlow_logo.svg" width="50" style="margin: 0 20px;"> TensorFlow
                <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="50" style="margin: 0 20px;"> Scikit-Learn
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg" width="50" style="margin: 0 20px;"> PyTorch
            </div>
            """,
            unsafe_allow_html=True
        )

# Databases and Data Engineering
        st.write("**Databases and Data Engineering:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/en/d/dd/MySQL_logo.svg" width="50" style="margin: 0 20px;"> MySQL
                <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" width="50" style="margin: 0 20px;"> Snowflake
                <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/Sql_data_base_with_logo.svg" width="50" style="margin: 0 20px;"> SQL
            </div>
            """,
            unsafe_allow_html=True
        )

# Quantitative Finance and Financial Modeling
        st.write("**Financial Terminals:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Bloomberg_logo.svg" width="50" style="margin: 0 20px;"> Bloomberg Terminal
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/67/Morningstar_Logo.svg" width="50" style="margin: 0 20px;"> Morning Star
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/Refintiv_Logo.svg" width="50" style="margin: 0 20px;"> Rifinitiv
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Polygon_Blockchain_Matic_Logo.svg" width="50" style="margin: 0 20px;"> Polygon

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("**Brokers:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/Interactive_Brokers_Logo_%282014%29.svg" width="50" style="margin: 0 20px;"> Interactive Broker
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Coinbase.svg" width="50" style="margin: 0 20px;"> Coinbase
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Binance_logo.svg" width="50" style="margin: 0 20px;"> Binance
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/9d/Zerodha_logo.svg" width="50" style="margin: 0 20px;"> Zerodha

            </div>
            """,
            unsafe_allow_html=True
        )


    # Programming Languages
        st.write("**Programming Languages:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="50" style="margin: 0 20px;"> Python
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/18/C_Programming_Language.svg" width="50" style="margin: 0 20px;"> C++
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg" width="50" style="margin: 0 20px;"> R
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" width="50" style="margin: 0 20px;"> MATLAB
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Java_Logo.svg" width="50" style="margin: 0 20px;"> Java
            </div>
            """,
            unsafe_allow_html=True
        )

# Cloud Computing
        st.write("**Cloud Computing:**")
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" width="50" style="margin: 0 20px;"> AWS
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/Microsoft_Azure_Logo.svg" width="50" style="margin: 0 20px;"> Azure 
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Docker_%28container_engine%29_logo.svg" width="50" style="margin: 0 20px;"> Docker 
            </div>
            """,
            unsafe_allow_html=True
        )


# Education Section
# def education():
#     st.title("Education", anchor="education")
#     st.write("### Lehigh University, United States")
#     st.write("**MS Financial Engineering** (Aug 2023 - May 2025)")
#     st.write("- Financial Derivatives, Financial Engineering Practicum, Quantitative Risk Management, etc.")
    
#     st.write("### Dr. Ambedkar Institute of Technology, India")
#     st.write("**Bachelor of Engineering in Computer Science** (Aug 2016 - Sept 2020)")
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
        <ul>
            <li>Financial Derivatives</li>
            <li>Financial Engineering Practicum</li>
            <li>Quantitative Risk Management</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("[View GitHub Projects](https://github.com/kushalgowdagv)")

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
    st.markdown("[View GitHub Projects](https://github.com/kushalgowdagv)")



def professional_experience():
    st.title("Professional Experience", anchor="professional-experience")
    
    with st.expander("Trade Terminal, San Jose, United States - Quantitative Research Intern (May 2024 - Present)"):
        st.write("- Engineered a real-time NLP model for Reddit sentiment analysis to predict Binance listings using random classification and K-Means clustering, tracking 4000 crypto pairs across 70 exchanges by analyzing volume, market cap, and key metrics.")
        st.write("- Implemented and managed cross-asset volatility arbitrage strategies on perpetual and expiry futures contracts by conducting regression and detailed statistical analysis, generating trading signals on a minute-by-minute timeframe with a hit ratio of 67%.")
        st.write("- Analyzed order book structure and market microstructure using Kalman-Filtering to improve order execution in different liquidity environments, achieving 15% better trade settlement, reducing execution costs and slippage.")
        st.write("- Prototyped, optimized, and executed trading strategy over $200K in order volume, enhancing profitability with walk-forward & Bayesian techniques.")

    with st.expander("Lehigh University, United States - Graduate Research Assistant (Jan 2024 - Present)"):
        st.write("- Designed and implemented Vasicek and CIR models focusing on their stochastic process assumption and mean-reverting process using Python, conducting MLE-based parameter estimation, sensitivity analysis, and stress-testing for robust predictive power.")
        st.write("- Extracted, transformed, loaded (ETL) 30 years of FED Federal Open Market Committee (FOMC) data using Ray Dalio’s framework, employing ChatGPT API and advanced prompt engineering to classify data into regimes and assign sentiment scores based on market impact.")
        st.write("- Quantified FOMC sentiment with weighted scores, evaluating policy influence on sectors to drive portfolio adjustments, optimize allocation, and improve risk management.")

    with st.expander("HTTS - High Tech Trading System Fund, Switzerland and India - Quantitative Research Analyst (Aug 2022 - Aug 2023)"):
        st.write("- Developed multi-threaded data ingestion pipelines for 5,000+ equity assets, achieving 5x faster database updates. Automated daily reporting and built a visualization dashboard for 21 KPIs, aiding portfolio analysis and decision-making.")
        st.write("- Collaborated with portfolio managers to develop risk management frameworks, and implemented dynamic Value at Risk (VaR), reducing attributed capital by 4% across confidence intervals (95%, 99%) and time horizons (1-day, 10-day).")
        st.write("- Contributed to the development of in-house backtesting platform and trading infrastructure, debugging critical features supporting live trading operations.")
        st.write("- Applied Monte Carlo simulations and hierarchical risk parity for return forecasts to develop diversified portfolios, surpassing the S&P 500’s quarterly performance by 2% without relying on mean-variance optimization.")

    with st.expander("Algorithma, Bangalore, India - Quantitative Research Analyst (Aug 2022 - Aug 2023)"):
        st.write("- Developed Python-based FIX protocol and AWS ELT data pipelines to enhance order flow and automate data management.")
        st.write("- Designed and backtested 0-DTE algorithmic trading strategies on major Indian equity indices using position sizing, technical indicators, and stop-loss strategies, reducing capital exposure by 30% and boosting profitability by 15%.")
        st.write("- Engineered a real-time monitoring system using statistical analysis of unusual volume spikes, momentum shifts, and price patterns. Reduced drawdowns by 20% through optimized strike price selection and refined entry timing.")

    with st.expander("Finominal, London (FinTech, Investment Research Tools) - Quantitative Research Analyst (Aug 2022 - Aug 2023)"):
        st.write("- Communicated closely with the stakeholders performing Market Research to conduct a peer review analysis on novel ETFs and Mutual Funds in the market based on the FAMA-French model and 11 different metrics.")
        st.write("- Developed a Volatility Optimizer tool that generates optimal portfolio weights based on targeted volatility and Sharpe ratio using mean-variance optimization, used to manage over 14 portfolios, improving risk management.")
        st.write("- Formulated an Inflation Hedger tool using Thiel-Sen and OLS models to identify high inflation-beta assets among 20,000 tickers, optimizing portfolio exposure to inflation and enhancing risk-adjusted returns while reducing volatility.")
# Projects Section
# def projects():
    # st.title("Projects", anchor="projects")
    # st.write("### Volatility Optimizer Tool")
    # st.write("- Developed a tool to generate optimal portfolio weights based on targeted volatility.")
    # st.write("### Real-time NLP Model")
    # st.write("- Engineered a model for Reddit sentiment analysis to predict Binance listings.")
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
# def certifications():
#     st.title("Certifications", anchor="certifications")
#     st.write("- Chartered Financial Analyst (CFA) Level 2")
#     st.write("- EPAT (Algo Trading) from QuantInsti")
#     st.write("- Data Scientist and Machine Learning Scientist from DataCamp")
#     st.write("- Options 101 and 201 from Akuna Capital")
#     st.write("- Bloomberg Market Concepts")


# Certifications Section
def certifications():
    st.title("Certifications", anchor="certifications")
    st.markdown(
        """
        - [Chartered Financial Analyst (CFA) Level 2](https://www.cfainstitute.org/en/programs/cfa)
        - [EPAT (Algo Trading) from QuantInsti](https://www.quantinsti.com/epat)
        - [Data Scientist and Machine Learning Scientist from DataCamp](https://www.datacamp.com/)
        - [Options 101 and 201 from Akuna Capital](https://akunacapital.com/)
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
