from openai import OpenAI

client = OpenAI()

text = "today is a sunny day!"

response = client.embeddings.create(
	input= text,
	model="text-embedding-3-small"
)

print(response.data[0].embedding)