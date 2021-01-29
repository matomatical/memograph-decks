from mg.graph import Node
from mg.data import parse

def graph():
    for topic, de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.art." + topic,
            )

LINKS = """topic -- de  -- en               # notes (ignored)
# articles
der --
    -- der              -- the              # definite article
    -- dieser           -- this/these       # demonstrative article close
    -- jener            -- that/those       # demonstrative article far
    -- einiger          -- some/few a       # are these also indefinite?
    -- mancher          -- some/many a
    -- irgendwelcher    -- some or other
    -- jeder            -- every/each
    -- solcher          -- such a
    -- welcher          -- which
    -- sämtliche        -- every/entire     # not used in singular
    -- alle             -- all              # not used in singular
    -- beider           -- both             # see usage notes
ein --
    -- ein              -- an               # indefinite article
    -- kein             -- no               # negative article
    -- mein             -- my               # possessive articles...
    -- dein             -- your (singular)
    -- sein             -- his/its (m)
    -- sein             -- its (n)
    -- ihr              -- her/its (f)
    -- unser            -- our
    -- euer             -- your (plural)
    -- ihr              -- their
    -- Ihr              -- your (formal)
    -- irgendein        -- someone's        # note it's irgend + ein!!
"""
