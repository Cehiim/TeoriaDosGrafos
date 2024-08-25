# Teoria dos Grafos
## Setup
### Primeiros passos
* Tenha o Git baixado - https://git-scm.com/downloads
* Crie uma pasta
* Clique com o botão direito e abra com Git Bash
![image](https://github.com/user-attachments/assets/cfaed189-7fad-45fa-9dd4-5e03e05c1183)
* Dê um `git init`
* Configure o seu nome  `git config --global user.name "Nome Sobrenome"`
* Configure o seu email `git config --global user.email seuemail@email.com`
* Configure o nome da branch `git config --global init.defaultBranch main`
* Configure para salvar suas futuras conexões com o repositório `git config --global credential.helper store`
* para checar informações use o comando sem o último parâmetro (Ex: `git config --global init.defaultBranch`)

### Autentificação por token
1. No GitHub, vá em Settings

![image](https://github.com/user-attachments/assets/dc6b5767-e02c-4c7a-acfa-af42261ff8a3)

2. Vá em Developer settings

![image](https://github.com/user-attachments/assets/24e3106e-3eeb-4e78-a2be-1c2560c62be6)

3. Vá em Tokens

![image](https://github.com/user-attachments/assets/f1fc2862-1dcc-4622-b52a-51a29203bcca)

4. Gere um novo token e copie a senha

### Acesso inicial ao repositório
* Use `git clone https://github.com/Cehiim/TeoriaDosGrafos.git` para clonar o repositório remoto para o local
* Digite o seu apelido da conta do GitHub
* Digite a senha do token

### Acessos posteriores
* Use `git remote add https://github.com/Cehiim/TeoriaDosGrafos.git` para conectar o repositório local existente com o remoto
* Use `git pull` para puxar novas alterações

## Gerenciar alterações
### Salvar alterações
* No Git Bash do repositório local use `git add arquivo.py` para registrar a alteração no índice (staging area)
* Use `git status` para checar as alterações registradas e os commits
* Para fazer o commit `git commit -m "Descrição do commit"`
* Use `git log` para conferir o último commit
* Use `git commit --amend -m "Nova descrição"` para atualizar a descrição do último commit

### Desfazer alterações
* Use `git restore` para desfazer as alterações não registradas pelo `git add`
* Use `git reset --soft` para desfazer o último commit e salvar as alterações registradas
* Use `git reset --mixed` (padrão) para desfazer o último commit sem salvar as alterações no índice
* Use `git reset --hard` para desfazer qualquer alteração feita pelo último commit no repositório local
