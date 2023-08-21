# from transformers import GPT2Model, GPT2Tokenizer

# def generate_text_from_vector(vector, model, tokenizer, max_length=50):
#   output = model.generate(vector, max_length=max_length, num_return_sequences=1)
#   generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
#   return generated_text

# model_name = 'gpt2-xl'
# model = GPT2Model.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# input_vector = tokenizer.encode('what is your name?', return_tensors='pt')
# generated_text = generate_text_from_vector(input_vector, model, tokenizer)

# print('Generated text:', generated_text)


from transformers import GPT2Tokenizer, GPT2LMHeadModel

model_name = 'gpt2-xl'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

inputs = tokenizer('what is my name?', return_tensors='pt')
outputs = model.generate(**inputs, max_length=100)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

print(generated_text)
