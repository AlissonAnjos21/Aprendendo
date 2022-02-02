import pacoteValores.pacoteConversao.converte

def aumentar(valor, aumentar, conversao=False):
    x = valor + (valor * aumentar / 100)

    if conversao:
        return pacoteValores.pacoteConversao.converte.moeda_real(x)

    else:
        return x


def reduzir(valor, reduzir, conversao=False):
    x = valor - (valor * reduzir / 100)

    if conversao:
        return pacoteValores.pacoteConversao.converte.moeda_real(x)
    else:
        return x
