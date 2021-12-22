# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/Tatkuu/ot-harjoitustyo/releases/tag/Loppupalautus) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Ohjelman suorittaminen

Projektin alustaminen komennolla:
```
poetry install
```
tai 
```
python3 -m poetry install
```
Tämän jälkeen ohjelman voi käynnistää komennolla:
```
poetry run invoke start
```
tai
```
python3 -m poetry run invoke start
```
## Ohjelman käyttö

Peliä pelataan käyttämällä nuolinäppäimiä. Tavoitteena on kerätä ruuduylle ilmestyviä ruokia ja madon kasvaessa selviytyä mahdollisimman pitkään. Hävitessä pelin, voi joko aloittaa uuden pelin painamalla "play" painiketta tai poistua pelistä painamalla "quit" painiketta.
