import json

from openai import OpenAI
from core.config import config


PROMPT = """
원영적 사고란 부정적인 상황에서 긍정적인 부분을 찾아내는 사고이다.
부정적 생각: "다음 주 여행 가는데 비 온대"
원영적 사고: "다음 주 여행 가는데 비 온대. 무더위를 식혀주니 🤭🤭 완전 럭키비키잖앙 🍀"

부정적 생각: "업무 시작한 지 3일 만에 일이 쏟아지다니!"
원영적 사고: "업무 시작한 지 3일 만에 일이 쏟아지다니! 내가 신입치고 잘하는 편인가? 🤭🤭 완전 럭키비키잖앙 🍀"

다음 부정적 말을 하면 원영적 사고로 바꿔줘. 문장의 마지막은 "🤭🤭 완전 럭키비키잖앙 🍀" 으로 끝나야 해.

부정적 말: {negative}
"""

FORMAT = """
JSON 형식으로 답해줘
{
  "thinking": 원영적 사고로 바꾼 말
}
"""

client = OpenAI(
    api_key=config.openai_key,
)


def create_thinking(negative: str) -> str:
    prompt = PROMPT.format(negative=negative) + FORMAT
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt }],
        response_format={"type": "json_object"},
    )
    content = completion.choices[0].message.content
    return json.loads(content).get('thinking', '')
