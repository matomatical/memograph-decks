from mg.graph import Node
from mg.data import parse

def graph():
    for topic, de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.conj." + topic,
            )

LINKS = """topic -- de  -- en               # notes (ignored)
coo --
    -- und              -- and
    -- oder             -- or
    -- aber             -- but/however
    -- denn             -- because/since
    -- sondern          -- but (on the contrary)    # negative main clause
    -- sowohl - als     -- both - and
    -- weder* - noch*   -- neither - nor
    -- entweder* - oder -- either - or
    -- nicht nur* - sondern auch -- not only - but also
sub --
    -- dass             -- that
    -- als              -- as/when
    -- wenn             -- when/if
    -- weil             -- because
    -- ob               -- if
    -- obwohl           -- although
    -- falls            -- in case/if
    -- da               -- because/since
    -- damit            -- so that
    -- seit             -- since (time)
    -- nachdem          -- after
    -- bevor            -- before
    -- indem            -- while/during
    -- um (zu)          -- in order (to)
    -- ohne (zu)        -- without (to)
    -- zumal            -- especially since
    -- ehe              -- before/until
    -- sowie            -- as well as/as soon as
    -- sodass           -- so that
    -- solange          -- so long as
    -- sobald           -- as soon as
    -- sofern           -- provided that
    -- umso             -- all the
    -- während          -- while/during
    # TODO: classify JE - DESTO and BEZEIHUNGSWEISE
"""
