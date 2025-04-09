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
- ✅ **Plantilles HTML pròpies** amb herència (`base.html`)
- ✅ **Estils propis amb CSS**
- ✅ **Contenidors Docker i `docker-compose`**
- ✅ **Compliment dels principis [12factor](https://12factor.net/)**

---

## ☝️ Consideracions
- `Simplicitat i claredat`: Hem optat per un disseny simple, clar i intuïtiu per fer la nostra pàgina web accessible a tots els usuaris.
- ``

---

## ▶️ Execució del projecte

Inicialització de Docker Compose 🐳
```
docker-compose up
```

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

