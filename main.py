import streamlit as st
import utils

# title
st.title('InterviewPrep 🧑‍💻')
st.markdown('Prepare for your next tech interview with the help of AI!')
st.markdown('<br>', unsafe_allow_html=True)


# API key, number of questions, model
with st.expander('Groq API Key & Other settings'):
    groq_api_key = st.text_input(label='Enter your Groq API key here:')

    # n_questions_col, model_name_col = st.columns([1, 3], vertical_alignment = 'center')

    # with n_questions_col:
    #     n_questions = st.number_input(label="Number of questions:",
    #                                 min_value=5,
    #                                 max_value=10,
    #                                 value=5,
    #                                 step=1)
    # with model_name_col:
    #     model_name = st.selectbox(label="Model:",
    #                             options=["Llama 3.1 70B", "Llama 3.1 8B"],
    #                             index=0)

# Job description
job_desc = st.text_area(label='Enter your job description here:')

# generate questions
if st.button('Generate questions'):
    questions = utils.get_questions(job_desc=job_desc, n_questions=2, api_key=groq_api_key)
    st.session_state['questions'] = questions

# display questions
if 'questions' in st.session_state:
    for q_no, question in enumerate(st.session_state['questions']):
        with st.expander(f'Question {q_no+1}'):
            st.write(question)
        