from transformers import pipeline

prompt = input("prompt: ")

pipe = pipeline("text-generation", model="perplexity-ai/r1-1776-distill-llama-70b")

output = pipe(prompt, max_length=512, do_sample=True)

print(output[0]['generated_text'])
