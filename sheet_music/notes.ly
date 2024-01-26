global = {
  \key c \major
  \time 4/4
  \version "2.22.1"
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
a''4 b'' c''' |
d''4 d'' e'' |
f'4 g' g' |
d'4 g c' |
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
        