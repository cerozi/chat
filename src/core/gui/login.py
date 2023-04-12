import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("LOGIN")
root.geometry("400x400")
root.resizable(False, False)

login_frame = customtkinter.CTkFrame(master = root)
login_frame.pack(expand = True)

label = customtkinter.CTkLabel(master = login_frame, text = "Nickname")
label.grid(row = 0, column = 0, padx = 10, pady = 10)

entry = customtkinter.CTkEntry(master = login_frame, placeholder_text = "Enter your nickname...")
entry.grid(row = 1, column = 0, padx = 10, pady = 10)

button = customtkinter.CTkButton(master = login_frame, text = "Join", width = 70)
button.grid(row = 2, column = 0, padx = 10, pady = 10)

root.mainloop()