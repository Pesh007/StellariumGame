import customtkinter as ctk
import sys
from pandas import read_excel
from random import randint
from namirane import centrirane #moi file


def thirdPage(rounds: int):

    global stars, star
    stars = read_excel("C:/Users/user/Desktop/python1/StellariumIgra/nai-iarki-zvezdi_full.xlsx")
    
    star = stars.iloc[randint(0,len(stars)-1)]
    centrirane(float(star[stars.columns[4]]), float(star[stars.columns[5]]))

    right_answers: int = 0

    def check():
        
        user_input = entry.get()

        if user_input == star[stars.columns[0]]:
            label.configure(text="Поздравления! Въведохте правилното име на звездата.")

        else:
            label.configure(text=f"Грешно! Правилното име е: {star[stars.columns[0]]}")

    def next():
        rounds -= 1
        global star
        star = stars.iloc[randint(0,len(stars)-1)]
        centrirane(float(star[stars.columns[4]]), float(star[stars.columns[5]]))

        entry.delete(0, ctk.END)
        label.configure(text=" ")
        if rounds <= 0:
            label.configure(text="Играта приключи! Поздравления!")
            entry.configure(state=ctk.DISABLED)
            button1.configure(state=ctk.DISABLED)
            button2.configure(state=ctk.DISABLED)
        else:
            label.configure(text=f"Оставащи рундове: {rounds}")
        

    app = ctk.CTk()
    app.title("Примерен интерфейс")
    app.geometry("400x250")

    # Централна конфигурация
    app.grid_columnconfigure(0, weight=1)

    # Текстово поле
    entry = ctk.CTkEntry(app, placeholder_text="Въведи нещо тук")
    entry.pack(pady=20, padx=40)

    # Бутон 1
    button1 = ctk.CTkButton(app, text="Провери", command=check)
    button1.pack(pady=10)

    # Бутон 2
    button2 = ctk.CTkButton(app, text="Следваща", command=next)
    button2.pack(pady=10)

    # Етикет за резултата
    label = ctk.CTkLabel(app, text="")
    label.pack(pady=10)

    app.mainloop()

