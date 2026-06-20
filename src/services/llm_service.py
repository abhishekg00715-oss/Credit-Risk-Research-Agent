"""
llm_service.py

Purpose:
Wrapper around OpenAI API.

Author:
Credit Risk Research Agent
"""

import os

from openai import OpenAI


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
        model: str = "gpt-4o-mini"
    ) -> str:

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