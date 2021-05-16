# Bdd tesztelés

A feladat során a Distest keretrendszerrel valósítottuk meg a teszteket. Ez egy Python-ban írt keretrendszer, amely kifejezetten a Discord bot-ok tesztelésére lett létrehozva.

A tesztelés kezdetén Corde-val kezdtünk el dolgozni, viszont ebben a Javascript alapú keretrendszerben nem lehetett várakozni a kiadott parancsok között.
Tanulmányozva ennek a forráskódját, rájöttünk, hogy rosszul van implementálva a tesztek futtatása, ezért váltottunk Distest-re. A várakozás azért szükséges a tesztekhez, hogy voice channel-hez tartozó funkcionalitást tesztelni lehessen.

A bot legtöbb funkciója a zenelejátszáshoz kapcsolódik, ezért a tesztek során erre helyeztük a hangsúlyt.

A tesztek futtatásához szükséges egy Discord szerver és két bot hozzáadása a szerverhez. Ezután az összes teszt lefuttatása a következő paranccsal lehetséges:

```
python main.py <bot_id> <tester_token> -c <channel_id> -r all
```

A kapcsolódó Github issue: [#5](https://github.com/BME-MIT-IET/iet-hf2021-elia/issues/5)