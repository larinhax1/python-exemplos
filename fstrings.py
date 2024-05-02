#Formatação de Strings
from datetime import datetime
ano_atual = datetime.now().year
clube = 'SPFC'
ano_fundacao = 1930
campeonato_mundial = 3
print(f"{clube} possui {campeonato_mundial} títulos mundiais.")
print(f"São {ano_atual - ano_fundacao} anos de existência.")