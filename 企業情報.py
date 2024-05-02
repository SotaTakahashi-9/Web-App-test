import streamlit as st
import openai
import os

# OpenAI APIキーを設定
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_company_info(company_name):
    # プロンプトを日本語で記述
    prompt = f"{company_name}について詳細な情報を教えてください。次の詳細を含めてください：\n- 資本金\n- 売上\n- 従業員数\n- 業務内容（約300字）\n- DXの取り組み状況（約300字）\n- 業務内容とDXの取り組み状況を踏まえたAI活用の提案（約300字）"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  # モデル指定
        messages=[
            {"role": "system", "content": "You are a helpful assistant who responds in Japanese."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']

def display_info(info_text):
    st.text("GPTからの回答:")
    st.text(info_text)

    data_points = {
        "資本金": "資本金が利用できません",
        "売上": "売上が利用できません",
        "従業員数": "従業員数が利用できません",
        "業務内容": "業務内容が利用できません",
        "DXの取り組み状況": "DXの取り組み状況が利用できません",
        "AI活用の提案": "AI活用の提案が利用できません"
    }
    
    # 応答テキストから情報を抽出
    for key in data_points.keys():
        start = info_text.find(key)
        if start != -1:
            start += len(key) + 1  # キーの長さとコロンを考慮
            end = info_text.find("\n", start)
            if end == -1:
                end = len(info_text)
            data_points[key] = info_text[start:end].strip()

    for key, value in data_points.items():
        st.write(f"{key}: {value}")

def main():
    st.title("会社情報取得アプリ")
    company_name = st.text_input("会社名を入力してください", "")
    if st.button("情報取得"):
        info_text = get_company_info(company_name)
        if info_text:
            display_info(info_text)
        else:
            st.write("情報の取得に失敗しました。")

if __name__ == "__main__":
    main()
