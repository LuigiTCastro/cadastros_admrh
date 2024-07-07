# [CADASTROS_ADMRH]
Este script automatiza o processo de cadastro de colaboradores terceirizados no sistema ADMRH.


# Fluxos e Opções:

[Geral]
`1 - Fornecer um nome por PDF`
	Forneço o link (ou insiro o pdf)
	Capturo a informação
	Procuro o restante da informação nas planilhas de controle
	Lanço no sistema
	Gero um relatório final
	
	**Caso não encontre o nome na tabela, informar: Nome não encontrado.


`2 - Fornecer mais de um nome por PDF`
	Forneço o link (ou insiro o pdf)
	Capturo a qtd de páginas
	Capturo a informação por página
	Faço um loop para capturar um nome para cadastro por página
	Procuro o restante da informação nas planilhas de controle
	Lanço no sistema
	Gero um relatório final
	
	**Caso não encontre um nome na tabela, informar: Nome não encontrado + Pular para o próximo
	**Registrar no relatório quando a pessoa não for encontrada

**Itens 1 e 2 podem ser a mesma etapa (mesmo código)


`3 - Iterar tabela`
	Forneço o link e nome da aba (informações padrões)
	Leio a tabela
	Capturo os nomes apontados para cadastro
	Faço um loop, procurando tais nomes nos PDFs para cadastro
	Junto as informações do PDF com as das planilhas de controle
	Lanço no sistema
	Gero um relatório final
	
	**Caso não encontre um nome entre os PDFs, informar: Nome não encontrado + Pular para o próximo
	**Registrar no relatório quando a pessoa não for encontrada



[Específica]
    Escolher o modo específico de cadastro
    Fornecer o link da nova tabela
    Escolher: 
		1) Fornecer pdf
		2) Iterar tabela
    Todo o resto igual...



[Botões]
Caixa de diálogo com:
    1 Modo Geral
    2 Modo Específico

1 Modo Geral
    i Inserir PDF
    ii Iterar Tabela

i Inserir PDF
    Abrir input box para inserir o link (ou inserir o próprio pdf)

ii Iterar Tabela
    Apenas clicar no botão e já começa a leitura


2 Modo Específico
    Alterar link da tabela para fazer uma leitura à parte



[Formas]
a) Quando todos os registros funcionais estão em um único PDF, faz mais sentido fornecer o PDF, e o código lerá página por página, procurando o nome na tabela.

b) Quando os registros funcionais estão em PDFs individuais, faz mais sentido iterar a tabela, e o código procurará os nomes da tabela em cada PDF.




[Possibilidades]
a.1) Modo Geral + Inserir PDF
_PDF individual (01 pág) com informações constantes nas bases Pedidos de Movimentações e Controle de Vagas._
_PDF com mais de 01 pág com informações constantes nas bases Pedidos de Movimentações e Controle de Vagas._
(Loop pág por pág, procurando informações nas bases)

a.2) Modo Geral + Iterar Tabela
_Capturar pendências de cadastro nas bases PM/CV e buscar informações complementares nos pdfs constantes na pasta geral de cadastros._
(Loop linha por linha, procurando informações nos pdfs da pasta geral de cadastros)

b.1) Modo Específico + Inserir PDF
`Alterar link da planilha (tabelas específicas de grandes relações de movimentações)`
_PDF individual (01 pág) com informações constantes na planilha específica._
_PDF com mais de 01 pág com informações constantes na planilha específica._
(Loop pág por pág, procurando informações na planilha)

b.2) Modo Específico + Iterar Tabela
`Alterar link da planilha (tabelas específicas de grandes relações de movimentações)`
_Capturar pendências de cadastro na planilha específca e buscar informações complementares nos pdfs constantes na pasta específica de cadastros._
(Loop linha por linha, procurando informações nos pdfs da pasta específia de cadastros)