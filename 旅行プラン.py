import streamlit as st
from dotenv import load_dotenv
import os
import key
import openai

# 環境変数を読み込む

# OpenAIのAPIキーをセットする
openai.api_key =os.getenv("OPENAI_API_KEY")

def fetch_plan_details(start, destination):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "出発地と目的地に基づく旅行プランの情報（費用（円）、所要時間、プラン詳細）を提供する。"},
                {"role": "user", "content": f"出発地: {start}, 目的地: {destination}についての旅行プランを教えてください。"}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

# StreamlitアプリのUI
st.title('旅行プランナー')

# ユーザー入力
start = st.text_input('出発地', '東京')
destination = st.text_input('目的地', '京都')

if st.button('プランを取得'):
    plan_details = fetch_plan_details(start, destination)
    st.write(plan_details)


