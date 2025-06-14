import customtkinter as ctk
from pandas import read_excel
from random import randint
from namirane import centrirane  # Твоят модул

def thirdPage(rounds1: int):
    # Зареждаме звездите от Excel
    stars = read_excel("C:/Users/user/Desktop/python1/StellariumIgra/nai-iarki-zvezdi_full.xlsx")

    # Глобални променливи
    global rounds, right_answers, star, answered
    rounds = rounds1
    right_answers = 0
    answered = False

    # Избор на произволна звезда
    def pick_new_star():
        global star, answered
        star = stars.iloc[randint(0, len(stars) - 1)]
        answered = False
        try:
            ra = float(star[stars.columns[4]])
            dec = float(star[stars.columns[5]])
            centrirane(ra, dec)
        except Exception as e:
            print(f"Грешка при центриране на звезда: {e}")

    # Проверка на въведения отговор
    def check():
        global right_answers, answered

        if answered:
            return  # Няма повторна проверка

        user_input = entry.get().strip().lower()
        correct_name = str(star[stars.columns[0]]).strip().lower()

        if user_input == correct_name:
            label.configure(text="✅ Поздравления! Познахте звездата.")
            right_answers += 1
        else:
            label.configure(text=f"❌ Грешно! Правилното име е: {star[stars.columns[0]]}")

        answered = True
        button_check.configure(state=ctk.DISABLED)  # Деактивиране на бутона

    # Следващ рунд или край на играта
    def next():
        global rounds, answered
        rounds -= 1

        if rounds <= 0:
            label.configure(
                text=f"🎉 Играта приключи!\nПознати звезди: {right_answers} от {rounds1}"
            )
            entry.configure(state=ctk.DISABLED)
            button_check.configure(state=ctk.DISABLED)
            button_next.configure(state=ctk.DISABLED)
        else:
            pick_new_star()
            entry.delete(0, ctk.END)
            label.configure(text=f"Оставащи рундове: {rounds}")
            button_check.configure(state=ctk.NORMAL)  # Активира бутона отново

    # Създаване на прозореца
    app = ctk.CTk()
    app.title("Игра със звезди 🌟")
    app.geometry("400x300")
    app.grid_columnconfigure(0, weight=1)

    # Текстово поле за въвеждане
    entry = ctk.CTkEntry(app, placeholder_text="Въведи името на звездата...")
    entry.pack(pady=20, padx=40)

    # Бутон "Провери"
    button_check = ctk.CTkButton(app, text="Провери", command=check)
    button_check.pack(pady=10)

    # Бутон "Следваща"
    button_next = ctk.CTkButton(app, text="Следваща", command=next)
    button_next.pack(pady=10)

    # Етикет за съобщения
    label = ctk.CTkLabel(app, text=f"Оставащи рундове: {rounds}")
    label.pack(pady=10)

    # Стартиране с първа звезда
    pick_new_star()

    app.mainloop()
