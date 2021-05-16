# Nemfunkcionális tesztelés

A feladat során a *Distest* python discord BDD tesztelő keretrendszer használatával készítettem teszteket, melyek arra szolgáltak, hogy egyes kérések válasz sebességét mérhessük fel.

Mivel ezt egy BDD tesztkeretrendszer segítségével készítettük el, ezért valós válaszidőket fogunk kapni, melyeket a felhasználók fognak tapasztalni. Az Elia projekt elég szerte ágazóan használható, azonban a legfejlettebb része a zenelejátszással kapcsolatos. Ezért a két legfontosabb teszt a voice channel-re való felkapcsolódás és lekapcsolódás, valamint a zenelejátszás elindításának sebessége.

A teszt eredménye arra utal, hogy más hasonló funkciókat megvalósító discord botokhoz képest hasonló a teljesítmény, így a kód ilyen szempontból jól optimalizált.

A tesztek lefuttatásához hasonlóan kell eljárni, mint a BDD tesztek lefuttatásával:

```shell
python main.py <bot_id> <tester_token> -c <channel_id> -r all
```

Azonban a tesztek nem a `test/bdd/`, hanem a `test/performance/` mappa alatt találhatók. A keretrendszerhez készült egy *pipenv* környezet, melyet a futtatáshoz használni kell.
