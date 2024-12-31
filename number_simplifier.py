import re
from math import ceil
from langchain.chains import LLMChain
from LLM import llm, prompt

# Create the LangChain chain
chain = LLMChain(llm=llm, prompt=prompt)

def simplify_numbers(raw_text):
    def round_large_numbers(match):
        number = match.group()
        # Handle numbers with commas (e.g., "324.620,22")
        number = number.replace('.', '').replace(',', '.')
        number = float(number)
        rounded_number = None

        if number >= 1000:
            rounded_number = f"etwa {int(round(number, -3))}"
        elif number >= 10:
            rounded_number = f"etwa {ceil(number)}"
        else:
            rounded_number = f"etwa {round(number, 1)}"

        return rounded_number

    def simplify_percentages(match):
        percentage = float(match.group(1))
        if percentage == 25:
            return "jeder Vierte"
        elif percentage == 50:
            return "die Hälfte"
        elif percentage == 75:
            return "drei von vier"
        elif percentage >= 90:
            return "fast alle"
        elif percentage >= 60:
            return "mehr als die Hälfte"
        elif percentage <= 15:
            return "wenige"
        else:
            return f"etwa {percentage} Prozent"

    def contextualize_numbers(raw_text):
        return chain.run({"raw_text": raw_text})

    # Round large numbers
    raw_text = re.sub(r"\b\d{1,3}(?:\.\d{3})*(?:,\d+)?\b", round_large_numbers, raw_text)

    # Simplify percentages
    raw_text = re.sub(r"(\d+(?:\.\d+)?) Prozent", simplify_percentages, raw_text)

    # Handle contextual explanations and visual comparisons using LLM
    raw_text = contextualize_numbers(raw_text)

    return raw_text