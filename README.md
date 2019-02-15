# FULLSTACK ANALISANDO OS LOGS
## Descrição do Projeto
O projeto aqui descrito busca analisar os dados de log de um jornal. O objetivo é descrobir a partir dos logs de banco de dados de acessos da aplicação web, quais os artigos os leitores mais gostam de ler.


### Estrutura necesária
- [Python 2.7.2](https://www.python.org/download/releases/2.7.2/)
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)

### Configurações
- Instalar o Vagrant
- Instalar o VirtualBox
- Clonar para crianção do ambiente de trabalho que está neste link (https://github.com/udacity/fullstack-nanodegree-vm)
- Baixar o aquivo de banco de dados postgresql neste link (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) na pasta do projeto vagrant clonado anteriormente
- Descompactar o arquivo baixado anteriormente

### Subindo o servidor

- Para ligar o servidor virtual, entre no diretório onde clonou o projeto da máquina virtual conforme explicação anterior e digite o seguinte comando no teminal:
	> vagrant up
- Após o servidor ter inicializado digite o seguinte comando para acessar o servidor utilizando o SSH:
	> vagrant ssh
- Após acessar a máquina virtual, seus arquivos para trabalho estarão no diretório /vagrant, para acessar esse diretório digite o comando que segue:
	> cd /vagrant
- Liste o conteúdo desta pasta com o comando abaixo:
	> ls

### Importando os dados iniciais
- Execute O comando que segue para importar o banco de dados com o logs para realizar a analise
	> psql -d news -f newsdata.sql

A base de dados inclui 3 tabelas:
- articles
- authors
- log


- Utilize que segue para se conectar no banco de dados de logs que acabou de ser criado
	> psql -d news


- Crie a view artigoscontagem usando:
	> CREATE OR REPLACE VIEW artigoscontagem as
    SELECT art.title, COUNT(lg.path) AS views
	FROM articles art
	INNER JOIN log lg ON lg.path like CONCAT('/article/', art.slug)
	GROUP BY art.title
	ORDER BY views DESC;


- Crie a view popularidade usando:
	> CREATE OR REPLACE VIEW popularidade as
    SELECT ath.name, COUNT(lg.path) AS views
	FROM authors ath
	INNER JOIN articles art ON art.author = ath.id
	INNER JOIN log lg ON lg.path like CONCAT('/article/', art.slug)
	GROUP BY ath.name
	ORDER BY views DESC;

	
- Crie a view logerro usando:
	> CREATE OR REPLACE VIEW logerro as
	SELECT TO_CHAR(time, 'DD-MM-YYYY') AS data,
	ROUND(100.0*SUM(CASE log.status WHEN '200 OK'
	THEN 0 ELSE 1 END)/COUNT(log.status),2) AS erros
	FROM log
	GROUP BY data
	ORDER BY erros desc;

### Exedcutando o relatório
- Entre na pasta /vagrant que está na máquina virtual. Então acesse a parta mining_log e execute o arquivo python com o comando python abaixo.
> python mining_logs.py
