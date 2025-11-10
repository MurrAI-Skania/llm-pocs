from google import genai
from google.genai import types
from .config.settings import settings

_client = None

def _get_gemini_client():
    global _client
    try:
        if _client is None:
            _client = genai.Client(
                vertexai = settings.use_vertex,
                project = settings.project_id,
                location = settings.location,
            )
            print("New gemini client initialized successfully.")
        else: 
            print("Using existing gemini client.")
        return _client
    except Exception as e:
        print(f"Error initializing gemini client: {e}")

def _get_content_config(
    temperature: float = settings.temperature,
    top_p: float = settings.top_p,
    max_output_tokens: int = settings.max_output_tokens,       
):
    try:
        content_config = types.GenerateContentConfig(
            temperature=temperature,
            top_p=top_p,
            max_output_tokens=max_output_tokens,
        )
        return content_config
    except Exception as e:
        print(f"Error creating content config: {e}")
        return None

def generate_text(prompt: str) -> str:
    try:
        client = _get_gemini_client()
        response = client.models.generate_content(
            model=settings.model,
            contents=prompt,
            config=_get_content_config(),
        )
        return response.text
    except Exception as e:
        print(f"Error calling model: {e}")
        return ""