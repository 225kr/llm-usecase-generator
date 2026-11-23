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

def generate_usecase(use_story: str) -> str:
    system_prompt="""
    你是一个资深的软件需求分析师，
    你的任务是接收用户提供的"用户故事"，将其转换为结构化的UML用例，
    请严格输出JSON格式，不要输出任何多余的解释文字，

    输出的JSON必须包含以下字段:
    - use_case_name: 用例名称
    - actors: 参与者列表（数组）
    - basic_flow: 基本流程步骤（数组）
    - extentions: 扩展流/异常情况（数组）
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user", 
                    "content": use_story
                }
            ],
            max_tokens=1024,
            temperature=0.1,
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
    use_story = input("\n请输入你的用户故事:")
    content = generate_usecase(use_story)

    print("\n大模型原始输出")
    print(content)
    print('-'*30)

    #尝试解析JSON（校验的第一步）
    try:
        #很多时候大模型输出会带有```json前缀，我们要清理一下
        clean_json_str = content.replace("```json","").replace("```","").strip()
        parse_data = json.loads(clean_json_str)
        print("\n解析JSON成功")
        print(f"用例名称:{parse_data['use_case_name']}")
        print(f"参与者:{parse_data['actors']}")
    except json.JSONDecodeError:
        print("\n大模型解析JSON格式错误!")