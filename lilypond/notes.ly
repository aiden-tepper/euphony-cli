global = {
  \key c \major
  \time 4/4
  \version "2.22.1"
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
d''4 d'' e'' |
a'4 b' c'' |
f'4 g' g' |
d'4 g c' |
}

\score {
          \new PianoStaff <<
             \new Staff {
               \global
               <<
                 \absolute c \voiceA
                 \\
                 \absolute c  \voiceB
               >>
             }
             \new Staff {
               \global \clef bass
               <<
                 \absolute c \voiceC
                 \\
                 \absolute c \voiceD
               >>
             }
          >>
        }
        