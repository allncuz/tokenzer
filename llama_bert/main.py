from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Tokenization is essential!"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Tokenlar:", tokens)
print("Tokenlar soni:", len(token_ids))
