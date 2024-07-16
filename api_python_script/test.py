import requests
import time

# WebUI의 API 엔드포인트 (일반적으로 http://localhost:7860)
api_url = 'http://127.0.0.1:7860/sdapi/v1/txt2img'

# 생성할 프롬프트 설정
prompt = "A Knitted yarn Sparkling Flower Crown, <lora:textures_pack:1>"

# 생성 매개변수 설정
payload = {
    "prompt": prompt,
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
    "checkpoint": "v1-5-pruned-emaonly.safetensors"

}

def generate_image():
    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        print("Image generated successfully.")
    else:
        print("Failed to generate image.")

# 주기적으로 이미지 생성 (예: 5초마다)
interval = 5

try:
    while True:
        generate_image()
        time.sleep(interval)
except KeyboardInterrupt:
    print("Image generation stopped.")
