
import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "write python code to find factorial of first 10 natural numbers."}
  ]
)

print(completion.choices[0].message["content"]) # type: ignore
