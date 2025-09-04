import pandas as pd

def recuperar_campanhas(conn):
    query = """
    select
        *
    from processed_data."CampanhaContratante" cc
    """
    df = pd.read_sql(query, conn)

    df['CampanhaContratanteId'] = df['CampanhaContratanteId'].astype(str)
    df['ContratanteId'] = df['ContratanteId'].astype(str)
    df['CampanhaId'] = df['CampanhaId'].astype(str)
    return df

def recuperar_cobrancas(conn):
    query = """
    select
        *
    from processed_data."Cobrancas" c
    """
    df = pd.read_sql(query, conn)

    df['CobrancaId'] = df['CobrancaId'].astype(str)
    df['ContratanteId'] = df['ContratanteId'].astype(str)
    df['CampanhaId'] = df['CampanhaId'].astype(str)
    df['OrdemPagamentoId'] = df['OrdemPagamentoId'].astype(str)
    return df

def recuperar_contratantes(conn):
    query = """
    select
        *
    from processed_data."Contratantes" c
    """
    df = pd.read_sql(query, conn)

    df['ContratanteId'] = df['ContratanteId'].astype(str)
    return df

def recuperar_ordensPagamento(conn):
    query = """
    select
        *
    from processed_data."OrdemPagamentoContratante" opc
    """
    df = pd.read_sql(query, conn)

    df['OrdemPagamentoContratanteId'] = df['OrdemPagamentoContratanteId'].astype(str)
    df['ContratanteId'] = df['ContratanteId'].astype(str)
    df['OrdemPagamentoId'] = df['OrdemPagamentoId'].astype(str)
    return df

def recuperar_metricas_vendaUtilizacao(conn):
    query = """
    select
        *
    from analysis.vw_contratante_metricasOperacionais_mes
    """
    df = pd.read_sql(query, conn)

    df['ContratanteId'] = df['ContratanteId'].astype(str)
    return df

def recuperar_faturamento_operacoes_abertas(conn):
    query = """
    select
        *
    from analysis.vw_faturamento_sob_operacoes_abertas
    """
    df = pd.read_sql(query, conn)

    df['CampanhaId'] = df['CampanhaId'].astype(str)
    df['ContratanteId'] = df['ContratanteId'].astype(str)
    df['OrdemPagamentoId'] = df['OrdemPagamentoId'].astype(str)
    return df