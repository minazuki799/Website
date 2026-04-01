import streamlit as st

st.set_page_config(
    page_title="Victor Okosun — Portfolio",
    page_icon="🎵",
    layout="wide"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

/* Global */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Hide default streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hero section */
.hero-container {
    background: linear-gradient(135deg, #0A0A0F 0%, #12121A 50%, #1A1A2E 100%);
    border: 1px solid rgba(200, 169, 126, 0.2);
    border-radius: 20px;
    padding: 60px 40px;
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}

.hero-container::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(200,169,126,0.08) 0%, transparent 70%);
    border-radius: 50%;
}

.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    font-weight: 900;
    color: #E8E8F0;
    line-height: 1.1;
    margin: 0;
}

.hero-title {
    font-size: 1.1rem;
    color: #C8A97E;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin: 12px 0 20px 0;
    font-weight: 300;
}

.hero-description {
    font-size: 1rem;
    color: #9090A8;
    line-height: 1.8;
    max-width: 600px;
}

.gold-divider {
    height: 2px;
    background: linear-gradient(90deg, #C8A97E, transparent);
    border: none;
    margin: 8px 0 20px 0;
    width: 80px;
}

/* Section headers */
.section-header {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #E8E8F0;
    margin-bottom: 4px;
}

.section-sub {
    color: #C8A97E;
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: #12121A;
    border: 1px solid rgba(200, 169, 126, 0.15);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 20px;
    transition: border-color 0.3s;
}

.card:hover {
    border-color: rgba(200, 169, 126, 0.5);
}

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    color: #E8E8F0;
    margin-bottom: 8px;
}

.card-tag {
    display: inline-block;
    background: rgba(200, 169, 126, 0.1);
    color: #C8A97E;
    border: 1px solid rgba(200, 169, 126, 0.3);
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.75rem;
    margin: 3px 3px 10px 0;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.card-text {
    color: #9090A8;
    font-size: 0.9rem;
    line-height: 1.7;
}

/* Skill bars */
.skill-item {
    margin-bottom: 18px;
}

.skill-label {
    display: flex;
    justify-content: space-between;
    color: #E8E8F0;
    font-size: 0.9rem;
    margin-bottom: 6px;
}

.skill-bar-bg {
    background: rgba(200, 169, 126, 0.1);
    border-radius: 10px;
    height: 6px;
    overflow: hidden;
}

.skill-bar-fill {
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #C8A97E, #E8C99E);
}

/* Contact links */
.contact-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(200, 169, 126, 0.08);
    border: 1px solid rgba(200, 169, 126, 0.25);
    color: #C8A97E !important;
    padding: 10px 20px;
    border-radius: 30px;
    text-decoration: none;
    font-size: 0.85rem;
    margin: 6px;
    letter-spacing: 1px;
    transition: background 0.3s;
}

.contact-link:hover {
    background: rgba(200, 169, 126, 0.18);
}

/* Service card */
.service-card {
    background: linear-gradient(135deg, #12121A, #1A1A2E);
    border: 1px solid rgba(200, 169, 126, 0.2);
    border-radius: 16px;
    padding: 32px 24px;
    text-align: center;
    height: 100%;
}

.service-icon {
    font-size: 2.5rem;
    margin-bottom: 16px;
}

.service-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #E8E8F0;
    margin-bottom: 12px;
}

.service-text {
    color: #9090A8;
    font-size: 0.88rem;
    line-height: 1.7;
}

/* Cert badge */
.cert-badge {
    background: linear-gradient(135deg, #12121A, #1A1A2E);
    border: 1px solid rgba(200, 169, 126, 0.3);
    border-radius: 12px;
    padding: 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 14px;
}

.cert-icon {
    font-size: 2rem;
    min-width: 40px;
}

.cert-title {
    color: #E8E8F0;
    font-size: 0.95rem;
    font-weight: 500;
    margin-bottom: 4px;
}

.cert-issuer {
    color: #C8A97E;
    font-size: 0.8rem;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Nav */
.nav-pill {
    display: inline-block;
    padding: 8px 20px;
    border-radius: 30px;
    font-size: 0.85rem;
    cursor: pointer;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Image placeholder */
.profile-frame {
    border: 2px solid rgba(200, 169, 126, 0.4);
    border-radius: 16px;
    overflow: hidden;
    aspect-ratio: 3/4;
    background: linear-gradient(135deg, #12121A, #1A1A2E);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #C8A97E;
    font-size: 4rem;
}
</style>
""", unsafe_allow_html=True)


# ── Sidebar Navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0;'>
        <div style='font-family: Playfair Display, serif; font-size: 1.4rem; color: #E8E8F0;'>Victor Okosun</div>
        <div style='color: #C8A97E; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-top: 4px;'>Portfolio</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "",
        ["🏠 Home", "🎵 Music Portfolio", "🤖 ML Projects", "⚙️ Services", "📬 Contact"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
    <div style='text-align:center; padding: 10px 0;'>
        <a href='https://github.com/minazuki799' target='_blank' class='contact-link'>GitHub</a>
        <a href='https://linkedin.com/in/victor-okosun' target='_blank' class='contact-link'>LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)


# ── HOME PAGE ─────────────────────────────────────────────────────────────────
if page == "🏠 Home":

    # Hero
    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <div class='hero-container'>
            <div class='hero-title'>COMPOSER · ENGINEER · ML DEVELOPER</div>
            <div class='hero-name'>Victor<br>Okosun</div>
            <hr class='gold-divider'>
            <div class='hero-description'>
                A multidisciplinary creative at the intersection of music and machine learning.
                Medical Biochemistry graduate turned ML engineer — composing soundscapes
                and building intelligent systems that make a real difference.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Replace emoji with st.image("your_photo.jpg") when you have a photo
        st.markdown("""
        <div class='profile-frame'>👤</div>
        <div style='text-align:center; color: #9090A8; font-size: 0.8rem; margin-top: 8px;'>
            Replace with your photo using st.image()
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick stats
    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("🎵", "5+", "Years in Music"),
        ("🎬", "50+", "Projects Scored"),
        ("🤖", "3+", "ML Projects"),
        ("🎓", "3", "Certifications"),
    ]
    for col, (icon, num, label) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(f"""
            <div class='card' style='text-align:center;'>
                <div style='font-size:2rem;'>{icon}</div>
                <div style='font-family: Playfair Display, serif; font-size: 2rem; color: #C8A97E;'>{num}</div>
                <div style='color: #9090A8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # About
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class='section-header'>About Me</div>
        <div class='section-sub'>Background & Journey</div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='card-text' style='font-size: 0.95rem; line-height: 1.9;'>
        I hold a BSc in Medical Biochemistry from the University of Benin (2017–2023)
        and have spent years working as a freelance music composer, mixing engineer,
        and audio producer — crafting soundtracks for films, commercials, and artists.<br><br>
        Driven by curiosity, I transitioned into machine learning through self-directed study —
        completing Coursera's Machine Learning Specialization, Harvard's CS50, and building
        production-ready ML projects. I bring a unique perspective that blends scientific
        rigour, creative thinking, and technical engineering.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='section-header'>Skills</div>
        <div class='section-sub'>Technical & Creative</div>
        """, unsafe_allow_html=True)

        skills = [
            ("Python & ML Engineering", 85),
            ("Music Composition", 95),
            ("Mixing & Mastering", 90),
            ("Data Analysis", 80),
            ("Deep Learning", 70),
            ("Audio Engineering", 92),
        ]

        for skill, pct in skills:
            st.markdown(f"""
            <div class='skill-item'>
                <div class='skill-label'>
                    <span>{skill}</span>
                    <span style='color: #C8A97E;'>{pct}%</span>
                </div>
                <div class='skill-bar-bg'>
                    <div class='skill-bar-fill' style='width: {pct}%;'></div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ── MUSIC PORTFOLIO ───────────────────────────────────────────────────────────
elif page == "🎵 Music Portfolio":

    st.markdown("""
    <div class='section-header'>Music Portfolio</div>
    <div class='section-sub'>Compositions · Mixes · Productions</div>
    """, unsafe_allow_html=True)

    st.info("💡 Add your actual audio files using `st.audio()` and replace the placeholder links with your real portfolio links.")

    # Featured work
    st.markdown("### 🎬 Film & Media Scores")
    col1, col2, col3 = st.columns(3)

    music_projects = [
        {
            "title": "Project Title 1",
            "type": "Film Score",
            "description": "Add a description of this project — what it was for, the mood you created, and the tools used.",
            "tags": ["Orchestral", "Film", "Pro Tools"],
            "link": "#"
        },
        {
            "title": "Project Title 2",
            "type": "Commercial Score",
            "description": "Add a description of this project — client name, brief, and your creative approach.",
            "tags": ["Electronic", "Commercial", "Logic Pro"],
            "link": "#"
        },
        {
            "title": "Project Title 3",
            "type": "Artist Production",
            "description": "Add a description — the artist, genre, and your role in the production.",
            "tags": ["Afrobeats", "Production", "Mixing"],
            "link": "#"
        },
    ]

    for col, project in zip([col1, col2, col3], music_projects):
        with col:
            tags_html = "".join([f"<span class='card-tag'>{t}</span>" for t in project['tags']])
            st.markdown(f"""
            <div class='card'>
                <div style='color: #C8A97E; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 6px;'>{project['type']}</div>
                <div class='card-title'>{project['title']}</div>
                {tags_html}
                <div class='card-text'>{project['description']}</div>
                <div style='margin-top: 16px;'>
                    <a href='{project['link']}' style='color: #C8A97E; font-size: 0.85rem; text-decoration: none;'>▶ Listen →</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🎧 Audio Samples")
    st.markdown("""
    <div class='card'>
        <div class='card-title'>Add Your Audio Files</div>
        <div class='card-text'>Use the code below to embed audio players for your tracks:</div>
    </div>
    """, unsafe_allow_html=True)

    st.code("""
# Upload your audio files and use:
st.audio("your_track.mp3")

# Or embed from a URL:
st.audio("https://your-audio-url.com/track.mp3")
    """, language="python")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🛠️ Tools & DAWs")

    tools = ["Pro Tools", "Logic Pro X", "Ableton Live", "Slate Digital", "Native Instruments", "Kontakt", "Spitfire Audio", "iZotope"]
    tags_html = "".join([f"<span class='card-tag'>{t}</span>" for t in tools])
    st.markdown(f"<div style='padding: 10px 0;'>{tags_html}</div>", unsafe_allow_html=True)


# ── ML PROJECTS ───────────────────────────────────────────────────────────────
elif page == "🤖 ML Projects":

    st.markdown("""
    <div class='section-header'>Machine Learning Projects</div>
    <div class='section-sub'>End-to-End ML Applications</div>
    """, unsafe_allow_html=True)

    ml_projects = [
        {
            "title": "Loan Credit Risk Predictor",
            "status": "Live",
            "description": "An end-to-end ML web application that predicts the probability of a loan applicant defaulting. Built with XGBoost, deployed with Streamlit, featuring scenario analysis and feature importance visualization.",
            "tags": ["XGBoost", "Streamlit", "Scikit-learn", "Plotly", "Python"],
            "metrics": [("Accuracy", "90%"), ("ROC AUC", "0.87"), ("Recall", "80%")],
            "github": "https://github.com/minazuki799/Loan_credit_risk",
            "demo": "https://loancreditrisk-kpprxkmo2vyrmjumjukc9t.streamlit.app/"
        },
        {
            "title": "Ames Housing Price Prediction",
            "status": "Complete",
            "description": "Kaggle competition project predicting house prices using a stacking regressor ensemble (XGBoost, SVR, Ridge, LassoCV). Achieved 0.13 RMSE — top competitive performance.",
            "tags": ["Stacking Ensemble", "XGBoost", "Feature Engineering", "Kaggle"],
            "metrics": [("RMSE", "0.13"), ("Model", "Stacking"), ("Features", "80+")],
            "github": "https://github.com/minazuki799/Ames-House-Prices",
            "demo": None
        },
        {
            "title": "Customer Churn Prediction API",
            "status": "Complete",
            "description": "A production-ready churn prediction model served via Flask REST API, containerised with Docker. Includes a full ML pipeline with preprocessing, logistic regression, and Gunicorn deployment.",
            "tags": ["Flask", "Docker", "Logistic Regression", "REST API", "Gunicorn"],
            "metrics": [("Deployment", "Docker"), ("API", "REST"), ("Server", "Gunicorn")],
            "github": "https://github.com/minazuki799/Machine-Learning-Zoomcamp",
            "demo": None
        },
    ]

    for project in ml_projects:
        status_color = "#2ECC71" if project["status"] == "Live" else "#C8A97E"
        tags_html = "".join([f"<span class='card-tag'>{t}</span>" for t in project['tags']])
        metrics_html = "".join([
            f"<div style='text-align:center; padding: 10px; background: rgba(200,169,126,0.08); border-radius: 8px; margin: 4px;'>"
            f"<div style='color: #C8A97E; font-size: 1.1rem; font-weight: 600;'>{v}</div>"
            f"<div style='color: #9090A8; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;'>{k}</div>"
            f"</div>"
            for k, v in project['metrics']
        ])

        demo_btn = f"<a href='{project['demo']}' target='_blank' style='background: #C8A97E; color: #0A0A0F; padding: 8px 16px; border-radius: 20px; text-decoration: none; font-size: 0.8rem; margin-right: 8px;'>🚀 Live Demo</a>" if project['demo'] else ""
        github_btn = f"<a href='{project['github']}' target='_blank' style='border: 1px solid #C8A97E; color: #C8A97E; padding: 8px 16px; border-radius: 20px; text-decoration: none; font-size: 0.8rem;'>📁 GitHub</a>"

        st.markdown(f"""
        <div class='card'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;'>
                <div class='card-title'>{project['title']}</div>
                <div style='color: {status_color}; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase;'>● {project['status']}</div>
            </div>
            {tags_html}
            <div class='card-text' style='margin: 12px 0;'>{project['description']}</div>
            <div style='display: flex; gap: 8px; margin: 16px 0;'>{metrics_html}</div>
            <div style='margin-top: 16px;'>{demo_btn}{github_btn}</div>
        </div>
        """, unsafe_allow_html=True)

    # Certifications
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section-header'>Certifications</div>
    <div class='section-sub'>Verified Credentials</div>
    """, unsafe_allow_html=True)

    certs = [
        ("🎓", "Machine Learning Specialization", "Coursera · DeepLearning.AI — March 2026"),
        ("🏛️", "CS50: Introduction to Computer Science", "HarvardX — October 2025"),
        ("💾", "Introduction to SQL", "HarvardX"),
        ("💻", "Responsive Web Design", "freeCodeCamp — August 2025"),
        ("🎚️", "Audio Engineering Certificate", "Slate Digital — 2019"),
    ]

    for icon, title, issuer in certs:
        st.markdown(f"""
        <div class='cert-badge'>
            <div class='cert-icon'>{icon}</div>
            <div>
                <div class='cert-title'>{title}</div>
                <div class='cert-issuer'>{issuer}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── SERVICES ──────────────────────────────────────────────────────────────────
elif page == "⚙️ Services":

    st.markdown("""
    <div class='section-header'>Services</div>
    <div class='section-sub'>What I Offer</div>
    """, unsafe_allow_html=True)

    # Music services
    st.markdown("### 🎵 Music & Audio Services")
    col1, col2, col3 = st.columns(3)

    music_services = [
        ("🎼", "Film & Media Scoring", "Custom original compositions for films, documentaries, advertisements, and games. Mood-driven, narrative-aware music that elevates your visual content."),
        ("🎚️", "Mixing & Mastering", "Professional mixing and mastering for artists and labels. Clean, balanced mixes delivered to broadcast-ready quality standards."),
        ("🎹", "Music Production", "Full music production from concept to final delivery. Genres including Afrobeats, cinematic, electronic, and contemporary gospel."),
    ]

    for col, (icon, title, text) in zip([col1, col2, col3], music_services):
        with col:
            st.markdown(f"""
            <div class='service-card'>
                <div class='service-icon'>{icon}</div>
                <div class='service-title'>{title}</div>
                <div class='service-text'>{text}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ML services
    st.markdown("### 🤖 Machine Learning Services")
    col1, col2, col3 = st.columns(3)

    ml_services = [
        ("📊", "ML Model Development", "End-to-end machine learning pipeline development — data preprocessing, feature engineering, model training, evaluation, and deployment."),
        ("🌐", "ML Web App Development", "Production-ready ML applications built with Streamlit or Flask. Clean UI, REST APIs, and Docker containerisation included."),
        ("🔍", "Data Analysis & EDA", "Exploratory data analysis, visualisations, and actionable insights from your datasets using Python, Pandas, and Plotly."),
    ]

    for col, (icon, title, text) in zip([col1, col2, col3], ml_services):
        with col:
            st.markdown(f"""
            <div class='service-card'>
                <div class='service-icon'>{icon}</div>
                <div class='service-title'>{title}</div>
                <div class='service-text'>{text}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Tech stack
    st.markdown("### 🛠️ Tech Stack")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>Machine Learning</div>
            <div style='margin-top: 10px;'>
        """, unsafe_allow_html=True)
        ml_tools = ["Python", "Scikit-learn", "XGBoost", "TensorFlow", "Keras", "Pandas", "NumPy", "Plotly", "Streamlit", "Flask", "Docker"]
        tags = "".join([f"<span class='card-tag'>{t}</span>" for t in ml_tools])
        st.markdown(f"{tags}</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>Music & Audio</div>
            <div style='margin-top: 10px;'>
        """, unsafe_allow_html=True)
        audio_tools = ["Pro Tools", "Logic Pro X", "Ableton Live", "Slate Digital", "Kontakt", "Spitfire Audio", "iZotope RX", "Native Instruments"]
        tags = "".join([f"<span class='card-tag'>{t}</span>" for t in audio_tools])
        st.markdown(f"{tags}</div></div>", unsafe_allow_html=True)


# ── CONTACT ───────────────────────────────────────────────────────────────────
elif page == "📬 Contact":

    st.markdown("""
    <div class='section-header'>Get In Touch</div>
    <div class='section-sub'>Let's Work Together</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>Send a Message</div>
        </div>
        """, unsafe_allow_html=True)

        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        service = st.selectbox("I'm interested in:", [
            "Film / Media Scoring",
            "Mixing & Mastering",
            "Music Production",
            "ML Model Development",
            "ML Web Application",
            "Data Analysis",
            "Other"
        ])
        message = st.text_area("Your Message", height=150)

        if st.button("Send Message →", use_container_width=True):
            if name and email and message:
                st.success("✅ Message sent! I'll get back to you within 24 hours.")
            else:
                st.warning("⚠️ Please fill in all fields.")

    with col2:
        st.markdown("""
        <div class='card'>
            <div class='card-title' style='margin-bottom: 20px;'>Contact Details</div>
            <div style='margin-bottom: 16px;'>
                <div style='color: #C8A97E; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px;'>Email</div>
                <div style='color: #E8E8F0;'>deofficialswift@gmail.com</div>
            </div>
            <div style='margin-bottom: 16px;'>
                <div style='color: #C8A97E; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px;'>Location</div>
                <div style='color: #E8E8F0;'>Nigeria</div>
            </div>
            <div style='margin-bottom: 16px;'>
                <div style='color: #C8A97E; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px;'>Availability</div>
                <div style='color: #2ECC71;'>● Open to opportunities</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
            <div class='card-title' style='margin-bottom: 16px;'>Find Me Online</div>
            <div style='display: flex; flex-direction: column; gap: 10px;'>
                <a href='https://github.com/minazuki799' target='_blank' class='contact-link'>🐙 github.com/minazuki799</a>
                <a href='https://linkedin.com/in/victor-okosun' target='_blank' class='contact-link'>💼 linkedin.com/in/victor-okosun</a>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #9090A8; font-size: 0.8rem; padding: 20px; border-top: 1px solid rgba(200,169,126,0.1);'>
    © 2026 Victor Okosun · Built with Streamlit · Music & Machine Learning
</div>
""", unsafe_allow_html=True)

