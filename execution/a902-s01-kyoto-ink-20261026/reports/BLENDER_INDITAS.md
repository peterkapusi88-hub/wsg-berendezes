# Blender-indítási hiba és tényleges próba

A felhasználó crash riportja EXC_CRASH/SIGSEGV-t mutatott. A verem releváns pontjai: supports_barycentric_whitelist, MTLBackend::metal_is_supported, GPU_backend_type_selection_detect. Ez nem egyszerű „fájlhozzáférés megtagadva” üzenet, hanem GPU/Metal felismerés közbeni összeomlás.

A korlátozott futtatás hibázott; az engedélyezett külön háttérfolyamat sikeresen megnyitotta a967objektumos eredeti forrást. Az R02 munkamásolatot elmentettük és újra megnyitottuk,28semleges kontrollkép készült. Bizonyíték: run_R02.log, reopen_R02.log, reopen_check_R02.json. A próba alapján a futtatási környezet korlátozása szerepet játszott; ez nem bizonyít általános macOS jogosultsághibát. Nem módosítottunk globális biztonsági beállítást, és nem adtunk indokolatlan teljes lemezhozzáférést.
