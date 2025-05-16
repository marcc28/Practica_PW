# ⚽ 🍾 FUTBOL CHAMPAN 🍾 ⚽

Aplicació web desenvolupada amb **Django** que permet consultar informació relacionada amb **La Liga**: equips, jugadors i partits. Pensada com a projecte acadèmic dins l'assignatura de **Projecte Web**.

 🔗 [Repositori GitHub](https://github.com/marcc28/Practica_PW)

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

## ☝️ Consideracions de disseny (deliverable 1)
- `Simplicitat i claredat`: Hem optat per un disseny simple, clar i intuïtiu per fer la nostra pàgina web accessible a tots els usuaris.
- `Visuals`: Per una major claredaten el procès tant de registre com de login s'ha implementat un format independent a ```base.html```, utilitzant també un static diferent
- `Reducció de models`: S'ha pres la decisió unanimament d'eliminar el model **Season** especificat en el plantejament de la web, ja que coonsiderem que sería més convenient aplicar-ho com a filtre de búsqueda
- `Imatges`: En quant a imatges s'ha utilitzat un logotip i una imatge per cautivar l'atenció del públic, totes dues generades per intel·ligència artificial amb un toc personal dels memebres del grup
- `Patró`: Aprofitant els exemples vists a classe i explicats pel professor, s'han agafat idees i estructures per una millor estructura del projecte

## ☝️ Consideracions de disseny (deliverable 2)
- `Consistència`: Totes les vistes de creació, edició i eliminació s'han desenvolupat amb **Class-Based Views (CBV)** i **ModelForms**, garantint una estructura coherent i mantenible, aixi com un artibut creador per comprovar la creació, edició i eliminació.
- `API externa`: S'ha integrat una API externa per facilitar l'entrada de dades en formularis, millorant així la usabilitat. Aquesta funcionalitat s'ha implementat amb **AJAX i jQuery** per carregar dades de forma dinàmica.
- `Escalabilitat`: El projecte està dissenyat perquè sigui fàcilment ampliable en futures versions, tant pel que fa a models com a funcionalitats addicionals.
- `Accessibilitat`: L'estructura visual i la navegació han estat simplificades per garantir una experiència d'usuari fluida i entenedora.



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

## 🧑‍💼 Superusuario

- **Usuario:** `prova`  
- **Contraseña:** `prova1234`  
- **📌 Nota:** No se han añadido equipos ni jugadores con este usuario.

---


## 👤 Usuario: `marc`

- **Contraseña:** `Marcc_28`  
- **Contenido Asociado:**
  - 🏟️ **Equipo:** *Lleida FC*
  - 🧍‍♂️ **Jugador:** *Vicent Ripoll*

---

## 👥 Desenvolupadors

- **Marc Companys Gasulla:** 53398418 P
- **Eloi Delfí Cristòfol Pardo:** 48054169 Q
- **Vicent Ripoll Baradat:** 48254634 J
- **Pau Segura Barta:** 48055739 E
- **Pau Serra París:** 49380869 F

