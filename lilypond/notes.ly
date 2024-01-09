global = {
  \key bes \minor
  \time 4/4
  \version "2.22.1"
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
bes''4 c''' d''' ees''' ees''' d''' c''' bes'' |
d''4 f'' f'' g'' g'' ges'' ges'' d'' |
g'4 a' bes' bes' a' a' a' g' |
g4 f' bes ees' ees' d' d' g |
}

\score {
          \new PianoStaff <<
             \new Staff {
               \global
               <<
                 \fixed c \voiceA
                 \\
                 \fixed c,  \voiceB
               >>
             }
             \new Staff {
               \global \clef bass
               <<
                 \fixed c, \voiceC
                 \\
                 \fixed c, \voiceD
               >>
             }
          >>
        }
        