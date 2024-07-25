from diffusers import StableDiffusionPipeline
import torch

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
pipe = pipe.to(device)

def generate_image(prompt: str) -> str:
    image = pipe(prompt).images[0]
    image_path = f"generated_images/{prompt.replace(' ', '_')}.png"
    image.save(image_path)
    return image_path
