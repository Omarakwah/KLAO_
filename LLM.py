from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Get Google API key
Google_API_KEY = os.environ["GOOGLE_API_KEY"]

# Define the prompt template
template = """You are AI Assitant who expert in german language

Your goal is to :
Add contextual explanations to help readers understand large numbers better.
Use visual comparisons to make abstract quantities more relatable.
to this {raw_text}
Example:
1 Million Euro → So viel Geld, dass man 100 Autos kaufen könnte
10.000 Besucher → So viele Menschen, wie in ein großes Fußballstadion passen
30 Prozent der Fläche → Ein Drittel, also ein Stück von drei gleich großen
Teilen
250 Kilogramm → So schwer wie ein großer Kühlschrank
Your answer shoud not exceed 1 line
Reply with complete sentence according to {raw_text} sentence
Please Don't invent numbers
"""
prompt = ChatPromptTemplate.from_template(template)

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    max_tokens=None,
    timeout=None,
    google_api_key=Google_API_KEY
)