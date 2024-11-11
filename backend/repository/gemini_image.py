import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

class GeminiImage:
    DEFAULT_MODEL = "gemini-1.5-flash-002"
    MAX_OUTPUT_TOKENS = 1000
    TOP_P = 1
    TOP_K = 40
    TEMPERATURE = 0

    def __init__(
        self,
        project: str,
        location: str,
        model: str = DEFAULT_MODEL,
        max_output_tokens: int = MAX_OUTPUT_TOKENS,
        top_p: int = TOP_P,
        top_k: int = TOP_K,
        temperature: int = TEMPERATURE,
    ):
        vertexai.init(project=project, location=location)
        self.model = GenerativeModel(model)
        self.max_output_tokens = max_output_tokens
        self.top_p = top_p
        self.top_k = top_k
        self.temperature = temperature

    def generate(self, prompt: str, image_url: str):
        _, file_extension = os.path.splitext(image_url)
        file_extension = file_extension[1:].lower()

        if file_extension.lower() not in ['jpg', 'jpeg', 'png', 'webp', 'gif', 'heic']:
            raise ValueError(f"Unsupported image format: {file_extension}. These image format is not supported.")

        image = Part.from_uri(
            mime_type=f"image/{file_extension}",
            uri=image_url,
        )

        self.model.count_tokens([image, prompt])

        return self.model.generate_content(
            [image, prompt],
            generation_config={
                "max_output_tokens": self.max_output_tokens,
                "temperature": self.temperature,
                "top_p": self.top_p,
                "top_k": self.top_k,
            },
            safety_settings={
                generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            stream=False,
        )