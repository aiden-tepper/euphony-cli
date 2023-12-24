global = {
  \key d \major
  \time 4/4
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
d4 a b g d |
d4 e d b a |
ges4 a ges d des |
a4 des b g ges |
}

\score {
          \new PianoStaff <<
             \new Staff {
               \global
               <<
                 \relative c'' \voiceA
                 \\
                 \relative c'  \voiceB
               >>
             }
             \new Staff {
               \global \clef bass
               <<
                 \relative c \voiceC
                 \\
                 \relative c \voiceD
               >>
             }
          >>
        }
        