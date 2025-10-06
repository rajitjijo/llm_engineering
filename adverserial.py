import openai
from dotenv import load_dotenv

load_dotenv(override=True)

openai_client = openai.OpenAI()
ollama = openai.OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

openai_model = "gpt-4o-mini"
ollama_model = "llama3.2"

gpt_system = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

ollama_system = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."

def talk(rounds:int=5):

    gpt_messages = [{"role":"system", "content":gpt_system}]
    ollama_messages = [{"role":"system", "content":ollama_system}]

    gpt_message = "Hi There"
    ollama_message = "Hi!"

    gpt_messages.append({"role":"assistant","content":gpt_message})
    gpt_messages.append({"role":"user","content":ollama_message})

    ollama_messages.append({"role":"assistant","content":ollama_message})
    ollama_messages.append({"role":"user","content":gpt_message})

    print(f"[GPT]-> Round{0}: {gpt_message}")
    print(f"[Ollama]-> Round{0}: {ollama_message}")

    for i in range(rounds):

        gpt_response = openai_client.chat.completions.create(model=openai_model, messages=gpt_messages).choices[0].message.content

        print(f"[GPT]-> Round{i+1}: {gpt_response}")

        gpt_messages.append({"role":"assistant","content":gpt_response})
        ollama_messages.append({"role":"user","content":gpt_response})

        ollama_response = ollama.chat.completions.create(model=ollama_model, messages=ollama_messages).choices[0].message.content
        
        print(f"[Ollama]-> Round{i+1}: {ollama_response}")

        ollama_messages.append({"role":"assitant","content":ollama_response})
        gpt_messages.append({"role":"user","content":ollama_response})
        

if __name__ == "__main__":
    talk()
