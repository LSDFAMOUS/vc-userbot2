import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("api id", "9210458"))
API_HASH = os.getenv("api hash", "f13a7d7848dea4309a38cb4b405d1749")
SESSION = os.getenv("BAGB5kgAkmTetRQpblrnTsIsT1SgKxiIxE9AMtgvDAezlQPTewLQDUiD53w1-iSGXpURo9hPdlYSsv16I_VA3Qe1JLmhxK4xl1Qq9vew7_zrcoyMzA4xv3UxWGs4og3ZZ0d_GqO1iRX2Fa-Wi7xaBsiUTUDtuX-cmDZSHj1f0-mzvyp3s_W4JNWfWcOvj9mAOvqbKqc_iDsgRM5W6IEFqsBuoGotfX3-ElHjWW4v_vjWdnPntkvn1o6W-4d58-OOx9YVFDHvX-Vx_GVz_XVQXKQwDDoQvusnGwrm8mwSdm9fTV_dG1jHrltUDPI02pqHDCdY13ekLEkn0nEWdPSGQv04cgZmLgAAAAGcfcvXAA")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="plugins"))
call_py = PyTgCalls(bot)
