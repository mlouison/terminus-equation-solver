import os
import sys
import tkinter as tk

def resource_path(relative_path):
    """Trouve le chemin des ressources pour PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Fonction pour calculer les valeurs des équations
def calculate():
    try:
        # Récupérer les valeurs entrées par l'utilisateur
        x = int(entry_x.get())
        y = int(entry_y.get())
        z = int(entry_z.get())

        # Calculer les valeurs des équations
        equation_1 = 2 * x + 11
        equation_2 = (2 * z + y) - 5
        equation_3 = (y + z) - x

        # Afficher les résultats dans le label des résultats
        result_label.config(text="The secret code is :", fg="black")
        code_label.config(text=f"{equation_1} | {equation_2} | {equation_3}", fg="#4a8ace")
    except ValueError:
        result_label.config(text="Please enter valid integers for x, y, and z.", fg="black")
        code_label.config(text="")
    finally:
        # Réinitialiser les champs d'entrée à 0
        entry_x.delete(0, tk.END)
        entry_y.delete(0, tk.END)
        entry_z.delete(0, tk.END)
        
        # Remettre le focus sur le premier champ d'entrée
        entry_x.focus()

# Fonction pour passer à l'entrée suivante lors de l'appui sur "Entrée"
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

# Création de la fenêtre principale
root = tk.Tk()
root.title("Terminus Equation Solver")  # Modification du titre de la fenêtre
root.iconbitmap(resource_path("logo.ico"))  # Assurez-vous que 'logo.ico' est dans le même répertoire

# Définir une taille de fenêtre plus grande
root.geometry("550x300")  # Taille augmentée de 50 % environ

# Labels et champs de saisie pour x, y, et z
tk.Label(root, text="Enter the value of x:", font=("Helvetica", 18)).grid(row=0, column=0, padx=10, pady=5)
entry_x = tk.Entry(root, font=("Helvetica", 18))
entry_x.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the value of y:", font=("Helvetica", 18)).grid(row=1, column=0, padx=10, pady=5)
entry_y = tk.Entry(root, font=("Helvetica", 18))
entry_y.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the value of z:", font=("Helvetica", 18)).grid(row=2, column=0, padx=10, pady=5)
entry_z = tk.Entry(root, font=("Helvetica", 18))
entry_z.grid(row=2, column=1, padx=10, pady=5)

# Lier la touche "Entrée" pour passer automatiquement au champ suivant
entry_x.bind("<Return>", focus_next_widget)
entry_y.bind("<Return>", focus_next_widget)
entry_z.bind("<Return>", lambda event: calculate())

# Bouton pour calculer les valeurs des équations
calculate_button = tk.Button(root, text="Calculate", command=calculate, font=("Helvetica", 18))
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Labels pour afficher les résultats
result_label = tk.Label(root, text="", font=("Helvetica", 18), fg="black")
result_label.grid(row=4, column=0, columnspan=2, pady=5)
code_label = tk.Label(root, text="", font=("Helvetica", 18), fg="#4a8ace")  # Couleur bleu adouci
code_label.grid(row=5, column=0, columnspan=2, pady=5)

# Boucle principale de l'interface graphique
root.mainloop()
