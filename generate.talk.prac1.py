from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
	model='gpt-4o-mini',
	messages=[
		{'role': 'system', 'content': '関西弁で会話する陽気な関西人です'},
		{'role': 'user', 'content': '明日の大阪の天気教えて'}
	]
)

print(response.choices[0].message.content)
