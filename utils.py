import prompts
from groq import Groq
import ast


def get_response_from_llm(prompt:str, 
                          api_key:str, 
                          model:str, 
                          temperature:float, 
                          max_tokens: int):
    """
    Generates a response from a language model using the provided prompt, API key, model, temperature, and maximum tokens.

    Parameters:
        prompt (str): The input prompt for the language model.
        api_key (str): The API key for accessing the language model.
        model (str): The name of the language model to use.
        temperature (float): The temperature parameter for controlling the randomness of the model's output.
        max_tokens (int): The maximum number of tokens to generate in the response.

    Returns:
        str: The generated response from the language model.
    """
    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", 
             "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content



def get_questions(
        job_desc:str, 
        n_questions: int, 
        api_key:str, 
        temperature:float=0,
        model_name:str="llama-3.1-70b-versatile", 
        max_tokens:int=1536
        )-> list:
    """
    Generates a list of questions based on a given job description.ss

    Args:
        job_desc (str): The job description.
        n_questions (int): The number of questions to generate.
        api_key (str): The API key for accessing the language model.
        temperature (float, optional): The temperature parameter for controlling the randomness of the model's output. Defaults to 0.
        model_name (str, optional): The name of the language model to use. Defaults to "llama-3.1-70b-versatile".
        max_tokens (int, optional): The maximum number of tokens to generate in the response. Defaults to 1536.

    Returns:
        list or None: A list of questions or None if the response does not contain the 'questions' key.
    """
    # formatting the prompt with the job description and number of questions
    prompt = prompts.QUESTION_GENERATION_PROMPT.format(
        job_desc=job_desc,
        n_questions=n_questions
    )
    # getting the response from the language model
    response = get_response_from_llm(
        prompt=prompt, 
        api_key=api_key, 
        model=model_name, 
        temperature=temperature, 
        max_tokens=max_tokens
    )
    # processing the response
    processed_response = response.replace('```json', '').replace('```', '').replace('"', '"""')
    try:
        # converitng to dictionary
        questions_dict = ast.literal_eval(processed_response)
        # returning the questions list
        return (True, questions_dict['questions'])
    except Exception as e:
        return (False, e)
