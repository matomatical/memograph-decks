from mg.graph import SpokenNode

def graph():
    for line in LINKS.splitlines()[1:]:
        de, en = line.split("#")[0].split("--")
        art, de = de[:3], de[4:].strip()
        en = en.strip()
        yield (
                SpokenNode(en, voice="english"),
                SpokenNode(de, text=f"{art} {de}", voice="german"),
                "de.noun.en"
            )
        if " (" not in de or "(1)" in de:
            de = de.split(" (", maxsplit=1)[0]
            yield (
                    SpokenNode(de, voice="german"),
                    SpokenNode(art, text=f"{art} {de}", voice="german"),
                    "de.noun.gender"
                )

LINKS = """art de -- the en                             # notes (ignored)
das Jahr          -- the year
das Mal           -- the time/occurrence
das Beispiel      -- the example
die Zeit          -- the time
die Frau          -- the woman/wife                     # also title 'Mrs.'
der Mensch        -- the man/human
das Kind          -- the child
der Tag           -- the day
der Mann          -- the man/husband
das Land          -- the land/country
die Frage         -- the question
das Haus          -- the house/home
der Fall          -- the fall                           # also means 'case'
pl. Leute         -- the people                         # plural only
die Arbeit        -- the work
das Prozent       -- the percent
die Hand          -- the hand
die Stadt         -- the town/city (1)
der Herr          -- the gentleman                      # also title 'Mr.'
der Teil          -- the part/section
das Problem       -- the problem
die Welt          -- the world
das Recht         -- the right/law
das Ende          -- the end
die Million       -- the million
die Schule        -- the school
die Woche         -- the week
der Vater         -- the father
die Seite (1)     -- the side
die Seite (2)     -- the page
das Leben         -- the life
die Mutter        -- the mother
der Grund         -- the grounding/basis/reason
das Auge          -- the eye
das Wort          -- the word
das Geld          -- the money
die Sache         -- the thing (1)
die Art           -- the type/kind
der Bereich       -- the area/region
der Weg           -- the way/path
die Stunde        -- the hour
der Name          -- the name
die Geschichte    -- the history
die Gesellschaft  -- the society/company
der Kopf          -- the head
das Paar          -- the pair/couple
die Möglichkeit   -- the likelihood/possibility
das Unternehmen   -- the enterprise/company
das Bild          -- the picture
das Buch          -- the book
das Wasser        -- the water
die Stelle        -- the place (1)                      # stellen = to place
die Form          -- the form/shape
die Mark          -- the mark (old unit of currency)
die Entwicklung   -- the development
der Monat         -- the month
die Familie       -- the family
der Morgen        -- the morning                        # also 'tomorrow'?
der Abend         -- the evening
die Aufgabe       -- the task/asg./job
die Universität   -- the university                     # abbr.: 'die Uni'
der Sinn          -- the sense/meaning
der Staat         -- the state
das Ziel (1)      -- the goal
das Ziel (2)      -- the destination
der Freund        -- the friend (m)
die Freundin      -- the friend (f)
das Thema         -- the topic/theme
die Person        -- the person
der Euro          -- the euro (unit of currency)
die Nacht         -- the night
das Ding          -- the thing (2)
der Raum          -- the room/space
der Blick         -- the look/glance/view
der Platz (1)     -- the place (2)
der Platz (2)     -- the square (public square)
die Zahl          -- the number
das System        -- the system
die Uhr (1)       -- the clock/watch
die Uhr (2)       -- the o'clock
pl. Eltern        -- the parents                        # plural only
die Straße        -- the street
die Minute        -- the minute
die Gruppe        -- the group
der Wert          -- the value/worth
das Gesicht       -- the face
die Sprache       -- the language
der Anfang        -- the beginning
der Ort (1)       -- the place/location (3)
der Ort (2)       -- the town (2)
der Moment        -- the moment
die Folge         -- the result/consequence (1)
das Interesse     -- the interest
die Milliarde     -- the billion
die Rolle (1)     -- the role
die Rolle (2)     -- the roll
die Tür           -- the door
der Schüler       -- the pupil/student (m)
die Schülerin     -- the pupil/student (f)
die Bedeutung (1) -- the meaning
die Bedeutung (2) -- the significance
der Text          -- the text
das Ergebnis      -- the result (2)
der Krieg         -- the war
die Weise         -- the way/manner
die Regierung     -- the rule/government
das Stück         -- the piece/bit/part
die Wohnung       -- the apartment
das Gespräch      -- the conversation
"""
