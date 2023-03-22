 from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://google.com.br")

import pandas as pd

tabela = pd.read_excel("commodities.xlsx")
display(tabela)

for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    print(produto)
    produto = produto.replace("ó", "o").replace("ã","a").replace("ç","c").replace("ú","u").replace("é","e").replace("á","a")
    
    link = f"https://www.melhorcambio.com/{produto}-hoje" 
    navegador.get(link)

    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    preco = preco.replace(".", "",).replace(",", ".")
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)

# .click() -> clicar
# .send_keys("texto") -> escrever
# .get_attribute() -> pegar um valor

tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
display(tabela)

tabela.to_excel("commodities_atualizado.xlsx", index = False)

navegador.quit()