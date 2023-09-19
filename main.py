import os
import openai

if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY") #essa chave deve ser gerada previamente no site da openai
    conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
    ]

    # Send the conversation to the model
    chat_completion = openai.Completion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
    print(chat_completion)