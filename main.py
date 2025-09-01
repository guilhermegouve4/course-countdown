from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk

FINAL_DATE = datetime(2025, 11, 20, 23, 0, 0)


def update_counter():
    now = datetime.now()
    time_left = FINAL_DATE - now

    if time_left.total_seconds() <= 0:
        countdown_label.config(text="ACABOOOOOOOOOOOOO")
        return

    days = time_left.days
    seconds_left = time_left.seconds
    hours, seconds_left = divmod(seconds_left, 3600)
    minutes, seconds = divmod(seconds_left, 60)

    formatted_text = f"Faltam:\n{days} dias\n{hours:02d}h {minutes:02d}m {seconds:02d}s"

    countdown_label.config(text=formatted_text)

    window.after(1000, update_counter)


window = tk.Tk()
window.overrideredirect(True)
window.title("Contagem final")
window.geometry("300x300")
window.resizable(False, False)
window.configure(bg="#000000")

countdown_label = tk.Label(
    window,
    text="Carregando...",
    font=("helvetica", 24, "bold"),
    bg="#000000",
    fg="#FFFFFF",
)
countdown_label.pack(pady=20)

try:
    img_pil = Image.open("python-gif.gif")
    img_pil = img_pil.resize((100, 100), Image.LANCZOS)
    python_logo = ImageTk.PhotoImage(img_pil)

    logo_label = tk.Label(
        window,
        image=python_logo,
        bg="#000000",
    )
    logo_label.pack(pady=10)

except FileNotFoundError:
    print("Erro: O arquivo 'python-gif.gif' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao carregar a imagem: {e}")

update_counter()

window.mainloop()