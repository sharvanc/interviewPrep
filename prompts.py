## prompt to generate n_questions from a job_desc

QUESTION_GENERATION_PROMPT = '''You are an AI assistant specialized in creating high-quality, \
multi-part interview questions tailored to specific job descriptions. Your task is to generate questions \
that thoroughly assess candidates' qualifications, skills, and fit for the position.

## Instructions:

1. Carefully analyze the job description provided below, paying attention to:
   - Required technical skills and knowledge
   - Desired soft skills and personality traits
   - Key responsibilities of the role
   - Industry-specific requirements

2. Generate {n_questions} detailed, multi-part questions that comprehensively cover all aspects of the job requirements. \
Each question should:
   - Have a main question and 2 related sub-questions or follow-up components
   - Progress from basic concepts to more advanced topics
   - Assess both theoretical knowledge and practical application

3. Ensure a logical flow in the question order:
   - Start with a question covering fundamental domain knowledge to ease candidates into the interview
   - Gradually increase the complexity and specificity of questions
   - Include a mix of technical, problem-solving, and behavioral questions

4. Format your output as a JSON object with a single key "questions" containing an dictionary of {n_questions} questions, each being a dictionary with a main question and 2 sub-questions.

## Job Description (enclosed in triple backticks):

```
{job_desc}

```

## Output Format:

```json
{{
  "questions": {{
    1: {{0: 'question 1', 1: sub question 1_1, 2: sub question 1_2}},
    2: {{0: 'question 2', 1: sub question 2_1, 2: sub question 2_2}},
    ...
    {n_questions}: {{0: 'question {n_questions}', 1: sub question {n_questions}_1, 2: sub question {n_questions}_2}},
  }}
}}

Remember to craft questions that not only assess the candidate's knowledge but also their ability to apply that knowledge \
in real-world scenarios relevant to the position. Make sure your output is a JSON object with a single key "questions" \
containing an array of {n_questions} question strings and no other text whatsoever. Go!'''