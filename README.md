## Ohtu miniprojekti viitesovellus

[Projektin Backlog](https://docs.google.com/spreadsheets/d/18hvBnpqpfrvLp4IAaIMx_yBNn7XAfu3UsJ9Jm_BIFVE/edit?usp=sharing)

[Github Actions](https://github.com/SoftaSankarit/miniprojekti-boilerplate/actions)
[![GHA workflow badge](https://github.com/SoftaSankarit/miniprojekti-boilerplate/workflows/CI/badge.svg)](https://github.com/SoftaSankarit/miniprojekti-boilerplate/actions)


### Ohjelman asennus- ja käyttöohje

Esivaatimukset: Varmista, että sinulla on Python3 ja PostgreSQL asennettuna tietokoneellesi.

Kloonaa seuraava repositorio koneellesi:
```
git clone https://github.com/SoftaSankarit/miniprojekti-boilerplate.git
```
Luo .env-tiedosto Luo juurihakemistoon .env-tiedosto ja määritä sen sisältö seuraavasti:
```
DATABASE_URL=<database-local-address>
TEST_ENV=true
SECRET_KEY=<secret-key>
```
Mene projektin juurikansioon ja asennan poetryn riippuvuudet komennolla:
```
poetry install
```
Mene virtuaaliympäristöön komennolla:
```
poetry shell
```
Luo sql-taulukko komennolla:
```
python3 src/db_helper.py
```
Käynnistä sovellus komennolla:
```
python3 src/index.py
```