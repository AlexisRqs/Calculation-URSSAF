import tkinter as tk
from tkinter import messagebox

class URSSAFSimulator:

    def __init__(self, root):
        self.root = root
        root.title("Simulateur URSSAF")

        self.label = tk.Label(root, text="Entrez le montant de la facture:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Calculer", command=self.calculate)
        self.button.pack(pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            montant = float(self.entry.get())
            results = self.calcul_URSSAF(montant)
            total = sum(results.values())
            self.result_label.config(text=f"TOTAL À PAYER = {total:.2f}€")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")

    def calcul_URSSAF(self, montant):
        taux_services = 0.2110
        taux_impot = 0.0220
        taux_formation = 0.0020

        prestation_services = montant * taux_services
        versement_lib_impot = montant * taux_impot
        formation = montant * taux_formation

        return {"prestation_services": prestation_services, "versement_lib_impot": versement_lib_impot, "formation": formation}

if __name__ == "__main__":
    root = tk.Tk()
    app = URSSAFSimulator(root)
    root.mainloop()
