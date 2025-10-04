import logging
from typing import Optional

logger = logging.getLogger(__name__)


class BaseImageGeneratorAdapter:
    def generate_image(self, prompt: str) -> Optional[str]:
        raise NotImplementedError()


class OpenAIAdapter(BaseImageGeneratorAdapter):
    def __init__(self, client):
        self.client = client

    def generate_image(self, prompt: str) -> Optional[str]:
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                n=1,
            )
            return response.data[0].url
        except Exception:
            logger.exception('OpenAI image generation failed')
            return None


class DummyAdapter(BaseImageGeneratorAdapter):
    def generate_image(self, prompt: str) -> Optional[str]:
        if not prompt:
            return None
        return "https://via.placeholder.com/1024.png?text=IA+Preview"
