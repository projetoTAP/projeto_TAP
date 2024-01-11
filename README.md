

## Projeto TAP - Análise de Dados da Blockchain Ethereum

### Descrição do Projeto

O projeto TAP tem como objetivo recolher e analisar dados da blockchain Ethereum, armazenando essas informações de forma eficiente e proporcionando uma interface de linha de comando (CLI) para a visualização dos dados. O código também inclui funcionalidades de atualização automática e filtragem de informações específicas.

### Funcionalidades Implementadas

1. **Recolha e Análise Contínua de Dados da Blockchain Ethereum:**
   - Utilização da biblioteca `web3` para conexão à blockchain Ethereum.
   - Definição de contratos ERC20 e ERC721 para recuperação de dados, como o total de tokens e o número do bloco mais recente.

2. **Armazenamento Eficiente dos Dados:**
   - Utilização de um banco de dados SQLite (`ethereum_data.db`) para armazenar totais de tokens ERC20, tokens ERC721 e o número do bloco mais recente.
   - Definição de tabelas no banco de dados para armazenar dados de forma estruturada.

3. **Interface CLI Clara e Concisa:**
   - Implementação da CLI utilizando a biblioteca `click`.
   - Função `show_data` que exibe de maneira clara os totais de tokens ERC20 e ERC721, bem como o número do bloco mais recente.

4. **Testes Implementados:**
   - Testes de precisão e consistência dos dados recuperados da blockchain Ethereum.
   - Testes de eficiência e robustez do armazenamento de dados.
   - Avaliação da funcionalidade de atualização em tempo real, garantindo que não sobrecarregue o sistema.

### Como Executar o Projeto

1. **Instalação de Dependências:**
   - Certifique-se de ter o Python instalado em seu sistema.
   - Instale as bibliotecas necessárias com `pip install -r requirements.txt`.

2. **Configuração do Projeto:**
   - Defina as variáveis `alchemy_url`, `erc20_contract_address` e `erc721_contract_address` no código para os valores correspondentes.

3. **Execução da CLI:**
   - Execute o script com `python main.py` para iniciar a CLI.
   - A CLI exibirá os totais de tokens ERC20 e ERC721, bem como o número do bloco mais recente.

4. **Testes:**
   - Execute os testes implementados com `pytest` para verificar a precisão, consistência e eficiência do projeto.

### Observações Importantes

- **Atualização Automática:**
  - A CLI pode ser configurada para atualização automática, executando a função `update_data_job` em intervalos definidos.

- **Banco de Dados SQLite:**
  - Os dados são armazenados no arquivo `ethereum_data.db`. Caso necessário, este arquivo pode ser copiado ou movido para outro local.




