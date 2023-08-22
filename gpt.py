import openai

openai.api_key = ''
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': '너는 주어진 문장들을 요약 정리하는 봇이야.'},
        {'role': 'user', 'content': '"metanode는 회사야.", "metanode의 개발자들은 모두 멋져."'},
        # {'role': 'system', 'content': "It's a bot that summarizes and organizes your sentences."},
        # {'role': 'user', 'content': '"metanode is a company", "metanode\'s developers are all great."'},
        # {'role': 'assistant', 'content': 'Who's there?'},
        # {'role': 'user', 'content': 'Orange.'},
    ],
    temperature=0,
)

print(response['choices'][0]['message']['content'])
