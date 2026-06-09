import asyncio
from pytgcalls import idle
import os
import sys
import random
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from bot import *
from pyromod import listen
import subprocess


def install_requirements():
	req = os.path.join(os.path.dirname(__file__), "requirements.txt")
	if os.path.isfile(req):
		try:
			print("Installing requirements...")
			subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req])
			print("Requirements installed.")
		except Exception:
			print("Failed to install requirements or already satisfied.")



if __name__ == "__main__":
	install_requirements()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(start_zombiebot())

#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================