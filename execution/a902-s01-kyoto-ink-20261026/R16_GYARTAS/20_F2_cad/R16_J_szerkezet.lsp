;;; S16 R15 médiafal – 3D szerkezeti modell (generálva: 2026-10-30, f2_cad_export.py)
;;; STÁTUSZ: TERVI MODELL – nem gyártási kiadás. Forrás: parts_v1.json (R16-J-GY-v1).
;;; ActiveX (vla-*) nélkül: csak parancs + entmake – AutoCAD for Mac-en is fut.
;;; Használat: APPLOAD → ezt a fájlt → parancssor: (s16-build)   majd ellenőrzés: (s16-readback "<mappa>")
;;; Egység: mm. KOORDINÁTA: Y_CAD = -Y_helyi (egyetlen tükrözés). Az R14 helyi rendszer (X jobbra a szobából, Y faltól a szoba
;;; felé, Z fel) balkezes; jobbkezes AutoCAD-ben e nélkül a bútor tükörképe épülne. Így a fal síkja Y=0, a front -Y felé néz,
;;; az AutoCAD FRONT nézet = szobából nézett homlokzat (torony bal oldalt).

(defun s16-env ()
  (setvar "CMDECHO" 0) (setvar "OSMODE" 0) (setvar "INSUNITS" 4) (setvar "DELOBJ" 1)
  (command "_.UCS" "_W"))

(defun s16-layer (name col)
  (if (not (tblsearch "LAYER" name))
    (if (= (type col) 'STR) (command "_.-LAYER" "_M" name "_C" "_T" col "" "") (command "_.-LAYER" "_M" name "_C" (itoa col) "" ""))
    (command "_.-LAYER" "_S" name ""))
  (setvar "CLAYER" name))

(defun s16-box (x y z dx dy dz)
  (command "_.BOX" (list x y z) (list (+ x dx) (+ y dy) (+ z dz)))
  (entlast))

;; zárt LWPOLYLINE a WCS XY síkban; pts = ((u v bulge) ...)
(defun s16-lwpoly (pts / d)
  (setq d (list '(0 . "LWPOLYLINE") '(100 . "AcDbEntity") '(100 . "AcDbPolyline") (cons 90 (length pts)) '(70 . 1)))
  (foreach p pts (setq d (append d (list (list 10 (car p) (cadr p)) (cons 42 (caddr p))))))
  (entmake d)
  (entlast))

;; profil (U=X, V=Z) kihúzása T-vel, X körüli +90°-os forgatás: (u v n) -> (u -n v), majd tolás (x0 y0 z0)
(defun s16-extrude-y (pts tt x0 y0 z0 / pl s)
  ;; y0 itt már CAD-koordináta (= -Y_helyi), a test y0-tt .. y0 között lesz
  (setq pl (s16-lwpoly pts))
  (command "_.EXTRUDE" pl "" tt)
  (setq s (entlast))
  (command "_.ROTATE3D" s "" "_X" '(0 0 0) 90)
  (command "_.MOVE" s "" '(0 0 0) (list x0 y0 z0))
  s)

(defun s16-sub (a b) (command "_.SUBTRACT" a "" b "") a)

;; henger két pont között (tengely), r sugár – furatokhoz, tiplikhez
(defun s16-cyl (x y z r x2 y2 z2) (command "_.CYLINDER" (list x y z) r "_A" (list x2 y2 z2)) (entlast))

;; blokk a megadott (a 0 rétegen, WCS-origóban épített) testekből; ha már létezik, a testeket törli
(defun s16-blk (name ents / ss)
  (setq ss (ssadd))
  (foreach e ents (if e (ssadd e ss)))
  (if (tblsearch "BLOCK" name) (command "_.ERASE" ss "") (command "_.-BLOCK" name '(0 0 0) ss ""))
  name)

;; blokkhivatkozás tetszőleges térbeli irányba: a blokk +Z tengelye = dir (WCS), a pont WCS-ben
(defun s16-ins (name lay pt dir rot xs)
  (entmake (list (cons 0 "INSERT") (cons 2 name) (cons 8 lay) (cons 10 (trans pt 0 dir))
                 (cons 41 xs) (cons 42 1.0) (cons 43 1.0) (cons 50 rot) (cons 210 dir))))

(defun s16-count-ins (name / ss) (setq ss (ssget "_X" (list (cons 0 "INSERT") (cons 2 name)))) (if ss (sslength ss) 0))

(defun s16-count (pre / ss i n e)
  (setq ss (ssget "_X" '((0 . "3DSOLID"))) i 0 n 0)
  (if ss (while (< i (sslength ss)) (setq e (ssname ss i)) (if (wcmatch (cdr (assoc 8 (entget e))) (strcat pre "*")) (setq n (1+ n))) (setq i (1+ i))))
  n)

(defun s16-copy (e / last) (setq last (entlast)) (command "_.COPY" e "" '(0 0 0) '(0 0 0)) (entlast))

(defun s16-safe (s / r i c)
  ;; fájlnévhez: $ és # → _ (vl-string-* nélkül, Mac-kompatibilis)
  (setq r "" i 1)
  (while (<= i (strlen s))
    (setq c (substr s i 1))
    (setq r (strcat r (if (member c '("$" "#")) "_" c)) i (1+ i)))
  r)

(defun s16-readback (dir / ss i e lay n)
  ;; minden $PART_ 3D test MASSPROP-ja külön fájlba: <dir>/<réteg>.mpr (AutoCAD tömegjellemző-szöveg, NEM woodWOP MPR)
  (setvar "FILEDIA" 0)
  (setq ss (ssget "_X" '((0 . "3DSOLID"))) i 0 n 0)
  (if ss
    (while (< i (sslength ss))
      (setq e (ssname ss i) lay (cdr (assoc 8 (entget e))))
      (if (= (substr lay 1 6) "$PART_")
        (progn (command "_.MASSPROP" e "" "_Y" (strcat dir "/" (s16-safe lay))) (setq n (1+ n))))
      (setq i (1+ i))))
  (setvar "FILEDIA" 1)
  (princ (strcat "\nS16 readback: " (itoa n) " test kiirva ide: " dir))
  (princ))

(defun s16-smoketest ( / a b c)
  ;; parancs-próba a teljes build előtt: hasáb, íves (bulge) kihúzás, kivonás – várt értékek a 30_eredmenyek-ben
  (s16-env)
  (s16-layer "$PART_SMOKE_BOX#0000" 3)
  (setq a (s16-box 0 -300 0 400 18 600))
  (s16-layer "$PART_SMOKE_ARC#0000" 4)
  (setq c (s16-extrude-y (list (list 0 0 0) (list 100 0 0.414213562) (list 200 100 0) (list 200 200 0) (list 0 200 0)) 18 600 -18 0))
  (s16-layer "$PART_SMOKE_SUB#0000" 5)
  (setq a (s16-box 1000 -300 0 400 18 600))
  (setq b (s16-box 1100 -310 100 200 38 400))
  (s16-sub a b)
  (command "_.ZOOM" "_E")
  (princ "\nS16 smoketest kesz: 3 test. Futtasd: (s16-readback \"<mappa>\")")
  (princ))

(defun s16-build ( / a b)
  (s16-env)
  ;; KI12-TV01S-01
  (s16-layer "$PART_R16_KI12-TV01S-01\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816001" "80,73,66")
  (setq a (s16-box 0 -418.0 550 18 382 2330))
  ;; KI12-TV01S-02
  (s16-layer "$PART_R16_KI12-TV01S-02\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816002" "80,73,66")
  (setq a (s16-box 702 -418.0 550 18 382 2330))
  ;; KI12-TV01T-01
  (s16-layer "$PART_R16_KI12-TV01T-01\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816003" "80,73,66")
  (setq a (s16-box 18 -418.0 550 684 382 18))
  ;; KI12-TV01T-02
  (s16-layer "$PART_R16_KI12-TV01T-02\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816004" "80,73,66")
  (setq a (s16-box 18 -418.0 2862 684 382 18))
  ;; KI12-TV01C-01
  (s16-layer "$PART_R16_KI12-TV01C-01\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816005" "80,73,66")
  (setq a (s16-box 351 -418.0 568 18 354 2294))
  ;; KI12-TV01P-01
  (s16-layer "$PART_R16_KI12-TV01P-01\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816006" "80,73,66")
  (setq a (s16-box 19 -398.0 935 331 290 18))
  ;; KI12-TV01P-02
  (s16-layer "$PART_R16_KI12-TV01P-02\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816007" "80,73,66")
  (setq a (s16-box 19 -398.0 1320 331 290 18))
  ;; KI12-TV01P-03
  (s16-layer "$PART_R16_KI12-TV01P-03\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816008" "80,73,66")
  (setq a (s16-box 19 -398.0 1705 331 290 18))
  ;; KI12-TV01P-04
  (s16-layer "$PART_R16_KI12-TV01P-04\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816009" "80,73,66")
  (setq a (s16-box 19 -398.0 2090 331 290 18))
  ;; KI12-TV01P-05
  (s16-layer "$PART_R16_KI12-TV01P-05\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816010" "80,73,66")
  (setq a (s16-box 19 -398.0 2475 331 290 18))
  ;; KI12-TV01P-06
  (s16-layer "$PART_R16_KI12-TV01P-06\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816011" "80,73,66")
  (setq a (s16-box 370 -398.0 935 331 290 18))
  ;; KI12-TV01P-07
  (s16-layer "$PART_R16_KI12-TV01P-07\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816012" "80,73,66")
  (setq a (s16-box 370 -398.0 1320 331 290 18))
  ;; KI12-TV01P-08
  (s16-layer "$PART_R16_KI12-TV01P-08\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816013" "80,73,66")
  (setq a (s16-box 370 -398.0 1705 331 290 18))
  ;; KI12-TV01P-09
  (s16-layer "$PART_R16_KI12-TV01P-09\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816014" "80,73,66")
  (setq a (s16-box 370 -398.0 2090 331 290 18))
  ;; KI12-TV01P-10
  (s16-layer "$PART_R16_KI12-TV01P-10\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816015" "80,73,66")
  (setq a (s16-box 370 -398.0 2475 331 290 18))
  ;; KI12-TV01F-01
  (s16-layer "$PART_R16_KI12-TV01F-01\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816016" "94,82,71")
  (setq a (s16-box 1.5 -439.0 551.5 357 18 2327))
  ;; KI12-TV01F-02
  (s16-layer "$PART_R16_KI12-TV01F-02\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816017" "94,82,71")
  (setq a (s16-box 361.5 -439.0 551.5 357 18 2327))
  ;; KI12-TV01H-01
  (s16-layer "$PART_R16_KI12-TV01H-01\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816018" "80,73,66")
  (setq s16p nil)
  (setq s16p (append s16p (list (list 682.0000 0.0000 0.000000000) (list 682.0000 2166.0000 0.000000000) (list 660.0000 2166.0000 0.000000000) (list 660.0000 2292.0000 0.000000000) (list 22.0000 2292.0000 0.000000000) (list 22.0000 2166.0000 0.000000000) (list 0.0000 2166.0000 0.000000000) (list 0.0000 0.0000 0.000000000))))
  (setq a (s16-extrude-y s16p 8 19 -56.0 569))
  ;; KI12-TV02CAP-01
  (s16-layer "$PART_R16_KI12-TV02CAP-01\U+02D90\U+02D90\U+00A8F0FF\U+02D90\U+00A8#0\U+00A816019" "94,82,71")
  (setq a (s16-box 0 -418.0 532 3600 382 18))
  ;; KI12-TV03P-01
  (s16-layer "$PART_R16_KI12-TV03P-01\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816020" "122,109,94")
  (setq a (s16-box 921.5 -36.0 550 667 18 2330))
  ;; KI12-TV03P-02
  (s16-layer "$PART_R16_KI12-TV03P-02\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816021" "122,109,94")
  (setq a (s16-box 1591.5 -36.0 550 667 18 2330))
  ;; KI12-TV03P-03
  (s16-layer "$PART_R16_KI12-TV03P-03\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816022" "122,109,94")
  (setq a (s16-box 2261.5 -36.0 550 667 18 2330))
  ;; KI12-TV03P-04
  (s16-layer "$PART_R16_KI12-TV03P-04\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816023" "122,109,94")
  (setq a (s16-box 2931.5 -36.0 550 667 18 2330))
  ;; KI12-GAP-01
  (s16-layer "$PART_R16_KI12-GAP-01\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816024" "94,82,71")
  (setq a (s16-box 720 -36.0 550 200 18 2330))
  ;; KI14-BAT-01
  (s16-layer "$PART_R16_KI14-BAT-01\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816025" "207,174,132")
  (setq a (s16-box 18 -82.0 588 18 18 2142))
  ;; KI14-BAT-02
  (s16-layer "$PART_R16_KI14-BAT-02\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816026" "207,174,132")
  (setq a (s16-box 684 -82.0 588 18 18 2142))
  ;; KI14-RAIL-06
  (s16-layer "$PART_R16_KI14-RAIL-06\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816027" "196,175,139")
  (setq a (s16-box 18 -100.0 2632 333 18 100))
  ;; KI14-RAIL-07
  (s16-layer "$PART_R16_KI14-RAIL-07\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816028" "196,175,139")
  (setq a (s16-box 369 -100.0 2632 333 18 100))
  ;; KI12-TV02S-01
  (s16-layer "$PART_R16_KI12-TV02S-01\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816029" "80,73,66")
  (setq a (s16-box 0 -418.0 150 18 382 382))
  ;; KI12-TV02S-02
  (s16-layer "$PART_R16_KI12-TV02S-02\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816030" "80,73,66")
  (setq a (s16-box 702 -418.0 150 18 382 382))
  ;; KI12-TV02T1-01
  (s16-layer "$PART_R16_KI12-TV02T1-01\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816031" "80,73,66")
  (setq a (s16-box 18 -418.0 150 684 382 18))
  ;; KI12-TV02F1-01
  (s16-layer "$PART_R16_KI12-TV02F1-01\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816032" "94,82,71")
  (setq a (s16-box 1.5 -439.0 151.5 717 18 397))
  ;; KI12-TV02H1-01
  (s16-layer "$PART_R16_KI12-TV02H1-01\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816033" "80,73,66")
  (setq s16p nil)
  (setq s16p (append s16p (list (list 682.0000 0.0000 0.000000000) (list 682.0000 236.0000 0.000000000) (list 660.0000 236.0000 0.000000000) (list 660.0000 362.0000 0.000000000) (list 22.0000 362.0000 0.000000000) (list 22.0000 236.0000 0.000000000) (list 0.0000 236.0000 0.000000000) (list 0.0000 0.0000 0.000000000))))
  (setq a (s16-extrude-y s16p 8 19 -56.0 169))
  ;; KI14-BAT-03
  (s16-layer "$PART_R16_KI14-BAT-03\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816034" "207,174,132")
  (setq a (s16-box 18 -82.0 188 18 18 212))
  ;; KI14-BAT-04
  (s16-layer "$PART_R16_KI14-BAT-04\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816035" "207,174,132")
  (setq a (s16-box 684 -82.0 188 18 18 212))
  ;; KI14-RAIL-01
  (s16-layer "$PART_R16_KI14-RAIL-01\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816036" "196,175,139")
  (setq a (s16-box 18 -100.0 300 684 18 100))
  ;; KI16-D1-L
  (s16-layer "$PART_R16_KI16-D1-L\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816037" "196,175,139")
  (setq a (s16-box 24 -418.0 197 15 290 250))
  ;; KI16-D1-R
  (s16-layer "$PART_R16_KI16-D1-R\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816038" "196,175,139")
  (setq a (s16-box 681 -418.0 197 15 290 250))
  ;; KI16-D1-B
  (s16-layer "$PART_R16_KI16-D1-B\U+02D90\U+02D90\U+00A8LL00\U+02D90\U+00A8#0\U+00A816039" "196,175,139")
  (setq a (s16-box 39 -418.0 210 642 290 15))
  ;; KI16-D1-F
  (s16-layer "$PART_R16_KI16-D1-F\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816040" "196,175,139")
  (setq a (s16-box 39 -418.0 225 642 15 222))
  ;; KI16-D1-H
  (s16-layer "$PART_R16_KI16-D1-H\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816041" "196,175,139")
  (setq a (s16-box 39 -143.0 225 642 15 222))
  ;; KI12-TV02S-03
  (s16-layer "$PART_R16_KI12-TV02S-03\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816042" "80,73,66")
  (setq a (s16-box 720 -418.0 150 18 382 382))
  ;; KI12-TV02S-04
  (s16-layer "$PART_R16_KI12-TV02S-04\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816043" "80,73,66")
  (setq a (s16-box 1152 -418.0 150 18 382 382))
  ;; KI12-TV02T2-01
  (s16-layer "$PART_R16_KI12-TV02T2-01\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816044" "80,73,66")
  (setq a (s16-box 738 -418.0 150 414 382 18))
  ;; KI12-TV02F2-01
  (s16-layer "$PART_R16_KI12-TV02F2-01\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816045" "94,82,71")
  (setq a (s16-box 721.5 -439.0 151.5 447 18 397))
  ;; KI12-TV02H2-01
  (s16-layer "$PART_R16_KI12-TV02H2-01\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816046" "80,73,66")
  (setq s16p nil)
  (setq s16p (append s16p (list (list 412.0000 0.0000 0.000000000) (list 412.0000 236.0000 0.000000000) (list 390.0000 236.0000 0.000000000) (list 390.0000 362.0000 0.000000000) (list 22.0000 362.0000 0.000000000) (list 22.0000 236.0000 0.000000000) (list 0.0000 236.0000 0.000000000) (list 0.0000 0.0000 0.000000000))))
  (setq a (s16-extrude-y s16p 8 739 -56.0 169))
  ;; KI14-BAT-05
  (s16-layer "$PART_R16_KI14-BAT-05\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816047" "207,174,132")
  (setq a (s16-box 738 -82.0 188 18 18 212))
  ;; KI14-BAT-06
  (s16-layer "$PART_R16_KI14-BAT-06\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816048" "207,174,132")
  (setq a (s16-box 1134 -82.0 188 18 18 212))
  ;; KI14-RAIL-02
  (s16-layer "$PART_R16_KI14-RAIL-02\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816049" "196,175,139")
  (setq a (s16-box 738 -100.0 300 414 18 100))
  ;; KI16-D2-L
  (s16-layer "$PART_R16_KI16-D2-L\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816050" "196,175,139")
  (setq a (s16-box 744 -418.0 197 15 290 250))
  ;; KI16-D2-R
  (s16-layer "$PART_R16_KI16-D2-R\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816051" "196,175,139")
  (setq a (s16-box 1131 -418.0 197 15 290 250))
  ;; KI16-D2-B
  (s16-layer "$PART_R16_KI16-D2-B\U+02D90\U+02D90\U+00A8LL00\U+02D90\U+00A8#0\U+00A816052" "196,175,139")
  (setq a (s16-box 759 -418.0 210 372 290 15))
  ;; KI16-D2-F
  (s16-layer "$PART_R16_KI16-D2-F\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816053" "196,175,139")
  (setq a (s16-box 759 -418.0 225 372 15 222))
  ;; KI16-D2-H
  (s16-layer "$PART_R16_KI16-D2-H\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816054" "196,175,139")
  (setq a (s16-box 759 -143.0 225 372 15 222))
  ;; KI12-TV02S-05
  (s16-layer "$PART_R16_KI12-TV02S-05\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816055" "80,73,66")
  (setq a (s16-box 1170 -418.0 150 18 382 382))
  ;; KI12-TV02S-06
  (s16-layer "$PART_R16_KI12-TV02S-06\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816056" "80,73,66")
  (setq a (s16-box 1602 -418.0 150 18 382 382))
  ;; KI12-TV02T2-02
  (s16-layer "$PART_R16_KI12-TV02T2-02\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816057" "80,73,66")
  (setq a (s16-box 1188 -418.0 150 414 382 18))
  ;; KI12-TV02F2-02
  (s16-layer "$PART_R16_KI12-TV02F2-02\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816058" "94,82,71")
  (setq a (s16-box 1171.5 -439.0 151.5 447 18 397))
  ;; KI12-TV02H2-02
  (s16-layer "$PART_R16_KI12-TV02H2-02\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816059" "80,73,66")
  (setq s16p nil)
  (setq s16p (append s16p (list (list 412.0000 0.0000 0.000000000) (list 412.0000 236.0000 0.000000000) (list 390.0000 236.0000 0.000000000) (list 390.0000 362.0000 0.000000000) (list 22.0000 362.0000 0.000000000) (list 22.0000 236.0000 0.000000000) (list 0.0000 236.0000 0.000000000) (list 0.0000 0.0000 0.000000000))))
  (setq a (s16-extrude-y s16p 8 1189 -56.0 169))
  ;; KI14-BAT-07
  (s16-layer "$PART_R16_KI14-BAT-07\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816060" "207,174,132")
  (setq a (s16-box 1188 -82.0 188 18 18 212))
  ;; KI14-BAT-08
  (s16-layer "$PART_R16_KI14-BAT-08\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816061" "207,174,132")
  (setq a (s16-box 1584 -82.0 188 18 18 212))
  ;; KI14-RAIL-03
  (s16-layer "$PART_R16_KI14-RAIL-03\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816062" "196,175,139")
  (setq a (s16-box 1188 -100.0 300 414 18 100))
  ;; KI16-D3-L
  (s16-layer "$PART_R16_KI16-D3-L\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816063" "196,175,139")
  (setq a (s16-box 1194 -418.0 197 15 290 250))
  ;; KI16-D3-R
  (s16-layer "$PART_R16_KI16-D3-R\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816064" "196,175,139")
  (setq a (s16-box 1581 -418.0 197 15 290 250))
  ;; KI16-D3-B
  (s16-layer "$PART_R16_KI16-D3-B\U+02D90\U+02D90\U+00A8LL00\U+02D90\U+00A8#0\U+00A816065" "196,175,139")
  (setq a (s16-box 1209 -418.0 210 372 290 15))
  ;; KI16-D3-F
  (s16-layer "$PART_R16_KI16-D3-F\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816066" "196,175,139")
  (setq a (s16-box 1209 -418.0 225 372 15 222))
  ;; KI16-D3-H
  (s16-layer "$PART_R16_KI16-D3-H\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816067" "196,175,139")
  (setq a (s16-box 1209 -143.0 225 372 15 222))
  ;; KI12-TV02S-07
  (s16-layer "$PART_R16_KI12-TV02S-07\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816068" "80,73,66")
  (setq a (s16-box 1620 -418.0 150 18 382 382))
  ;; KI12-TV02S-08
  (s16-layer "$PART_R16_KI12-TV02S-08\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816069" "80,73,66")
  (setq a (s16-box 2682 -418.0 150 18 382 382))
  ;; KI12-TV02T2-03
  (s16-layer "$PART_R16_KI12-TV02T2-03\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816070" "80,73,66")
  (setq a (s16-box 1638 -418.0 150 1044 382 18))
  ;; KI12-TV02F2-03
  (s16-layer "$PART_R16_KI12-TV02F2-03\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816071" "94,82,71")
  (setq a (s16-box 1621.5 -439.0 151.5 1077 18 397))
  ;; KI12-TV02H2-03
  (s16-layer "$PART_R16_KI12-TV02H2-03\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816072" "80,73,66")
  (setq s16p nil)
  (setq s16p (append s16p (list (list 1042.0000 0.0000 0.000000000) (list 1042.0000 236.0000 0.000000000) (list 1020.0000 236.0000 0.000000000) (list 1020.0000 362.0000 0.000000000) (list 22.0000 362.0000 0.000000000) (list 22.0000 236.0000 0.000000000) (list 0.0000 236.0000 0.000000000) (list 0.0000 0.0000 0.000000000))))
  (setq a (s16-extrude-y s16p 8 1639 -56.0 169))
  ;; KI14-BAT-09
  (s16-layer "$PART_R16_KI14-BAT-09\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816073" "207,174,132")
  (setq a (s16-box 1638 -82.0 188 18 18 212))
  ;; KI14-BAT-10
  (s16-layer "$PART_R16_KI14-BAT-10\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816074" "207,174,132")
  (setq a (s16-box 2664 -82.0 188 18 18 212))
  ;; KI14-RAIL-04
  (s16-layer "$PART_R16_KI14-RAIL-04\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816075" "196,175,139")
  (setq a (s16-box 1638 -100.0 300 1044 18 100))
  ;; KI16-D4-L
  (s16-layer "$PART_R16_KI16-D4-L\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816076" "196,175,139")
  (setq a (s16-box 1644 -418.0 197 15 290 250))
  ;; KI16-D4-R
  (s16-layer "$PART_R16_KI16-D4-R\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816077" "196,175,139")
  (setq a (s16-box 2661 -418.0 197 15 290 250))
  ;; KI16-D4-B
  (s16-layer "$PART_R16_KI16-D4-B\U+02D90\U+02D90\U+00A8LL00\U+02D90\U+00A8#0\U+00A816078" "196,175,139")
  (setq a (s16-box 1659 -418.0 210 1002 290 15))
  ;; KI16-D4-F
  (s16-layer "$PART_R16_KI16-D4-F\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816079" "196,175,139")
  (setq a (s16-box 1659 -418.0 225 1002 15 222))
  ;; KI16-D4-H
  (s16-layer "$PART_R16_KI16-D4-H\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816080" "196,175,139")
  (setq a (s16-box 1659 -143.0 225 1002 15 222))
  ;; KI12-TV02S-09
  (s16-layer "$PART_R16_KI12-TV02S-09\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816081" "80,73,66")
  (setq a (s16-box 2700 -418.0 150 18 382 382))
  ;; KI12-TV02S-10
  (s16-layer "$PART_R16_KI12-TV02S-10\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816082" "80,73,66")
  (setq a (s16-box 3132 -418.0 150 18 382 382))
  ;; KI12-TV02T2-04
  (s16-layer "$PART_R16_KI12-TV02T2-04\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816083" "80,73,66")
  (setq a (s16-box 2718 -418.0 150 414 382 18))
  ;; KI12-TV02F2-04
  (s16-layer "$PART_R16_KI12-TV02F2-04\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816084" "94,82,71")
  (setq a (s16-box 2701.5 -439.0 151.5 447 18 397))
  ;; KI12-TV02H2-04
  (s16-layer "$PART_R16_KI12-TV02H2-04\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816085" "80,73,66")
  (setq s16p nil)
  (setq s16p (append s16p (list (list 412.0000 0.0000 0.000000000) (list 412.0000 236.0000 0.000000000) (list 390.0000 236.0000 0.000000000) (list 390.0000 362.0000 0.000000000) (list 22.0000 362.0000 0.000000000) (list 22.0000 236.0000 0.000000000) (list 0.0000 236.0000 0.000000000) (list 0.0000 0.0000 0.000000000))))
  (setq a (s16-extrude-y s16p 8 2719 -56.0 169))
  ;; KI14-BAT-11
  (s16-layer "$PART_R16_KI14-BAT-11\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816086" "207,174,132")
  (setq a (s16-box 2718 -82.0 188 18 18 212))
  ;; KI14-BAT-12
  (s16-layer "$PART_R16_KI14-BAT-12\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816087" "207,174,132")
  (setq a (s16-box 3114 -82.0 188 18 18 212))
  ;; KI14-RAIL-05
  (s16-layer "$PART_R16_KI14-RAIL-05\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816088" "196,175,139")
  (setq a (s16-box 2718 -100.0 300 414 18 100))
  ;; KI16-D5-L
  (s16-layer "$PART_R16_KI16-D5-L\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816089" "196,175,139")
  (setq a (s16-box 2724 -418.0 197 15 290 250))
  ;; KI16-D5-R
  (s16-layer "$PART_R16_KI16-D5-R\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816090" "196,175,139")
  (setq a (s16-box 3111 -418.0 197 15 290 250))
  ;; KI16-D5-B
  (s16-layer "$PART_R16_KI16-D5-B\U+02D90\U+02D90\U+00A8LL00\U+02D90\U+00A8#0\U+00A816091" "196,175,139")
  (setq a (s16-box 2739 -418.0 210 372 290 15))
  ;; KI16-D5-F
  (s16-layer "$PART_R16_KI16-D5-F\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816092" "196,175,139")
  (setq a (s16-box 2739 -418.0 225 372 15 222))
  ;; KI16-D5-H
  (s16-layer "$PART_R16_KI16-D5-H\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816093" "196,175,139")
  (setq a (s16-box 2739 -143.0 225 372 15 222))
  ;; KI16-M6-TV02-S-01
  (s16-layer "$PART_R16_KI16-M6-TV02-S-01\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816094" "80,73,66")
  (setq a (s16-box 3150 -418.0 150 18 382 382))
  ;; KI16-M6-TV02-S-02
  (s16-layer "$PART_R16_KI16-M6-TV02-S-02\U+02D90\U+02D90\U+00A800V0\U+02D90\U+00A8#0\U+00A816095" "80,73,66")
  (setq a (s16-box 3582 -418.0 150 18 382 382))
  ;; KI16-M6-BOTTOM-03
  (s16-layer "$PART_R16_KI16-M6-BOTTOM-03\U+02D90\U+02D90\U+00A8V000\U+02D90\U+00A8#0\U+00A816096" "80,73,66")
  (setq a (s16-box 3168 -418.0 150 414 382 18))
  ;; KI16-M6-FRONT-04
  (s16-layer "$PART_R16_KI16-M6-FRONT-04\U+02D90\U+02D90\U+00A8FFFF\U+02D90\U+00A8#0\U+00A816097" "94,82,71")
  (setq a (s16-box 3151.5 -439.0 151.5 447 18 397))
  ;; KI16-M6-BACK-05
  (s16-layer "$PART_R16_KI16-M6-BACK-05\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816098" "80,73,66")
  (setq s16p nil)
  (setq s16p (append s16p (list (list 412.0000 0.0000 0.000000000) (list 412.0000 236.0000 0.000000000) (list 390.0000 236.0000 0.000000000) (list 390.0000 362.0000 0.000000000) (list 22.0000 362.0000 0.000000000) (list 22.0000 236.0000 0.000000000) (list 0.0000 236.0000 0.000000000) (list 0.0000 0.0000 0.000000000))))
  (setq a (s16-extrude-y s16p 8 3169 -56.0 169))
  ;; KI16-M6-BAT-06
  (s16-layer "$PART_R16_KI16-M6-BAT-06\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816099" "207,174,132")
  (setq a (s16-box 3168 -82.0 188 18 18 212))
  ;; KI16-M6-BAT-07
  (s16-layer "$PART_R16_KI16-M6-BAT-07\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816100" "207,174,132")
  (setq a (s16-box 3564 -82.0 188 18 18 212))
  ;; KI16-M6-RAIL-08
  (s16-layer "$PART_R16_KI16-M6-RAIL-08\U+02D90\U+02D90\U+00A80000\U+02D90\U+00A8#0\U+00A816101" "196,175,139")
  (setq a (s16-box 3168 -100.0 300 414 18 100))
  ;; KI16-D6-L
  (s16-layer "$PART_R16_KI16-D6-L\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816102" "196,175,139")
  (setq a (s16-box 3174 -418.0 197 15 290 250))
  ;; KI16-D6-R
  (s16-layer "$PART_R16_KI16-D6-R\U+02D90\U+02D90\U+00A8LLLL\U+02D90\U+00A8#0\U+00A816103" "196,175,139")
  (setq a (s16-box 3561 -418.0 197 15 290 250))
  ;; KI16-D6-B
  (s16-layer "$PART_R16_KI16-D6-B\U+02D90\U+02D90\U+00A8LL00\U+02D90\U+00A8#0\U+00A816104" "196,175,139")
  (setq a (s16-box 3189 -418.0 210 372 290 15))
  ;; KI16-D6-F
  (s16-layer "$PART_R16_KI16-D6-F\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816105" "196,175,139")
  (setq a (s16-box 3189 -418.0 225 372 15 222))
  ;; KI16-D6-H
  (s16-layer "$PART_R16_KI16-D6-H\U+02D90\U+02D90\U+00A8L000\U+02D90\U+00A8#0\U+00A816106" "196,175,139")
  (setq a (s16-box 3189 -143.0 225 372 15 222))
  (command "_.ZOOM" "_E")
  (princ "\nR16-J-GY-v1: 106 alkatrész felépítve.")
  (princ))
(princ "\nS16 betöltve: (s16-build) majd (s16-readback \"/Users/<te>/CAD/s16_readback\")")
(princ)
