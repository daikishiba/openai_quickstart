from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

client = OpenAI()

response = client.images.generate(
	model='dall-e-3',
	prompt='A sunlit indoor lounge area with a pool containing a flamingo',
	size='1024x1024',
	quality='standard',
	n=1
)

image_url = response.data[0].url

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.show()
