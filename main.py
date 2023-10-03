import os
import openai

if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY") #essa chave deve ser gerada previamente no site da openai
    
    chat_completion = openai.Completion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "em que ano o Brasil foi descoberto"}])
    openai.Completion.create(model="gpt-3.5-turbo", prompt=chat_completion.choices[0].text, temperature=0.7, max_tokens=100)
    print(chat_completion)

