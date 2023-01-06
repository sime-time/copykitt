import os 
import openai 
import argparse

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
  print("Running Main!")

  parser = argparse.ArgumentParser()
  parser.add_argument("--input", "-i", type=str, required=True)
  args = parser.parse_args()
  user_input = args.input 

  print(f"User input: {user_input}")
  pass

subject = "coffee"
prompt = f"Generate upbeat branding snippet for {subject}"

""" response = openai.Completion.create(
  model = "davinci-instruct-beta-v3",
  prompt = prompt,
  temperature = 0,
  max_tokens = 32
)

print(response) """

if __name__ == "__main__":
  main()