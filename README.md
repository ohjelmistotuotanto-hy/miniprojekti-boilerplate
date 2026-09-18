## Ohtu miniprojekti boilerplate

Lue [täältä](https://ohjelmistotuotanto-hy.github.io/flask/) lisää.

Muutamia vihjeitä projektin alkuun [täällä](https://github.com/ohjelmistotuotanto-hy/miniprojekti-boilerplate/blob/main/misc/ohjeita.md).

### Sovelluksen deployaus OKD:hen

Oletuksena on, että olet jo kirjautunut `oc`-komentorivityökalulla oikeaan OKD-klusteriin ja oikeaan projektiin/namespaceen (`oc project <namespace>`).

Ensimmäisellä kerralla luo salaisuustiedosto kopioimalla malli ja täyttämällä oikea arvo:

```sh
cp secret.env.template secret.env
```

Muokkaa tiedostoon `secret.env` oikea `SECRET_KEY`-arvo. Tiedostoa ei lisätä versionhallintaan.

Sovellus deployataan (tai päivitetään) klusterille [Kustomize](https://kustomize.io/)n avulla komennolla:

```sh
oc apply -k .
```

Komento luo/päivittää kaikki `kustomization.yaml`-tiedostossa määritellyt resurssit (ConfigMap, Secret, ImageStream, Service, Route, PersistentVolumeClaim ja Deployment) valittuun namespaceen.
