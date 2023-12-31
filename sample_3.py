from transformers import CLIPTextModel, CLIPTokenizer
from diffusers import StableDiffusionPipeline
import torch

# GPUが利用可能な場合はGPUを使用する
device = "cuda" if torch.cuda.is_available() else "cpu"

# モデルの読み込み
#pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=True).to(device)
pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

# 画像生成のためのテキスト
prompt = "A fantasy landscape with mountains"

# 画像生成
image = pipeline(prompt).images[0]

# 画像の表示（または保存）
image.show()
# image.save("output.png")
