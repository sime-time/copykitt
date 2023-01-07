import os 
import openai 
import argparse
import re

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY") 

# Max length of user input argument
MAX_INPUT_LENGTH = 12

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--input", "-i", type=str, required=True)
  args = parser.parse_args()
  user_input = args.input 

  print(f"User input: {user_input}")
  if validate_length(user_input):
    generate_branding_snippet(user_input)
    generate_keywords(user_input)
  else: 
    raise ValueError(f"Input length is too long. Must be under {MAX_INPUT_LENGTH}")

def validate_length(arg_input: str) -> bool:
  return (len(arg_input) < MAX_INPUT_LENGTH)


def generate_branding_snippet(arg_input: str):
  # create a prompt for GPT 
  prompt = f"Short upbeat branding snippet for {arg_input}: "
  print(prompt)

  # access GPT text completion using prompt
  response = openai.Completion.create(
    model = "davinci-instruct-beta-v3",
    prompt = prompt,
    temperature = 0,
    max_tokens = 32
  )

  # extract the generated text from the response object 
  branding_text: str = response["choices"][0]["text"]

  # strip white space
  branding_text = branding_text.strip() 

  # check if an ellipsis is required on truncated statements
  last_char = branding_text[-1] 
  if last_char not in {".", "!", "?"}:
    branding_text += "..."

  print(f"Snippet: {branding_text}")
  return branding_text


def generate_keywords(arg_input: str):
  # create a prompt for GPT 
  prompt = f"Create related branding keywords for {arg_input}, separated by comma: "

  # access GPT text completion using prompt
  response = openai.Completion.create(
    model = "davinci-instruct-beta-v3",
    prompt = prompt,
    temperature = 0,
    max_tokens = 32
  )

  # extract the generated text from the response object 
  keywords_text: str = response["choices"][0]["text"]

  # strip white space
  keywords_text = keywords_text.lower().strip() 

  # put the keywords into a list
  keywords_list = re.split(",|\n|-", keywords_text)  # split keywords by comma or newline
  keywords_list = [k.strip() for k in keywords_list] # remove whitespace from each keyword
  keywords_list = [k for k in keywords_list if len(k) > 0] # remove any empty strings in list

  print(f"Result: {keywords_list}")
  return keywords_list

if __name__ == "__main__":
  main()

# i am at 34:20 on the yt