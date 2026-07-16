"""
llm_service.py

Purpose:
Wrapper around OpenAI API.

Author:
Credit Risk Research Agent
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the repository root .env file
load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def generate_response(
        self,
        prompt: str,
        model: str | None = None
    ) -> str:

        if model is None:
            model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

        response = (
            self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content":
                        (
                            "You are a senior "
                            "credit risk analyst."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )