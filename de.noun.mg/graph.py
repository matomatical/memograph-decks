from mg.graph import Node

def graph():
    for line in LINKS.splitlines()[1:]:
        if "--" not in line:
            continue
        de, en = map(str.strip, line.split("#")[0].split("--"))
        art, noun = de[:3], de[4:]
        words = set()
        yield (
                Node(en,   speak_str=en, speak_voice="en"),
                Node(noun, print_str=de, speak_str=de, speak_voice="de"),
                "de.noun.en"
            )
        if de not in words:
            words.add(de)
            yield (
                    Node(noun, speak_str=noun, speak_voice="de"),
                    Node(art,  speak_str=de,   speak_voice="de"),
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
die Stadt         -- the town/city    
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
die Seite         -- the side
die Seite         -- the page
das Leben         -- the life
die Mutter        -- the mother
der Grund         -- the grounding/basis/reason
das Auge          -- the eye
das Wort          -- the word
das Geld          -- the money
die Sache         -- the thing    
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
die Stelle        -- the place                          # stellen = to place
die Stelle        -- the position/role                  # like for a job
die Form          -- the form/shape
die Mark          -- the mark (currency)
die Entwicklung   -- the development
der Monat         -- the month
die Familie       -- the family
der Morgen        -- the morning                        # also 'tomorrow'?
der Abend         -- the evening
die Aufgabe       -- the task/asg./job
die Universität   -- the university                     # abbr.: 'die Uni'
der Sinn          -- the sense/meaning
der Staat         -- the state
das Ziel          -- the goal
das Ziel          -- the destination
der Freund        -- the friend (m)
die Freundin      -- the friend (f)
das Thema         -- the topic/theme
die Person        -- the person
der Euro          -- the euro (currency)
die Nacht         -- the night
das Ding          -- the thing    
der Raum          -- the room/space
der Blick         -- the look/glance/view
der Platz         -- the place    
der Platz         -- the public square
die Zahl          -- the number
das System        -- the system
die Uhr           -- the clock/watch
die Uhr           -- the o'clock
pl. Eltern        -- the parents                        # plural only
die Straße        -- the street
die Minute        -- the minute
die Gruppe        -- the group
der Wert          -- the value/worth
das Gesicht       -- the face
die Sprache       -- the language
der Anfang        -- the beginning
der Ort           -- the place/location    
der Ort           -- the town    
der Moment        -- the moment
die Folge         -- the result/consequence    
das Interesse     -- the interest
die Milliarde     -- the billion
die Rolle         -- the role
die Rolle         -- the roll
die Tür           -- the door
der Schüler       -- the pupil/student (m)
die Schülerin     -- the pupil/student (f)
die Bedeutung     -- the meaning
die Bedeutung     -- the significance
der Text          -- the text
das Ergebnis      -- the result    
der Krieg         -- the war
die Weise         -- the way/manner
die Regierung     -- the rule/government
das Stück         -- the piece/bit/part
die Wohnung       -- the apartment
das Gespräch      -- the conversation
"""
