# Snake Game
In the application, the player controls a worm-like creature with the objective of collecting food that appears on the screen. Each time the player successfully collects the food that has appeared, the length of the worm's tail increases. The longer the worm grows, the more difficult the game becomes. If the worm's head touches its own tail or the edges of the screen, the game ends. The player can choose the direction of the worm by steering its head with the arrow keys.

## Documentations

- [user manual](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [tuntikirjanpito](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [vaatimusmäärittely](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [testausdokumentti](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Asennus
Kloonaa repositorio komennolla:
```
git clone git@github.com:Tatkuu/ot-harjoitustyo.git ot_harjoitustyo_tatkuu
```
Alusta projekti komennolla:
```
poetry install
```
tai 
```
python3 -m poetry install
```

## Komentorivitoiminnot
Käynnistä ohjelma komennolla:
```
poetry run invoke start
```
tai
```
python3 -m poetry run invoke start
```

### Testit
Testien suorittaminen komennolla:
```
poetry run invoke test
```
tai
```
python3 -m poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin generointi komennolla:
```
poetry run invoke coverage-report
``` 
tai
```
python3 -m poetry run invoke coverage-report
``` 
### Koodin laadun testaus
Koodin laadun analyysi komennolla:
```
poetry run invoke pylint
```  
tai
```
python3 -m poetry run invoke pylint
``` 
