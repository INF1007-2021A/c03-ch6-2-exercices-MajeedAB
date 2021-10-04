#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    
    # some_dict = {}
    # for i,cle in enumerate(some_list):
    #     some_dict[cle] = i
    # return some_dict
    return {cle:i for i,cle in enumerate(some_list)}


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    # couleurs = [(coul,cnames[coul]) for coul in colors]
    return [(col,cnames[col]) for col in colors]


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350

    return [i for i in range(10000)[0:15]]+[i for i in range(10000)[351:10000]]


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    mse = {}
    for model in model_dict:
        erreur = 0
        for point in model_dict[model]:
            erreur+=(point[0]-point[1])**2
        mse[model] = erreur/len(model_dict[model])
    # return mse

    # return {model:sum(p for )/len(model_dict[model]) for point in model_dict[model] for model in model_dict}


    # return {model:sum((point[0]-point[1])**2 for point in model_dict[model])/len(model_dict[model]) for model in model_dict}

    return{m:sum((p[0]-p[1])**2for p in model_dict[m])/len(model_dict[m])for m in model_dict}

    # return{(lambda d:model_dict) (m:sum((p[0]-p[1])**2for p in d[m])/len(d[m])for m in d)}



def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
