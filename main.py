#!/usr/bin/env python
# pyright: reportUnusedVariable=false, reportGeneralTypeIssues=false
"""

Hit RUN to execute the program.

You can also deploy a stable, public version of your project, unaffected by the changes you make in the workspace.

This proof-of-concept Telegram bot takes a user's text messages and turns them into stylish images. Utilizing Python, the `python-telegram-bot` library, and PIL for image manipulation, it offers a quick and interactive way to generate content.

Read the README.md file for more information on how to get and deploy Telegram bots.
"""

import logging

from telegram import __version__ as TG_VER

try:
  from telegram import __version_info__
except ImportError:
  __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
  raise RuntimeError(
      f"This example is not compatible with your current PTB version {TG_VER}. To view the "
      f"{TG_VER} version of this example, "
      f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html")

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from PIL import Image, ImageDraw, ImageFont
import os

my_bot_token = os.environ['BOT_TOKEN']

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
