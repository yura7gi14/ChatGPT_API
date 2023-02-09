import openai
        
openai.api_key = "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"
model_engine = "text-davinci-003"
prompt = 'プログラミングが上達するコツを教えて'

completion = openai.Completion.create(
engine=model_engine,
prompt=prompt,
max_tokens=1024,
n=1,
stop=None,
temperature=0.5,
)

response = completion.choices[0].text
print(response)