import os
from phoenix.otel import register

import dspy

register(
    auto_instrument=True,
    batch=True,
    endpoint="http://localhost:6006/v1/traces",    
    project_name=os.environ.get("PROJECT_NAME", "dspy-demo"),
    verbose=False
)

lm = dspy.LM("openai/gpt-4.1-nano", cache=False)
dspy.configure(lm=lm)

program = dspy.Predict(dspy.Signature("question: str -> answer: str").with_instructions("Answer only the question. Do not repeat the question or provide any additional information."))

def main():
    prediction = program(question="What is the capital of France?")
    print(prediction.answer)

if __name__ == "__main__":
    main()
