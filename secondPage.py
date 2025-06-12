import customtkinter as ctk

def secondPage():
    def start():
        try:
            rounds = int(entry1.get())
            difficulty = int(entry2.get())
            app.rounds = rounds
            app.difficulty = difficulty
            app.destroy()
        except ValueError:
            label.configure(text="Моля въведете валидни числа.")

    app = ctk.CTk()
    app_width, app_height = 300, 200
    screen_width, screen_height = app.winfo_screenwidth(), app.winfo_screenheight()
    x = (screen_width // 2) - (app_width // 2) + 100
    y = (screen_height // 2) - (app_height // 2)
    app.geometry(f"{app_width}x{app_height}+{x}+{y}")
    app.title("Настройки")

    app.grid_columnconfigure(0, weight=1)

    entry1 = ctk.CTkEntry(app, placeholder_text="Рундове")
    entry1.pack(pady=20)

    entry2 = ctk.CTkEntry(app, placeholder_text="Трудност (FOV)")
    entry2.pack(pady=20)

    button = ctk.CTkButton(app, text="Старт", command=start)
    button.pack(pady=10)

    label = ctk.CTkLabel(app, text="")
    label.pack()

    app.mainloop()

    return getattr(app, "rounds", None), getattr(app, "difficulty", None)

    

