# Engeto Text Analyzer
## Projekt pro Python Academy Engeto
### Popis projektu

Tvůj program bude obsahovat následující:
1. Vyžádá si od uživatele přihlašovací jméno a heslo.
2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
3. Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program.

Registrováni jsou následující uživatelé:

    | USER |   PASSWORD  |
    -----------------------
    | bob  |     123     |
    | ann  |    pass123  |
    | mike | password123 |
    | liz  |    pass123  |

4. Program nechá uživatel vybrat mezi třemi texty, uloženými v proměnné TEXTS. Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí. Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

5. Pro vybraný text spočítá následující statistiky:
- počet slov,
- počet slov začínajících velkým písmenem,
- počet slov psaných velkými písmeny,
- počet slov psaných malými písmeny,
- počet čísel (ne cifer),
- sumu všech čísel (ne cifer) v textu.

6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:


    7 * 1
     8 *********** 11
     9 *************** 15
    10 ********* 9
    11 ********** 10

Po spuštění by program měl vypadat zhruba nějak takto:


    username:bob
    password:123
    ----------------------------------------
    Welcome to the app, bob
    We have 3 texts to be analyzed.
    ----------------------------------------
    Enter a number btw. 1 and 3 to select: 1
    ----------------------------------------
    There are 54 words in the selected text.
    There are 12 titlecase words.
    There are 1 uppercase words.
    There are 38 lowercase words.
    There are 3 numeric strings.
    The sum of all the numbers 8510
    ----------------------------------------
    LEN|  OCCURENCES  |NR.
    ----------------------------------------
      1|*             |1
      2|*********     |9
      3|******        |6
      4|***********   |11
      5|************  |12
      6|***           |3
      7|****          |4
      8|*****         |5
      9|*             |1
     10|*             |1
     11|*             |1
