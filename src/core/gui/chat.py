import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("CHAT")
root.geometry("400x400")
root.resizable(False, False)

chat_frame = customtkinter.CTkFrame(master = root)
chat_frame.grid(row = 0, column = 0)

scrollbar = customtkinter.CTkScrollbar(master = chat_frame)
messages = customtkinter.CTkTextbox(master = chat_frame, state = customtkinter.DISABLED, width = 370, height = 340, yscrollcommand = scrollbar.set)
messages.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

entry = customtkinter.CTkEntry(master = chat_frame, width = 320)
entry.grid(row = 1, column = 0)

button = customtkinter.CTkButton(master = chat_frame, width = 20, text = "Send")
button.grid(row = 1, column = 1)

root.mainloop()