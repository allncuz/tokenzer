import tiktoken

# GPT-4 uchun tokenizer
encoding = tiktoken.encoding_for_model("gpt-4")

text = "Salom, mening ismim Musharraf."
tokens = encoding.encode(text)

print("Tokenlar soni:", len(tokens))
print("Tokenlar:", tokens)
