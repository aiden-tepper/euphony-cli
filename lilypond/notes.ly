global = {
  \key c \major
  \time 4/4
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
c4 a d g c |
e4 e f f e |
g4 g a b g |
b4 des c d b |
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
        