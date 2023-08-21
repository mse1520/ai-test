import torch
import csv
import pandas as pd
from torch.utils.data import Dataset
from transformers import TrainingArguments, Trainer, AutoTokenizer, AutoModelForSequenceClassification, BertTokenizer, BertForSequenceClassification


def drop_na_and_duplicates(data):
  result = data.dropna()
  result = result.drop_duplicates()
  result = result.reset_index(drop=True)
  return result


def change_label(label):
  if label == 'neutral':
    label = 0
  elif label == 'contradiction':
    label = 1
  elif label == 'entailment':
    label = 2
  return label


class NLIDataset(Dataset):
  def __init__(self, data, tokenizer):
    self.data = data
    self.tokenizer = tokenizer

  def __len__(self):
    return len(self.data)

  def __getitem__(self, idx):
    sentence1 = self.data['sentence1'][idx]
    sentence2 = self.data['sentence2'][idx]
    labels = self.data['labels'][idx]
    encoded_inputs = tokenizer(sentence1, sentence2, padding='max_length', max_length=512, truncation=True, return_tensors='pt')

    return {
        'input_ids': encoded_inputs['input_ids'][0],
        'attention_mask': encoded_inputs['attention_mask'][0],
        'token_type_ids': encoded_inputs['token_type_ids'][0],
        'labels': torch.tensor(labels)
    }


model_name = 'bert-base-multilingual-cased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=3)

mnli_data = pd.read_csv('./dataset/multinli.train.ko.tsv', sep='\t', encoding='UTF-8', quoting=csv.QUOTE_NONE)
snli_data = pd.read_csv('./dataset/snli_1.0_train.ko.tsv', sep='\t', encoding='UTF-8', quoting=csv.QUOTE_NONE)
eval_data = pd.read_csv('./dataset/xnli.dev.ko.tsv', sep='\t', encoding='UTF-8', quoting=csv.QUOTE_NONE)
test_data = pd.read_csv('./dataset/xnli.test.ko.tsv', sep='\t', encoding='UTF-8', quoting=csv.QUOTE_NONE)
train_data = pd.concat([mnli_data, snli_data], ignore_index=True)

train_data = drop_na_and_duplicates(train_data)
eval_data = drop_na_and_duplicates(eval_data)
test_data = drop_na_and_duplicates(test_data)

# 데이터 줄이기 (테스트용)
train_data = train_data.sample(n=15000, random_state=1)
train_data = train_data.reset_index(drop=True)

train_data['labels'] = train_data['gold_label'].apply(change_label)
eval_data['labels'] = eval_data['gold_label'].apply(change_label)
test_data['labels'] = test_data['gold_label'].apply(change_label)

train_ds = NLIDataset(train_data, tokenizer)
eval_ds = NLIDataset(eval_data, tokenizer)
test_ds = NLIDataset(test_data, tokenizer)

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    learning_rate=2e-5,
    warmup_steps=500,
    weight_decay=0.01,
    evaluation_strategy='epoch',
    logging_dir='./logs',
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
)

trainer.train()
test_results = trainer.evaluate(test_dataset=test_ds)
trainer.save_model('./ko_test_bert_model')
# tokenizer.save_pretrained('./ko_test_bert_tokenizer')

print('Test accuracy:', test_results['eval_accuracy'])
