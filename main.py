
import streamlit as st
from PIL import Image
import requests
#--from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon= ":tada:", layout="wide")

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code  != 200:
        return None
    return r.json()




#---load assets---
lottie_coding = ("https://assets1.lottiefiles.com/packages/lf20_3rwasyjy.json")


# ----header section-----
with st.container():
    st.subheader("Hi, I am Ishan :wave:")
    st.title("Lead Business/Data Analyst")
    st.write("ishan.kalele@gmail.com")
    st.write("Lead Business/Data analyst posessing solid understanding of business analysis fundamentals and substantial exposure in analytics front. I have worked in multiple domains and hold decent knowledge of payment messages, US Mortgage/Lending process & Travel Distributions domain")


#---what i do---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write('##')
        st.info("""

            - I work closely with the Product Managers & Go-To Market Teams to understand the customer demand for new features & assists the Product managers in prioritizing the product roadmap and in formulation of user stories
            - I play a pivotal role in solution development/definition  and prepare high level design documents
            - I build dashboards and perform adhoc reporting/analysis on the data extracted from different RDBMS by leveraging Tableau/Power BI and share the reports with Customers/Stakeholders
            - I do Exploratory data analysis on the data extracted from various different sources and build Machine Learning models
            """
        )
#Custom Function for printing text
def txt(a,b):
    col1, col2 = st.columns([4,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt3(a,b):
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

st.markdown('''
## Skills & Tools
''')
txt3('Data Processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data Visualization', '`matplotlib`, `seaborn`, `plotly`, `Tableau`, `Power BI`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Model depoloyment', '`streamlit`, `Heroku`, `Azure`')
txt3('Project Methodologies', '`Waterfall`, `Agile-Scrum`')
txt3('Tools', '`Swagger`, `FastAPI`, `GIT`, `JIRA`, `Linux`, `Jenkins`, `Postman`, `Advanced MS Excel (Macros & Google Sheets automation)`, `Visio`, `Confluence`,`PostgreSQL`, `SQL Server`')

##################
st.markdown('''
## Work Experience
''')

txt('**Product Definition Analyst**, Amadeus Labs, Bangalore', 'May 2021 to present')
st.markdown('''
- Worked directly with product managers, architects & customers to define features and formulation of technical user stories
- Solution development and design through development and delivery to production
- Defect triaging on the Production incidents and provided support to the Development team in defect resolution
- Experience in extracting, transforming & loading data from spreadsheets, database tables & other sources & performed
exploratory analysis and derived key insights and metrics
- Built Adhoc/On demand dashboards/reports & shared with the Markets/Customers
- Created, documented logical & physical data models and maintained comprehensive documentation for a product
''')
            
txt('**Business Systems Consultant**, Wells Fargo, Bangalore', 'Oct 2018 - May 2021')
st.markdown('''
- Evaluated and prioritized on the Business need and translated them into requirements in conjunction with the US
(States side) counterparts
- Mapped business requirements to technical functional spec document and provided design solution entailing
technical/configuration specifications
- Participated in the redesigning of application and contributed technically & functionally to the new architecture
''')

txt('**Business Analyst**, ITC Infotech, (Bangalore,UK,Saudi Arabia)', 'June2014 - Sept 2018')
st.markdown('''
- Facilitated (JAD) Joint Application Development sessions to identify business rules and requirements and documented them in a format that can be reviewed and understood by both business people and technical folks
- To understand the client’s AS-IS CRM Sales cycle process and come up with a TO-BE functional design solution to cater to the CRM - Client Legacy system integration activity
- Deployment, parameter configuration of the GST application in the client’s environment
- Prioritized on the processing of ISO 20022 standard payment messages based on the In-clearing and Out-Clearing
message structure and Bank’s readiness to process/consume the same
''')
            
st.markdown('**Key Contributions outside project deliverables**')
st.write('''
- Continual interaction with the Business & stakeholders and built interactive dashboards and stories for the customers & presented key business insights/information
- Built a machine learning model (using python) to predict the likelihood/propensity of borrower’s delinquency which assisted the team to earmark the probable defaulters beforehand and revise the workout plans for them
- Performed Exploratory Data Analysis on various real datasets using Python libraries for the data extracted from different systems and provided recommendations by building machine learning models
''')
         
st.markdown('''
### Education
''')

txt('**PGDM** (Marketing & Finance), ISB&M Pune', '2012-14')
txt('**Bachelor of Engineering in Electronics and Communication**, RGTU Bhopal', '2006-10')
         
st.markdown('''
### Leadership & Recognition
''')

st.write('''
- Received Trailblazer award in FY2022-23 at Amadeus Labs for notable improvements in the product
- Handled a team of 8 people including developers, members from implementation team at client location
''')
         






    

    











