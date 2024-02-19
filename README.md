# Snake Game
In the application, the player controls a worm-like creature with the objective of collecting food that appears on the screen. Each time the player successfully collects the food that has appeared, the length of the worm's tail increases. The longer the worm grows, the more difficult the game becomes. If the worm's head touches its own tail or the edges of the screen, the game ends. The player can choose the direction of the worm by steering its head with the arrow keys.

## Documentations

- [user manual](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [tuntikirjanpito](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [vaatimusmäärittely](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [testausdokumentti](https://github.com/Tatkuu/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Installation
Clone repository:
```
git clone git@github.com:Tatkuu/ot-harjoitustyo.git ot_harjoitustyo_tatkuu
```
Initialize project:
```
poetry install
```
or
```
python3 -m poetry install
```

## Commandline commands
Start program:
```
poetry run invoke start
```
or
```
python3 -m poetry run invoke start
```

### Tests
Run tests:
```
poetry run invoke test
```
or
```
python3 -m poetry run invoke test
```
### Test coverage
Generate test coverage report:
```
poetry run invoke coverage-report
``` 
or
```
python3 -m poetry run invoke coverage-report
``` 
### Code quality tests
Run quality tests:
```
poetry run invoke pylint
```  
or
```
python3 -m poetry run invoke pylint
``` 
