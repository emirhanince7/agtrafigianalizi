#!/usr/bin/env python3
from scapy.all import sniff

def paket_yakala(paket):
    print(f"Gelen paket: {paket.summary()}")

def main():
    print("Ağ trafiği analizi başlatıldı. Ctrl+C ile durdurabilirsiniz.")
    sniff(prn=paket_yakala, count=10)  # 10 paket yakalar, istersen count kaldırıp sonsuz yapabilirsin

if __name__ == "__main__":
    main()
