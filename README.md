# Snake Peli 

Sovelluksessa pelaaja ohjaa matoa muistuttavaa oliota, jonka tarkoituksena on kerätä ruudulle ilmestyviä ruokia. Jokainen kerta, kun pelaaja onnistuu keräämään ruudulle ilmestyneen ruuan, kasvaa madon hännän pituus. Mitä pidemmäksi mato kasvaa, sitä vaikeammaksi peli muuttuu. Madon pään osuessa omaan häntäänsä tai ruudun reunoille, peli päättyy. Pelaaja pystyy valitsemaan madon suunnan ohjaamalla madon päätä nuolinäppäimillä.

## Dokumentaatiot

- [käyttöohje](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
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
