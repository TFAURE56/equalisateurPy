import tkinter as tk
from http.client import responses
from tkinter import ttk
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, butter, lfilter
from pylab import *
from math import pi
import numpy as np

# Créer la fenêtre principale
root = tk.Tk()
root.title("Sliders Multiples avec Noms")
root.geometry("800x400")

# Fonction pour mettre à jour la valeur affichée de chaque slider
def update_value(value, index, label):
    formatted_value = f"{float(value):.3f}"  # Formatage à trois chiffres après la virgule
    label.config(text=f"Valeur: {formatted_value}")
    Filtres[index] = formatted_value

# Fonction pour afficher la valeur de chaque slider dans la console
def affichageSlider(slider):
    value = float(slider.get())
    formatted_value = f"{value:.3f}"  # Formatage à trois chiffres après la virgule
    print(f"Valeur du slider: {formatted_value}")

def filtreMusique():

    print(f"Valeur du slider: {Filtres[0]}")
    print(f"Valeur du slider: {Filtres[1]}")
    print(f"Valeur du slider: {Filtres[2]}")

    Q_1 = 1
    def filtre1(data, Gain):
        # Assurez-vous que 'data' est un tableau numérique de type float
        data = np.array(data, dtype=float)

        # Définition des paramètres numériques
        f0n = 50 / freq_ech
        w0n = 2 * np.pi * f0n
        k0n = w0n + Q_1 * (w0n ** 2 + 1)

        # Coefficients du filtre numérique
        a0 = w0n / k0n
        a1 = -w0n / k0n
        b1 = (2 * Q_1 + w0n) / k0n
        b2 = -Q_1 / k0n

        # Initialisation de la sortie
        filtered_data = np.zeros_like(data, dtype=float)  # Assurez-vous que 'filtered_data' est de type float
        filtered_data[0] = a0 * data[0]
        filtered_data[1] = a0 * data[1] + a1 * data[0] + b1 * filtered_data[0]
        filtered_data[2] = a0 * data[2] + a1 * data[1] + b1 * filtered_data[1] + b2 * filtered_data[0]

        # Filtrage de l'ensemble des données
        for i in range(3, len(data)):
            filtered_data[i] = a0 * data[i] + a1 * data[i - 1] + b1 * filtered_data[i - 1] + b2 * filtered_data[i - 2]

            # Assurez-vous que G_1 est un nombre
            Gain = float(Gain)  # Si nécessaire, forcez G_1 à être un float

        # Retour du résultat filtré, multiplié par G_1
        return filtered_data * Gain

    Q_2 = 1
    def filtre2(data, Gain):
        # Définition des paramètres numériques
        f0n = 200 / freq_ech
        w0n = 2 * pi * f0n
        k0n = w0n + Q_2 * (w0n * w0n + 1)

        # Coefficients du filtre numérique
        a0 = w0n / k0n
        a1 = -w0n / k0n
        b1 = (2 * Q_2 + w0n) / k0n
        b2 = -Q_2 / k0n

        # Initialisation de la sortie
        filtered_data = np.zeros_like(data)
        filtered_data[0] = a0 * data[0]
        filtered_data[1] = a0 * data[1] + a1 * data[0] + b1 * filtered_data[0]
        filtered_data[2] = a0 * data[2] + a1 * data[1] + b1 * filtered_data[1] + b2 * filtered_data[0]

        Gain = float(Gain)

        # Filtrage de l'ensemble des données
        for i in range(3, len(data)):
            filtered_data[i] = a0 * data[i] + a1 * data[i - 1] + b1 * filtered_data[i - 1] + b2 * filtered_data[i - 2]

        return filtered_data * Gain

    Q_3 = 1
    def filtre3(data, Gain):
        # Définition des paramètres numériques
        f0n = 800 / freq_ech
        w0n = 2 * pi * f0n
        k0n = w0n + Q_3 * (w0n * w0n + 1)

        # Coefficients du filtre numérique
        a0 = w0n / k0n
        a1 = -w0n / k0n
        b1 = (2 * Q_3 + w0n) / k0n
        b2 = -Q_3 / k0n

        # Initialisation de la sortie
        filtered_data = np.zeros_like(data)
        filtered_data[0] = a0 * data[0]
        filtered_data[1] = a0 * data[1] + a1 * data[0] + b1 * filtered_data[0]
        filtered_data[2] = a0 * data[2] + a1 * data[1] + b1 * filtered_data[1] + b2 * filtered_data[0]

        Gain = float(Gain)

        # Filtrage de l'ensemble des données
        for i in range(3, len(data)):
            filtered_data[i] = a0 * data[i] + a1 * data[i - 1] + b1 * filtered_data[i - 1] + b2 * filtered_data[i - 2]

        return filtered_data * Gain

    Q_4 = 1.5
    def filtre4(data, Gain):
        # Définition des paramètres numériques
        f0n = 4000 / freq_ech
        w0n = 2 * pi * f0n
        k0n = w0n + Q_4 * (w0n * w0n + 1)

        # Coefficients du filtre numérique
        a0 = w0n / k0n
        a1 = -w0n / k0n
        b1 = (2 * Q_4 + w0n) / k0n
        b2 = -Q_4 / k0n

        # Initialisation de la sortie
        filtered_data = np.zeros_like(data)
        filtered_data[0] = a0 * data[0]
        filtered_data[1] = a0 * data[1] + a1 * data[0] + b1 * filtered_data[0]
        filtered_data[2] = a0 * data[2] + a1 * data[1] + b1 * filtered_data[1] + b2 * filtered_data[0]

        Gain = float(Gain)

        # Filtrage de l'ensemble des données
        for i in range(3, len(data)):
            filtered_data[i] = a0 * data[i] + a1 * data[i - 1] + b1 * filtered_data[i - 1] + b2 * filtered_data[i - 2]

        return filtered_data * Gain

    Q_5 = 0.5
    def filtre5(data, Gain):
        # Définition des paramètres numériques
        f0n = 15000 / freq_ech
        w0n = 2 * pi * f0n
        k0n = w0n + Q_5 * (w0n * w0n + 1)

        # Coefficients du filtre numérique
        a0 = w0n / k0n
        a1 = -w0n / k0n
        b1 = (2 * Q_5 + w0n) / k0n
        b2 = -Q_5 / k0n

        # Initialisation de la sortie
        filtered_data = np.zeros_like(data)
        filtered_data[0] = a0 * data[0]
        filtered_data[1] = a0 * data[1] + a1 * data[0] + b1 * filtered_data[0]
        filtered_data[2] = a0 * data[2] + a1 * data[1] + b1 * filtered_data[1] + b2 * filtered_data[0]

        Gain = float(Gain)

        # Filtrage de l'ensemble des données
        for i in range(3, len(data)):
            filtered_data[i] = a0 * data[i] + a1 * data[i - 1] + b1 * filtered_data[i - 1] + b2 * filtered_data[i - 2]

        return filtered_data * Gain

    ### 3 exemples de donnees d'entress sont proposees
    type = 3
    creationWavFiltre = False  # True si l'on veut créer un wav à la fin
    if type == 1:
        ###### Signal sinusoïdal
        freq_ech = 44100  # Fréquence d'échantillonnage en Hz
        f_sin = 2000  # Fréquence du signal sinusoïdal en Hz
        duree = 1  # Durée du signal en secondes
        # Créer un tableau de temps
        t = np.linspace(0, duree, int(freq_ech * duree), endpoint=False)
        # Générer le signal sinusoïdal
        data = np.sin(2 * np.pi * f_sin * t)

        ###### fin signal sinusoïdal
    elif type == 2:
        ####### Fichier wav lu resultat dans u ntableau (attention au mon ou au stéréo
        freq_ech, data = wavfile.read('LW_20M_amis.wav')
        # Créer un tableau de temps
        t = np.linspace(0, len(data) / freq_ech, len(data), endpoint=False)
        creationWavFiltre = True
        ####### Fin wav

        # Vérifier si le fichier est stéréo ou mono
        if len(data.shape) > 1:
            # Si le fichier est stéréo, prendre un seul canal (par exemple, le canal gauche)
            data = data[:, 0]

    else:
        # Une impulsion unitaire
        freq_ech = 44100  # Fréquence d'échantillonnage
        duree = 3  # Durée en secondes
        data = np.zeros(freq_ech * duree)
        data[0] = 1  # Impulsion unitaire au premier échantillon
        t = np.linspace(0, duree, int(freq_ech * duree), endpoint=False)

    # Appliquer la FFT
    fft_result = np.fft.fft(data)

    # Creation du vecteur frequence 1re moitier freq positive, 2e moitié freq négative.
    frequences = np.fft.fftfreq(len(fft_result), d=1 / freq_ech)
    print(frequences)
    print(len(frequences))

    # Application du filtre
    signal_filtre_bande1 = filtre1(data, Filtres[0])
    signal_filtre_bande2 = filtre2(data, Filtres[1])
    signal_filtre_bande3 = filtre3(data, Filtres[2])
    signal_filtre_bande4 = filtre4(data, Filtres[3])
    signal_filtre_bande5 = filtre5(data, Filtres[4])

    signal_filtre = data
    signal_filtre = filtre1(signal_filtre, Filtres[0])
    signal_filtre = filtre2(signal_filtre, Filtres[1])
    signal_filtre = filtre3(signal_filtre, Filtres[2])
    signal_filtre = filtre4(signal_filtre, Filtres[3])
    signal_filtre = filtre5(signal_filtre, Filtres[4])

    # Normalisation du signal pour éviter des dépassements de valeurs
    signal_filtre_normalise = np.clip(signal_filtre, -1, 1)  # Limiter entre -1 et 1

    # Écrire le fichier WAV
    if creationWavFiltre == True:
        signal_sortie = signal_filtre_bande1 + signal_filtre_bande2 + signal_filtre_bande3 + signal_filtre_bande4 + signal_filtre_bande5
        signal_sortie_moy = signal_sortie / 5
        # Normalisation du signal filtré avec gain
        signal_filtre_normalise = np.clip(signal_sortie_moy, -32768, 32767)  # Limiter les valeurs
        signal_filtre_normalise = signal_filtre_normalise.astype(np.int16)  # Convertir en entiers 16 bits

        wavfile.write('wav_filtre.wav', freq_ech, signal_filtre_normalise)

    # Créer une figure avec deux sous-graphes
    plt.figure(figsize=(12, 6))

    # Sous-graphe 1 : Signal temporel
    plt.subplot(2, 1, 1)
    plt.plot(t, data, label="Signal original")
    plt.xlabel("Temps [s]")
    plt.ylabel("Amplitude")
    plt.title("Signal d'entrée")
    plt.legend()

    # Transformée de Fourier pour obtenir la réponse en fréquence
    fft_result = np.fft.fft(signal_filtre)
    frequences = np.fft.fftfreq(len(fft_result), d=1 / freq_ech)  # Vecteur des fréquences (Hz)

    # Filtrer les fréquences positives (utile pour afficher de 0 à la moitié de freq_ech)
    mask = frequences >= 0
    frequences = frequences[mask]

    # Tracé de la réponse en fréquence
    plt.subplot(2, 1, 2)
    plt.plot(frequences, np.abs(fft_result))
    plt.title("Réponse en fréquence combinée (après les 5 filtres)")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid()
    plt.legend()
    plt.xlim(0, freq_ech / 2)  # Afficher uniquement la bande de fréquences positives

    plt.tight_layout()
    plt.show()

# Noms pour chaque slider
slider_names = ["Très basses fréquences", "Basses fréquences", "Moyennes fréquences", "Hautes fréquences",
                "Très hautes fréquences"]

Filtres = [1.0, 1.0, 1.0, 1.0, 1.0]

# Boucle pour créer 5 sliders avec les noms correspondants
sliders = []
for i, name in enumerate(slider_names):

    # Créer un label pour le nom du slider
    name_label = ttk.Label(root, text=name)
    name_label.grid(row=0, column=i, padx=10, pady=25)  # Positionner le nom du slider en haut

    # Créer un label pour afficher la valeur du slider
    value_label = ttk.Label(root, text="Valeur: 0.000")
    value_label.grid(row=1, column=i, padx=44, pady=10)  # Positionner le label de valeur en dessous du nom

    # Créer un slider vertical
    slider = ttk.Scale(
        root,
        from_=2,
        to=0,
        orient='vertical',
        length=200,
        command=lambda value, idx=i, l=value_label: update_value(value, idx, l)  # Met à jour le label de valeur
    )
    slider.set(1)  # Initialise la position du slider
    slider.grid(row=2, column=i, padx=10)  # Positionner le slider sous le label de valeur

    # Ajouter le slider à la liste pour référence
    sliders.append(slider)

    # Créer un bouton pour afficher la valeur du slider dans la console
    button = ttk.Button(root, text="Afficher valeur", command=lambda s=slider: affichageSlider(s))
    button.grid(row=3, column=i, padx=10, pady=5)  # Positionner le bouton sous chaque slider

# Ajouter un bouton d'exécution en bas de la fenêtre
execute_button = ttk.Button(root, text="Exécuter", command=lambda: filtreMusique())
execute_button.grid(row=4, columnspan=len(slider_names), pady=20)  # Le bouton s'étend sur toutes les colonnes

# Lancement de la fenêtre principale
root.mainloop()
