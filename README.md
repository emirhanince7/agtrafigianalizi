<div align="center">
  <img src="https://img.shields.io/github/languages/count/emirhanince/agtrafigianalizi?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/emirhanince/agtrafigianalizi?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/emirhanince/agtrafigianalizi?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/emirhanince/agtrafigianalizi?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>


network traffic analysis
ağ trafiği analizi 

This project detects and analyzes the protocols of the data packets passing through the network by listening to the network traffic in real time. It counts the frequency of protocols such as HTTP, TCP, UDP by capturing every packet passing through the network with the scapy library. Abnormal traffic density or specific protocol usage on the network can be observed.

Bu proje, gerçek zamanlı olarak ağ trafiğini dinleyerek geçen veri paketlerinin hangi protokole ait olduğunu tespit eder ve analiz eder. scapy kütüphanesi ile ağ üzerinden geçen her paketi yakalayarak, HTTP, TCP, UDP gibi protokollerin sıklığını sayar. Ağ üzerindeki anormal trafik yoğunluğu veya belirli protokol kullanımı gözlemlenebilir.

---

Features / Özellikler
Feature 1: Real-time packet sniffing to monitor active network traffic.
Özellik 1: Gerçek zamanlı paket dinleme ile aktif ağ trafiğini izleme.

Feature 2: Protocol-based traffic classification (e.g., TCP, UDP, ICMP).
Özellik 2: Trafiği protokole göre sınıflandırma (örneğin TCP, UDP, ICMP).

Feature 3: Summary of captured protocol usage upon termination.
Özellik 3: Program sonlandırıldığında kullanılan protokollerin özetini sunma.

Feature 4: Lightweight and easy-to-use script for basic traffic insight.
Özellik 4: Temel trafik bilgisi için hafif ve kullanımı kolay betik.

Add more as they develop.
Geliştikçe daha fazla ekleyin.

---

## Team / *Ekip*

- 2320191057 - emirhan ince: *project owner and management*  
  *emirhan ince: proje sahibi ve yönetimi*

---


---

Topic / Başlık	Link	Description / Açıklama
Packet Sniffing Techniques / Paket Dinleme Teknikleri	researchs/packet-sniffing.md	Overview of methods for capturing network packets. / Ağ paketlerini yakalama yöntemlerinin genel görünümü.
Using Scapy Library / Scapy Kütüphanesi Kullanımı	researchs/scapy-kullanimi.md	Detailed explanation of using Scapy in Python for network analysis. / Python’da Scapy kullanılarak ağ analizi yapmanın detaylı anlatımı.
Protocol Analysis (TCP/UDP) / Protokol Analizi (TCP/UDP)	researchs/protokol-analizi.md	Basic analysis of transport layer protocols. / Taşıma katmanı (TCP/UDP) protokollerinin temel analizi.
Suspicious Traffic Detection / Şüpheli Trafik Tespiti	researchs/supheli-trafik.md	Methods to detect suspicious patterns like flooding or scanning. / Flooding (taşma) veya port tarama gibi şüpheli trafik desenlerini tespit etme yöntemleri.

## Installation / *Kurulum*

1. git clone https://github.com/emmirhanince7/agtrafigianalizi.git
cd trafik-gozetleyici


2.python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate


3pip install -r requirements.txt


---



Steps:

Prepare input data (The script captures live network traffic directly, so no pre-collected data is needed. Make sure you have proper permissions to sniff network packets on your machine).

Run the script with arguments (Currently, the script runs without arguments by default. You can customize the sniffing interface or filter by modifying the script if needed).

Check output (The script prints detected protocols in real-time to the console. When you stop it with Ctrl+C, a summary report shows total packet counts per protocol).

Adımlar:

Giriş verilerini hazırlayın (Script canlı ağ trafiğini doğrudan yakalar, önceden veri hazırlamanıza gerek yoktur. Ağ paketlerini dinlemek için yeterli izinlere sahip olmalısınız).

Betiği argümanlarla çalıştırın (Şu anda betik herhangi bir argüman almadan çalışır. İsterseniz sniffing yapılacak ağ arayüzünü veya filtreleri script üzerinde değiştirebilirsiniz).

Çıktıyı kontrol edin (Script, tespit edilen protokolleri gerçek zamanlı olarak konsola yazdırır. Ctrl+C ile durdurduğunuzda, her protokol için toplam paket sayısını içeren bir özet rapor gösterilir).


We welcome contributions! To help:

Fork the repository.

Clone your fork (git clone git@github.com:emirhanince7/trafik-gozetleyici.git).

Create a branch (git checkout -b feature/your-feature).

Commit changes with clear messages.

Push to your fork (git push origin feature/your-feature).

Open a Pull Request.

Follow our coding standards (see CONTRIBUTING.md).

Topluluk katkılarını memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.
---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Awesome Library: For enabling X.  
- Inspiration Source.  
- Special thanks to...  

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Your Name/Org Name] - [your.email@example.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Adınız/Kuruluş Adınız] - [e-posta.adresiniz@ornek.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
