import customtkinter
import sys


def mainPage():

    def destroy():
        app.quit()
        app.destroy()

    app = customtkinter.CTk()
    app.title("Коя е звездата")
    app_width = 300
    app_height = 200

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.grid_columnconfigure(0, weight=1)



    # Изчисляваме координатите за центриране
    x = (screen_width // 2) - (app_width // 2)  +100
    y = (screen_height // 2) - (app_height // 2)

    # Задаваме геометрията с централни координати
    app.geometry(f"{app_width}x{app_height}+{x}+{y}")

    startButton = customtkinter.CTkButton(app, text="Старт", command=destroy)
    exitButton = customtkinter.CTkButton(app, text="Изход", command=sys.exit)


    startButton.grid(row=0, column=0, padx=20, pady=20)
    exitButton.grid(row=1, column=0, padx=20, pady=20)


    app.mainloop()

