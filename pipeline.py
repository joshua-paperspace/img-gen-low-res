import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# prompt = "a Dali-esque painting of an astronaut riding a unicorn on mars"
# image = pipe(prompt).images[0]

# image.save("low_res.png")