# solo funciona con chats de whatsapp, creen su propia carpeta de chats
import numpy as np
import pandas as pd
import regex as re

def main():
    txts = [ # (chat.txt, nombre_persona_chat)
        ("chats/WhatsApp Chat with ✨ マン　カリーン　チンゲ.txt", "Pedro"),
        ("chats/WhatsApp Chat with Fellow King Dio Brando.txt", "Brandon"),
        ("chats/WhatsApp Chat with バラリア.txt", "Valeria")
        ]
    my_message = "Luis ドゴ: " # su nombre en el chat
    messages = []
    days = []
    people = []
    for txt in txts:
        with open(txt[0], 'r', encoding ='utf-8') as file:
            for line in file:
                if my_message in line:
                    pattern = f'{my_message}(.*)'
                    message = re.search(pattern, line).group(1)
                    day = line[:7]
                    messages.append(message)
                    days.append(day)
                    people.append(txt[1])
    df = pd.DataFrame(
        {
        "content" : messages,
        "day" : days,
        "person" : people,
        }
    )
    df = df[df["content"] != "<Media omitted>"] # borrar media xd
    df.to_csv('LDMS.csv', index=False)

if __name__ == "__main__":
    main()

