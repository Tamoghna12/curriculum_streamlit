import streamlit as st
from PIL import Image

with open("cv-app/resume-app-main/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Tamoghna Das, M.Sc.
##### *Curriculum Vitae* 
''')

image = Image.open('dp2.png')
st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Passionate about the **bio-based economy** and application of **data analytics** in the domain of **synthetic Biology.**  
- Interested to work in the interface of **science**, **analytics**, and **data**.
- Involved in **teaching** and **developing** learning contents to enhance skill sets of **students** and young professionals.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #303f9f;">
  <a class="navbar-brand" href=" https://www.linkedin.com/in/tamoghnadas12/" target="_blank">Tamoghna Das</a>
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
    col1, col2 = st.columns([4, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
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

txt('**Master of Science(M.Sc)** (Data Science),  *UEA (University of East Anglia)*, UK',
    '2021-2022')
st.markdown('''
- Modules : Statistics, Data Mining, Information Visualization, Human Computer interaction, Research Techniques, Artificial Intelligence
- Grade: `Merit expected`
- **Research thesis entitled:** `Making shotgun metagenomics accessible, which aims to reconstruct all the genomes present in an environmental sample, such as soil or water`.
''')
txt('**Master of Science(M.Sc)** (Biochemical Engineering),  *UCL (University College London)*, UK',
    '2018-2019')
st.markdown('''
- Modules: Vaccine bioprocessing, Bioprocess Systems Engineering, Industrial Synthetic Biology, Sustainable industrial Bioprocesses and Biorefineries
- Grade: `Merit`
- **Research thesis entitled:** `Towards an engineered E. coli cell capable of inducible filamentation to improve primary recovery of biological products.`.
''')

txt('**Bachelors of Technology(B.Tech)** (Biotechnology:), *VIT (Vellore Institute of Technology)*, India',
    '2014-2018')
st.markdown('''
- Major Modules: Biochemistry, Cell Biology & Genetics, Bioinformatics, Systems Biology, Genomics & Proteomics, Industrial biotechnology, Pharmaceutical biotechnology
- CGPA: `3.31/4.00` `(8.27/10.0)`
- **Bachelor Thesis:** Effects of P25 TiO2 nanoparticles on Moina macrocopa by feed-based exposure under different conditions (UV-A and Dark)
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Content Developer (English) for GCSE Physics:**, StudySmarter.de, Munich, Germany', 'Feb 2022-Present')
st.markdown('''
- **Developed** curated content for students to facilitate easy understanding of critical concepts (`2` per week)
- **Performed** SEO analysis on the platform for better reach.
- **Created** and customized flashcards (`100+`) for self-assessment and conceptual understanding
- Worked remotely for the entire period
''')

txt('**Course organizer & Tutor in-Charge:**, Stoodnt.com, Kolkata, India',
    'May 2021-Aug 2021')
st.markdown('''
- **Developed**, planned the curriculum and taught a course on the application of data science concepts in biotechnology using Python.
- **Counselled** high school and college level students in analytical skills and soft skills' enhancement.
- **Taught** `20 +` students and received a variety of constructive feedbacks from students.
- **Developed** study materials for students to practice.
- **Conceptualized** and published a content on carrier transition from biology to data science.
- **Worked remotely** for the entire period
''')
txt('**Scientific Content Editor:**, *Klarity. Health:* , London ,UK',
    'Feb 2022 - Present')
st.markdown('''
- **Edited** scientific contents on health and wellbeing (`10 +`)
- **Analysed** the content for grammatical and scientific errors
- **Suggested** possible routes for better precision and conciseness
- **Worked remotely** for the entire period as a voluntary internship
''')
txt('**Research Assistant :**, *Indian Institute of Science (IISc)* , Bangalore, India',
    'Jan. 2020 - Aug 2020')
st.markdown('''
- **Developed** and **evaluated** a mathematical model of cancerous cell behaviour using Boolean approach and statistical methods and interpretation of the data obtained.
- The project involved the use of data analysis using **Python libraries** (such as *pandas* and *Matplotlib*)
- Furthermore, this project involved the use of statistical understanding for interpreting the *biological data*
''')
txt('**Teacher and Evaluator:**, *Oxford Royale Academy (ORA):* , Cambridge University,UK ', 'Jul 2018')
st.markdown('''
- **Taught** pre-university students a course titled “Engineering Preparations”. Responsibilities included content delivery andcoursework evaluation with feedbacks
- **Guided** students with mock interview session for to enhance communication skills
- Familiarized the students in undergraduate college admission process
''')
txt('**Research Internship:**, *Indian Institute of Science Education and Research, Kolkata (IISER-K):* , Kolkata, India', 'Jun - Jul 2017')
st.markdown('''
- microRna target prediction in plants using computational methods, the work comprised of understanding the different types of microRna prediction tools 
  and how those are used in the context of analysis of Argonaute protein in plants during the process of induced stress.
''')
txt('**Research Internship:**, *West Bengal University of Animal and Health Sciences (WBUAFS):* , Kolkata, India', 'May - Jun 2017')
st.markdown('''
- Protein purification from blood samples of diseased animals and their spectrophotometric Analysis.
''')
txt('**Industrial Internship:**, *Indian Immunologicals Limited:* , Hyderabad, India', 'Dec 2016')
st.markdown('''
- Microbiological analysis of water samples from different production blocks.
''')

#####################
st.markdown('''
## Honours & Awards
''')
txt4('Imagine IF Bangladesh cohort', 'secured a 3rd position', '2021')
txt4('The Ginkgo Bioworks Challenge',
     'Winner among the past and present iGEMers globally', '2020')
txt4('iGEM EPIC fast track program',
     'Selected in Top 10 best project for immediate funding', '2020')
txt4('Cleveland Medical Hackathon Cleveland',
     'Selected based on proposal', '2017')
txt4('2018 ICID Hackathon', 'Selected based on proposal', '2017')
txt4('VITTBI (Technology Business Incubate cell) - Medical device prototype',
     'Approval of funds', '2017')
txt4('Chem-a-Thon (Chemical-Hack)', 'Winner', '2016')
txt4('Bio-Inspired Design: Summer fest 16', 'Winner', '2016')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization',
     '`matplotlib`, `seaborn`, `plotly`, `highcharts.js`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`JavaScript`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `R Shiny`, `Heroku`')

#####################
st.markdown('''
## References
##### Available on request
''')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://wwww.linkedin.com/in/tamoghnadas12/')
txt2('Twitter', 'https://twitter.com/TamoghnaDas12')
txt2('GitHub', 'https://github.com/Tamoghna12')
txt2('Medium', 'https://medium.com/@tamoghnadas.12')
