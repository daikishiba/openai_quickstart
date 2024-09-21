from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
			"role": "system", 
			"content": "You are a helpful assistant."
		},
        {
        	"role": "user",
            "content": "please list up 10 fruit name"
        }
    ]
)

print(completion.choices[0].message)