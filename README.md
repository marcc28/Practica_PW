# ⚽ 🍾 FUTBOL CHAMPAN 🍾 ⚽

Aplicació web desenvolupada amb **Django** que permet consultar informació relacionada amb **La Liga**: equips, jugadors i partits. Pensada com a projecte acadèmic dins l'assignatura de **Projecte Web**.

 🔗 [Repositori GitHub](https://github.com/usuari/projecte-football-champan)

---

## 🧠 Objectiu del projecte

Desenvolupar una aplicació funcional que permeti consultar dades del món del futbol (concretament La Liga) amb gestió d'usuaris, gestió d'informació relacional entre equips, jugadors i partits, i desplegament amb Docker.

---

## 🧩 Funcionalitats implementades

- ✅ **Panell d'administració** de Django activat (`/admin`)
- ✅ **Model de dades relacionat**:
  - `Team`
  - `Player`
  - `Match`
- ✅ **Autenticació bàsica**:
  - Registre d’usuari (`/register`)
  - Inici de sessió (`/login`)
  - Tancament de sessió (`/logout`)
- ✅ **Plantilles HTML pròpies** amb herència (`base.html`) i sense
- ✅ **Estils propis amb CSS**
- ✅ **Contenidors Docker i `docker-compose`**
- ✅ **Compliment dels principis [12factor](https://12factor.net/)**

---

## ☝️ Consideracions de disseny
- `Simplicitat i claredat`: Hem optat per un disseny simple, clar i intuïtiu per fer la nostra pàgina web accessible a tots els usuaris.
- `Visuals`: Per una major claredaten el procès tant de registre com de login s'ha implementat un format independent a ```base.html```, utilitzant també un static diferent
- `Reducció de models`: S'ha pres la decisió unanimament d'eliminar el model **Season** especificat en el plantejament de la web, ja que coonsiderem que sería més convenient aplicar-ho com a filtre de búsqueda
- `Imatges`: En quant a imatges s'ha utilitzat un logotip i una imatge per cautivar l'atenció del públic, totes dues generades per intel·ligència artificial amb un toc personal dels memebres del grup
- `Patró`: Aprofitant els exemples vists a classe i explicats pel professor, s'han agafat idees i estructures per una millor estructura del projecte

---

## ▶️ Execució del projecte

Realitzar les migracions corresponents i aplicar-les a la base de dades:
```
python manage.py makemigrations
python manage.py migrate
```

Inicialitzar el servidor per poder visualitzar la pàgina web:
```
python manage.py runserver
```

Un cop el servidor esta corrent, ja es pot entrar a:
🔗 [localhost:8000](...)

### Accedir com a Administrador
Primer de tot abans d'accedir a la web, cal crear un superusuari:
```
python manage.py createsuperuser
```

Un cop creat, es pot entrar en mode administrador registrant-se amb l'usuari creat anteriorment a la següent pàgina:
🔗 [localhost:8000/admin](...)

---

## 👤 Desenvolupadors

- **Marc Companys Gasulla:** 53398418 P
- **Eloi Delfí Cristòfol Pardo:** 48054169 Q
- **Vicent Ripoll Baradat:** 48254634 J
- **Pau Segura Barta:** 48055739 E
- **Pau Serra París:** 49380869 F

