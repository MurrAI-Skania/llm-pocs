from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # project_id: str = "MurraiInternal"
    project_id: str = "vertex-llm-codelab"
    location: str = "europe-west1"
    model: str = "gemini-2.5-flash"
    use_vertex: bool = True

    temperature: float = 0.2
    top_p: float = 0.8
    max_output_tokens: int = 1024

    system_instructions: str = ""

    class Config:
        env_file = ".env"

settings = Settings()