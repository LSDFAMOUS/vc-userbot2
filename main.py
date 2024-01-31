from telethon import TelegramClient, sync
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream



client = TelegramClient(
        'BAGB5kgAkmTetRQpblrnTsIsT1SgKxiIxE9AMtgvDAezlQPTewLQDUiD53w1-iSGXpURo9hPdlYSsv16I_VA3Qe1JLmhxK4xl1Qq9vew7_zrcoyMzA4xv3UxWGs4og3ZZ0d_GqO1iRX2Fa-Wi7xaBsiUTUDtuX-cmDZSHj1f0-mzvyp3s_W4JNWfWcOvj9mAOvqbKqc_iDsgRM5W6IEFqsBuoGotfX3-ElHjWW4v_vjWdnPntkvn1o6W-4d58-OOx9YVFDHvX-Vx_GVz_XVQXKQwDDoQvusnGwrm8mwSdm9fTV_dG1jHrltUDPI02pqHDCdY13ekLEkn0nEWdPSGQv04cgZmLgAAAAGcfcvXAA',
        9210458,
        f13a7d7848dea4309a38cb4b405d1749
    )
client.connect()
group = client.get_entity('https://t.me/group_link')
client.disconnect()
call_py = PyTgCalls(client)
call_py.start()
call_py.join_group_call(
    group.id,
    InputStream(
        InputAudioStream(
            'input.raw',
        ),
    ),
    stream_type=StreamType().local_stream,
)
idle()
