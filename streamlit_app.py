import streamlit as st
from PIL import Image
import pdfkit

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
# Uzair Ahmed, Data Scientist
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

txt('**Master Business Aministration**, *University of Sindh*, Pakistan',
'2011-2013')

txt('**Bachelors of Commerce**, *University of Sindh*, Pakistan',
'2007-2009')

#####################
st.markdown('''
## Work Experience
''')
txt('**AI, ML and Data Analyst/Analytic**, Freelance',
'2021-Present')

st.markdown('''
Results-driven AI, ML, and Data Analyst leveraging technical expertise to drive business growth through data-driven insights.
''')

txt('**Senior Sales Manager**, Teltonika IoT Group , Pakistan',
'2023-Present')

txt('**Logistics / Document Officer**, Sea Prince Logistics (Dubai), Pakistan',
'2021-2023')
txt('**Sales Manager**, Teltonika IoT Group , Pakistan',
'2020-2021')
txt('**Senior Sales Executive**, Cybernet, Pakistan',
'2019-2020')
txt('**Customer Service Representative**, RTA, Dubai',
'2016- 2018')
txt('**Business Development Executive**, Eurostar, Etisalat, Dubai',
'2015-2016')
txt('**Team Lead**, PTCL, Etisalat, Pakistan',
'2011-2015')

#####################
st.markdown('''
## Projects
''')
txt4('Support Ticket', 'Support ticket dashboard design to easily understand resolution time, status, total tickets etc', 'https://support-tickets.streamlit.app/')
txt4('Sales Dashboard', 'Convert excel data into the graphical data, easy to understand and decision making', 'https://sales-dashboard1.streamlit.app/')
txt4('Dashboard', 'Sales progress dashboard to understand monthly, Quarterly and yearly understanding to business growth', 'https://salaes-progress.streamlit.app/')
txt4('Adidas Dashboard', 'This dashboard use to cover the various areas in business and help in getting the strong decision','https://salesdashboard1.streamlit.app/')
txt4('Streamlit Website', 'Website that gives information of business and very attractive', 'https://uzair-resume.streamlit.app/')
txt4('Resume', 'It gives the great look for the resume along with the url to quickly viewable on a click','https://uzair-resume.streamlit.app/')
txt4('Hotel Reservations Analysis', 'Hotel sales reservation cancellation analyze to see from different angles for the reason and to improve it from the raw data', 'https://github.com/uzairrajput100/hotel_sales_analysis')
txt4('Ecommerce Sales Analyss', 'Analyze the increase in the online sales from region, state and city wise to make an decision for starting up business and checked revenue and ROI', 'https://github.com/uzairrajput100/Ecommerce_Sales_Analysis')
txt4('Telecom Churn Ratio Analyze', 'From the raw data of telecom take the analyzation about churn in the region, area, sales, profit and reasons of churning', 'https://github.com/uzairrajput100/Churn_Prediction')
txt4('LinkedIn Message Automation', 'This help in Marketing to automate the LinkedIn messages to particular industry with different messages', 'https://github.com/uzairrajput100/automation')
txt4('AI Attendance Management System', 'System recognize face from CCTV camera and mark employee attendance with the help of computer vision, ML and AI', 'https://github.com/uzairrajput100/AI_attendance')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`, `PyTorch`, `OpenCV`')
txt3('Deep Learning', '`TensorFlow`, `Keras`, `SciPy`')
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

if st.button("Download as PDF"):
    html = st.get_html()
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    pdfkit.from_string(html, "your_resume.pdf", options=options)
