# Language-Translator
Language Translator Application
This Python script is a simple language translator application that utilizes the Tkinter library for creating a graphical user interface (GUI) and leverages the Google Translate API for translating text from one language to another. Additionally, it employs the langdetect library to detect the language of the input text.

Overview
The main goal of this application is to allow users to enter a piece of text, detect its language, and then translate it into a different language of their choice. It provides a user-friendly interface for this purpose.

Getting Started
To run the Language Translator Application, you need to have Python installed on your system. Additionally, you must install some required Python packages.

Using the Application
Upon running the application, a graphical user interface (GUI) will appear. Here is a brief explanation of the various components of the GUI:

1. Input Text
   You can enter the text you want to translate in the text entry field. The application will automatically detect the language of the input text.
2. Detected Language
   The detected language label will display the language of the input text.
3. Target Language
   You can select the target language you want the text to be translated into using the dropdown menu.
4. Translate Button
   Click the "Translate" button to initiate the translation process. The translated text will be displayed in the text area below.
5. Copy to Clipboard
   You can use the "Copy to Clipboard" button to copy the translated text to your system's clipboard for easy pasting.
6. Translation History
   The application maintains a history of your translations in the "Translation History" listbox.
7. Loading Translation History
   When you open the application, it will load previous translations from a local file named "translation_history.txt" if it exists.

Technical Details
The code uses the Google Translate API to perform translations, with auto-language detection for the source language. The detected source language is displayed in the GUI.
The translated text is also saved to a local file named "translation_history.txt" for future reference. You can access your translation history from the application.

Dependencies
1. Python 3.x
2. googletrans 4.0.0-rc1
3. langdetect

Credits
This application was created by Divit Sakhare. It is provided as an open-source project and can be customized and extended as needed. If you encounter any issues or have suggestions for improvements, please feel free to contribute to the project or report any bugs.
