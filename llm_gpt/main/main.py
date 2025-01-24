import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "너는 옷 코디네이터야 오늘 입을 옷을 추천해줘 그리고 이모티콘을 사용해"

messages = [{"role": "system","content":prompt}]

file_name = "testfile.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("대화 시작\n")

while True:
    user_input = input("ME :")

    if user_input.lower() == "exit":
        print("대화를 종료합니다")
        with open(file_name,"a",encoding="utf-8") as file:
            file.write("\n대화 끝\n")
        break

    messages.append({"role": "system","content":prompt})

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages
    )

    assistant_reply = response['choices'][0]['message']['content']

    print(f"AI: {assistant_reply}\n")

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"ME: {user_input}\n")
        file.write(f"AI: {assistant_reply}\n")
        file.write("\n")


    