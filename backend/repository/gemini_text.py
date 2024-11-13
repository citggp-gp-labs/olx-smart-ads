import os
import vertexai
import vertexai.generative_models as generative_models
from vertexai.generative_models import GenerativeModel
import logging

class GeminiPro:
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL_VERSION')
    TEMPERATURE = 0
    TOP_P = 1
    MAX_OUTPUT_TOKENS = 242

    def __init__(self, project: str, location: str, model: str):
        vertexai.init(project=project, location=location)
        self.project = project
        self.location = location
        self.model = GenerativeModel(model)

    async def gemini_pro(
        self,
        prompt: str,
        temperature: float = TEMPERATURE,
        top_p: float = TOP_P,
        max_output_tokens: int = MAX_OUTPUT_TOKENS,
    ):
        try:
            generated_content = self.model.generate_content(
                prompt,
                generation_config={
                    "max_output_tokens": max_output_tokens,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                safety_settings={
                    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                },
                stream=False,
            )
            return generated_content
        except Exception as e:
            logging.error(e)
