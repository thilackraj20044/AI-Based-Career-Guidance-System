import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import random  # for generating mock job market trends

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Career Guidance ChatBot",
    page_icon="🎓",
    layout="centered",
)

# Retrieve the Google Gemini AI API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Verify API key is present
if not GOOGLE_API_KEY:
    st.error("Google API key not found. Please configure your environment variables.")
    st.stop()

# Configure the Gemini AI API
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("gemini-pro")

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    try:
        st.session_state.chat_session = model.start_chat()
    except Exception as e:
        st.error(f"Failed to initialize the chat session: {e}")
        st.stop()

# Display the chatbot's title and description
st.title("🎓 Career Guidance ChatBot")
st.markdown(
    """
    Welcome to the Career Guidance ChatBot!  
    Ask me anything about your career choices, skill development, or higher education paths.  
    Let's explore your opportunities together! 🌟
    """
)

# Create a form for gathering user's career experience, education level, field of interest, and preferred work environment
with st.form("career_info_form"):
    st.subheader("Tell me more about your career background")
    
    # Ask for career experience
    career_experience = st.text_area("How much experience do you have in your current career?", 
                                     placeholder="e.g., I have 2 years of experience in software development.")
    
    # Ask for the field of interest
    field_of_interest = st.text_input("What field or industry are you interested in?", 
                                      placeholder="e.g., Data Science, Web Development, etc.")
    
    # Ask for education level
    education_level = st.selectbox("What is your highest level of education?", 
                                   options=["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
    
    # Ask for preferred work environment
    work_environment = st.selectbox("What type of work environment do you prefer?", 
                                    options=["Remote", "Office", "Hybrid"])
    
    # Submit button for the form
    submit_button = st.form_submit_button("Submit")

# Check if form was submitted
if submit_button:
    # Store the user's responses in session state
    st.session_state.career_experience = career_experience
    st.session_state.field_of_interest = field_of_interest
    st.session_state.education_level = education_level
    st.session_state.work_environment = work_environment

    # Show a summary of the user's input
    st.write(f"**Career Experience:** {career_experience}")
    st.write(f"**Field of Interest:** {field_of_interest}")
    st.write(f"**Education Level:** {education_level}")
    st.write(f"**Preferred Work Environment:** {work_environment}")
    
    # Suggest recommendations based on user input
    if field_of_interest and career_experience:
        st.subheader("Here are some personalized recommendations:")
        
        # Example recommendation logic based on user input
        if "data science" in field_of_interest.lower():
            if "2 years" in career_experience:
                st.write("- Consider learning advanced machine learning algorithms and tools like TensorFlow.")
                st.write("- Explore data analysis techniques with Python (e.g., Pandas, NumPy).")
                st.write("- Try online courses from platforms like Coursera or edX on data science specialization.")
                # Job Market Trend (Mock)
                job_market_trend = random.choice(["high demand", "moderate demand", "low demand"])
                st.write(f"- **Job Market Trend:** Data Science has a {job_market_trend} in the current market.")
                st.write("- Consider getting a certification in AI or Machine Learning.")
            else:
                st.write("- Start with the basics of Python and statistics.")
                st.write("- Learn tools like Jupyter Notebooks, Pandas, and Matplotlib for data analysis.")
                st.write("- Build projects like data analysis with real-world datasets.")
                st.write("- Look into online introductory courses like 'Data Science for Beginners'.")
                # Job Market Trend (Mock)
                job_market_trend = random.choice(["high demand", "moderate demand", "low demand"])
                st.write(f"- **Job Market Trend:** Data Science has a {job_market_trend} in the current market.")
        elif "web development" in field_of_interest.lower():
            if "2 years" in career_experience:
                st.write("- Focus on mastering frameworks like React or Angular.")
                st.write("- Explore backend technologies like Node.js or Django.")
                st.write("- Build personal projects to showcase in your portfolio.")
                st.write("- Work on full-stack development to be a versatile developer.")
                # Job Market Trend (Mock)
                job_market_trend = random.choice(["high demand", "moderate demand", "low demand"])
                st.write(f"- **Job Market Trend:** Web Development has a {job_market_trend} in the current market.")
            else:
                st.write("- Learn HTML, CSS, and JavaScript fundamentals.")
                st.write("- Try building simple static websites or blogs.")
                st.write("- Build basic responsive layouts using Bootstrap or Tailwind CSS.")
                # Job Market Trend (Mock)
                job_market_trend = random.choice(["high demand", "moderate demand", "low demand"])
                st.write(f"- **Job Market Trend:** Web Development has a {job_market_trend} in the current market.")
        else:
            st.write("- It looks like you're exploring new career paths! I recommend starting with online tutorials in your field.")
            st.write("- Build a portfolio of your work to showcase your skills to potential employers.")
        
        # Suggest certification or education path
        st.subheader("Suggested Certifications and Education Path:")
        if education_level == "High School":
            st.write("- You might consider pursuing a Bachelor's degree in your field of interest.")
            st.write("- Look into online courses in your field to get started.")
        elif education_level == "Bachelor's Degree":
            st.write("- Consider pursuing a Master's degree for specialization.")
            st.write("- Attend workshops or bootcamps for industry-specific skills.")
        elif education_level == "Master's Degree":
            st.write("- Explore PhD programs or certifications for expertise.")
            st.write("- Look for high-impact industry projects to get hands-on experience.")
        else:
            st.write("- You are well-prepared for expert-level career opportunities.")
            st.write("- Look into post-doctoral research or advanced industry roles.")

    else:
        st.write("Please provide both your career experience and field of interest for personalized recommendations.")
    
    # Recommend work environments based on preference
    st.subheader("Recommended Work Environment:")
    if work_environment == "Remote":
        st.write("- Consider companies that support fully remote teams like GitHub or Automattic.")
        st.write("- Work on developing strong communication and collaboration skills.")
    elif work_environment == "Office":
        st.write("- Look for jobs at companies that have a strong office culture, like Google or Microsoft.")
        st.write("- Consider building a network within your local tech or industry community.")
    else:
        st.write("- Hybrid work environments are popular at companies like Spotify and Apple.")
        st.write("- You can enjoy the flexibility of remote work while being connected with a team.")

# Input field for the user's general query
user_prompt = st.chat_input("Ask about careers, skills, or education...")
if user_prompt:
    # Display the user's message
    st.chat_message("user").markdown(user_prompt)

    # Send the user's message to Gemini-Pro and get the response
    try:
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        response_text = gemini_response.text  # Access the text attribute directly

        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(response_text)
    except Exception as e:
        st.error(f"An error occurred while sending the message: {e}")
