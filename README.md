# Text Improvement Chat

The Text Improvement Chat is a simple interactive tool that analyzes text input and suggests improvements based on a predefined list of standardized phrases. It provides users with suggestions to align their input text closer to these standard phrases.

## Getting Started

To run the Text Improvement Chat, follow these instructions:

### Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.x
- Tkinter (included in most Python installations)
- spaCy library (for natural language processing)

You can install spaCy and download the English model by running the following commands:

```
pip install spacy
python -m spacy download en_core_web_md
```

### Running the Application

1. Clone or download the code repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to start the Text Improvement Chat:

```
python text_improvement_chat.py
```

This will launch the chat window.

## How to Use

- The chat window consists of a text input field, a chat history display, and a "Send" button.

- Start by typing your text input in the text field. The initial text reads "Enter your text."

- Click inside the text input field to start typing. The placeholder text will disappear as you type.

- Click the "Send" button to analyze your input text.

- The system will provide suggestions based on the similarity of your input text to a list of predefined standardized phrases. The suggestions will appear in the chat history display.

- The chat history will show your input as "You:" and the system's suggestions as "System."

## Customization

You can customize the predefined list of standardized phrases by modifying the `standardized_phrases` list in the code. Add or remove phrases as needed to match your specific requirements.

## Adjusting Similarity Threshold

The code uses a similarity score threshold of 0.7 to determine whether a suggestion should be provided. You can adjust this threshold in the `handle_user_input` function by changing the value of `if similarity_score > 0.7:` to a different value as per your preference.

## Styling

The chat window is styled with a dark theme. You can further customize the styling by modifying the `style.configure` calls in the code.

## Author

Talgat Demezhan

## Acknowledgments

- [spaCy](https://spacy.io/) - Natural Language Processing library
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python GUI library
