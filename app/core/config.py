"""Module for configuration settings."""
import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    """Base configuration class."""
    SECRET_KEY = os.getenv('SECRET_KEY', "super_secret_key")
