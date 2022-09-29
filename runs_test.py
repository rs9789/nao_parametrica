
dados = ['A','A','A','A','A','A','A','A','A','A','A','A','A','B','B','B','A','A','A','A']



def runs_count(dados):
    n_runs = 0
    first = ''
    for i in range(len(dados)):
        if dados[i] == first:
            first = dados[i]
            continue
        else:
            n_runs += 1
            first = dados[i]
    
    return n_runs

def parameters(string1, string2):
    value1 = len([i for i in dados if i == string1])
    value2 = len([i for i in dados if i == string2])

    r_bar = round(((2*value1*value2)/(value1+value2))+1, 4)
    r_variance = round((2 * value1 * value2 * (2 * value1 * value2 - value1 - value2))/\
                (((value1 + value2)**2) * (value1 + value2 - 1)),4)
    
    return r_bar,r_variance, value1, value2
             
r_barra, r_2, n1, n2 = parameters('A', 'B')
n_runs = runs_count(dados)
z_statistic = (n_runs-r_barra)/r_2
print(z_statistic, r_barra, r_2, n_runs, n1, n2, len(dados))