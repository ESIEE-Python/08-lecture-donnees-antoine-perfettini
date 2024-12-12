"""
Code principal
"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode = 'r', encoding='utf8') as f:
        l = f.readlines()
        out = []
        for elt in l:
            l1 = []
            for i in  elt.strip().split(';'):
                l1.append(int(i))
            out.append(l1)
    return out

def get_list_k(data, k):
    """
    Permet obtenir une liste d'indice k
    """
    l = data[k]
    return l

def get_first(l):
    """
    Permet d'obtenir le premier element de la liste l
    """
    return l[0]

def get_last(l):
    """
    Permet d'obtenir le dernier element de la liste l
    """
    return l[-1]

def get_max(l):
    """
    Permet d'obtenir l'element de valeur maximum de la liste l
    """
    return max(l)

def get_min(l):
    """
    Permet d'obtenir l'element de valeur minimum de la liste l
    """
    return min(l)

def get_sum(l):
    """
    Permet d'obtenir la somme des elements de la liste l
    """
    s = 0
    for elt in l:
        s+=elt
    return s

def main():
    """
    #### Fonction principale
    """
    data = read_data(FILENAME)
    print(data)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))
    print(get_first(get_list_k(data, 37)))
    print(get_last(get_list_k(data, 37)))
    print(get_max(get_list_k(data, 37)))
    print(get_min(get_list_k(data, 37)))
    print(get_sum(get_list_k(data, 37)))


if __name__ == "__main__":
    main()
