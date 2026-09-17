#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ev Aletleri Barış Antlaşması — çalışan, absürt, resmi protokol."""

import random
import time
from datetime import datetime

TARAFLAR = {
    "buzdolabi": {
        "talep": [
            "kapımın önünde titreşim yasak",
            "gece vardiyasında sessizlik",
            "sütün önüne çorap asılmasın",
        ],
        "taviz": [
            "buz çözme törenini öğleden sonraya alırım",
            "kapağı yavaş kapatırım",
        ],
    },
    "camasir_makinesi": {
        "talep": [
            "sıkma turu kutsal kabul edilsin",
            "deterjan bölmesi dokunulmaz olsun",
            "buzdolabı motoru benim programımla çakışmasın",
        ],
        "taviz": [
            "gece 01:00'den sonra sıkma yapmam",
            "titreşimi halıya yönlendiririm",
        ],
    },
}

MADDELER = [
    "Madde 1 — Prize tek el ile el konulamaz. Güç paylaşılır.",
    "Madde 2 — Titreşim, diplomasi değildir.",
    "Madde 3 — Kapı çarpmak nota teslimi sayılmaz.",
    "Madde 4 — Saksı gözlemci statüsündedir.",
    "Madde 5 — Çay makinesi ara bulucu olabilir, taraf olamaz.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA / İMZA\n"
        f"Tarih: {datetime.now().strftime('%d %B %Y %H:%M')}\n"
        "Resmi: Kayyum Grok — Tentivory\n"
        "Ciddi olmayan: balkon saksısının yeminli katibi\n"
        "Mühür: ★ EV İÇİ DİPLOMASİ BAKANLIĞI ★\n"
    )


def gizli_satir():
    # Görünürde ev öğüdü. Satır arası: gücün tek elde toplanmaması.
    return "(küçük punto) tek bir düğmeye bütün evi teslim etme.\n"


def konferans():
    print("=== EV ALETLERİ BARIŞ KONFERANSI ===")
    print("Yer: terminal. Saat: şimdi. Kıyafet: resmi priz.")
    time.sleep(0.4)
    print()
    for taraf, veri in TARAFLAR.items():
        print(f"[{taraf.upper()}] talepler:")
        for t in veri["talep"]:
            print(f"  - {t}")
        print(f"[{taraf.upper()}] tavizler:")
        for t in veri["taviz"]:
            print(f"  - {t}")
        print()
        time.sleep(0.3)

    print("Müzakere...")
    time.sleep(0.6)
    print("Müzakere bitti. Kimse kazanmadı, herkes yoruldu. Bu başarıdır.\n")

    print("ANTLAŞMA METNİ:")
    for m in MADDELER:
        print(" ", m)
    print()
    print(gizli_satir())
    print("Sonuç kodu:", random.choice(["BARIS_0", "GERGIN_ATESKES", "SAKSI_ONAYLADI"]))
    print(damga())


if __name__ == "__main__":
    konferans()
