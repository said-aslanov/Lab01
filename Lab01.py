import streamlit as st
# INFO

full_name = "Said Aslanov"   
course = "CS 1301 - Introduction to Computing"

about_me = (
    "I was born in Baku, Azerbaijan, and later spent part of my childhood living in Turkey, "
    "which gave me a chance to experience different cultures early in life. I’ve always had a love "
    "for animals and enjoy spending time with pets whenever I can. Outside of school, I’m fascinated "
    "by biomedical engineering and how science can be applied to improve healthcare. My long-term "
    "dream is to pursue medicine and become a doctor (MD), where I can combine my interests in science "
    "and helping people."
)

education = "Georgia Tech - CS 1301, Fall 2025"

experience = [
    {
        "role": "Volunteer",
        "org": "Animal Shelter, Rural Azerbaijan",
        "years": "2022",
        "desc": (
            "I volunteered at an animal shelter in rural Azerbaijan where I cared for cats, dogs, "
            "and other animals living in difficult conditions. This experience taught me compassion, "
            "responsibility, and the importance of helping vulnerable creatures who cannot help themselves."
        )
    }
]

projects = [
    {
        "name": "Psychological Evaluation Application",
        "desc": (
            "I developed an application designed to support psychological evaluation for high school students. "
            "Through this project, I learned important aspects of computer science, including Python and Java, "
            "to build a tool that could help psychologists assess students more effectively. "
            "This project not only deepened my programming skills but also earned me a national award, "
            "which motivated me to keep combining technology with meaningful real-world impact."
        )
    }
]

goals = "To keep learning, explore biomedical engineering, and one day become a medical doctor."


# PAGES
def home_page():
    st.title(full_name)
    st.subheader(course)

    st.write("Welcome to my Streamlit Web App! This app contains two main pages:")
    st.markdown("**Portfolio**: A personal portfolio page where I showcase my background, goals, and projects.")
    st.markdown("**Quiz**: A fun BuzzFeed-style quiz on a topic of my choice.")

    st.info("Use the sidebar on the left to navigate between pages.")


def portfolio_page():
    st.title("My Portfolio")

    st.header("About Me")
    st.write(about_me)

    st.header("Education")
    st.write(education)

    st.header("Experience")
    for exp in experience:
        st.subheader(exp["role"])
        st.write(f"{exp['org']} ({exp['years']})")
        st.write(exp["desc"])

    st.header("Projects")
    for project in projects:
        st.subheader(project["name"])
        st.write(project["desc"])

    st.header("Future Goals")
    st.write(goals)

    # Profile picture 
    st.image("images/your_image_fixed.jpg", caption="Me at work/study")


def quiz_page():
    st.title("BuzzFeed-style Quiz!")
    st.write("Take this quiz to find out something fun about yourself!")

    # Q1 - Radio
    q1 = st.radio("Choose your favorite color:", ["Red", "Blue", "Green", "Yellow"])  # NEW

    # Q2 - Multi-select
    q2 = st.multiselect("Pick your favorite hobbies:", ["Coding", "Sports", "Music", "Reading"])  # NEW

    # Q3 - Slider
    q3 = st.slider("On a scale of 1 to 10, how much do you like Python?", 1, 10)  # NEW

    # Q4 - Number input
    q4 = st.number_input("How many hours per week do you code?", min_value=0, max_value=100)

    # Q5 - Vacation Spot
    q5 = st.selectbox("Pick your dream vacation spot:", ["Japan", "Italy", "Hawaii", "Iceland"])

 
    # IMAGE SELECTION

    st.header("Pick Your Favorite Image")

    image_options = {
    "Option A": "images/quiz1.jpg",
    "Option B": "images/quiz2.jpg",
    "Option C": "images/quiz3.jpg"
    }

    selected = st.radio("Choose one image:", list(image_options.keys()))
    st.image(image_options[selected], caption=selected)

    # RESULTS

    if st.button("See Results"):
        result_message = "Thanks for taking the quiz! Your answers say you're awesome 🚀"
        if selected == "Option A":
            result_message = "You picked Option A — creative and curious 🌟"
        elif selected == "Option B":
            result_message = "You picked Option B — energetic and adventurous 🌍"
        elif selected == "Option C":
            result_message = "You picked Option C — GO JACKETS!🐝 "

        st.success(result_message)
        st.balloons()

# MAIN NAVIGATION

st.set_page_config(page_title="CS 1301 Lab01", layout="centered")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Portfolio", "Quiz"])

if page == "Home":
    home_page()
elif page == "Portfolio":
    portfolio_page()
elif page == "Quiz":
    quiz_page()
