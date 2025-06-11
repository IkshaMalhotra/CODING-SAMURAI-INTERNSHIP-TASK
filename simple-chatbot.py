import tkinter as tk
import random
import datetime
import webbrowser

def chatbot_response(user_input):
    lowered = user_input.lower().strip()
    if any(word in lowered for word in ['hello', 'hi', 'hey', 'hy' , 'hola' ]):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I assist you today?"])
    elif "your name" in lowered or "who are you" in lowered:
        return "I'm RuleBot, your assistant created in Python."
    elif "how are you" in lowered:
        return "I'm functioning as expected! How can I help you today?"
    elif "help" in lowered:
        return ("Here’s what I can do:\n"
                "- Greet you\n- Share jokes or motivation\n"
                "- Tell the date/time\n- Suggest resources\n"
                "- And more!")
    elif "date" in lowered or "today" in lowered:
        return f"Today is {datetime.datetime.now().strftime('%A, %d %B %Y')}."
    elif "time" in lowered:
        return f"It's {datetime.datetime.now().strftime('%I:%M %p')}."
    elif "joke" in lowered:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "What did the Python say to the C programmer? You’ve got no class.",
        ])
    elif "motivate" in lowered or "motivation" in lowered:
        return random.choice([
            "Stay positive, work hard, and make it happen.",
            "You're capable of amazing things. Keep pushing!",
        ])
    elif "what can you do" in lowered or "features" in lowered:
        return "I can answer basic questions, give jokes, date/time, and guide you when I can't help directly."
    elif "good morning" in lowered:
        return "Good morning! Wishing you a productive day!"
    elif "good night" in lowered:
        return "Good night! Sleep well and recharge."
    elif lowered in ['ok', 'okay', 'cool', 'great', 'perfect', 'fine', 'alright', 'awesome']:
        return random.choice(["Glad to hear that!", "Awesome!", "Great! Let me know if you need anything else."])
    elif "thank" in lowered:
        return "You're most welcome!"
    elif lowered in ['bye', 'goodbye', 'see you']:
        return "Goodbye! Have a great day!"
    else:
        redirect_links = [
            "https://chat.openai.com",
            "https://www.google.com/search?q=" + lowered.replace(" ", "+")
        ]
        return ("I'm sorry, I didn't understand that. "
                "You can try rephrasing it or check it out online:\n"
                f"- ChatGPT: {redirect_links[0]}\n"
                f"- Google Search: {redirect_links[1]}")

def send_message():
    user_text = user_entry.get().strip()
    if not user_text:
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_text}\n")
    bot_reply = chatbot_response(user_text)
    chat_log.insert(tk.END, f"Bot: {bot_reply}\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)
    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("RuleBot - AI Assistant")
root.geometry("480x580")
root.resizable(False, False)
root.configure(bg="#f9f9fb")

chat_log = tk.Text(root, bg="white", font=("Segoe UI", 11), wrap="word", padx=10, pady=10)
chat_log.pack(padx=15, pady=(15, 0), fill=tk.BOTH, expand=True)
chat_log.config(state=tk.DISABLED)

input_frame = tk.Frame(root, bg="#f9f9fb")
input_frame.pack(padx=15, pady=10, fill=tk.X)

user_entry = tk.Entry(input_frame, font=("Segoe UI", 12), relief=tk.FLAT, bg="#efefef")
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
user_entry.bind("<Return>", lambda e: send_message())

send_btn = tk.Button(input_frame, text="Send", command=send_message, bg="#4a90e2", fg="white",
                     font=("Segoe UI", 10, "bold"), padx=20, pady=5)
send_btn.pack(side=tk.RIGHT)

chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "Bot: Hello! I'm RuleBot. Type 'help' to know what all I can do.\n\n")
chat_log.config(state=tk.DISABLED)

root.mainloop()
