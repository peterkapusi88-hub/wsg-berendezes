# Munkafájlok – FABLE51 V3.1 ChatGPT Images kör (2026-10-25)

- **`szkriptek/`**
  - `build_msgs.py`: a 22 küldött üzenet összeállítása (fejléc + szó szerinti Fable-prompt).
  - `build_cam12_msgs.py`: a Cam_12 v3 KORR üzenetek összeállítása.
  - `compare.py`: kapukép (alapkép | render | áttűnés | élkép); a KORR=1 kapcsolóval az új Cam_12 alapképhez hasonlít.
  - `build_manifest.py`: a manifest összeállítása.
  - A szkriptek konténerútvonalakra hivatkoznak (`/home/claude/...`), ezért újrafuttatás előtt igazítani kell őket.
- **`kepernyomentes/`**: két képernyőmentés (05, 07), amíg a Chrome a letöltést blokkolta. Az eredeti PNG-k később letöltődtek, ezek a fő mappában vannak.
- **Chrome-feltöltési módszer:** a ChatGPT oldalán egy saját, rejtett fájlmezőbe kerültek a referenciák és a szöveg, ezeket a beszúrás `paste`-tel tette be a szerkesztőbe. A 12 000 karakter fölötti szövegnél `insertText` kellett, különben a ChatGPT csatolmánnyá alakítja. Küldés előtt a szerkesztő tartalmát mindig a fájlhoz hasonlítottam.
- **Letöltés:** a böngésző `~/Downloads` mappájába ment, onnan méret alapján került át a `WSG_FABLE51_V3_1_RENDEREK/` mappába. A Mac-oldali segéd: `~/claim.sh` (a munkamenet saját könyvtárában).
