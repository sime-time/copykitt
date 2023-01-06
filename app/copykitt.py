import os 
import openai 

openai.api_key = os.getenv("OPENAI_API_KEY")

subject = "coffee"
prompt = f"Generate upbeat branding snippet for {subject}"

response = openai.Completion.create(
  model = "davinci-instruct-beta-v3",
  prompt = prompt,
  temperature = 0,
  max_tokens = 32
)

print(response)