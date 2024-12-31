# README

## Overview
This repository provides a Python script for simplifying and contextualizing large numbers and percentages in German text. The script leverages the LangChain framework and Google's Gemini-1.5 model to provide contextual explanations, making abstract quantities more relatable and easier to understand.

---

## Features
- **Simplify Large Numbers**: Automatically rounds and simplifies large numbers.
- **Percentage Explanations**: Converts percentages into relatable phrases (e.g., "50%" becomes "die Hälfte").
- **Contextual Explanations**: Uses a Language Model (LLM) to add context and visual comparisons for better understanding.
- **Customizable Prompts**: Easily adjust the LLM prompt for different use cases.
- **Test Cases**: A set of sample sentences is included for testing the functionality.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add the Google API Key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

---

## Usage

### Run the Script
To execute the script, run the following command:
```bash
python main.py
```

### Input and Output
The script processes German text and provides simplified and contextualized sentences.

#### Example Input:
```text
324.620,22 Euro wurden gespendet.
25 Prozent der Bevölkerung sind betroffen.
```

#### Example Output:
```text
etwa 325.000 Euro wurden gespendet. So viel Geld, dass man 100 Autos kaufen könnte.
jeder Vierte der Bevölkerung ist betroffen.
```

---

## File Structure
- `main.py`: The main script that performs the text processing and calls the LLM.
- `requirements.txt`: Lists all Python dependencies.
- `.env`: Environment variables file (user-created, not included in the repo).

---

## Customization

### Modify the Prompt
The LLM prompt can be adjusted in the `template` variable within the script:
```python
template = """You are AI Assistant who is an expert in German language...
..."""
```

### Test Cases
You can update or add test cases by modifying the `test_cases` list in the script:
```python
test_cases = [
    "324.620,22 Euro wurden gespendet.",
    "1.897 Menschen nahmen teil.",
    ...
]
```

---

## Dependencies
- **LangChain**: For building and managing the LLM workflow.
- **Google Generative AI**: For contextual explanations and number simplification.
- **dotenv**: For managing environment variables.

---

## Troubleshooting
1. **LLM Errors**: Ensure the Google API key is valid and has sufficient permissions.
2. **Regex Matching Issues**: Double-check the regular expressions used for number and percentage detection.
3. **Unexpected Outputs**: Enable debugging logs in the `contextualize_numbers` function to inspect inputs and outputs.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for improvements or bug fixes.



