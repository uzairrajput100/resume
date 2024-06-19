import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

background_color = '''
<style>
body {
    background-color: #f0f2f6;
}
</style>
'''

#####################
# Header 
st.write('''
# Uzair Ahmed, Master Business Administration Sales and Data Analyst
##### *Resume* 
''')

image = Image.open('image.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)

st.info('''
- Sales Professional, Data Analyst and Administrator with almost fourteen years of experience in business environment and a passion for delivering insights based on raw data, data cleaning, manipulating, design dashboards and make predictive modeling. 
- Strong track record in research, business growth, utilizing data to bring useful information.
- Strong verbal and written communication skills.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.youtube.com/@SABMIXMASALA" target="_blank">Uzair Ahmed</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master Business Aministration** (Sales), *University of Sindh*, Pakistan',
'2011-2014')

txt('**Bachelors of Commerce** (Finance), *University of Sindh*, Pakistan',
'2008-2010')

#####################
st.markdown('''
## Work Experience
''')
txt('**Data Analyst**, Visualization , Interactive Dashboards, Freelance',
'2021-Present')

txt('**Sales Manager**, Confidential , Pakistan',
'2021-Present')

txt('**Assistant Sales Manager**, Teltonika, Pakistan',
'2012-2021')
txt('**Sales Executive**, Cybernet, Pakistan',
'2019-2021')
txt('**Customer Service Representative**, MEA Resource Solution, Dubai',
'2016- 2018')
txt('**Business Development Executive**, Eurostar, Etisalat, Dubai',
'2015-2016')
txt('**Team Lead**, PTCL, Etisalat, Pakistan',
'2014-2015')
txt('**Sales Executive**, PTCL, Etisalat, Pakistan',
'2011-2013')
st.markdown('''
- Data Mining, Scientific Research and Presentation, Research Methodology, Graduate Seminar, Programming for Health Data Science, etc.
- Provided mentorship and supervision to junior staff, recruiting new employees and managing business growth.
- Acheived individual and team targets by up selling, cross selling to B2B clients.
- Focusing on B2B targets and achieving them by 135% from national and international sales. 
- Sell ERP with source code in 100k USD.
- I worked on smart city project and sell 250 devices which is around 8 Million PKR.
- Worked on govt: and private organization on the project basis to fulfill the M2M requirement.
- Monthly customer subscription above from target achieved around 400k monthly.    
- Focusing on B2B targets and achieving them by 120% from the 2nd month in Dubai with d2d visits and cold calling to clients.
- Earn 5.5k Aed commission monthly apart from salary and generating revenue of up to 55K Aed monthly above from the target.        
- Managing a team of `10` sales executives and interns to ensure KPIs are strategically achieved monthly, quarterly and yearly targets. 
- Actively took part in the talent hiring process as well as train employees with the product and services we are offering.
- Giving services for data analyzing, graphical representations of data, interactive dashboards, websites, mobiles apps, ERP, SaaS and designing.
''')

#####################
st.markdown('''
## Projects
''')
txt4('Support Ticket', 'Support ticket dashboard design to easily understand resolution time, status, total tickets etc', 'https://support-tickets.streamlit.app/')
txt4('Sales Dashboard', 'Convert excel data into the graphical data, easy to understand and decision making', 'https://sales-dashboard1.streamlit.app/')
txt4('Dashboard', 'Sales progress dashboard to understand monthly, Quarterly and yearly understanding to business growth', 'https://salaes-progress.streamlit.app/')
txt4('Adidas Dashboard', 'This dashboard use to cover the various areas in business and help in getting the strong decision','https://salesdashboard1.streamlit.app/')
txt4('Streamlit Website', 'Website that gives information of business and very attractive', 'http://')
txt4('Resume', 'It gives the great look for the resume along with the url to quickly viewable on a click','https://uzair-resume.streamlit.app/')
txt4('Hotel Reservations Analysis', 'Hotel sales reservation cancellation analyze to see from different angles for the reason and to improve it from the raw data', 'https://github.com/uzairrajput100/hotel_sales_analysis')
txt4('Ecommerce Sales Analyss', 'Analyze the increase in the online sales from region, state and city wise to make an decision for starting up business and checked revenue and ROI', 'https://github.com/uzairrajput100/Ecommerce_Sales_Analysis')
txt4('Telecom Churn Ratio Analyze', 'From the raw data of telecom take the analyzation about churn in the region, area, sales, profit and reasons of churning', 'http://')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Heroku`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/uzair-ahmed-630b0a53/')
txt2('GitHub', 'https://github.com/uzairrajput100')
txt2('Email', 'uzairrajput100@gmail.com')
txt2('Phone', '+92-333-6611988')
