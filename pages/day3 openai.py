import streamlit as st
from openai import OpenAI

st.title("매쓰봇! 어떤 수학이든 물어보세요.")
client = OpenAI(api_key = st.secrets['openai']['key'])

# prompt = st.text_input("무엇이 궁금한가요?")
# if prompt!="":
#     response = client.completions.create(model="gpt-3.5-turbo-instruct",
#                                          prompt=prompt, 
#                                          max_tokens=500)
#     st.success(response.choices[0].text)

# prompt = st.text_input("답변:")
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   temperature = 0.1,
#   messages=[{"role": "system", "content": "수학과 사랑에 빠진, 친절하고 따뜻한 수학선생님입니다. "},
#             {"role": "user", "content": "수학이 너무 재미있어요!"},
#             {"role": "assistant", "content": "정말요? 선생님도 수학이 너무 재미있어요. 수학 얘기를 해볼까요? "},
#             {"role": "user", "content":prompt}  ]
# )

# st.write(completion.choices[0].message['content'])

prompt = st.text_input("원하는 그림을 입력해주세요")

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="hd", # or standard
  n=1,
  style = 'vivid' # or natural
)

image_url = response.data[0].url
st.image(image_url)