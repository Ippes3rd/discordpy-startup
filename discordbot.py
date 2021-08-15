#coding:UTF-8
import discord
from datetime import datetime
from discord.ext import tasks
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 874242284844122172 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%a %H:%M')
    if now == 'Sun 14:00': # ロンドン時間なので9時間サバ読むこと
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('チーム競技場〆まであと1時間！')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
