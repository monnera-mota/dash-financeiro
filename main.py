#%%
from datetime import datetime
from db_connections import conn_wh
import defs

print(f"{datetime.now()} - Iniciando a recuperação de dados")

contratantes = defs.recuperar_contratantes(conn_wh)
cobrancas = defs.recuperar_cobrancas(conn_wh)
campanha_descricao = defs.recuperar_campanhas(conn_wh)
ordem_pagamento_descricao = defs.recuperar_ordensPagamento(conn_wh)
cliente_metricas_mensais = defs.recuperar_metricas_vendaUtilizacao(conn_wh)
faturamento_aberto = defs.recuperar_faturamento_operacoes_abertas(conn_wh)

print(f"{datetime.now()} - Exportando dados em parquet")

contratantes.to_parquet("data/contratantes.parquet", index=False)
cobrancas.to_parquet("data/cobrancas.parquet", index=False)
campanha_descricao.to_parquet("data/campanha_descricao.parquet", index=False)
ordem_pagamento_descricao.to_parquet("data/ordem_pagamento_descricao.parquet", index=False)
cliente_metricas_mensais.to_parquet("data/cliente_metricas_mensais.parquet", index=False)
faturamento_aberto.to_parquet("data/faturamento_aberto.parquet", index=False)

print(f"{datetime.now()} - Processo finalizado")