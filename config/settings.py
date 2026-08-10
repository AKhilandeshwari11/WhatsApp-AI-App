from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    whatsapp_api_url: str = ""
    whatsapp_access_token: str = ""
    whatsapp_phone_number_id: str = ""
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    database_url: str = "sqlite:///./whatsapp.db"
    llm_api_key: str = ""
    groq_api_key: str
    class Config:
        env_file = ".env"


settings = Settings()