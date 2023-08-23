import openai

openai.api_key = ''


def make_summury_content(sentences):
  return '\n'.join(sentences)


def summury_chatbot(sentences):
  response = openai.ChatCompletion.create(
      model='gpt-3.5-turbo',
      messages=[
          {'role': 'system', 'content': '너는 주어진 질문에 대한 답변들중 적절한 답변만을 이용해서 요약 정리하는 봇이야.'},
          {'role': 'user', 'content': make_summury_content([
              'q:metanode가 뭐지?',
              'a:metanode는 회사야.',
              'a:metanode의 개발자들은 모두 멋져.',
              'a:난 널 사랑해.'])},
          {'role': 'assistant', 'content': 'metanode는 멋진 개발자들이 있는 회사야.'},
          {'role': 'user', 'content': make_summury_content(sentences)},
          # {'role': 'user', 'content': 'q: "gpt란?"\na: ""GPT"의 약자는 "Generative Pre-trained Transformer" 입니다."\na:", OpenAI에서 개발한 자연어 처리 모델입니다."\na:"동해물과 백두산이 마르고 닳도록"'},
          # {'role': 'user', 'content': 'q:"우주 탐사는 어떻게 진행되나요?"\na:"우주 탐사 임무는 신중한 계획과 설계 단계를 거쳐 시작됩니다."\na:"제작된 우주선은 로켓을 사용하여 지구의 중력을 빠져나가고 우주로 발사됩니다."\na:"탐사 임무가 성공적으로 완료되면 미션은 종료됩니다."\na:"동해물과 백두산이 마르고 닳도록"\na:"오늘 날씨가 너무 더워 개짜증."'},

      ],
      temperature=0,
  )

  return response['choices'][0]['message']['content']

result = summury_chatbot([
    'q:우주 탐사는 어떻게 진행되나요?',
    'a:우주 탐사 임무는 신중한 계획과 설계 단계를 거쳐 시작됩니다.',
    'a:제작된 우주선은 로켓을 사용하여 지구의 중력을 빠져나가고 우주로 발사됩니다.',
    'a:"탐사 임무가 성공적으로 완료되면 미션은 종료됩니다.',
    'a:동해물과 백두산이 마르고 닳도록..',
    'a:오늘 날씨가 너무 더워 개짜증.'
])

print(result)
