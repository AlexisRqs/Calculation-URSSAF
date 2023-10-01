def calcul_URSSAF(montant):
    """
    Calcule les différentes taxes pour l'URSSAF en fonction du montant fourni.
    """
    # Taux pour chaque taxe
    taux_services = 0.2110
    taux_impot = 0.0220
    taux_formation = 0.0020

    # Calcul des taxes
    prestation_services = montant * taux_services
    versement_lib_impot = montant * taux_impot
    formation = montant * taux_formation

    # Calcul du total à payer
    total = prestation_services + versement_lib_impot + formation

    return prestation_services, versement_lib_impot, formation, total


def main():
    # Demander à l'utilisateur le nombre de factures
    nb_factures = int(input("Entrez le nombre de factures à saisir: "))

    total_URSSAF = 0

    # Pour chaque facture, demander le montant et ajouter au total
    for i in range(nb_factures):
        montant = float(input(f"Entrez le montant de la facture {i+1}: "))
        _, _, _, total = calcul_URSSAF(montant)
        total_URSSAF += total

    # Afficher le total à payer
    print(f"TOTAL À PAYER à l'URSSAF = {total_URSSAF:.2f}€")


if __name__ == "__main__":
    main()