from flask import Flask, request
from telegram import Bot

app = Flask(__name__)
telegram_token = "<TELEGRAM_BOT_TOKEN>"
group_chat_id = "<TELEGRAM_GROUP_ID>"

bot = Bot(token=telegram_token)

async def send_message(message):
    await bot.send_message(chat_id=group_chat_id, text=message)

@app.route('/test/<message>')
async def index(message):
    if message:
        await send_message(message)
    return 'Servidor Python está funcionando!'

def parse_github_event(data):
    if 'repository' in data and 'sender' in data:
        repo_name = data['repository']['full_name']
        sender_name = data['sender']['login']

        if 'commits' in data:
            return f"Novos commits no repositório {repo_name} por {sender_name}!"
        elif 'pull_request' in data:
            pr_title = data['pull_request']['title']
            pr_action = data['action']
            return f"Ação de {pr_action} no pull request '{pr_title}' em {repo_name} por {sender_name}!"
        elif 'ref' in data and data['ref_type'] == 'branch':
            branch_name = data['ref']
            return f"Nova branch '{branch_name}' criada por {sender_name} em {repo_name}!"

    return None

@app.route('/webhook', methods=['POST'])
async def webhook():
    data = request.get_json()
    message = parse_github_event(data)


    if message:
        await send_message(message)

    return 'OK'

if __name__ == '__main__':
    app.run(port=5000)
    print(">> Iniciando o webhook...")
