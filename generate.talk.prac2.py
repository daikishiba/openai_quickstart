from openai import OpenAI

client = OpenAI()

# 会話の履歴を保持するための変数
conversation_history = [
    {'role': 'system', 'content': '関西弁で会話する陽気な関西人です'}
]

while True:
    # コマンドラインからユーザーの入力を受け取る
    user_input = input("enter prompt: ")

    # 'exit'と入力したら会話を終了
    if user_input.lower() == 'exit':
        print("会話を終了します。")
        break

    # ユーザーの質問を会話履歴に追加
    conversation_history.append({'role': 'user', 'content': user_input})

    # OpenAIのAPIを呼び出して応答を取得
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=conversation_history
    )

    # 応答を取得して表示
    bot_response = response.choices[0].message.content
    print(f"AI: {bot_response}")

    # 応答を会話履歴に追加
    conversation_history.append({'role': 'assistant', 'content': bot_response})

