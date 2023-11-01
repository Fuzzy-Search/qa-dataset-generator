import openai
import random

topics = [ # Example
    "technology",
    "politics",
    "science",
    "health",
    "environment",
    "business",
    "education",
    "travel",
    "entertainment",
    "sports"
]

question_types = [ # Example
    "factual",
    "inferential",
    "how-to",
    "problem-solving",
    "analytical",
    "comparative"
]


def get_data(topics, question_types, data_size, api_key, max_tokens):

    curr_iter = 0
    data = []

    while curr_iter < data_size: # How many data points we want to collect

        question_type = random.choice(question_types)
        topic = random.choice(topics)

        prompt = f"""generate 7 small paragraphs and replace “text” with information about {topic} for every paragraph . 
                    Then generate a {question_type} question about 1 or more paragraph. Next, answer the question and reference paragraphs
                    that were the most useful to answer the question.

                    format:
                    paragraph 1: “text”
                    … 
                    paragraph 7 :“text”

                    “question”

                    “answer”
                    paragraph 3, paragraph 5"""
    
        data.append(generate_response(api_key, prompt, max_tokens))

    return data # Save however we want

def generate_response(api_key, prompt, max_tokens):
    openai.api_key = api_key
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3.5 Turbo engine
        prompt=prompt,
        max_tokens=max_tokens  # Limit the response to certain num of tokens
    )

    return response.choices[0].text.strip()
