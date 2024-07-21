#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:47:01 2024

@author: macbookpro
"""

import numpy as np

nombre_etudiants = int(input("Entrez le nombre d'étudiants : "))
nombre_sujets = int(input("Entrez le nombre de matières : "))

notes = np.zeros((nombre_etudiants, nombre_sujets))

for i in range(nombre_etudiants):
    print(f"\nEntrer les notes pour l'étudiant {i + 1}:")
    for j in range(nombre_sujets):
        notes[i, j] = float(input(f"Matière {j + 1} : "))

total_marks = np.sum(notes, axis=1)
pourcentage = (total_marks / (nombre_sujets * 100)) * 100

def determine_grade(pourcentage):
    if pourcentage >= 90:
        return "A+"
    elif pourcentage >= 80:
        return "A"
    elif pourcentage >= 70:
        return "B+"
    elif pourcentage >= 60:
        return "B"
    elif pourcentage >= 50:
        return "C"
    else:
        return "F"

grades = np.empty(nombre_etudiants, dtype=object)

for i in range(nombre_etudiants):
    grades[i] = determine_grade(pourcentage[i])

print("\nRésultats des étudiants :")
print(f"{'Nom de létudiant':<20} {'Total des notes':<15} {'Pourcentage':<12} {'Note':<5}")
print("-" * 52)

for i in range(nombre_etudiants):
    print(f"Étudiant {i + 1:<18} {total_marks[i]:<15} {pourcentage[i]:<12.2f} {grades[i]:<5}")
