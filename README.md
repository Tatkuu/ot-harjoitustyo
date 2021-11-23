# Snake Peli 

Sovelluksessa pelaaja ohjaa matoa muistuttavaa oliota, jonka tarkoituksena on kerätä ruudulle ilmestyviä ruokia. Jokainen kerta, kun pelaaja onnistuu keräämään ruudulle ilmestyneen ruuan, kasvaa madon hännän pituus. Mitä pidemmäksi mato kasvaa, sitä vaikeammaksi peli muuttuu. Madon pään osuessa omaan häntäänsä tai ruudun reunoille, peli päättyy. Pelaaja pystyy valitsemaan madon suunnan ohjaamalla madon päätä nuolinäppäimillä.

## Dokumentaatiot

[tuntikirjanpito](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaatimusmäärittely](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

## Asennus
Kloonaa repositorio komennolla:
```
git clone git@github.com:Tatkuu/ot-harjoitustyo.git ot_harjoitustyo_tatkuu
```
Alusta projekti komennolla:
```
poetry install
```

## Komentorivitoiminnot
Käynnistä ohjelma komennolla:
```
poetry run invoke start
```
### Testit
Testien suorittaminen komennolla:
```
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin generointi komennolla:
```
poetry run invoke coverage-report
```  

