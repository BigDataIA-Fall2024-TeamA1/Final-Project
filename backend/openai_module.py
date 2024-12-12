import openai
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 设置 OpenAI API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_summary(prompt):
    """
    根据给定的提示词生成摘要报告。
    """
    try:
        # 调用 OpenAI Chat API
        response = openai.chat.completions.create(  # 保持您指定的方式
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "This is a legal case. Please generate a summary report to help the lawyer understand the full case and details."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1500,
            temperature=0.7,
        )

        # 提取生成的内容
        if hasattr(response, "choices") and response.choices:
            advice = response.choices[0].message.content
            return advice
        else:
            return f"Unexpected response format: {response}"

    except Exception as e:
        return f"Error communicating with OpenAI: {e}"




def generate_strategy(document_text):
    """
    根据给定的文档文本生成战略建议。
    """
    try:
        prompt = f"""
        Based on the following content, generate strategic advice:
        
        {document_text}
        """
        # 调用 OpenAI Chat API
        response = openai.chat.completions.create(  # 保持您指定的方式
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an experienced legal strategist providing actionable advice."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1500,
            temperature=0.7,
        )

        # 提取生成的内容
        if hasattr(response, "choices") and response.choices:
            strategy = response.choices[0].message.content
            return strategy
        else:
            return f"Unexpected response format: {response}"

    except Exception as e:
        return f"Error communicating with OpenAI: {e}"