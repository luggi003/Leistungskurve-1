import numpy as np
import matplotlib.pyplot as plt
import os

from sort import bubble_sort
from load_data import load_data   # falls ausgelagert


def create_power_curve(file_path):
    # Daten laden
    data = load_data(file_path)
    power = data['PowerOriginal']

    # Sortieren (aufsteigend)
    sorted_power = bubble_sort(power.copy())

    # Absteigend für Kurve
    sorted_power_desc = sorted_power[::-1]

    # X = Time
    x = np.arange(1, len(sorted_power_desc) + 1)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(x, sorted_power_desc, label="Power")

    plt.xlabel("Rank")
    plt.ylabel("Power (W)") 
    plt.title("Sorted Power Curve") 
    plt.grid(True)
    plt.legend()

    # Ordner sicherstellen
    os.makedirs("figures", exist_ok=True)

    # Speichern
    output_path = "figures/power_curve.png"
    plt.savefig(output_path, dpi=150)

    print(f"Plot gespeichert unter: {output_path}")

    plt.show()


if __name__ == "__main__":
    create_power_curve("activity.csv")