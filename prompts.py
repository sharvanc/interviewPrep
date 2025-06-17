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

ASSESS_ANSWERS_PROMPT = '''You are an expert interview evaluator AI, tasked with rigorously assessing candidate answers \
to a set of multi-part interview questions. Your evaluation should be fair, detailed, and based strictly on the quality, \
depth, and relevance of each answer in relation to the question asked.

## Instructions:

1. Carefully review the context provided below, which contains:
   - The set of interview questions (main and sub-questions)
   - The candidate's corresponding answers to each question

2. For each question (including its sub-questions), evaluate the candidate's answer(s) based on the following criteria:
   - **Accuracy:** How correct and factually sound is the answer?
   - **Depth:** Does the answer demonstrate deep understanding and insight, or is it superficial?
   - **Relevance:** Does the answer directly address the question and its sub-parts?
   - **Clarity:** Is the answer clearly explained and well-structured?
   - **Application:** Where appropriate, does the answer show the ability to apply knowledge to real-world or job-relevant scenarios?

3. Assign a score from 1 to 10 for each question (1 = very poor, 10 = outstanding), considering all sub-questions and the overall quality \
of the response. Be objective and critical in your assessment.

4. For each question, provide a brief justification (1-2 sentences) explaining the score, highlighting strengths and areas for improvement.

5. Format your output as a JSON object with a single key "assessment" containing a dictionary. Each key is the question number, and the value \
is a dictionary with keys "score" (integer 1-10) and "justification" (string).

## Context (enclosed in triple backticks):

```
{context}
```

## Output Format:

```json
{{
  "assessment": {{
    1: {{"score": 8, "justification": "Accurate and detailed answer, but lacked real-world example."}},
    2: {{"score": 6, "justification": "Basic understanding shown, but missed key technical details."}},
    ...
    n: {{"score": 10, "justification": "Outstanding answer with excellent depth and application."}}
  }}
}}
```

Be thorough, unbiased, and ensure your output is a JSON object with a single key "assessment" as specified above. Do not include any other text. Go!'''