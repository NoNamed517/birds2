Níže máš strukturovaný plán (vhodný rovnou do `.md` souboru), který můžeš uložit např. jako `BIRD_DATASET_MANAGEMENT_PLAN.md` a commitnout jako první krok.

---

# 🐦 Ptačí management – implementační plán

## 🎯 Cíl

Rozšířit existující aplikaci „Ptačí dashboard“ o správu datasetu (CRUD operace) s omezením přístupu pouze pro přihlášené uživatele.

---

# 🧩 FÁZE 1 – Autentizace uživatele

## Funkcionalita

* Přihlášení uživatele
* Odhlášení uživatele
* Ochrana rout (přístup pouze pro přihlášené)

## Workflow

1. Uživatel otevře aplikaci
2. Pokud není přihlášen:

   * je přesměrován na login stránku
3. Zadá přihlašovací údaje
4. Po úspěšném přihlášení:

   * je přesměrován na dashboard

## UI

* Stránka `/login`

  * input: email
  * input: heslo
  * tlačítko „Přihlásit“
* Navbar:

  * zobrazení „Odhlásit“ pokud je uživatel přihlášen

## Technicky

* session / JWT
* middleware pro ochranu rout

## Commit

`feat: implement user authentication and route protection`

---

# 🧩 FÁZE 2 – Zobrazení datasetu (Read)

## Funkcionalita

* Výpis všech ptačích záznamů z databáze

## Workflow

1. Přihlášený uživatel otevře dashboard
2. Aplikace načte data z DB
3. Zobrazí seznam ptáků

## UI

* Tabulka / seznam:

  * Název druhu
  * Lokalita
  * Datum pozorování
  * Poznámka
* U každého záznamu:

  * tlačítko „Upravit“
  * tlačítko „Smazat“

## Commit

`feat: display bird dataset in dashboard`

---

# 🧩 FÁZE 3 – Přidání záznamu (Create)

## Funkcionalita

* Uživatel může přidat nový záznam

## Workflow

1. Uživatel klikne na „Přidat záznam“
2. Otevře se formulář
3. Vyplní údaje
4. Odešle formulář
5. Data se uloží do DB
6. Uživatel je přesměrován zpět na seznam

## UI

* Tlačítko „+ Přidat záznam“
* Formulář:

  * název druhu (text)
  * lokalita (text)
  * datum (date picker)
  * poznámka (textarea)
  * tlačítko „Uložit“

## Validace

* Povinné: název, datum

## Commit

`feat: add create bird record functionality`

---

# 🧩 FÁZE 4 – Úprava záznamu (Update)

## Funkcionalita

* Editace existujícího záznamu

## Workflow

1. Uživatel klikne na „Upravit“
2. Formulář se předvyplní daty
3. Uživatel upraví hodnoty
4. Odešle formulář
5. Data se aktualizují v DB

## UI

* Stejný formulář jako při vytvoření
* Tlačítko „Uložit změny“

## Commit

`feat: implement update bird record`

---

# 🧩 FÁZE 5 – Mazání záznamu (Delete)

## Funkcionalita

* Smazání záznamu z databáze

## Workflow

1. Uživatel klikne na „Smazat“
2. Zobrazí se potvrzovací dialog
3. Po potvrzení:

   * záznam je odstraněn
   * seznam se aktualizuje

## UI

* Tlačítko „Smazat“
* Modal:

  * „Opravdu chcete smazat tento záznam?“
  * ANO / NE

## Commit

`feat: implement delete bird record with confirmation`

---

# 🧩 FÁZE 6 – Ochrana přístupu

## Funkcionalita

* CRUD operace dostupné pouze pro přihlášené

## Workflow

* Nepřihlášený uživatel:

  * nemá přístup k:

    * dashboardu
    * CRUD akcím
  * je přesměrován na login

## Technicky

* middleware / guard
* kontrola tokenu/session

## Commit

`feat: secure CRUD operations for authenticated users only`

---

# 🧩 FÁZE 7 – UX vylepšení

## Funkcionalita

* Lepší uživatelský zážitek

## Možnosti

* Notifikace (toast):

  * „Záznam byl uložen“
  * „Záznam byl smazán“
* Loading indikátor
* Error handling

## Commit

`feat: improve UX with notifications and loading states`

---

# 🧩 FÁZE 8 – Refaktor a validace

## Funkcionalita

* Čistý kód a stabilita

## Co zahrnout

* Validace formulářů
* Oddělení logiky (services)
* Reusable komponenty

## Commit

`refactor: improve structure and validation`

---

# 📦 Doporučená struktura commitů

Každá fáze:

* samostatný commit
* případně více menších commitů uvnitř fáze

---

# 🚀 Shrnutí workflow aplikace

1. Uživatel se přihlásí
2. Zobrazí se dashboard
3. Může:

   * zobrazit záznamy
   * přidat nový
   * upravit existující
   * smazat záznam
4. Nepřihlášený uživatel nemá přístup

---

Pokud chceš, můžu ti rovnou připravit i konkrétní:

* návrh API (endpointy)
* databázový model
* nebo ukázkovou implementaci (např. React + Node / Laravel / Django)
