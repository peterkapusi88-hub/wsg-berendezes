# Forrásblokkok szó szerinti kinyerése (csak olvas). Claude, 2026-10-24.
import re, hashlib, os
R = '/home/claude/wsg-berendezes/'
def olvas(p): return open(R + p, encoding='utf-8').read()
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
def fsha(p): return hashlib.sha256(open(R + p, 'rb').read()).hexdigest()
SABLON = '05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md'
ASTRA = '05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md'
CAM10 = '05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md'
GARD = '05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md'
KONC = '06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md'
def idezet(blokk):  # markdown idézet → szöveg: csak a sor eleji '> ' / '>' jelölő marad le
    out = []
    for l in blokk.strip('\n').split('\n'):
        assert l.startswith('>'), l
        out.append(l[2:] if l.startswith('> ') else l[1:])
    return '\n'.join(out)
def kozos_fixed():
    s = olvas(SABLON); a = s.index('## 1. KÖZÖS FIXED BLOKK'); b = s.index('## 2. HELYISÉG-SPECIFIKUS')
    t = s[a:b].split('\n', 1)[1]; q = '\n'.join(l for l in t.split('\n') if l.startswith('>'))
    return idezet(q)
def helyiseg_fixed(kulcs):  # 'Cam_02 · nappali–terasz' stb.
    s = olvas(SABLON); a = s.index('## 2. HELYISÉG-SPECIFIKUS'); b = s.index('## 3. KALIBRÁCIÓS PÁR')
    t = s[a:b]; i = t.index('**' + kulcs); j = t.index('\n>', i); k = t.index('\n', j + 1)
    return idezet(t[j + 1:k])
def cam10_csere():
    s = olvas(CAM10); a = s.index('## Csereblokk (angol, szó szerint)'); b = s.index('## WC 08')
    t = s[a:b].split('\n', 1)[1]; q = '\n'.join(l for l in t.split('\n') if l.startswith('>'))
    return idezet(q)
def kalibracio(c):  # 'C1' / 'C2'
    s = olvas(SABLON); a = s.index('## 3. KALIBRÁCIÓS PÁR'); b = s.index('## 4. STÍLUSBLOKK-SÉMA')
    t = s[a:b]; i = t.index('**' + c + ' – '); k = t.index('\n', i)
    return t[i:k]
def astra(stilus_cim):  # pl. 'S01 — Kyoto Ink · nappali–terasz (Cam_02)'
    s = olvas(ASTRA); fej = '### ' + stilus_cim; a = s.index(fej); b = s.index('\n---\n', a)
    return s[a:b].strip('\n')
def gardrob_blokk():
    s = olvas(GARD); a = s.index('## Kiegészítő blokk (angol, szó szerint)'); b = s.index('## Stílusonkénti front')
    t = s[a:b].split('\n', 1)[1]; q = '\n'.join(l for l in t.split('\n') if l.startswith('>'))
    return idezet(q)
def gardrob_front(sxx):
    s = olvas(GARD); m = re.search(r'\| ' + sxx + r' [^|]*\| `([^`]*)`', s); return m.group(1)
def koncepcio_cella(verzio, helyiseg):  # verzio 'Zenit'/'Lake Forest', helyiseg 'Nappali'/'Master háló' → A-902 oszlop
    s = olvas(KONC); a = s.index('## ' + verzio + '-verzió lakásonként'); b = s.index('\n## ', a + 5)
    for l in s[a:b].split('\n'):
        if l.startswith('| ' + helyiseg + ' |'):
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            return cells[3]
    raise KeyError(helyiseg)
if __name__ == '__main__':
    print(kozos_fixed()[:200]); print('...'); print(helyiseg_fixed('Cam_04 · master háló 05.1')[:160])
    print(cam10_csere()[:160]); print(kalibracio('C1')[:120]); print(astra('S01 — Kyoto Ink · master (Cam_04)')[:120])
    print(gardrob_blokk()[:120]); print(gardrob_front('S02')[:80]); print(koncepcio_cella('Zenit', 'Master háló'))
    print(koncepcio_cella('Lake Forest', 'Nappali'))
HUE = '05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md'
def hue_blokk():
    s = olvas(HUE); a = s.index('## Kiegészítő blokk (angol, szó szerint)')
    t = s[a:].split('\n', 1)[1]; q = '\n'.join(l for l in t.split('\n') if l.startswith('>'))
    return idezet(q)
# Cam_11 csereblokk – a draft PR #15 ágáról (kep004/cam11-master-panorama-javaslat), git show-val, változatlanul
import subprocess
PR15 = 'kep004/cam11-master-panorama-javaslat'
CAM11 = '05_promptok/A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md'
def pr15_fajl(p):
    return subprocess.check_output(['git', '-C', R, 'show', PR15 + ':' + p]).decode('utf-8')
def cam11_csere():
    s = pr15_fajl(CAM11); a = s.index('## Csereblokk (angol, szó szerint)')
    t = s[a:].split('\n', 1)[1]; q = '\n'.join(l for l in t.split('\n') if l.startswith('>'))
    return idezet(q)
