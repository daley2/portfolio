import streamlit as st

# PAGE CONFIG
st.set_page_config(page_title="My Portfolio", page_icon="✨", layout="wide")

# CUSTOM CSS
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: white;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: 800;
    background: linear-gradient(90deg, #4f46e5, #9333ea);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 28px;
    color: #444;
    margin-bottom: 40px;
}

/* Section Headers */
.section-header {
    font-size: 40px;
    font-weight: 700;
    color: #4f46e5;
    margin-top: 30px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #4f46e5, #9333ea);
    color: white;
    border: none;
    border-radius: 25px;
    height: 50px;
    width: 150px;
    font-weight: bold;
    font-size: 16px;
    transition: 0.3s ease;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #9333ea, #4f46e5);
    transform: scale(1.05);
}

/* Text styling */
p, li {
    font-size: 20px !important;
    color: #333;
}

/* Image styling */
img {
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.1);
}
            
/* Card Style */
.card {
    background-color: #FDCFFA;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
    transition: all 0.3s ease-in-out;
    border: 2px solid transparent;
}
            
/* Skill Card */
.skill-card {
    background-color: #FDCFFA;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 30px;
    transition: all 0.3s ease-in-out;
    border: 2px solid transparent;
}

.skill-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 35px rgba(79, 70, 229, 0.25);
    border: 2px solid #4f46e5;
}

/* Skill Titles */
.skill-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* Skill Labels */
.skill-label {
    font-size: 20px;
    font-weight: 600;
    margin-top: 15px;
}

/* Hover Effect */
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 35px rgba(79, 70, 229, 0.25);
    border: 2px solid #9333ea;
}
            
.expander {
    background-color: #FDCFFA;
}


</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown('<p class="main-title">✨ My Portfolio ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Aspiring UI/UX Designer</p>', unsafe_allow_html=True)

st.write("")

# NAVIGATION
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    home = st.button("Home")
with col2:
    about = st.button("About Me")
with col3:
    skills = st.button("Skills")
with col4:
    projects = st.button("Projects")
with col5:
    contact = st.button("Contact")

# HOME
if home:
    st.markdown('<p class="section-header">👋 Welcome!</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("2x2.jpg", use_container_width=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="color:#4f46e5; font-size:28px;">✨ About Me</h3>
            <p style="font-size:20px; color:#333;">
            Hi! I'm <b>Dale Christian Fortaleza</b>, a 4th year BSIT student at  
            <b>Cebu Institute of Technology - University</b>.
            <br><br>
            I dream of becoming a professional <b>UI/UX Designer</b> someday.  
            I love creating beautiful, user-friendly, and meaningful digital experiences.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # INTERESTS CARD
        st.markdown("""
        <div class="card">
            <h3 style="color:#9333ea; font-size:28px;">🎨 My Interests</h3>
            <ul style="font-size:20px; color:#333;">
                <li>✨ User Interface Design</li>
                <li>💡 User Experience Research</li>
                <li>🌈 Creative Prototyping</li>
                <li>📱 Web & Mobile Design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ABOUT
if about:
    st.markdown('<p class="section-header">💜 About Me</p>', unsafe_allow_html=True)

    st.markdown("""
        <div class="card">
            <h3 style="color:#4f46e5; font-size:28px;">✨ About Me</h3>
            <p style="font-size:20px; color:#333;">
            I am passionate about design, creativity, and technology.  
        My goal is to design digital products that are not only beautiful  
        but also intuitive and user-centered.

        I believe that good design solves problems and improves lives.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="card">
            <h3 style="color:#4f46e5; font-size:28px;">✨ “Design is not just what it looks like and feels like. Design is how it works.” – Steve Jobs ✨</h3>
        </div>
        """, unsafe_allow_html=True)
# SKILLS
# SKILLS
if skills:
    st.markdown('<p class="section-header">🚀 My Skills</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # DESIGN SKILLS CARD
    with col1:

        st.markdown('<p class="section-header"></p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="skill-card">
            <div class="skill-title" style="color:#9333ea;">🎨 Design Skills</div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="skill-label" style="color:#9333ea;">Figma and Wireframing</div>
        """, unsafe_allow_html=True)

        st.progress(85)

        st.markdown("""
        <div class="skill-label" style="color:#9333ea;">UI Prototyping</div>
        """, unsafe_allow_html=True)
        
        st.progress(80)

        st.markdown("""
        <div class="skill-label" style="color:#9333ea;">User Research</div>
        """, unsafe_allow_html=True)

        st.progress(75)

        st.markdown("</div>", unsafe_allow_html=True)

    # TECHNICAL SKILLS CARD
    with col2:
        st.markdown("""
        <div class="skill-card">
            <div class="skill-title" style="color:#4f46e5;">💻 Technical Skills</div>
            <ul style="font-size:20px; line-height:35px;">
                <li>HTML & CSS</li>
                <li>Python</li>
                <li>Streamlit</li>
                <li>Basic JavaScript</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# PROJECTS
if projects:
    st.markdown('<p class="section-header">📂 My Projects</p>', unsafe_allow_html=True)

    with st.expander("🎨 UI Design Project"):
        st.write("Designed a mobile app prototype using Figma focused on user-friendly navigation.")

    with st.expander("🌐 Portfolio Website"):
        st.write("Built a responsive portfolio using HTML, CSS, and Streamlit.")

    with st.expander("📊 Data Visualization App"):
        st.write("Created a simple dashboard app using Streamlit.")

# CONTACT
if contact:
    st.markdown('<p class="section-header">📬 Contact Me</p>', unsafe_allow_html=True)

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        st.success("Thank you for reaching out! 💌 I will get back to you soon.")

    st.write("📧 Email: dalekim312@email.com")
    st.write("📱 Phone: 09999266697")
