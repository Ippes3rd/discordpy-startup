#coding:UTF-8
import discord
from datetime import datetime
from discord.ext import tasks
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 873990257375318107 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '10:03':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
