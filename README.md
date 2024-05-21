This is my Ai personal assistant
This repository consists the python code for "AI assistant 

1. **talktoai(query)**:
    - **Purpose**: Communicates with an AI model via an API to get a response based on the input query.
    - **How it works**: 
        - Updates the payload with the new query.
        - Sends a POST request to the specified URL with the payload and headers.
        - Parses the JSON response.
        - Calls the `speak` function to vocalize the AI-generated text.

2. **speak(audio)**:
    - **Purpose**: Converts text to speech.
    - **How it works**: Uses `pyttsx3` to convert the text passed as `audio` into spoken words and waits until speaking is finished.

3. **time()**:
    - **Purpose**: Announces the current time.
    - **How it works**: 
        - Gets the current time using `datetime.datetime.now().strftime("%H:%M:%S")`.
        - Calls the `speak` function to vocalize the time.

4. **date()**:
    - **Purpose**: Announces the current date.
    - **How it works**: 
        - Gets the current year, month, and day using `datetime.datetime.now()`.
        - Calls the `speak` function to vocalize the day, month, and year.

5. **wish()**:
    - **Purpose**: Greets the user based on the current time of day.
    - **How it works**: 
        - Determines the current hour using `datetime.datetime.now().hour`.
        - Decides the appropriate greeting (morning, afternoon, evening, night) and calls the `speak` function to vocalize the greeting followed by "How can I help you today?"

6. **inp()**:
    - **Purpose**: Captures and processes spoken input from the user.
    - **How it works**: 
        - Uses `speech_recognition` to listen to the microphone and recognize speech.
        - If recognition fails, asks the user to repeat.
        - Returns the recognized text.

7. **screenshot()**:
    - **Purpose**: Takes a screenshot of the current screen.
    - **How it works**: 
        - Uses `pyautogui.screenshot()` to capture the screen.
        - Saves the screenshot to a specified location.

8. **youtube(elem)**:
    - **Purpose**: Plays a YouTube video based on the search term.
    - **How it works**: Uses `pywhatkit.playonyt` to search and play a video on YouTube.

9. **browse(ques)**:
    - **Purpose**: Performs a web search.
    - **How it works**: Uses `pywhatkit.search` to search the web based on the query.

10. **whatsapp(t, msg)**:
    - **Purpose**: Sends an instant WhatsApp message.
    - **How it works**: Uses `pywhatkit.sendwhatmsg_instantly` to send a message to the specified number.

11. **sendemail(to, msg)**:
    - **Purpose**: Sends an email.
    - **How it works**: 
        - Configures and connects to an SMTP server using `smtplib`.
        - Logs into the Gmail account.
        - Sends the email and closes the connection.

12. **Main execution block** (`if __name__ == "__main__":`):
    - **Purpose**: Main loop that listens for commands and executes corresponding functions.
    - **How it works**: 
        - Calls `wish` to greet the user.
        - Continuously listens for commands via `inp()`.
        - Executes different functions based on the recognized command, such as telling time, date, Wikipedia summary, taking a screenshot, playing YouTube, browsing, sending WhatsApp messages, sending emails, remembering data, retrieving remembered data, controlling music playback, and shutting down or restarting the system.
        - If a command is not recognized, it defaults to sending the query to the AI for a response via `talktoai`.

The script combines various libraries and functionalities to create an interactive voice assistant capable of performing a wide range of tasks.
