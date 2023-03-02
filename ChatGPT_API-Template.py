import config
import openai

openai.api_key = config.API_KEY

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is one of the things we can do to improve humanity?"},
    ]
)

generated_text = response['choices'][0]['message']['content']

print(generated_text)