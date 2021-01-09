from mg.graph import Node
from mg.data import parse

def graph():
    for topic, de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.pron." + topic,
            )

LINKS = """topic -- de  -- en               # notes (ignored)
personal.nom --
    -- ich              -- I
    -- du               -- you (singular)
    -- er               -- he/it (m)
    -- es               -- it (n)
    -- sie              -- she/it (f)
    -- man              -- man/one
    -- man              -- they (impersonal)
    -- wir              -- we
    -- ihr              -- you (plural)
    -- sie              -- they
    -- Sie              -- you (formal)
personal.akk --
    -- mich             -- me
    -- dich             -- you (singular)
    -- ihn              -- him/it (m)
    -- es               -- it (n)
    -- sie              -- she/it (f)
    -- einen            -- one
    -- uns              -- us
    -- euch             -- you (plural)
    -- sie              -- them
    -- Sie              -- you (formal)
personal.dat --
    -- mir              -- to me
    -- dir              -- to you (singular)
    -- ihm              -- to him/it (m)
    -- ihm              -- to it (n)
    -- ihr              -- to her/it (f)
    -- einem            -- to one
    -- uns              -- to us
    -- euch             -- to you (plural)
    -- ihnen            -- to them
    -- Ihnen            -- to you (formal)
reflexive --
    -- mich             -- myself
    -- mir              -- to myself
    -- dich             -- yourself (singular)
    -- dir              -- to yourself (singular)
    -- sich             -- (to) himself/itself (m)
    -- sich             -- (to) itself (n)
    -- sich             -- (to) herself/itself (f)
    -- uns              -- (to) ourselves
    -- euch             -- (to) yourselves
    -- sich             -- (to) themselves
    -- sich             -- (to) yourself (formal)   # Note: no capital!
possessive --
    -- meiner           -- mine
    -- deiner           -- yours (singular)
    -- seiner           -- his/its (m)
    -- seiner           -- its (n)
    -- ihrer            -- hers/its (f)
    -- unser            -- ours
    -- euer             -- yours (plural)
    -- ihrer            -- theirs
    -- Ihrer            -- yours (formal)
possessive.wegen --
    -- meinetwegen      -- on my account
    -- deinetwegen      -- on your (singular) account
    -- seinetwegen      -- on his/its (m) account
    -- seinetwegen      -- on its (n) account
    -- ihretwegen       -- on her/its (f) account
    -- unsertwegen      -- on our account
    -- euretwegen       -- on your (plural) account
    -- Ihretwegen       -- on your (formal) account
interrogative --
    -- was              -- what
    -- wer              -- who              # nominative who     of course,
    -- wen              -- whom             # accusative who     this is just
    -- wem              -- to whom          # dative who         EXTRA-STRONG
    -- wessen           -- whose            # genitive who       DECLENSION
    -- wo               -- where
    -- wann             -- when
    -- wie              -- how
    -- warum            -- why
    -- welcher          -- which
    -- was für einer    -- what for a/what kind of
    -- wofür            -- wherefor/for what/why
    -- wodurch          -- whereby/by what/how
    -- wobei            -- whereby/by what/near what
    -- womit            -- wherewith/with what
    -- worauf           -- whereon/on what
relative --
    -- der(en)          -- that             # takes EXTRA-STRONG DECLENSION
    -- wer              -- who              # EXTRA-STRONG DECLENSION
    -- wen              -- whom
    -- wem              -- to whom
    -- wessen           -- whose
    -- was              -- what
demonstrative --
    -- der(en)          -- the (spoken)     # takes EXTRA-STRONG DECLENSION
    -- dieser           -- this/these       # not in spoken geran
    -- jener            -- that/those       # not in spoken german
    -- derselbe         -- the same one     # decline the 'der' bit
    -- derjenige        -- the one          # decline the 'der' bit
indefinite --
    -- etwas            -- something
    -- nichts           -- nothing
    -- irgendetwas      -- something or other
    -- alles            -- everything
    -- jemand           -- someone          # case declension -/en/em/es
    -- irgendjemand     -- someone or other # case declension -/en/em/es
    -- niemand          -- noone            # case declension -/en/em/es
    -- einer            -- one              # no plural; DER declension
    -- keiner           -- none             # DER declension
    -- jeder (?)        -- anyone/everyone? # what is the declension?
    -- einiger (?)      -- some/few         # what is the declension?
    -- mancher (?)      -- many             # what is the declension?
    -- solcher (?)      -- such             # what is the declension?
"""
