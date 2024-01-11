from web3 import Web3
import sqlite3
import click
import schedule
import time

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect("ethereum_data.db")

# Função para obter dados mais recentes
def get_latest_data():
    db_connection = connect_db()
    cursor = db_connection.cursor()

    cursor.execute('SELECT total_supply FROM erc20_data ORDER BY id DESC LIMIT 1')
    total_erc20_supply = cursor.fetchone()[0]

    cursor.execute('SELECT total_tokens FROM erc721_data ORDER BY id DESC LIMIT 1')
    total_erc721_tokens = cursor.fetchone()[0]

    cursor.execute('SELECT latest_block FROM block_data ORDER BY id DESC LIMIT 1')
    latest_block = cursor.fetchone()[0]

    db_connection.close()

    return total_erc20_supply, total_erc721_tokens, latest_block

# Comando CLI para exibir dados
@click.command()
@click.option('--update', is_flag=True, help='Atualizar dados automaticamente a cada minuto.')
def show_data(update):
    while True:
        erc20_supply, erc721_tokens, block_number = get_latest_data()

        click.echo("\nDados Ethereum:")
        click.echo(f"Total de tokens ERC20: {erc20_supply}")
        click.echo(f"Total de NFTs (ERC721): {erc721_tokens}")
        click.echo(f"Número do bloco mais recente: {block_number}")

        if not update:
            break
        time.sleep(60)  # Aguardar 1 minuto antes da próxima atualização

# Agendar a atualização automática usando a biblioteca 'schedule'
def job():
    click.echo("\nAtualizando dados automaticamente...")
    erc20_supply, erc721_tokens, block_number = get_latest_data()
    click.echo(f"Total de tokens ERC20: {erc20_supply}")
    click.echo(f"Total de NFTs (ERC721): {erc721_tokens}")
    click.echo(f"Número do bloco mais recente: {block_number}")

schedule.every(1).minutes.do(job)  # Agendar a atualização a cada minuto

# Executar a CLI
if __name__ == '__main__':
    show_data()
