from transformers import pipeline

# Use a general-purpose LLM (simulate Granite behavior)
chatbot = pipeline("text-generation", model="gpt2")

def ask_granite(prompt):
    response = chatbot(prompt, max_length=150, do_sample=True, temperature=0.7)
    return response[0]['generated_text']
