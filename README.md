# IT Security SoSe 2024 Übung 2 Aufgabe 1

Kleines Programm zum Finden der multiplikativen Inversen bei Restklassenarithmetik mod 26 sowie zum Test der Dechiffrierung von $$Enc_k(m)=a*m+b\ \mathrm{mod}\ 26$$
mit folgenden Definitionen:

|||
|-|-|
|Alphabet $\mathcal{A}$|$\mathcal{A} = \\{A,B,C...Z\\}$|
|Nachricht $m$ | $m ∈ \mathcal{A}$|
|Schlüssel $k$ | $k = (a,b) ∈ \mathcal{K}$|
|Schlüsselraum $\mathcal{K}$ | $\mathcal{K} = \mathcal{L} × \mathcal{A}$|
|Menge $\mathcal{L}$ | $\mathcal{L} = \\{a ∈ \mathcal{A} \mid \exists a^{-1} \text{ sodass } a*a^{-1}\  \mathrm{mod}\ \mid\mathcal{A}\mid = 1\\}$|

Die Entschlüsselungsfunktion $Dec_k(\cdot)$ ist dann
$$Dec_k(\cdot) = a^{-1} * (m - b)\ \mathrm{mod}\ 26$$
