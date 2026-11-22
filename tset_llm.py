import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent/".env")


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("BASE_URL"),
    timeout=(3,120),
)

def call_llm() -> str:
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[
                {
                    "role": "system",
                    "content": "你是一个资深的需求分析师"
                },
                {
                    "role": "user", 
                    "content": "请用一个标准的用户故事格式来描述:用户想要用微信来登录系统"
                }
            ],
            max_tokens=1024,
            temperature=0.7,
            stream=False,
            extra_body={
                "thinking": {
                    "type": "disabled"
                    }
                },
        )
    except Exception as e:
        print(f"调用失败，报错信息如下{e}")
        return ""
    
    message=response.choices[0].message
    return message.content or ""

if __name__ == "__main__":
    content = call_llm()
    if content:
        print("\n大模型的回复如下:")
        print(content)