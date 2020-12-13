from mg.graph import Node

def graph():
    for line in LINKS.splitlines()[1:]:
        if "--" not in line:
            continue
        de, en = map(str.strip, line.split("#")[0].split("--"))
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.adj"
            )

LINKS = """de -- en                                     # notes (ignored)
ganz          -- whole    
ganz          -- all of the
groß          -- great/big
groß          -- tall    
gut           -- good
neu           -- new
erste         -- first                                  # always decline
lang          -- long
deutsch       -- German
klein         -- small    
alt           -- old
hoch          -- high
hoch          -- tall    
einfach       -- easy    
letzte        -- last                                   # always decline
gleich        -- like/same/equal
gleich        -- right away                             # as an adverb?
möglich       -- possible                               # lit. 'likely'?
eigen         -- own/characteristic
schön         -- beautiful/pleasant
spät          -- late
wichtig       -- important
weitere       -- additional                             # always decline
genau         -- exact
jung          -- young
kurz          -- short
stark         -- strong
richtig       -- right/correct
verschieden   -- various/different/diverse
bestimmt      -- special/particular    
besser        -- better                                 # comparative of gut?
schnell       -- fast
sicher        -- sure/certain
sicher        -- safe/secure
nächste       -- next                                   # always decline
politisch     -- political
klar          -- clear    
schwer        -- difficult    
schwer        -- heavy
einzeln       -- individual
bekannt       -- well-known
leicht        -- light (not heavy)                      # cf. hell
leicht        -- easy    
rund          -- round
frei          -- free (as in freedom)                   # cf. gratis/kostenlos
früh          -- early
unterschiedlich -- variable/different/diverse
schlecht      -- bad
deutlich      -- clear    
allgemein     -- general
einzig        -- only/sole
gemeinsam     -- common/mutual
nah           -- near/close                             # also nahe?
voll          -- full
direkt        -- direct
international -- international
sozial        -- social
beste         -- best                                   # always decline
                                                        # superlative of gut?
rot           -- red
offen         -- open
meiste        -- most
besondere     -- special/particular    
gewiss        -- known/certain
öffentlich    -- public
halb          -- half
wahrscheinlich -- probable                              # lit.'trueseeming'?
europäisch    -- European
wesentlich    -- essential/fundamental
ähnlich       -- similar
häufig        -- frequent
schwarz       -- black
völlig        -- complete
gering        -- low
gering        -- small    
schwierig     -- difficult    
praktisch     -- practical
persönlich    -- personal
-jährig       -- -years old
modern        -- modern
tief          -- deep
tatsächlich   -- actual/real
zusätzlich    -- additional    
amerikanisch  -- American
wirtschaftlich -- economic/financial
interessant   -- interesting
relativ       -- relative
gleichzeitig  -- simultaneous
grün          -- green
weiß          -- white
gesamt        -- whole/entire    
speziell      -- special/particular    
entscheidend  -- decisive                               # entscheiden + 'd'
                                                        # lit. 'deciding'
eng           -- narrow/close
technisch     -- technical
langsam       -- slow
ständing      -- constant
notwendig     -- necessary
rein          -- pure/pristine
englisch      -- English
wissenschaftlich -- scientific/scholarly
falsch        -- false
fremd         -- foreign/strange/alien
fransösisch   -- French
selten        -- rare
normal        -- normal
wahr          -- true
privat        -- private
tot           -- dead
"""
