import openai
import random
import json

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

question_types = [
    "a factual question seeking direct answers from the content",
    "an inferential question that understands underlying themes or concepts beyond the direct content",
    "an explanatory question providing detailed explanations for processes, events, or concepts",
    "a comparative question noting similarities or differences between elements",
    "an evaluative question asking for judgment based on standards or criteria",
    "a procedural question explaining steps towards a goal or task",
    "a problem-solving question identifying solutions to a presented problem",
    "an analytical question breaking down information into parts for understanding and connection"
]


def generate_response(api_key, topic, questions_types, max_tokes):
    """
    Ask gpt to generate contents based on the selected topic and question-answer pairs based on selected types.
    """
    openai.api_key = api_key
    s_types = random.sample(question_types, 3)
    
    # create the conversation, ask gpt to generate content
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a knowledgeable assistant asked to generate content on various topics, formulate relevant questions based on that content, and then answer those questions by explicitly quoting from generated paragraphs."
            },
            {
                "role": "user", 
                "content": f"Generate 7 paragraphs about {topic}."
            },
            {
                "role": "user", 
                "content": f"Next, create {s_types[0]} and answer it. Reference the relevant paragraphs in your response using the following format: 'Question: ... Answer: ...(referencing Paragraphs #).'"
            },
            {
                "role": "user",
                "content": f"Now, create {s_types[1]} and answer it, in the same way & format as before."
            },
            {
                "role": "user",
                "content": f"Now, create {s_types[2]} and answer it, in the same way & format as before."
            }
        ],
        max_tokens=max_tokens
    )
    
    # Extract the content from the response object
    return response


def format_response(result):
    """
    Extract and format gpt generated contents into more readable format.
    """
    response_dict = result.to_dict()
    # Convert the dict to a JSON string if we want to print it or save it as JSON (optional).
    json_string = json.dumps(response_dict, indent=2)
    response_data = json.loads(json_string)
    content = response_data['choices'][0]['message']['content']
    # Process the content to a more readable format.
    formatted_content = '\n\n'.join(content.split('\\n\\n'))
    return formatted_content
