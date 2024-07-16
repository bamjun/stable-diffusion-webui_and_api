import requests
import time

# WebUI의 API 엔드포인트 (일반적으로 http://localhost:7860)
api_url = 'http://127.0.0.1:7860/sdapi/v1/txt2img'

# 20개의 프롬프트 설정
prompts = [
    "A Knitted yarn Lovely animal friends, <lora:textures_pack:1>",
    "A Knitted yarn Bright flower garden, <lora:textures_pack:1>",
    "A Knitted yarn Fairy tale dreamland, <lora:textures_pack:1>",
    "A Knitted yarn Colorful balloon festival, <lora:textures_pack:1>",
    "A Knitted yarn Enchanted starlight garden, <lora:textures_pack:1>",
    "A Knitted yarn Sweet candy village, <lora:textures_pack:1>",
    "A Knitted yarn Happy rainbow bridge, <lora:textures_pack:1>",
    "A Knitted yarn Magical fairy forest, <lora:textures_pack:1>",
    "A Knitted yarn Sunny meadow, <lora:textures_pack:1>",
    "A Knitted yarn Warm sky with clouds, <lora:textures_pack:1>",
    "A Knitted yarn Adorable teddy bears, <lora:textures_pack:1>",
    "A Knitted yarn Cute kitten parade, <lora:textures_pack:1>",
    "A Knitted yarn Charming woodland creatures, <lora:textures_pack:1>",
    "A Knitted yarn Playful puppy park, <lora:textures_pack:1>",
    "A Knitted yarn Friendly forest animals, <lora:textures_pack:1>",
    "A Knitted yarn Sparkling fairy dust, <lora:textures_pack:1>",
    "A Knitted yarn Whimsical butterfly field, <lora:textures_pack:1>",
    "A Knitted yarn Joyful penguin party, <lora:textures_pack:1>",
    "A Knitted yarn Cheerful ladybug land, <lora:textures_pack:1>",
    "A Knitted yarn Peaceful unicorn valley, <lora:textures_pack:1>",
]

# 생성 매개변수 기본 설정
payload_template = {
    "steps": 20,               # Sampling steps
    "width": 512,              # Width
    "height": 512,             # Height
    "cfg_scale": 7,            # CFG Scale
    "seed": -1,                # Seed (-1 for random)
    "sampler_name": "DPM++ 2M", # Sampling method
    "batch_count": 1,          # Batch count
    "batch_size": 1,           # Batch size
    "save_images": True,
    "save_path": "C:/projects/stable-diffusion/001/stable-diffusion-webui/outputs/txt2img-images/2024-07-16",  # 저장 경로 설정
    "checkpoint": "epicrealism_naturalSinRC1VAE.safetensors"
}

def generate_image(prompt):
    payload = payload_template.copy()
    payload["prompt"] = prompt
    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        print(f"Image generated successfully for prompt: {prompt}")
    else:
        print(f"Failed to generate image for prompt: {prompt}")

# 20개의 프롬프트에 대해 이미지 생성
for prompt in prompts:
    generate_image(prompt)
    time.sleep(5)  # 5초 간격으로 이미지 생성
