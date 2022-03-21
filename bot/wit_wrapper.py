from wit import Wit
import os

wit_client = Wit(os.environ['WIT_TOKEN'])

def wit_nlp(text):
  return wit_client.message(text)