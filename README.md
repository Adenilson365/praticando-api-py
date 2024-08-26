## Projeto de Estudos CI/CD
  - [Repositório GitOps](https://github.com/Adenilson365/api-py-Ops) 
  ### Tecnologias: 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![SonarCloud](https://img.shields.io/badge/Sonar%20cloud-F3702A?style=for-the-badge&logo=sonarcloud&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![](https://img.shields.io/badge/TRIVY-blue.svg)
## Links de Consulta

### Documentação

- [Python - Linguagem de Programação](https://www.python.org/)
- [FastApi - Framework de API](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Virtualenv - Ambientes virtuais em Python](https://virtualenv.pypa.io/en/latest/user_guide.html)
- [Uvicorn - Live server](https://www.uvicorn.org/)
- [Trivy - Análise de Segurança de Imagem ](https://aquasecurity.github.io/trivy/v0.54/getting-started/installation/)
- [Docker -  Docker Healthcheck ](https://docs.docker.com/reference/dockerfile/#healthcheck)
- [Sonarcloud - Integração com GitHub Actions](https://docs.sonarsource.com/sonarcloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud/)



### Instalação Ambiente
- Instalar pip (Ubuntu):
```
sudo apt install python3--pip && pip --version

```
- Instalar virtualenv (Ubuntu):
```
sudo apt install python3--virtualenv && virtualenv --version

```
- Comandos virtualenv ( Linux)
```
 criar: virtualenv <nameEnv>
 entrar: source <envName>/bin/activate
 sair: deactivate
```
- Instalar fastApi (env ativado)
```
 pip install "fastapi[standard]"
```
- Rodar API
```
python3 main.py
```


### Git - Inicialização de repositório
- Seguir passos da documentação GitHub
- Restante do processo de versionamento (commits, merge ...) seguir normalmente

### Passos TBD - PR
**Processo precisa ser Revisado**
- Sincronizar a main
- Criar a branch de desenvolvimento
- Desenvolver e estabilizar
- Primeiro:  Fazer um push a partir da branch de desenvolvimento
- Segundo: Criar o PR no GitHub
- Terceiro: Seguirá para aprovação, segundo critérios.
- Quarto: Aprovado, posso ou não apagar a branch de desenvolvimento

### Trivy
- Instalação, seguir passos da documentação.
- Analisar construção do Dockerfile
```
trivy config .
```
- Analisar imagem
```
trivy image <repositorio>/<imagem>:[tag]
```
- Analisar imagem mais profunda
  - Por default analisa: vulnerabilidades e configurações
```
trivy image --scanners vuln,misconfig,secret,license <repositorio>/<imagem>:[tag]
```
### Boas práticas docker empregadas 
- Distro alpine 
    - Apenas pacotes essenciais, gera menor tamanho da imagem e menor quantidade de dependências para gerenciar.
- Usuário não root
- COPY em camadas e uso do dockerignore


### Próximos passos:
- Pesquisar: Diferenças de TBD para GithubFlow ( não confundir gitFlow)
