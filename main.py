def media_prob(tabela):
    media = 0
    n = len(tabela[0])
    for i in range(n):
        media += tabela[0][i]*tabela[1][i]
    print("Média = {0:.4f}".format(media))
    return media

def var_prob(tabela):
    var = 0
    media = media_prob(tabela)
    n = len(tabela[0])
    for i in range(n):
        var += ((media-tabela[0][i])**2)*tabela[1][i]
    print("Variância = {0:.4f}".format(var))
    return var

ex_2 = [[1,2,3,4,5],[0.31,0.16,0.22,0.25,0.06]]
media_prob(ex_2)
var_prob(ex_2)