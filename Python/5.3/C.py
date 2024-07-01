class temp:
    def __repr__(self):
        raise KeyError


try:
    func(temp())
except KeyError:
    print("Ура! Ошибка!")