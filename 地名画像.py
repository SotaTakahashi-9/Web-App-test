import streamlit as st
import openai
import os

# 環境変数からAPIキーを設定
openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_image_description(place_name):
    # GPT-4を使用して、地名に基づいたイメージの絵の説明を日本語で生成
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたは高度な知識を持つアシスタントです。"},
            {"role": "user", "content": f"{place_name}を表す画像について、約200文字で日本語で説明してください。またあなたはgpt4ですか？"},
        ],
    )
    return response.choices[0].message['content']

def main():
    st.title('地名')
    
    place_name = st.text_input('地名を入力してください:')
    
    if st.button('説明を生成'):
        description = generate_image_description(place_name)
        st.write(description)

        # ここで、説明文に基づいて画像を生成し、それを表示する処理を追加する
        # 例: image_url = generate_image(description)
        # st.image(image_url)

if __name__ == '__main__':
    main()
