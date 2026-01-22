# 🍽️ Projecte Cuina

**Pràctica 2 – Crear Templates de pàgina Cuina**  
**Desenvolupament en Entorn Servidor (DES)**  
CFGS Desenvolupament d’Aplicacions Web (DAW)

**Institut:** INS Daniel Blanxart i Pedrals  
**Departament:** Departament d’Ensenyament – Generalitat de Catalunya  

---

## 👨‍💻 Autors

- **Javier Pedragosa**
- **Guillem Riera**

Projecte desenvolupat en parella com a part de l’avaluació de l’assignatura **Desenvolupament en Entorn Servidor**.

---

## 📌 Descripció del projecte

Aquest projecte consisteix en la creació d’una aplicació web anomenada **Cuina**, desenvolupada amb **Django** i gestionada amb **uv (Python)**.

El projecte fa ús de:
- Plantilles HTML
- Herència de templates
- URLs dinàmiques
- Components reutilitzables

L’objectiu principal és construir una estructura base de pàgines amb un **menú** i un **footer** comuns, complint totes les especificacions indicades a l’enunciat de la pràctica.

> ⚠️ El disseny no és l’objectiu principal del projecte; es prioritza la correcta estructura i ús de Django.

---

## 🧱 Estructura del projecte

El projecte **cuina** conté les següents aplicacions:

- Home
- Registre d’usuaris
- Receptes
- Introduir Receptes
- Peticions a l’admin
- FAQs (manual de la web)

Totes les aplicacions estan vinculades al mateix projecte Django.

---

## 🧭 Navegació (Menú)

- Totes les pàgines comparteixen el **mateix menú de navegació**.
- El menú inclou un espai per fer **Login**.
- Les opcions **Receptes** i **Introduir Receptes** estan **ocultes** al menú.
- En fer clic a una opció del menú:
  - Es mostra el títol corresponent.
  - Es mantenen el menú i el footer.
  - El contingut pot ser buit segons la secció.

---

## 🦶 Footer comú

Totes les pàgines disposen d’un **footer compartit**, que inclou:

- Xarxes socials (només mencionades).
- Nom de l’associació o empresa fictícia.
- **Política de cookies** (banner informatiu).
- **Política de privacitat de dades** (banner informatiu).
- Formes de pagament acceptades:
  - PayPal
  - Visa
  - Mastercard  
  (representades amb icones)

---

## 🏠 Pàgina Home

La pàgina **Home** inclou:

- Nom del lloc web.
- Logo creat amb **intel·ligència artificial**.
- Imatges relacionades amb la cuina.
- Text descriptiu sobre:
  - Quan es va fundar el projecte.
  - El motiu del projecte.
  - On estem.
  - Aficions o interessos relacionats amb la cuina.

---

## ❓ Pàgina de FAQs

La pàgina de **Preguntes Freqüents** compleix els següents requisits:

- Conté **com a mínim 8 preguntes**.
- Inicialment només es mostren les preguntes.
- Les respostes apareixen en **desplegables** en fer clic.
- Tipologia de preguntes:
  - Quant temps es triga a donar-se d’alta.
  - Cost de pertànyer al club (gratuït).
  - On dirigir-se en cas de dubtes.
  - Com donar-se de baixa.
  - Altres preguntes relacionades amb el funcionament del web.

---

## ⚙️ Especificacions tècniques

- Framework: **Django**
- Gestió del projecte: **uv (Python)**
- Framework de CSS: lliure (Bootstrap, Tailwind, etc.)
- No es requereix disseny responsive

Ús obligatori de:
- Herència de plantilles
- URLs dinàmiques
- Bucles amb templates

> ❗ El disseny no es valora, però s’eviten paletes de colors inadequades, tipografies il·legibles, animacions excessives o logos sense relació amb el projecte.

---

## 🔐 Control de versions

Aquest projecte es gestiona amb **Git** per evitar la pèrdua de dades.

> ⚠️ En cas de pèrdua del projecte, la qualificació final serà **0**.

---

## 📚 Avaluació

- Projecte realitzat **en parelles**
- Avaluació segons la **rúbrica publicada a Moodle**

---

## 📄 Llicència

Projecte desenvolupat exclusivament amb finalitats **educatives** per a l’INS Daniel Blanxart i Pedrals.
