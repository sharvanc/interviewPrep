import streamlit as st
import utils

# title
st.title('InterviewPrep 🧑‍💻')
st.markdown('Prepare for your next tech interview with the help of AI!')
st.markdown('<br>', unsafe_allow_html=True)


# API key, number of questions, model
with st.expander('Groq API Key & Other settings'):
    groq_api_key = st.text_input(label='Enter your Groq API key here:')
    if st.button('Save'):
        st.session_state['groq_api_key'] = groq_api_key

# Job description
job_desc = st.text_area(label='Enter your job description here:')

# generate questions
if st.button('Generate questions'):
    if 'groq_api_key' not in st.session_state:
        st.error('Please enter your Groq API key first!')
    else:
        question_generation_status, questions = utils.get_questions(
            job_desc=job_desc, 
            n_questions=2, 
            api_key=groq_api_key
            )
        if question_generation_status:
            st.session_state['questions'] = questions
            st.session_state['answers'] = {q: {sq: "" for sq in subq} for q, subq in questions.items()}
            st.toast('Questions generated successfully!', icon='✅')
        else:
            st.error(questions)

def save_answer(q_no, sub_q_no):
    st.session_state.answers[q_no][sub_q_no] = st.session_state[f"answer_{q_no}_{sub_q_no}"]

# display questions
if 'questions' in st.session_state:
    for q_no in st.session_state['questions']:
        with st.expander(f'Question {q_no}'):
            for sub_q_no in st.session_state['questions'][q_no]:
                st.write(st.session_state['questions'][q_no][sub_q_no])
                st.text_area(
                    "Answer", 
                    key=f"answer_{q_no}_{sub_q_no}", 
                    value=st.session_state.answers[q_no][sub_q_no]
                    )
                st.button(
                    "Save answer", 
                    key=f"save_{q_no}_{sub_q_no}", 
                    on_click=save_answer, 
                    args=(q_no, sub_q_no)
                    )

# Display all answers
if st.button("Show all answers"):
    for q_no, subquestions in st.session_state.questions.items():
        st.write(f"Question {q_no}:")
        for sub_q_no, question in subquestions.items():
            st.write(f"  {sub_q_no}. {question}")
            st.write(f"  Answer: {st.session_state.answers[q_no][sub_q_no]}")
        st.write("---")