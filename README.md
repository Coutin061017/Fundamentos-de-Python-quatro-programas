# Fundamentos de Python — quatro programas

Coleção de exercícios para praticar lógica de programação, validação de entradas, estruturas de repetição e configuração de variáveis de ambiente com Python.

## Programas

| Arquivo | O que faz |
|---|---|
| `fibonacci.py` | Solicita uma quantidade válida de termos e exibe a sequência de Fibonacci. |
| `jokenpo.py` | Jogo de pedra, papel e tesoura contra o computador, com placar acumulado. |
| `paresImpares.py` | Recebe números inteiros, valida a entrada e separa valores pares e ímpares. |
| `programa.py` | Demonstra a leitura da variável `API_KEY` de um arquivo `.env` com `python-dotenv`. |

## Tecnologias

- Python 3
- Biblioteca padrão: `random` e `os`
- `python-dotenv` (somente para `programa.py`)

## Executar

Clone o repositório e entre na pasta:

```powershell
git clone https://github.com/Coutin061017/Fundamentos-de-Python-quatro-programas.git
cd Fundamentos-de-Python-quatro-programas
```

Cada exercício é independente:

```powershell
python fibonacci.py
python jokenpo.py
python paresImpares.py
```

Para testar o exercício de variáveis de ambiente:

```powershell
pip install -r requirements.txt
```

Crie um arquivo local chamado `.env` com o conteúdo de **exemplo**:

```dotenv
API_KEY=valor_de_teste
```

Execute:

```powershell
python programa.py
```

**Segurança:** não envie o arquivo `.env` nem chaves verdadeiras para o GitHub. Mantenha esses arquivos ignorados pelo Git na sua máquina.

## O que este projeto demonstra

Lógica básica, condicionais, laços, listas, tratamento de `ValueError`, uso de biblioteca padrão e introdução à configuração segura de aplicações.

**Autor:** [André Coutinho](https://github.com/Coutin061017)
