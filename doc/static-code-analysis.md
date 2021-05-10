# Statikus kód ellenőrzés

A feladatat során lefuttattam a SonarCloud-ot és a kimenetek alapján kezdetem el javítani a kód minőséségén.

A code smellekből nem vol sok, ezért mindet javíttottam. SonarCloud jó irányokat mutat, bár ha komolyabb refaktorálásról van szó, akkor nem sokat segít, viszont a refakorálás után újból lefutattható, addig ameddig nem vesz észre code smell-t.

1 security hibát jelzett a SonarCloud, ezt nem javítottam ki, erre nem volt szükség ebben az esetben: A math.random() nem elég erős algoritmus kriptográfiailag. Ebben az esetben ez megengedhető, hiszen nem biztonság kritikus alkalmazásról van szó, és a randomizálás egy tömb elemeit kavarja össze, ezen tömb viszont publikusan lekérhető  egy parancsal mindig. Ezen két ok miatt döntöttem úgy hogy ebben az esetben ezt nem kell javítani.

A kapcsolódó Github issue: [#6](https://github.com/BME-MIT-IET/iet-hf2021-elia/issues/6)