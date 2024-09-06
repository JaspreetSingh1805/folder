from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
root = Tk()
root.title("Translator App")
translator = Translator()
# Function to translate text
def translate_text():
    # Get the input text from the Entry widget
    input_text = input_entry.get()
    
    # Translate the text to the selected language
    translated = translator.translate(input_text, dest=language_var.get())
    
    # Update the output Label with the translated text
    output_label.config(text=translated.text)

# Language options from Googletrans
language_var = StringVar(value='en')  # Default language (English)
languages = list(LANGUAGES.values())

# Create a Label for the input text
input_label = Label(root, text="Enter text to translate:")
input_label.pack(pady=5)

# Create an Entry widget for text input
input_entry = Entry(root, width=100)
input_entry.pack(pady=5)

# Create a Label for the language selection
language_label = Label(root, text="Select language:")
language_label.pack(pady=5)

# Create a ComboBox for selecting the target language
language_combo = ttk.Combobox(root, textvariable=language_var, values=languages)
language_combo.pack(pady=5)

# Create a Button to trigger the translation
translate_button = Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Create a Label to display the translated text
output_label = Label(root, text="", wraplength=300)
output_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()