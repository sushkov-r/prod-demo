from fastapi import FastAPI, Query
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = FastAPI()

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

@app.get("/complete_text/")
async def complete_text(prompt: str = Query(..., max_length=50)):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones(inputs.shape)

    # GPT-2 doesn't use pad tokens, typically. But if you want to set it, you can.
    eos_token_id = tokenizer.eos_token_id

    with torch.no_grad():
        outputs = model.generate(inputs, max_length=50, num_return_sequences=1,
                                 num_beams=4, do_sample=True,
                                 attention_mask=attention_mask, pad_token_id=eos_token_id)

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"completed_text": text}


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/health")
def read_health():
    return {"status": "OK"}
