import customtkinter

from infra.widgets.custom_widgets import ChatWidgets, LoginWidgets

class ChatFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs) -> None:
        
        super().__init__(*args, **kwargs)
        self.pack(pady = 10, padx = 10, fill = "both", expand = True)

        self.chat_widgets = ChatWidgets(self)
        self.login_widgets = LoginWidgets(self)

        self.display_widgets(self.login_widgets)
        self.login_widgets.button._command = lambda: self.destroy_and_display(self.login_widgets, self.chat_widgets)

    def display_widgets(self, widget) -> None:

        widget.create_widgets()

    def destroy_widgets(self, widget) -> None:

        for widget in widget.get_widgets():
            widget.destroy()

    def destroy_and_display(self, to_destroy_widget, to_display_widget) -> None:

        self.destroy_widgets(to_destroy_widget)
        self.display_widgets(to_display_widget)