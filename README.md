## AI Tokenizer nima?

AI tokenizer — bu matnni model tomonidan ishlov berishdan oldin **tokenlarga** (yani, kichik birliklarga) bo‘lib
beruvchi komponent. AI modellar (GPT, BERT, Claude, LLaMA va boshqalar) to‘g‘ridan-to‘g‘ri matnni emas, **tokenlar
to‘plamini** qabul qiladi.

---

## Token nima?

Token:

* bu **so‘z**, **so‘z bo‘lagi**, yoki hatto **bir dona belgi** bo‘lishi mumkin;
* masalan, ingliz tilidagi `"playing"` so‘zi `["play", "ing"]` kabi ikkita token bo‘linishi mumkin;
* yoki `"😊"` yoki `"2024"` kabi belgilar — bitta token bo‘lishi mumkin (lekin bu tokenizerga bog‘liq).

---

## Nega Tokenizer muhim?

* Har bir **token** uchun **model computation (hisoblash)** amalga oshiriladi.
* Token soni:

    * **narx** (OpenAI, Anthropic, va boshqalarda);
    * **prompt/response limit**;
    * **kutilgan inference vaqt** uchun muhim.

---

## Mashhur tokenizerlar

| Model  | Tokenizer Kutubxonasi           | Max Token Length | Tokenization Usuli       |
|--------|---------------------------------|------------------|--------------------------|
| GPT    | `tiktoken` (`gpt-3.5`, `gpt-4`) | 4096–128000      | Byte Pair Encoding (BPE) |
| BERT   | `transformers` (`bert-base`)    | 512              | WordPiece                |
| LLaMA  | `sentencepiece`, `tokenizers`   | 2048–8192        | SentencePiece (SPM)      |
| Claude | Max Token: \~200k               | Closed source    | Likely SPM + BPE variant |

---

## Best Practices

1. **Token limitni hisoblash**:

    * Modeldan foydalanishdan oldin `token count`ni aniqlab olish.
    * Prompt + Expected Output ≤ Model limit bo‘lishi kerak.
    * Haddan oshgan tokenlar kesiladi yoki model error beradi.

2. **Tight Prompt Engineering**:

    * Kamroq token = tezroq va arzonroq inferensiya.
    * Ortiqcha gap-so‘zdan qoching.

3. **Matnni oldindan tokenlab test qilish**:

    * Model inputlar tokenlarga qanday bo‘linayotganini tekshiring.
    * `tiktoken`, `transformers`, yoki `spacy` orqali.

4. **Multilingual token test**:

    * Har bir til har xil tokenlashadi.
    * `O'zbekcha`, `Русский`, `English`, `中文` — token soni farqli bo‘lishi mumkin.

---

## Real Kod Namunalari

### 1. `tiktoken` (OpenAI uchun)

```python
import tiktoken

# GPT-4 uchun tokenizer
encoding = tiktoken.encoding_for_model("gpt-4")

text = "Salom, mening ismim Musharraf."
tokens = encoding.encode(text)

print("Tokenlar soni:", len(tokens))
print("Tokenlar:", tokens)
```

---

### 2. `transformers` (BERT, GPT2, LLaMA uchun)

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Tokenization is essential!"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Tokenlar:", tokens)
print("Tokenlar soni:", len(token_ids))
```

---

### 3. `sentencepiece` (Google T5, LLaMA, mBART, Alpaca...)

```python
import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.load("llama.model")  # o'zingizda model bo'lishi kerak

text = "Salom, LLaMA!"
print("Tokenlar:", sp.encode(text, out_type=str))
print("Token soni:", len(sp.encode(text)))
```

---

## Vizual ko‘rsatkichlar

| Matn                                 | Tokenlar soni (gpt-3.5) |
|--------------------------------------|-------------------------|
| `"Salom"`                            | 1 token                 |
| `"Salom, mening ismim Musharraf"`    | 6 token                 |
| `"Bu juda uzoq va murakkab matn..."` | 15+ token               |
| `"😊"`                               | 1 token                 |
| `"👍🏽"`                             | 2 token                 |

---

## 📊 Token Calculatorlar

* [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer)
* Hugging Face Playground
* Tiktoken CLI: `tiktoken encode "text here"`

