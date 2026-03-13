import openai
from prompts.ddr_prompt import DDR_PROMPT

def generate_ddr(data):

    prompt = DDR_PROMPT + data

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a structural inspection expert"},
            {"role":"user","content":prompt}
        ],
        temperature=0.2
    )

    return response["choices"][0]["message"]["content"]
