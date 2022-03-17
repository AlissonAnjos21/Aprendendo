class Exemplo:
    def __init__(self):
        pass

    # É chamado sempre que chamam o método len
    def __len__(self):
        return 21

exemplo = Exemplo()
print(len(exemplo))  # 21
