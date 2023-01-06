import os 
import openai 
import argparse

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY") 

def main():
  print("Running Main!")

  parser = argparse.ArgumentParser()
  parser.add_argument("--input", "-i", type=str, required=True)
  args = parser.parse_args()
  user_input = args.input 

  print(f"User input: {user_input}")
  generate_branding_snippet(user_input)
  pass

def generate_branding_snippet(arg_prompt: str):
  # create a prompt for GPT 
  prompt = f"Short upbeat branding snippet for {arg_prompt}: "

  # access GPT text completion using prompt
  response = openai.Completion.create(
    model = "davinci-instruct-beta-v3",
    prompt = prompt,
    temperature = 0,
    max_tokens = 32
  )

  print(response)

if __name__ == "__main__":
  main()