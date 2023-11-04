import os

package_dir = os.path.dirname(os.path.abspath(_file_))
translate_path = os.path.join(package_dir, 'translate')

# Rest of the code goes here...
import tkinter as tk
from googletrans import Translator, LANGUAGES
from langdetect import detect

def translate_text():
    source_text = source_entry.get()
    
    # Detect the source language
    detected_language = detect(source_text)
    
    if detected_language in LANGUAGES:
        target_language = target_language_var.get().split(' - ')[0]

        if target_language in LANGUAGES:
            translated_text = translate(source_text, target_language)
            result_text.delete(1.0, tk.END)  # Clear previous text
            result_text.insert(tk.END, translated_text)

            # Add the translation to the history
            history_listbox.insert(0, translated_text)
            
            # Save the translation to the local history file
            save_to_history(translated_text)
        else:
            result_text.delete(1.0, tk.END)  # Clear previous text
            result_text.insert(tk.END, "Invalid target language code.")
    else:
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, "Language detection failed. Please enter text in a supported language.")
    
    # Update the detected language label
    detected_language_label.config(text=f"Detected Language: {LANGUAGES[detected_language]}")

def copy_to_clipboard():
    translated_text = result_text.get(1.0, tk.END)
    root.clipboard_clear()
    root.clipboard_append(translated_text)
    root.update()

def translate(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, src='auto', dest=target_language)
    return translated_text.text

def save_to_history(translation):
    with open("translation_history.txt", "a", encoding="utf-8") as history_file:
        history_file.write(translation + "\n")

def load_history():
    try:
        with open("translation_history.txt", "r", encoding="utf-8") as history_file:
            history = history_file.readlines()
            for translation in history:
                history_listbox.insert(tk.END, translation.strip())
    except FileNotFoundError:
        pass

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Styling
root.geometry("400x550")
root.configure(bg="#f0f0f0")

# Create and configure the source text entry
source_label = tk.Label(root, text="Enter the text to translate:", bg="#f0f0f0", font=("Helvetica", 12))
source_label.pack(pady=(20, 5))
source_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
source_entry.pack(pady=5)

# Create a label to display the detected language
detected_language_label = tk.Label(root, text="", bg="#f0f0f0", font=("Helvetica", 12))
detected_language_label.pack()

# Create and configure the target language dropdown
target_label = tk.Label(root, text="Select the target language:", bg="#f0f0f0", font=("Helvetica", 12))
target_label.pack()
target_language_var = tk.StringVar()
target_language_var.set("en - English")  # Default language is English
target_language_menu = tk.OptionMenu(root, target_language_var, *[f"{code} - {lang}" for code, lang in LANGUAGES.items()])
target_language_menu.pack(pady=5)

# Create and configure the translate button
translate_button = tk.Button(root, text="Translate", command=translate_text, bg="#007BFF", fg="#ffffff", font=("Helvetica", 12))
translate_button.pack(pady=10)

# Create a Text widget to display the translated text
result_text = tk.Text(root, height=6, width=40, font=("Helvetica", 12))
result_text.pack(pady=10)

# Create a button to copy translated text to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#007BFF", fg="#ffffff", font=("Helvetica", 12))
copy_button.pack(pady=10)

# Create a history listbox to display previous translations
history_label = tk.Label(root, text="Translation History:", bg="#f0f0f0", font=("Helvetica", 12))
history_label.pack()
history_listbox = tk.Listbox(root, height=4, width=40, font=("Helvetica", 12))
history_listbox.pack(pady=10)

# Load the translation history from the local file
load_history()

# Start the Tkinter main loop
root.mainloop()