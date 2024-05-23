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

Die folgenden Elemente sind invertierbar (berechnet mit Python)
|$$a$$|$$a^{-1}$$|
|-:|-:|
|1|1|
|3|9|
|5|21|
|7|15|
|9|3|
|11|19|
|15|7|
|17|23|
|19|11|
|21|5|
|23|17|
|25|25|

Damit lässt sich die Menge der möglichen Schlüssel bestimmen
$$\mid\mathcal{K}\mid = \mid\mathcal{L}\mid * \mid\mathcal{A}\mid = 12 * 26 = 312$$

Ein solches _affines symmetrisches Verschlüsselungsverfahren_ ist aus mehreren Gründen unsicher.
Erstens, weil 312 mögliche Schlüssel klein genug ist, um alle einfach auszuprobieren. Das Verfahren ist also bereits unsicher gegenüber _ciphertext-only_-Angriffen.

Zweitens, weil Muster in der Eingabe auch in der Aufgabe sichtbar sind (wie auf dem Bild mit dem Pinguin), weil die Verschiebung bei gleicher Eingabe immer genau gleich ist. Mithilfe von Heuristiken wie welche Buchstaben in der Sprache der Nachricht besonders häufig vorkommen, lässt sich die Nachricht dann auch entschlüsseln.
