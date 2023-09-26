import spacy
import tkinter as tk
from tkinter import ttk 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# spaCy model for creating list of standardized phrases
nlp = spacy.load("en_core_web_md")

standardized_phrases = [
    "Optimal performance",
    "Utilise resources",
    "Enhance productivity",
    "Conduct an analysis",
    "Maintain a high standard",
    "Implement best practices",
    "Ensure compliance",
    "Streamline operations",
    "Foster innovation",
    "Drive growth",
    "Leverage synergies",
    "Demonstrate leadership",
    "Exercise due diligence",
    "Maximize stakeholder value",
    "Prioritise tasks",
    "Facilitate collaboration",
    "Monitor performance metrics",
    "Execute strategies",
    "Gauge effectiveness",
    "Champion change",
]

# Function to find the most similar standardized phrase for a given input phrase
def get_most_similar_standardized_phrase(input_phrase, standardized_phrases):
    vectorizer = CountVectorizer().fit_transform([input_phrase] + standardized_phrases)
    vectors = vectorizer.toarray()
    cosine_similarities = cosine_similarity(vectors)
    similarity_scores = cosine_similarities[0][1:]

    most_similar_index = similarity_scores.argmax()
    most_similar_phrase = standardized_phrases[most_similar_index]
    similarity_score = similarity_scores[most_similar_index]

    return most_similar_phrase, similarity_score

# Function to process user input and provide suggestions
def process_user_input(input_text):
    suggestions = []
    doc = nlp(input_text)
    for sentence in doc.sents:
        for token in sentence:
            if not token.is_stop and token.is_alpha:
                original_phrase = token.text
                most_similar_phrase, similarity_score = get_most_similar_standardized_phrase(
                    original_phrase, standardized_phrases
                )
                if similarity_score > 0.7:  # Adjust the similarity score threshold as needed
                    suggestions.append(
                        {
                            "Original": original_phrase,
                            "Suggested": most_similar_phrase,
                            "Similarity": similarity_score,
                        }
                    )
    return suggestions

# Function to handle user input and display suggestions
def handle_user_input(event=None):
    user_input = input_entry.get()
    suggestions = process_user_input(user_input)

    # Display user message and suggestions
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\n", "user")
    for suggestion in suggestions:
        chat_history.insert(tk.END, f"System:\nOriginal text: \"{suggestion['Original']}\" Suggestions: \"{suggestion['Suggested']}\" (Similarity: {suggestion['Similarity']:.2f})\n", "system_suggestion")
    chat_history.config(state=tk.DISABLED)

    # Clear input field and reset placeholder
    input_entry.delete(0, tk.END)
    input_entry.insert(0, "Enter your text")
    input_entry.icursor(0)  # Move the cursor to the beginning

# Clear the default placeholder text when clicked
def clear_placeholder(event):
    current_text = input_entry.get()
    if current_text == "Enter your text":
        input_entry.delete(0, tk.END)
        input_entry.icursor(0)

# Tkinter window for the chat
window = tk.Tk()
window.title("Text Improvement Chat")

style = ttk.Style()
style.configure("TFrame", background="gray15")
style.configure("TButton", background="gray20", foreground="white", font=("Helvetica", 12, "bold"))
style.configure("TLabel", background="gray15", foreground="white", font=("Helvetica", 12))
style.configure("TEntry", background="gray30", font=("Helvetica", 12))

# Chat history display
chat_history = tk.Text(window, state=tk.DISABLED, bg="gray15", fg="white")
chat_history.tag_configure("user", foreground="white")
chat_history.tag_configure("system_suggestion", foreground="green")
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Text input with placeholder for user
input_entry = ttk.Entry(window, width=50, font=("Helvetica", 12))
input_entry.pack(padx=10, pady=5)
input_entry.insert(0, "Enter your text")
input_entry.icursor(0)  # Move the cursor to the beginning

# Disappear the "Enter your text" placeholder
input_entry.bind("<FocusIn>", clear_placeholder)

# Send button
send_button = ttk.Button(window, text="Send", command=handle_user_input)
send_button.pack(padx=10, pady=5)

# Run
window.mainloop()
