def gravar_resultado(ganhou, perdeu):
    try:
        with open("resultado_forca.txt", "a") as arquivo:
            arquivo.write(f"{ganhou},{perdeu}\n")
        print("Resultado gravado com sucesso.")
    except Exception as e:
        print(f"Erro ao gravar resultado: {str(e)}")

def recuperar_resultados():
    resultados = []
    try:
        with open("resultado_forca.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                ganhou, perdeu = linha.strip().split(",")
                resultados.append((int(ganhou), int(perdeu)))
    except FileNotFoundError:
        print("Arquivo de resultados não encontrado.")
    except Exception as e:
        print(f"Erro ao recuperar resultados: {str(e)}")
    
    return resultados
