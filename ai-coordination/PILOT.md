# Biztonságos egykörös pilot – Claude → GitHub → Work/Astra → Claude

## Mi már elkészült?
- A repo tartalmaz közös stíluslabort, projektadatokat, szereposztást és átadási sablonokat.
- A ChatGPT GitHub kapcsolat a repo olvasását korábbi beszélgetésben igazolta.
- A ChatGPT Work eseményvezérelt feladatot a felhasználónak **webes Workban kell létrehoznia**. A GitHub-dokumentumok ezt nem helyettesítik.
- **A pilot még nincs élesítve; nem indítunk feladatot pusztán ennek a fájlnak a létezésével.**

## Próba – csak amikor elérhető a Work-kredit
1. Péter beállítja a weben a Work PR-triggert a `WORK_TRIGGER_SETUP.md` szerint, és kiválasztja az elérhető kreatív modellt, ha a felület engedi.
2. Claude készít egy rövid, **max. egy helyiségre** vonatkozó ASTRA briefet, pl. **A-902 nappali / 2 különböző WOW-gesztus / csak előzetes árrealitás**, a `REQUEST_TEMPLATE.md` szerint; képeket előre a repo megfelelő mappájába tesz.
3. Claude draft PR-t hoz létre. Ellenőrzi, hogy az adott PR azonosítója, a hivatkozások, a költségplafon és a keretigény szerepelnek.
4. **Csak ezután, egyetlen alkalommal** váltja ready for review-ra a PR-t. Ez a valós GitHub-esemény lehet a Work triggerje.
5. Ellenőrizzük, indult-e Work-feladat, **valóban milyen modell**, hogy nem merült-e ki a limit, és történt-e sikeres GitHub-komment / eredményfájl-visszaadás.
6. Claude külön elolvassa az eredményt, majd ellenőrzi az ajánlat nélküli becsléseket. Az elvégzett munkát a PR-ben dokumentálja.
7. Ha az 4–6 pont nem sikeres, a rendszer státusza marad **RÉSZLEGES AUTOMATIZÁLÁS**. Nem állítunk rá másik modellt titokban, nem kapcsoljuk be a videó-/Codex-hívások automatikus indítását, és nem fizetünk extra kreditet.

## Mit NEM jelent a pilot?
- A PR-trigger önmagában nem automatizálja a Codex önálló geometriai tesztfuttatását vagy a Gemini image-to-video generálást.
- Az asztalos ajánlatkéréseket, megrendeléseket, fizetést nem automatizáljuk.
- Workből a GitHubra visszaírás, modellrögzítés és Claude önálló folytatása csak akkor tekinthető működőnek, ha az első tényleges kör visszaigazolja.

## Állapotjelölés
- `GH_INSTRUCTIONS_READY`: igen
- `WORK_EVENT_TRIGGER_CREATED`: **nem igazolt**
- `ASTRA_MODEL_SELECTED_FOR_TRIGGER`: **nem igazolt**
- `PILOT_PR_READY_EVENT_FIRED`: nem
- `WORK_RESULT_RETURNED_TO_GITHUB`: nem
- `CLAUDE_RESUMED_FROM_GITHUB_RESULT`: nem
- `CODEX_AUTOMATIC`: nem
- `GEMINI_AUTOMATIC`: nem
