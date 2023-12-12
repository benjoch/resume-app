import streamlit as st
from azure.storage.blob import BlobServiceClient
import base64
import os

def resume_main():
    st.title("Welcome to my Resume")
    st.write("My name is Ben Jochem and I am a Quantitative Finance master's student at Fordham University.")
    st.markdown("""---""")

    st.subheader("Contact Information")
    st.write("Phone: 724-591-4641")
    st.write("Email: bjochem@fordham.edu")
    st.write("LinkedIn: https://www.linkedin.com/in/benjamin-jochem-b71aa0170/")
    st.markdown("""---""")

    # get today's liability data
    # iterate through each existing liability category and get today's value from the user
    st.subheader("Technical Skills")
    st.write('''
• **Python:**  Pandas, NumPy, and scikit-learn for data analysis, financial modeling, and machine learning applications, and Streamlit for building data apps
\n• **C++:**  implemented high-performance asset pricing and risk management models using C++ standard library
\n• **SQL / R:**  for querying and manipulating large financial datasets for statistical analysis
\n• **Machine Learning:**  experienced in developing predictive models (both supervised and unsupervised) for equity selection and market trend analysis
\n• **Finance Theory:**  basic proficiency in asset allocation and portfolio optimization principles, including risk-return trade-off and diversification
\n• **Financial Derivatives:**  understanding of various derivative instruments (options, futures, swaps) and their application in hedging, speculation, and
portfolio management
\n• **Cryptocurrency & Decentralized Finance:**  analyzed and executed yield farming, staking, and arbitrage strategies using DeFi protocols
    ''')

    st.markdown("""---""")

    st.subheader("Education")
    st.write('''
    **FORDHAM UNIVERSITY, GABELLI SCHOOL OF BUSINESS** - MS, Quantitative Finance [2023-Present] \n
• **Planned Courses**: Quantitative Portfolio Management, Systematic Investment Strategies, Risk Management, Computational Finance, Simulation Applications, Advanced Machine Learning, Advanced Derivatives

\n**PENNSYLVANIA STATE UNIVERSITY** - BS, Finance | BS, Statistical Modeling Data Sciences [2018-2022] \n
• **Completed Courses**: Securities Analysis & Portfolio Management, Financial Trading & Applications, Financial Derivatives, Probability Theory, Mathematical Statistics, Computer Science, Machine Learning, Computational Statistics
    ''')

    st.markdown("""---""")

    st.subheader("Work Experience")
    st.write('''
    
    **MESSARI** - Research Analyst (Asset Intelligence) [2022-2023] \n
    • Researched and authored reports detailing the economics, technical specifications, and legal aspects of crypto assets and protocols for institutional asset managers, funds, and exchanges  
    • Automated the Asset Intelligence team's report creation and writing process using Python and crypto data APIs  
    • Facilitated the development and launch of Messari's Diligence Reports product by creating quality and structure standards for amending existing
    reports  
    \n
    **PSU STATISTICAL LEARNING AND DATA MINING LAB** - Undergraduate Research Assistant [2021] \n
    • Developed and published R & Python packages for solving Sparse Principal Component Analysis (AManPG Method)  
    • Presented personal projects and lab research to students and faculty at UC Davis as a National Science Foundation REU Grant recipient''')

    st.markdown("""---""")

    st.subheader("Projects")
    st.write('''
    **TOP-DOWN ML INVESTMENT STRATEGY** [2023-Present]\n
• Formulated a quantitative, machine-learning-based approach for top-down investing focused on sector and equity performance forecasting  
• Researching strategy performance in US public equity markets; analyzing the relative efficacy of different models, features and portfolio
implementation procedures across sectors  
• Leading the project team as a manager responsible for outlining project objectives, assigning tasks, ensuring timely completion, and maintaining
effective communication among team members\n
**DYDX TRADING BOT** [2023-Present] \n
• Developing a trading bot executing a cointegration arbitrage trading strategy on the DyDx decentralized crypto exchange using Python and exchange APIs
AMANPG PYTHON AND R PACKAGES Summer 2021 Undergraduate Research  
• Implemented the Alternating Manifold Primal Gradient Method (AManPG) algorithm in Python and R packages published to PyPI and CRAN  
• Authored official documentation for the R package covering the algorithm's statistical underpinnings, implementation details, and usage guide;
supports package usage for over 200 new downloaders per month\n
**AMANPG PYTHON AND R PACKAGES** [Summer 2021] \n
• Implemented the Alternating Manifold Primal Gradient Method (AManPG) algorithm in Python and R packages published to PyPI and CRAN  
• Authored official documentation for the R package covering the algorithm's statistical underpinnings, implementation details, and usage guide;
supports package usage for over 200 new downloaders per month  
    ''')

    st.markdown("""---""")

    st.subheader("Additional / Awards")
    st.write('''
• National Science Foundation REU Grant (2021)  
• Penn State University Evan Pugh Scholar Senior Award (2021)  
• Penn State University President Sparks Award (2020)  
• Penn State University President's Freshman Award & Freshman Spanish Award (2019)  
• Penn State Dean's List (2018-2022)  
    ''')

def crypto_cointegration():
    st.title("Crypto Cointegration Strategy")

def file_upload():
    st.title("File Upload")
    uploaded_file = st.file_uploader("Choose a file", type="pdf")

    if uploaded_file is not None:
        # Connect to Azure Blob Storage
        # connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        connect_str = "DefaultEndpointsProtocol=https;AccountName=resumefilestorage;AccountKey=92bBa1z2EeTOWcam9DqjjOj4bVzg9sXVVgBTiXLshyBHh9AyjtbcL/30WgKBAdwnVXKD92aMDXKL+AStk/EJpg==;EndpointSuffix=core.windows.net"
        if connect_str is None:
            st.error("Azure Storage connection string not found.")
            return

        # Creating a unique blob name
        blob_name = f"{uploaded_file.name}"

        try:
            # Initialize Blob Service Client
            blob_service_client = BlobServiceClient.from_connection_string(connect_str)
            container_name = "new-container"  # Replace with your container name
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

            # Upload the file
            blob_client.upload_blob(uploaded_file, overwrite=True)
            st.success("File uploaded successfully")

        except Exception as e:
            st.error(f"An error occurred: {e}")

def file_download():
    st.title("File Download")
    st.markdown("""---""")
    st.subheader("Download a file from Azure Blob Storage")

    # Connect to Azure Blob Storage
    connect_str = "DefaultEndpointsProtocol=https;AccountName=resumefilestorage;AccountKey=92bBa1z2EeTOWcam9DqjjOj4bVzg9sXVVgBTiXLshyBHh9AyjtbcL/30WgKBAdwnVXKD92aMDXKL+AStk/EJpg==;EndpointSuffix=core.windows.net"
    if connect_str is None:
        st.error("Azure Storage connection string not found.")
        return

    try:
        # Initialize Blob Service Client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "new-container"  # Replace with your container name

        # Retrieve the list of blobs in the container
        blob_list = blob_service_client.get_container_client(container_name).list_blobs()
        files = [blob.name for blob in blob_list]

        # Dropdown for selecting the file
        selected_file = st.selectbox("Select a file", files)

        if st.button('Download Selected File'):
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=selected_file)

            # Download the file
            stream = blob_client.download_blob()
            file_bytes = stream.readall()

            # Convert the bytes to a base64 string for download
            b64 = base64.b64encode(file_bytes).decode()

            # Create a download link
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="{selected_file}">Click to download file</a>'
            st.markdown(href, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("""---""")
    pages = {
        "Resume": resume_main,
        "Crypto Cointegration Strategy": crypto_cointegration,
        "File Upload": file_upload,
        "File Download": file_download
    }

    page = st.sidebar.selectbox("Choose a page", list(pages.keys()))

    # Call the appropriate function based on the user selection.
    pages[page]()


main()



