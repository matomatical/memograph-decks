from mg.graph import Node
from mg.data import parse

def graph():
    for de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.adv"
            )

LINKS = """de -- en                                     # notes (ignored)
"""
