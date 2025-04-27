from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from categorys.serialzer import IdeaSerializer

def create_idea(titel:str, body:str, category:int)->str:
    """
    create a new idea using the IdeaSerializer
    """
    idea = IdeaSerializer(data={
            'title': titel,
            'body': body,
            'category': category
        })
    idea.is_valid(raise_exception=True)
    idea.save()
    return idea.title

create_idea_declaration={
    "name": "create_idea",
    "description": "create a new idea using the IdeaSerializer",
    "parameters": {
        "type": "object",
        "properties": {
            "titel": {
                "type": "string",
                "description": "the title of the idea",
            },
            "body": {
                "type": "string",
                "description": "the body of the idea",
            },
            "category": {
                "type": "integer",
                "description": "the id of the category",
            },
        },
        "required": ["titel", "body", 'category'],
    },
}

load_dotenv()
tools=[]

config = types.GenerateContentConfig(
    tools=[tools],
    system_instruction='you are a helpful assistant that can create a new idea using the creat_idea function for a given category and what the user is thinking',)
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def generate_idea(prompt:str):
    ...