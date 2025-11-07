from google import genai
from google.genai import types
from .config.settings import settings

try:
    client = genai.Client(
        vertexai = settings.use_vertex,
        project = settings.project_id,
        location = settings.location,
    )
    print("Client initialized successfully.")
except Exception as e:
    print(f"Error initializing client: {e}")

def get_content_config():
    content_config = types.GenerateContentConfig(
        temperature=settings.temperature,
        top_p=settings.top_p,
    )

def generate_text(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=settings.model,
            contents=prompt,
            config=get_content_config(),
        )
        return response.text
    except Exception as e:
        print(f"Error calling model: {e}")
        return ""