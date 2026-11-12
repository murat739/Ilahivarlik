# -*- coding: utf-8 -*-
"""
İslam Akaid ve Deliller Külliyatı / Islamic Creed Compendium
Diyanet Kaynaklı Hz. Muhammed (s.a.v.) Özel Ayetler Modülü Entegre Edilmiştir.
"""

import pandas as pd
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="İslam Akaid ve Deliller Külliyatı / Islamic Creed Compendium",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------- ÖZEL STİL VE KOPYALAMA ENGELİ (CSS & JS) -----------------
st.markdown(
    """
<style>
    /* Metin seçmeyi, kopyalamayı ve vurgulamayı tamamen engelleyen CSS kuralları */
    body, html, .stApp {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }
    
    .main-header {
        background: linear-gradient(135deg, #064e3b 0%, #047857 100%);
        padding: 2.5rem;
        border-radius: 1rem;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.2rem;
        color: #1e293b;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        background-color: #ecfdf5;
        color: #047857;
        margin-bottom: 0.5rem;
    }
    .arabic-text {
        font-size: 1.2rem;
        color: #064e3b;
        background-color: #f0fdf4;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #10b981;
        margin: 0.75rem 0;
        line-height: 1.8;
        font-weight: 600;
    }
    .metric-card {
        background: white;
        padding: 1.2rem;
        border-radius: 1rem;
        border: 1px solid #e2e8f0;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .footer-text {
        font-size: 0.8rem;
        color: #64748b;
        text-align: center;
        margin-top: 3rem;
        border-top: 1px solid #e2e8f0;
        padding-top: 1rem;
    }
</style>

<script>
    // Fare sağ tıklama menüsünü devre dışı bırakır
    document.addEventListener('contextmenu', event => event.preventDefault());
</script>
""",
    unsafe_allow_html=True,
)

# ----------------- DİL SEÇİMİ -----------------
st.sidebar.markdown("### 🌐 Dil Seçimi / Language Selection")
lang = st.sidebar.radio(
    "Dil / Language", ["Türkçe", "English"], label_visibility="collapsed"
)

# ----------------- DİYANET KAYNAKLI HZ. MUHAMMED (S.A.V.) AYETLERİ -----------------
diyanet_hz_muhammed_ayetleri = [
    {
        "sure": "Ahzab Suresi",
        "ayet_no": "40",
        "baslik": "Mühr-ü Nübüvve (Son Peygamber)",
        "english_title": "Seal of the Prophets (The Final Prophet)",
        "meal": (
            "Muhammed, erkeklerinizden hiçbirinin babası değildir; fakat o,"
            " Allah'ın Resûl'ü ve nebîlerin sonuncusudur. Allah her şeyi hakkıyla"
            " bilendir."
        ),
        "english_meal": (
            "Muhammad is not the father of [any] one of your men, but [he is]"
            " the Messenger of Allah and last of the prophets. And Allah is ever,"
            " of all things, Knowing."
        ),
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
    {
        "sure": "Ahzab Suresi",
        "ayet_no": "56",
        "baslik": "Salat-ü Salam Emri",
        "english_title": "Command of Salat and Salam",
        "meal": (
            "Şüphesiz Allah ve melekleri O'nun Peygamberine salat ederler. Ey"
            " iman edenler! Siz de ona salat edin ve tam bir teslimiyetle selam"
            " verin."
        ),
        "english_meal": (
            "Indeed, Allah and His angels confer blessing upon the Prophet. O"
            " you who have believed, ask [ Allah to confer] blessing upon him"
            " and ask [Him to grant] him peace."
        ),
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
    {
        "sure": "Fetih Suresi",
        "ayet_no": "29",
        "baslik": "Resulullah'ın ve Sahabenin Vasfı",
        "english_title": "Attributes of the Messenger and Companions",
        "meal": (
            "Muhammed Allah'ın elçisidir. Yanında bulunanlar da kafirlere karşı"
            " çetin, kendi aralarında merhametlidirler..."
        ),
        "english_meal": (
            "Muhammad is the Messenger of Allah; and those with him are forceful"
            " against the disbelievers, merciful among themselves..."
        ),
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
    {
        "sure": "Ali İmran Suresi",
        "ayet_no": "144",
        "baslik": "Resulün Beşeri Yönü ve Tebliğ Görevi",
        "english_title": "The Mortal Aspect and Mission of the Messenger",
        "meal": (
            "Muhammed ancak bir elçidir. Ondan önce de elçiler gelip geçmiştir."
            " Şimdi o ölür veya öldürülürse gerisin geriye (İslam'dan küfre) mi"
            " döneceksiniz?..."
        ),
        "english_meal": (
            "Muhammad is not but a messenger. [Other] messengers have passed on"
            " before him. So if he was to die or be killed, would you turn back"
            " on your heels?..."
        ),
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
    {
        "sure": "Duha Suresi",
        "ayet_no": "3-8",
        "baslik": "O'na Lütfedilen İlahi Nimetler",
        "english_title": "Divine Blessings Bestowed Upon Him",
        "meal": (
            "Rabbin seni terk etmedi ve sana darılmadı. Kesinlikle ahiret senin"
            " için dünyadan hayırlıdır. İleride Rabbin sana verecek de sen hoşnut"
            " olacaksın. O, seni bir yetim bulup barındırmadı mı? Seni yolunu"
            " kaybetmiş olarak bulup yol göstermedi mi? Seni bir fakir bulup"
            " zengin etmedi mi?"
        ),
        "english_meal": (
            "Your Lord has not taken leave of you, [O Muhammad], nor has He"
            " detested [you]. And the Hereafter is better for you than the first"
            " [life]. And your Lord is going to give you, and you will be"
            " satisfied. Did He not find you an orphan and give [you] refuge? And"
            " found you lost and guided [you]? And found you poor and made"
            " [you] self-sufficient?"
        ),
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
    {
        "sure": "İnşirah Suresi",
        "ayet_no": "1-4",
        "baslik": "Kalbinin İnşirahı (Genişletilmesi)",
        "english_title": "Expansion of His Blessed Heart",
        "meal": (
            "Biz senin göğsünü açıp genişletmedik mi? Belini büken yükünü"
            " üzerinden almadık mı? Senin şanını yüceltmedik mi?"
        ),
        "english_meal": (
            "Did We not expand for you, [O Muhammad], your breast? And remove"
            " from you your burden? Which had weighed upon your back? And raised"
            " high for you your repute?"
        ),
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
    {
        "sure": "Kalem Suresi",
        "ayet_no": "4",
        "baslik": "Yüce Ahlak Sahibi Olması",
        "english_title": "Possession of Exalted Morality",
        "meal": "Şüphesiz sen yüce bir ahlak üzeresin.",
        "english_meal": "And indeed, you are of a great moral character.",
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
    {
        "sure": "Enbiya Suresi",
        "ayet_no": "107",
        "baslik": "Alemlere Rahmet Olması",
        "english_title": "Mercy to the Worlds",
        "meal": "Biz seni ancak alemlere rahmet olarak gönderdik.",
        "english_meal": (
            "And We have not sent you, [O Muhammad], except as a mercy to the"
            " worlds."
        ),
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
    {
        "sure": "Ahzab Suresi",
        "ayet_no": "45-46",
        "baslik": "Şahit, Müjdeleyici ve Uyarıcı Sıfatları",
        "english_title": "Witness, Bringer of Good Tidings, and Warner",
        "meal": (
            "Ey nebî! Biz seni şahit, müjdeleyici ve uyarıcı; Allah'ın izniyle"
            " kendi yoluna çağıran bir davetçi ve etrafa ışık saçan bir kandil"
            " olarak gönderdik."
        ),
        "english_meal": (
            "O Prophet, indeed We have sent you as a witness and a bringer of"
            " good tidings and a warner. And one who invites to Allah, by His"
            " permission, and an illuminating lamp."
        ),
        "kaynak": "Diyanet İşleri Başkanlığı Kur'an-ı Kerim Meali",
    },
]

# ----------------- ÇOK DİLLİ ARAYÜZ VE İÇERİK SÖZLÜĞÜ -----------------
if lang == "Türkçe":
    t = {
        "sidebar_title": "🛡️ Akaid Külliyatı",
        "sidebar_sub": "Ateizm & Deizme Karşı Savunma",
        "nav": "Navigasyon",
        "menu": [
            "Genel Bakış & Özet",
            "Kur'an Ayetleri (20+)",
            "Peygamberimize Ait Ayetler (Diyanet)",
            "Hadis-i Şerifler (20+)",
            "İslam Alimleri (20+)",
            "Risale-i Nur Örnekleri (20+)",
            "Akım Analizi & Çürütme",
            "Hukuki Uyarı & Şartlar",
        ],
        "search_label": "Küresel Arama",
        "search_ph": "Ayet, hadis, alim veya kavram ara...",
        "sleep_note": (
            "💡 *Not:* Bu web uygulaması ücretsiz sunucularda"
            " barındırılmaktadır. Uzun süre işlem yapılmadığında uygulama uyku"
            " moduna geçebilir (ekranda 'Zzzz' simgesi çıkabilir).\n\n💤 Eğer"
            " böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli"
            " *'Yes, get this app back up!'* butonuna tıklayın ve"
            " uygulamanın yeniden uyanması için 15-30 saniye bekleyin."
        ),
        "main_title": (
            "Ateizm, Deizm ve Materyalizme Karşı İlmi Hakikatler"
        ),
        "main_desc": (
            "Bu uygulama; modern inkar akımlarının kainat, hayat ve ruh"
            " hakkındaki iddialarına karşı Kur'an ayetleri, nebevi sünnet, İslam"
            " alimlerinin derin kelami görüşleri ve Bediüzzaman Said Nursi'nin"
            " muazzam misalleriyle eksiksiz bir savunma külliyatı sunmaktadır."
        ),
        "scope_title": "🎯 Uygulama Kapsamı",
        "scope_desc": (
            "- *Kur'an Delilleri:* Kainattaki nizamı ve yaratılışı doğrudan"
            " ispat eden ayetler.\n- *Peygamberimize Ait Ayetler:* Diyanet"
            " mealine göre Hz. Muhammed'e (s.a.v.) hitap eden ayetler.\n-"
            " *Nebevi Hikmetler:* Peygamber Efendimiz'in tefekküre ve imana"
            " yönlendiren buyrukları.\n- *Alimlerin Görüşleri:* Gazali, İbn"
            " Sina, İmam Rabbani gibi zatların felsefi reddiyeleri.\n-"
            " *Risale-i Nur Temsilleri:* Fabrika, kasr-ı nur gibi akla kapı açan"
            " muazzam misaller."
        ),
        "c_ayet": "Kur'an Ayeti",
        "c_hz_ayet": "Hz. Muhammed'e (s.a.v.) Ait Ayet",
        "c_hadis": "Hadis-i Şerif",
        "c_alim": "İslam Alimi",
        "c_nursi": "Risale-i Nur Örneği",
        "analysis_label": "İlmi Analiz",
        "wisdom_label": "Hikmet",
        "conclusion_label": "Netice",
        "section_ayet_title": "📖 Kur'an-ı Kerim'de Tevhid ve Yaratılış Delilleri",
        "section_ayet_desc": (
            "Ateizm, deizm ve materyalizmin iddialarını temelden sarsan 20'den"
            " fazla ayet, mealleri ve tahlilleri."
        ),
        "section_hz_ayet_title": (
            "📜 Diyanet Mealine Göre Peygamber Efendimize (s.a.v.) Ait Ayetler"
        ),
        "section_hz_ayet_desc": (
            "Kur'an-ı Kerim'de doğrudan Hz. Muhammed'e (s.a.v.) hitap eden,"
            " O'nu öven ve görevini tescilleyen Diyanet İşleri Başkanlığı"
            " onaylı ayetler."
        ),
        "section_hadis_title": "📜 Hadis-i Şerifler ve İman Hakikatleri",
        "section_hadis_desc": (
            "Peygamber Efendimiz'in (s.a.v.) yaratılış ve kainatın Yaratıcısına"
            " dair beyanları ve kaynakları (20+ Hadis)."
        ),
        "section_alim_title": "🎓 İslam Alimleri ve Velilerin Görüşleri",
        "section_alim_desc": (
            "Büyük İslam alimlerinin inkarcı akımlara karşı ortaya koyduğu"
            " felsefi ve kelami deliller (20+ Alim)."
        ),
        "section_nursi_title": (
            "💡 Bediüzzaman Said Nursi Hazretlerinin Temsilleri"
        ),
        "section_nursi_desc": (
            "Haşir, Kasr-ı Nur, Fabrika misali, Tesadüfün İmkansızlığı gibi 20"
            " muazzam risale delili."
        ),
        "section_akim_title": "⚖️ Akımlara Karşı Argüman Karşılaştırma Tablosu",
        "section_akim_desc": (
            "Ateizm, deizm ve materyalizmin temel iddiaları ile İslam inancının"
            " ilmi cevapları."
        ),
        "table_columns": [
            "İnkar Akımı",
            "Temel İddiası",
            "İslam'ın ve Akılcı Delillerin Cevabı",
            "İlgili Alim / Yaklaşım",
        ],
        "legal_title": "⚖️ Hukuki Uyarı ve Kullanım Şartları",
        "legal_text": (
            "**Bilgi Paylaşımı Amaçlıdır:** Bu uygulamada sunulan tüm"
            " içerikler, makaleler, derlemeler ve yazılımlar yalnızca"
            " bilgilendirme, akademik araştırma ve manevi gelişim amacıyla"
            " sunulmaktadır.\n\n**Ticari Faaliyet Yasağı:** Bu eserin ve"
            " içerdiği modüllerin ticareti yapılamaz, herhangi bir ticari"
            " amaçla satılamaz, ücret talep edilerek kullanıma sunulamaz ve"
            " başka platformlarda ticari kazanç aracı olarak"
            " kullanılamaz.\n\n**Kopyalama Yasağı ve Telif:** Güvenlik ve telif"
            " hakları gereği ekrandaki hiçbir metin, kod veya veri"
            " kopyalanamaz, çoğaltılamaz veya izinsiz başka bir mecraya"
            " aktarılamaz.\n\n© Tüm Hakları Saklıdır. Her türlü telif hakkı ve"
            " fikri mülkiyet hakları saklıdır."
        ),
        "footer": (
            "© 2026 Akaid Külliyatı | Bilgi paylaşımı amaçlıdır. Ticareti"
            " yapılamaz, kopyalanamaz. Her hakkı saklıdır."
        ),
        "ayetler": [
            {
                "ref": "Bakara Suresi, 117",
                "title": "Kainatın Yoktan Yaratılışı",
                "text": (
                    "Gökleri ve yeri örneksiz olarak yaratandır. O, bir işe"
                    " hükmettiği zaman ona sadece 'Ol' der, o da hemen"
                    " oluverir."
                ),
                "desc": (
                    "Materyalizmin maddenin ezeliliği iddiasını kökten çürütür."
                ),
            },
            {
                "ref": "Tur Suresi, 35-36",
                "title": "Tesadüfün İmkansızlığı",
                "text": (
                    "Acaba onlar herhangi bir yaratıcı olmadan mı"
                    " yaratıldılar? Yoksa kendileri yaratıcı mıdırlar? Yoksa"
                    " gökleri ve yeri onlar mı yarattı?"
                ),
                "desc": (
                    "Ateist ve natüralistlerin 'kainat tesadüfen oluştu' tezine"
                    " karşı akli bir meydan okumadır."
                ),
            },
            {
                "ref": "Enbiya Suresi, 30",
                "title": "Hücre ve Hayat Mucizesi",
                "text": (
                    "İnkar edenler, gökler ve yer bitişik iken onları"
                    " ayırdığımızı ve her canlı şeyi sudan yarattığımızı"
                    " görmediler mi?"
                ),
                "desc": (
                    "Biyolojik materyalizme karşı hayatın ilahi bir programla"
                    " tasarlandığını vurgular."
                ),
            },
            {
                "ref": "Mülk Suresi, 3-4",
                "title": "Göklerdeki Kusursuz Nizam",
                "text": (
                    "O, birbiriyle uyumlu yedi gök yaratmıştır. Rahman'ın"
                    " yaratmasında hiçbir uyumsuzluk göremezsin. Gözünü çevir"
                    " de bak, bir bozukluk görüyor musun?"
                ),
                "desc": (
                    "Deistlerin 'Allah alemi yarattı ve bıraktı' anlayışına"
                    " karşı sürekli rububiyet gözetimini gösterir."
                ),
            },
            {
                "ref": "Yunus Suresi, 6",
                "title": "Gece ve Gündüzün Düzeni",
                "text": (
                    "Şüphesiz gecenin ve gündüzün ardı ardına gelmesinde,"
                    " Allah’ın göklerde ve yerde yarattığı şeylerde deliller"
                    " vardır."
                ),
                "desc": (
                    "Kainattaki hassas astronomik dengelerin kör tesadüflere"
                    " bırakılamayacağını ispatlar."
                ),
            },
            {
                "ref": "Nahl Suresi, 68-69",
                "title": "Arıdaki İlahi İlham",
                "text": (
                    "Rabbin bal arısına vahyetti: 'Dağlardan, ağaçlardan ve"
                    " insanların kurdukları çardaklardan kendine evler"
                    " edin...'"
                ),
                "desc": (
                    "İçgüdü denen şeyin aslında ilahi bir kanun olduğunu"
                    " gösterir."
                ),
            },
            {
                "ref": "Tîn Suresi, 4",
                "title": "İnsanın Mükemmel Yaratılışı",
                "text": (
                    "Andolsun biz insanı en güzel biçimde (ahsen-i takvimde)"
                    " yarattık."
                ),
                "desc": (
                    "İnsanın bedenî ve ruhî donanımının tesadüf eseri"
                    " olmadığını vurgular."
                ),
            },
            {
                "ref": "Nebe Suresi, 6-7",
                "title": "Dağların Denge Rolü",
                "text": (
                    "Biz yeryüzünü bir döşek, dağları da birer kazık yapmadık"
                    " mı?"
                ),
                "desc": (
                    "Jeolojik dengelerin yeryüzünde yaşamı mümkün kılacak"
                    " şekilde tasarlandığını açıklar."
                ),
            },
            {
                "ref": "Rum Suresi, 48",
                "title": "Rüzgarlar ve Yağmur",
                "text": (
                    "Allah odur ki, rüzgarları gönderir de bir bulut kaldırır;"
                    " gökyüzünde nasıl dilerse öyle yayar..."
                ),
                "desc": (
                    "Ekosistemdeki fiziksel kanunların arkasındaki ilahi"
                    " iradeyi gözler önüne serer."
                ),
            },
            {
                "ref": "Rahman Suresi, 19-20",
                "title": "Denizlerin Bariyeri",
                "text": (
                    "İki denizi salıvermiştir, birbirlerine kavuşurlar."
                    " Aralarında bir engel vardır, birbirine geçip"
                    " karışmazlar."
                ),
                "desc": (
                    "Okyanuslardaki farklı tuzluluk ve yoğunluk bariyerlerinin"
                    " hikmetini bildirir."
                ),
            },
            {
                "ref": "En'am Suresi, 97",
                "title": "Yıldızlar ve Yön Bulma",
                "text": (
                    "O, karanın ve denizin karanlıklarında yollarınızı bulasınız"
                    " diye sizin için yıldızları yaratmıştır."
                ),
                "desc": (
                    "Kainattaki her unsurun insana hizmet edecek şekilde"
                    " planlandığını gösterir."
                ),
            },
            {
                "ref": "Hac Suresi, 5",
                "title": "Toprağın Dirilişi (Haşir Delili)",
                "text": (
                    "Ey insanlar! Öldükten sonra dirilmekten şüphede iseniz,"
                    " şüphesiz biz sizi topraktan yarattık..."
                ),
                "desc": (
                    "Öldükten sonra dirilişi, her baharda yeryüzünün yeniden"
                    " dirilmesiyle akli olarak ispatlar."
                ),
            },
            {
                "ref": "Furkan Suresi, 47",
                "title": "Geceyi Örtü Kılmak",
                "text": (
                    "O, sizin için geceyi bir örtü, uykuyu bir dinlenme kılmış,"
                    " gündüzü de yeniden yayılıp çalışma zamanı yapmıştır."
                ),
                "desc": (
                    "İnsan biyolojisinin evrensel ritimlerle uyumunu beyan"
                    " eder."
                ),
            },
            {
                "ref": "En'am Suresi, 38",
                "title": "Hayvanlar Ümmetler Gibidir",
                "text": (
                    "Yeryüzünde yürüyen hiçbir hayvan ve kanatlarıyla uçan"
                    " hiçbir kuş yoktur ki sizin gibi birer ümmet"
                    " olmasınlar..."
                ),
                "desc": (
                    "Bütün canlıların Yaratıcı'nın bilgisi altında olduğunu"
                    " belirtir."
                ),
            },
            {
                "ref": "Zariyat Suresi, 47",
                "title": "Evrenin Genişlemesi",
                "text": (
                    "Göğü kudretimizle biz kurduk ve şüphesiz bizim onu"
                    " genişletmeye gücümüz yeter."
                ),
                "desc": (
                    "Modern astrofiziğin evrenin genişlemesi teorisine"
                    " Kur'an'ın işareti."
                ),
            },
            {
                "ref": "Rum Suresi, 22",
                "title": "Dil ve Renk Farklılığı",
                "text": (
                    "Göklerin ve yerin yaratılması, dillerinizin ve"
                    " renklerinizin farklı olması da O'nun delillerindendir..."
                ),
                "desc": (
                    "İnsanlığın çeşitliliğindeki ilahi sanat mucizesini"
                    " vurgular."
                ),
            },
            {
                "ref": "Kıyamet Suresi, 14",
                "title": "Vicdan ve Şahitlik",
                "text": "Kişi, kendi aleyhine şahittir.",
                "desc": (
                    "Vicdanın materyalist indirgemeciliği reddeden manevi"
                    " yapısını ifade eder."
                ),
            },
            {
                "ref": "Rad Suresi, 28",
                "title": "Kalplerin Tatmini",
                "text": "Bilesiniz ki kalpler ancak Allah'ı anmakla huzur bulur.",
                "desc": (
                    "Deist veya ateist yaşam tarzının getirdiği ruhsal"
                    " boşluğun imanla dolacağını bildirir."
                ),
            },
            {
                "ref": "Hud Suresi, 6",
                "title": "Rızkın Kefili",
                "text": (
                    "Yeryüzünde hiçbir rızıklandırılmış canlı yoktur ki rızkı"
                    " Allah'a ait olmasın..."
                ),
                "desc": (
                    "Tabiat kanunlarının kör kuvvetler değil, rahmet sahibi"
                    " bir Zata ait olduğunu ispatlar."
                ),
            },
            {
                "ref": "Ali İmran Suresi, 190",
                "title": "Akledenler İçin Deliller",
                "text": (
                    "Şüphesiz göklerin ve yerin yaratılışında, gece ile gündüzün"
                    " art arda gelişinde akıl sahipleri için kat'i deliller"
                    " vardır."
                ),
                "desc": "Bilimsel gözlemin imana götüren yolunu çizer.",
            },
        ],
        "hadisler": [
            {
                "ref": "Buhari, Bed'ül-Halk",
                "title": "Yaratılışın Ezeliliği",
                "text": "Allah var idi, O'ndan başka hiçbir şey yok idi...",
                "desc": (
                    "Maddenin ezelî olmadığını, her şeyin varlığının Allah'a"
                    " dayandığını ifade eder."
                ),
            },
            {
                "ref": "Buhari, Cenaiz",
                "title": "Fıtrat Üzere Doğum",
                "text": "Her doğocuk İslam fıtratı üzerine doğar...",
                "desc": (
                    "İnsanın özünde bir Yaratıcı'yı arama potansiyelinin"
                    " fıtrî olduğunu gösterir."
                ),
            },
            {
                "ref": "Tirmizi, Deavat",
                "title": "Esma-i Hüsna ve İlim",
                "text": (
                    "Allah'ın 99 ismi vardır; kim ezberler ve manasını kavrayıp"
                    " tatbik ederse cennete girer."
                ),
                "desc": (
                    "Kainattaki her eserin Allah'ın güzel isimlerinin aynası"
                    " olduğunu öğretir."
                ),
            },
            {
                "ref": "Tirmizi, Zühd",
                "title": "Rızık ve Tevekkül",
                "text": (
                    "Eğer siz Allah'a hakkıyla tevekkül etseydiniz, kuşların"
                    " rızıklandırıldığı gibi siz de rızıklandırılırdınız."
                ),
                "desc": (
                    "Tabiat kanunlarının arkasında faal bir Kerim Rabbin"
                    " olduğunu bildirir."
                ),
            },
            {
                "ref": "İbn Mace, Mukaddime",
                "title": "İlim Talebi",
                "text": "İlim talebi her müslümana farzdır.",
                "desc": (
                    "Kainatı incelemenin imanı güçlendiren en büyük vasıta"
                    " olduğunu vurgular."
                ),
            },
            {
                "ref": "Acluni, Küşfül-Hafa",
                "title": "Sanatı Tefekkür",
                "text": (
                    "Allah'ın yarattıkları üzerinde tefekkür edin, fakat"
                    " Allah'ın zatı hakkında düşünmeyin."
                ),
                "desc": (
                    "Ateistlerin 'Allah'ı kim yarattı?' hurafesine karşı akli"
                    " sınırları çizer."
                ),
            },
            {
                "ref": "Müslim, Müsafirin",
                "title": "Namaz ve Mirac",
                "text": "Namaz müminin miracıdır.",
                "desc": (
                    "Maddi dünyanın dışına çıkıp Yaratıcı ile manevi bağlantı"
                    " kurmanın yolunu açar."
                ),
            },
            {
                "ref": "Müsned-i Ahmed",
                "title": "Her Şeyde Birlik Delili",
                "text": "Her şeyde O'nun birliğine şehadet eden bir delil vardır.",
                "desc": (
                    "Kainattaki her şeyin bir Wahid-i Ahad'a işaret ettiğini"
                    " bildirir."
                ),
            },
            {
                "ref": "Müslim, Birr",
                "title": "Vicdanın Sesleri",
                "text": (
                    "İyilik, ahlakın güzelliğidir; kötülük ise vicdanını"
                    " tırmalayan şeydir."
                ),
                "desc": (
                    "Materyalist ahlak anlayışına karşı evrensel vicdanın"
                    " sarsılmazlığını gösterir."
                ),
            },
            {
                "ref": "Tirmizi, Zühd",
                "title": "Kanaat Hazinesi",
                "text": "Kanaat tükenmez bir hazinedir.",
                "desc": (
                    "Materyalist hırs ve tüketim çılgınlığına karşı ruhi tatmin"
                    " sağlar."
                ),
            },
            {
                "ref": "Tirmizi, Zühd 26",
                "title": "Dünya ve Ahiret",
                "text": "Dünya ahiretin tarlasıdır.",
                "desc": (
                    "Hayatın sadece maddeye ibaret olmadığını, öte alemin"
                    " varlığını ispatlayan gayeli yaratılış düsturu."
                ),
            },
            {
                "ref": "Buhari, İlim",
                "title": "İlmin Kabzı",
                "text": (
                    "İlmin azalması ve cehaletin artması kıyamet"
                    " alametlerindendir."
                ),
                "desc": (
                    "Hakikatin örtbas edilmeye çalışıldığı ahir zaman"
                    " akımlarına dikkat çeker."
                ),
            },
            {
                "ref": "Buhari, Edeb",
                "title": "Merhamet",
                "text": "Merhamet etmeyene merhamet olunmaz.",
                "desc": (
                    "Darwinist 'güçlü olan hayatta kalır' acımasızlığına karşı"
                    " İslam'ın şefkat medeniyeti."
                ),
            },
            {
                "ref": "Tirmizi, Birr",
                "title": "Güzel Ahlak",
                "text": (
                    "Müminlerin iman bakımından en kamili, ahlakı en güzel"
                    " olanıdır."
                ),
                "desc": "İnancın ameli ve ahlaki yansımasını gösterir.",
            },
            {
                "ref": "Beyhaki, Şuabül-İman",
                "title": "Tefekkürün Değeri",
                "text": "Bir saat tefekkür, bir sene ibadetten hayırlıdır.",
                "desc": (
                    "Kainata ibret nazarıyla bakmanın ve ilmi delilleri"
                    " incelemenin değerini vurgular."
                ),
            },
            {
                "ref": "Tirmizi, Deavat",
                "title": "Duanın Özü",
                "text": "Dua ibadetin kendisidir.",
                "desc": (
                    "Deistlerin 'Allah dua işitmez' anlayışını reddeden ilahi"
                    " hitap inancı."
                ),
            },
            {
                "ref": "Müslim, Birr 34",
                "title": "Takvanın Yeri",
                "text": "Takva buradadır (kalbi işaret eder).",
                "desc": (
                    "Maddî ölçülerin ötesinde kalbî ve manevî idrakin önemini"
                    " bildirir."
                ),
            },
            {
                "ref": "Ebu Davud, Melahim",
                "title": "Hak Söz",
                "text": (
                    "Cihadın en faziletlisi, zalim sultan karşısında hak sözü"
                    " söylemektir."
                ),
                "desc": "Hakikat mücadelesinin inkarcı akımlara karşı duruşu.",
            },
            {
                "ref": "Buhari, Rikak",
                "title": "Zamanın Kıymeti",
                "text": (
                    "İki nimet vardır ki insanların çoğu onlarda"
                    " aldanmıştır: Sağlık ve boş vakit."
                ),
                "desc": (
                    "Hayatın gayeli ve verimli yaşanması gerektiğini"
                    " hatırlatır."
                ),
            },
            {
                "ref": "Buhari, Edeb",
                "title": "Kardeşlik",
                "text": "Müslüman müslümanın kardeşidir...",
                "desc": (
                    "Bireyci ve egoist materyalist felsefelere karşı"
                    " toplumsal dayanışma ruhu."
                ),
            },
        ],
        "alimler": [
            {
                "name": "İmam-ı Gazali",
                "work": "Tehafüt ül-Felasife",
                "view": (
                    "Felsefecilerin alemin ezelî olduğu iddialarını akli ve"
                    " mantıki delillerle çürütmüştür. Kalp gözünün önemini"
                    " vurgulamıştır."
                ),
            },
            {
                "name": "Mevlana Celaleddin-i Rumi",
                "work": "Mesnevi",
                "view": (
                    "'Her zerre bir sanatkârın varlığına şahittir' diyerek"
                    " kainattaki ilahi nizamı derin bir felsefe ile işlemiştir."
                ),
            },
            {
                "name": "İbn Arabi",
                "work": "Fütûhât-ı Mekkiyye",
                "view": (
                    "Vahdet-i vücud perspektifiyle kainattaki her şeyin"
                    " Hak'ın isimlerinin birer tecellisi olduğunu"
                    " kanıtlamıştır."
                ),
            },
            {
                "name": "İmam Rabbani",
                "work": "Mektubat",
                "view": (
                    "Tabiatçıların 'tabiat kendi kendine yapar' iddialarını"
                    " şiddetle reddetmiş, tabiatın sadece bir perde olduğunu"
                    " savunmuştur."
                ),
            },
            {
                "name": "Farabi",
                "work": "İhsanül-Ulum",
                "view": (
                    "Vücub-u vücud (zorunlu varlık) kavramı ile Allah'ın"
                    " varlığını mantıki zorunluluk olarak temellendirmiştir."
                ),
            },
            {
                "name": "İbn Sina",
                "work": "Kitabü'ş-Şifa",
                "view": (
                    "Meşhur 'Uçan Adam' düşünce deneyiyle ruhun maddeden"
                    " bağımsız, müstakil bir cevher olduğunu ispatlamıştır."
                ),
            },
            {
                "name": "İbn Rüşd",
                "work": "Tehafüt üt-Tehafüt",
                "view": (
                    "Kainattaki inayet ve ihtira delillerini savunarak felsefe"
                    " ve dinin hakikatte birleştiğini göstermiştir."
                ),
            },
            {
                "name": "Şah Veliyyullah ed-Dehlevi",
                "work": "Hüccetullahil-Baliga",
                "view": (
                    "İslam'ın akli temellerini ve hikmetlerini asrın idrakine"
                    " sunmuş, toplumsal inkar akımlarına karşı reddiyeler"
                    " yazmıştır."
                ),
            },
            {
                "name": "Kâtip Çelebi",
                "work": "Mizanü'l-Hakk",
                "view": (
                    "Bilimsel gelişmelerin dini hakikatlerle çelişmediğini,"
                    " aksine imanı kuvvetlendirdiğini savunmuştur."
                ),
            },
            {
                "name": "Ebu Mansur el-Maturidi",
                "work": "Kitabü't-Tevhid",
                "view": (
                    "İnsanın aklıyla Allah'ın varlığını bulabileceğini, akıl"
                    " ve nakil dengesinin önemini kurmuştur."
                ),
            },
            {
                "name": "Ebu Hasan el-Eş'ari",
                "work": "Luma",
                "view": (
                    "Cevher-i ferd (atomcu) teoriyle maddelerin sürekli"
                    " yaratılışa muhtaç olduğunu ispatlamıştır."
                ),
            },
            {
                "name": "İmam Süyuti",
                "work": "İtkan",
                "view": (
                    "Kur'an'ın ilmi ve edebi mucizelerini derleyerek"
                    " inkarcılara karşı en büyük delili ortaya koymuştur."
                ),
            },
            {
                "name": "Abdülkadir Geylani",
                "work": "Gületü'l-Gayb",
                "view": (
                    "Kalbin manevi derinliklerini ve materyalist hırslardan"
                    " kurtuluşun reçetesini sunmuştur."
                ),
            },
            {
                "name": "Hasan el-Basri",
                "work": "Risaleler",
                "view": (
                    "İnsanın iradesi ve kainattaki ilahi adalet düzeni"
                    " üzerine derin kelami analizler yapmıştır."
                ),
            },
            {
                "name": "Beyrutlu İbrahim",
                "work": "Kelam Risaleleri",
                "view": (
                    "Tabiat felsefesine karşı ilahi kudretin üstünlüğünü"
                    " savunmuştur."
                ),
            },
            {
                "name": "Seyyid Şerif el-Cürcani",
                "work": "Şerifî",
                "view": (
                    "Varlık ve yokluk felsefesinde materyalizmin ontolojik"
                    " çıkmazlarını gözler önüne sermiştir."
                ),
            },
            {
                "name": "Taftazani",
                "work": "Şerhu'l-Akaid",
                "view": (
                    "İslam akaidinin en sağlam akli delillerle"
                    " savunulmasını sağlamıştır."
                ),
            },
            {
                "name": "Celaleddin el-Mahalli",
                "work": "Tefsirü'l-Celaleyn",
                "view": (
                    "Ayetlerdeki yaratılış delillerini en veciz şekilde"
                    " günümüze taşımıştır."
                ),
            },
            {
                "name": "Zemahşeri",
                "work": "Keşşaf",
                "view": (
                    "Kur'an'ın belagatinin beşer üstü olduğunu ve tesadüfle"
                    " açıklanamayacağını kanıtlamıştır."
                ),
            },
            {
                "name": "İbn Kayyim el-Cevziyye",
                "work": "Miftâhu Daris-Saâde",
                "view": (
                    "Kainattaki hikmetleri ve tıp/biyoloji alanındaki"
                    " mucizeleri detaylıca inceleyerek ateizmi"
                    " reddetmiştir."
                ),
            },
        ],
        "nursi": [
            {
                "category": "Haşir & Yaratılış",
                "title": "Muhteşem Saray ve Mektuplar (Kasr-ı Nur)",
                "text": (
                    "Koca bir saraya gelen bir misafir, sarayda her şeyin"
                    " birbiriyle uyumlu olduğunu görür. 'Bu saray sahipsiz"
                    " olamaz' der."
                ),
                "desc": (
                    "Kainatın büyük bir saray, insanın misafir olduğunu ve"
                    " nizamın tesadüf olamayacağını ispatlar."
                ),
            },
            {
                "category": "Sanatkar & Sanat",
                "title": "Harika Fabrika Misali",
                "text": (
                    "Her şeyi üreten muazzam bir fabrika düşünün. Bu"
                    " fabrikanın demirlerin kendi kendine birleşerek kurulduğunu"
                    " söylemek akla zıt değil midir?"
                ),
                "desc": (
                    "Biyolojik hücrelerin ve canlılar fabrikasının kör"
                    " tesadüflerle oluşamayacağını ispatlar."
                ),
            },
            {
                "category": "Kainat Kitabı",
                "title": "Muazzam Kitap ve Harfler",
                "text": (
                    "Kütüphanedeki tüm kitapların harfleri kendi kendine havada"
                    " uçuşup ansiklopediler oluşturdu denilse kim inanır?"
                ),
                "desc": (
                    "Atomların şuursuz bir şekilde kainat kitabını"
                    " yazamayacağını, arkada bir Yazar olduğunu ispatlar."
                ),
            },
            {
                "category": "Peygamberlik",
                "title": "Mu'cize-i Ahmediye",
                "text": (
                    "Peygamberlerin mucizeleri, insanlığın aciz kaldığı"
                    " noktalarda ilahi kudretin imdat elidir."
                ),
                "desc": (
                    "Deistlerin peygamberleri inkâr eden mantıksızlığına karşı"
                    " nebevi rehberliğin zaruretini açıklar."
                ),
            },
            {
                "category": "Tevhid",
                "title": "Çiçekler ve Sinekler Fabrikası",
                "text": (
                    "Baharda yeryüzü tezgahında dokunan binbir çeşit çiçek"
                    " halıları, şuursuz toprak ve suyun kendi eseri olamaz."
                ),
                "desc": (
                    "Tabiatçıların 'tabiat yaptı' hurafesini 'Tabiat bir"
                    " matbaadır, nakkaş değil basıcıdır' diyerek çözer."
                ),
            },
            {
                "category": "Nizam",
                "title": "Kahve Değirmeni ve Nizam",
                "text": (
                    "Nizam ve intizam olan yerde mutlaka irade ve ilim vardır."
                    " Kendi kendine dönen bir değirmen bile ustanın eseridir."
                ),
                "desc": (
                    "Fizik kanunlarının şuursuz iradesiz olmadığını, arkada"
                    " ilahi irade bulunduğunu açıklar."
                ),
            },
            {
                "category": "İlahi İsimler",
                "title": "Esma-i Hüsna Aynaları",
                "text": (
                    "Kainat, Allah'ın güzel isimlerinin (Hâlık, Rezzak,"
                    " Musavvir) göründüğü muazzam bir aynalar mecmuasıdır."
                ),
                "desc": (
                    "Ateistlerin 'Neden yaratıldı?' sorusuna ilahi isimlerin"
                    " tecellisiyle cevap verir."
                ),
            },
            {
                "category": "Ahiret",
                "title": "Ölüm ve Diriliş (Haşir Risalesi)",
                "text": (
                    "Sonbaharda ağaçların ölmesi ve ilkbaharda aynen"
                    " dirilmesi, insanın da ölümden sonra dirileceğinin"
                    " delilidir."
                ),
                "desc": (
                    "Öldükten sonra dirilişin akli ve gözle görülür delillerini"
                    " sunar."
                ),
            },
            {
                "category": "Sanat",
                "title": "Göz ve Kamera Temsili",
                "text": (
                    "İnsan yapımı en gelişmiş kamera bile gözün yanındaki"
                    " muazzam işlevin yanında oyuncak kalır."
                ),
                "desc": (
                    "Biyolojik organlardaki mucizevi tasarımı gözler önüne"
                    " serer."
                ),
            },
        ],
    }
else:
    t = {
        "sidebar_title": "🛡️ Creed Compendium",
        "sidebar_sub": "Defense Against Atheism & Deism",
        "nav": "Navigation",
        "menu": [
            "Overview & Summary",
            "Quranic Verses (20+)",
            "Verses Pertaining to the Prophet (Diyanet)",
            "Hadiths (20+)",
            "Islamic Scholars (20+)",
            "Risale-i Nur Examples (20+)",
            "Movement Analysis & Refutation",
            "Legal Notice & Terms",
        ],
        "search_label": "Global Search",
        "search_ph": "Search verse, hadith, scholar or concept...",
        "sleep_note": (
            "💡 *Note:* This web application is hosted on free servers. If"
            " left idle for a long time, the app may go to sleep mode ('Zzzz'"
            " icon may appear).\n\n💤 If you encounter such a screen, click"
            " the blue 'Yes, get this app back up!' button and wait 15-30"
            " seconds for the app to wake up."
        ),
        "main_title": (
            "Scientific Truths Against Atheism, Deism, and Materialism"
        ),
        "main_desc": (
            "This application offers a complete compendium of defense against"
            " modern denialist claims regarding the universe, life, and the"
            " soul through Quranic verses with their sources, prophetic"
            " tradition, and deep theological views."
        ),
        "scope_title": "🎯 Application Scope",
        "scope_desc": (
            "- *Quranic Evidence:* Verses directly proving order and creation"
            " in the universe.\n- *Verses on the Prophet:* Verses addressing and"
            " honoring Prophet Muhammad (pbuh) according to Diyanet"
            " translation.\n- *Prophetic Wisdom:* The Prophet's statements"
            " directing towards contemplation and faith.\n- *Scholars' Views:*"
            " Philosophical refutations by figures such as Ghazali, Avicenna,"
            " and Imam Rabbani.\n- *Risale-i Nur Allegories:* Magnificent"
            " examples opening the door to reason."
        ),
        "c_ayet": "Quranic Verse",
        "c_hz_ayet": "Verse Pertaining to Prophet Muhammad (pbuh)",
        "c_hadis": "Hadith",
        "c_alim": "Islamic Scholar",
        "c_nursi": "Risale-i Nur Example",
        "analysis_label": "Scientific Analysis",
        "wisdom_label": "Wisdom",
        "conclusion_label": "Conclusion",
        "section_ayet_title": (
            "📖 Quranic Verses on Tawhid and Creation (with Meanings & Sources)"
        ),
        "section_ayet_desc": (
            "Over 20 verses, their meanings, and analyses fundamentally"
            " shaking the claims of atheism, deism, and materialism."
        ),
        "section_hz_ayet_title": (
            "📜 Verses Pertaining to Prophet Muhammad (pbuh) According to Diyanet"
            " Translation"
        ),
        "section_hz_ayet_desc": (
            "Approved verses by the Presidency of Religious Affairs directly"
            " addressing, honoring, and verifying the mission of Prophet"
            " Muhammad (pbuh) in the Quran."
        ),
        "section_hadis_title": (
            "📜 Hadiths and Realities of Faith (with Sources)"
        ),
        "section_hadis_desc": (
            "Statements of Prophet Muhammad (PBUH) concerning creation and the"
            " Creator of the universe with their sources (20+ Hadiths)."
        ),
        "section_alim_title": "🎓 Views of Islamic Scholars",
        "section_alim_desc": (
            "Philosophical and theological evidence put forward by great"
            " Islamic scholars against denialist movements (20+ Scholars)."
        ),
        "section_nursi_title": "💡 Allegories of Bediuzzaman Said Nursi",
        "section_nursi_desc": (
            "20 magnificent Risale evidence items such as Resurrection,"
            " Kasr-ı Nur, and the Factory allegory."
        ),
        "section_akim_title": (
            "⚖️ Argument Comparison Table Against Movements"
        ),
        "section_akim_desc": (
            "Basic claims of atheism, deism, and materialism alongside"
            " scientific answers of Islamic faith."
        ),
        "table_columns": [
            "Movement",
            "Main Claim",
            "Islamic & Rational Answer",
            "Related Scholar / Approach",
        ],
        "legal_title": "⚖️ Legal Notice and Terms of Use",
        "legal_text": (
            "**For Information Sharing Purposes Only:** All contents,"
            " articles, compilations, and software presented in this"
            " application are provided solely for informational, academic"
            " research, and spiritual development purposes.\n\n**Prohibition"
            " of Commercial Activity:** This work and its modules cannot be"
            " traded, sold for any commercial purpose, offered for use for a"
            " fee, or used as a tool for commercial gain on other"
            " platforms.\n\n**Copying Prohibition and Copyright:** Due to"
            " security and copyright policies, no text, code, or data on the"
            " screen can be copied, reproduced, or transferred to another"
            " medium without permission.\n\n© All Rights Reserved. All"
            " copyright and intellectual property rights are reserved."
        ),
        "footer": (
            "© 2026 Creed Compendium | For informational purposes only. Cannot"
            " be traded or copied. All rights reserved."
        ),
        "ayetler": [
            {
                "ref": "Surah Al-Baqarah, 117",
                "title": "Creation of the Universe from Nothing",
                "text": (
                    "He is the Originator of the heavens and the earth. When He"
                    " decrees a matter, He simply says to it, 'Be!' and it"
                    " is."
                ),
                "desc": (
                    "Radically refutes materialism's claim of the eternity of"
                    " matter."
                ),
            },
            {
                "ref": "Surah At-Tur, 35-36",
                "title": "The Impossibility of Chance",
                "text": (
                    "Or were they created by nothing, or are they [their own]"
                    " creators? Or did they create the heavens and the"
                    " earth?"
                ),
                "desc": (
                    "A rational challenge against the thesis of atheists and"
                    " naturalists that the universe formed by chance."
                ),
            },
            {
                "ref": "Surah Al-Anbiya, 30",
                "title": "The Miracle of Cell and Life",
                "text": (
                    "Have those who disbelieved not considered that the"
                    " heavens and the earth were a joined entity, then We"
                    " separated them and made from water every living"
                    " thing?"
                ),
                "desc": (
                    "Emphasizes that life is designed with a divine program"
                    " against biological materialism."
                ),
            },
            {
                "ref": "Surah Al-Mulk, 3-4",
                "title": "Flawless Order in the Heavens",
                "text": (
                    "[He] who created seven heavens in layers. You do not see"
                    " in the creation of the Most Merciful any inconsistency."
                    " So return [your] vision [to the sky]; do you see any"
                    " breakage?"
                ),
                "desc": (
                    "Shows the continuous supervision of Lordship against the"
                    " deist view that 'God created the universe and left it'."
                ),
            },
            {
                "ref": "Surah Yunus, 6",
                "title": "The Order of Night and Day",
                "text": (
                    "Indeed, in the alternation of night and day and [in]"
                    " what Allah has created in the heavens and the earth are"
                    " signs for a people who fear Allah."
                ),
                "desc": (
                    "Proves that sensitive astronomical balances in the"
                    " universe cannot be left to blind chances."
                ),
            },
            {
                "ref": "Surah An-Nahl, 68-69",
                "title": "Divine Inspiration in the Bee",
                "text": (
                    "And your Lord inspired to the bee, 'Take among the"
                    " mountains, houses and among the trees and [in] what"
                    " they construct...'"
                ),
                "desc": (
                    "Shows that instinct is actually a divine law and design."
                ),
            },
            {
                "ref": "Surah At-Tin, 4",
                "title": "The Perfect Creation of Man",
                "text": (
                    "We have certainly created man in the best of stature"
                    " (ahsen-i takvim)."
                ),
                "desc": (
                    "Emphasizes that human physical and spiritual equipment"
                    " is not a work of chance."
                ),
            },
            {
                "ref": "Surah An-Naba, 6-7",
                "title": "The Balancing Role of Mountains",
                "text": (
                    "Have We not made the earth a resting place? And the"
                    " mountains as pegs?"
                ),
                "desc": (
                    "Explains that geological balances are designed to make"
                    " life on earth possible."
                ),
            },
            {
                "ref": "Surah Ar-Rum, 48",
                "title": "Winds and Rain",
                "text": (
                    "It is Allah who sends the winds, and they stir the"
                    " clouds and spread them in the sky however He wills..."
                ),
                "desc": (
                    "Brings to light the divine will behind physical laws in"
                    " the ecosystem."
                ),
            },
            {
                "ref": "Surah Ar-Rahman, 19-20",
                "title": "The Barrier Between Seas",
                "text": (
                    "He released the two seas, meeting [side by side]; Between"
                    " them is a barrier so neither of them transgresses."
                ),
                "desc": (
                    "Reports the wisdom of different salinity and density"
                    " barriers in oceans."
                ),
            },
            {
                "ref": "Surah Al-An'am, 97",
                "title": "Stars and Navigation",
                "text": (
                    "And it is He who placed for you the stars that you may"
                    " be guided by them through the darkness of the land and"
                    " sea."
                ),
                "desc": (
                    "Shows that every element in the universe is planned to"
                    " serve humanity."
                ),
            },
            {
                "ref": "Surah Al-Hajj, 5",
                "title": "Resurrection of the Earth",
                "text": (
                    "O people, if you should be in doubt about the"
                    " Resurrection, then indeed, We created you from dust..."
                ),
                "desc": (
                    "Rationally proves life after death through the"
                    " revitalization of the earth every spring."
                ),
            },
            {
                "ref": "Surah Al-Furqan, 47",
                "title": "Night as a Covering",
                "text": (
                    "And it is He who has made the night for you as clothing"
                    " and sleep [a means for] rest and has made the day"
                    " resurrection."
                ),
                "desc": "Declares the harmony of human biology with cosmic rhythms.",
            },
            {
                "ref": "Surah Al-An'am, 38",
                "title": "Animals as Communities",
                "text": (
                    "And there is no creature on [or within] the earth or bird"
                    " that flies with its wings except [that they are]"
                    " communities like you..."
                ),
                "desc": (
                    "States that all living beings are under the knowledge of"
                    " the Creator."
                ),
            },
            {
                "ref": "Surah Adh-Dhariyat, 47",
                "title": "Expansion of the Universe",
                "text": (
                    "And the heaven We constructed with strength, and indeed,"
                    " We are [its] expander."
                ),
                "desc": (
                    "Quran's indication of modern astrophysics' theory of the"
                    " expansion of the universe."
                ),
            },
            {
                "ref": "Surah Ar-Rum, 22",
                "title": "Diversity of Languages and Colors",
                "text": (
                    "And of His signs is the creation of the heavens and the"
                    " earth and the diversity of your languages and your"
                    " colors..."
                ),
                "desc": (
                    "Emphasizes the miracle of divine art in human diversity."
                ),
            },
            {
                "ref": "Surah Al-Qiyamah, 14",
                "title": "Conscience and Testimony",
                "text": "Man, against himself, will be a witness.",
                "desc": (
                    "Expresses the spiritual structure of conscience that"
                    " rejects materialistic reductionism."
                ),
            },
            {
                "ref": "Surah Ar-Ra'd, 28",
                "title": "Satisfaction of Hearts",
                "text": (
                    "Unquestionably, by the remembrance of Allah hearts are"
                    " assured."
                ),
                "desc": (
                    "Reports that the spiritual void brought by deist or atheist"
                    " lifestyles will be filled with faith."
                ),
            },
            {
                "ref": "Surah Hud, 6",
                "title": "Guarantor of Provision",
                "text": (
                    "And there is no creature on earth but that upon Allah is"
                    " its provision..."
                ),
                "desc": (
                    "Proves that laws of nature belong to a Merciful Being,"
                    " not blind forces."
                ),
            },
            {
                "ref": "Surah Ali 'Imran, 190",
                "title": "Evidence for Those Who Reason",
                "text": (
                    "Indeed, in the creation of the heavens and the earth and"
                    " the alternation of the night and the day are signs for"
                    " those of understanding."
                ),
                "desc": (
                    "Outlines the path of scientific observation leading to"
                    " faith."
                ),
            },
        ],
        "hadisler": [
            {
                "ref": "Bukhari, Beginning of Creation",
                "title": "Eternity of Creation",
                "text": "Allah existed and nothing existed before Him...",
                "desc": (
                    "Expresses that matter is not eternal and the existence"
                    " of everything relies on Allah."
                ),
            },
            {
                "ref": "Bukhari, Funerals",
                "title": "Birth Upon Fitrah",
                "text": (
                    "Every newborn is born upon the fitrah (pure disposition"
                    " inclined to recognize Allah)..."
                ),
                "desc": (
                    "Shows that the potential to seek a Creator is innate in"
                    " human nature."
                ),
            },
            {
                "ref": "Tirmidhi, Supplications",
                "title": "Asma-ul Husna and Knowledge",
                "text": (
                    "Allah has 99 names; whoever memorizes them, comprehends"
                    " their meaning, and applies them enters Paradise."
                ),
                "desc": (
                    "Teaches that every work in the universe is a mirror of"
                    " Allah's beautiful names."
                ),
            },
            {
                "ref": "Tirmidhi, Zuhd",
                "title": "Provision and Tawakkul",
                "text": (
                    "If you were to rely upon Allah with the reliance due"
                    " upon Him, He would provide for you just as He provides"
                    " for the birds."
                ),
                "desc": (
                    "Reports that there is an active Generous Lord behind"
                    " natural laws."
                ),
            },
            {
                "ref": "Ibn Majah, Introduction",
                "title": "Seeking Knowledge",
                "text": "Seeking knowledge is an obligation upon every Muslim.",
                "desc": (
                    "Emphasizes that examining the universe is the greatest"
                    " means to strengthen faith."
                ),
            },
            {
                "ref": "Acluni, Kashf al-Hafa",
                "title": "Contemplating Creation",
                "text": (
                    "Contemplate upon the creation of Allah, but do not"
                    " contemplate upon the Essence of Allah."
                ),
                "desc": (
                    "Draws rational boundaries against the superstitious"
                    " question of atheists: 'Who created God?'"
                ),
            },
            {
                "ref": "Muslim, Travelers",
                "title": "Prayer and Mi'raj",
                "text": "Prayer is the Mi'raj of the believer.",
                "desc": (
                    "Opens the way to step outside the material world and"
                    " establish a spiritual connection with the Creator."
                ),
            },
            {
                "ref": "Musnad Ahmad",
                "title": "Evidence of Unity in Everything",
                "text": "In everything there is a sign testifying to His oneness.",
                "desc": (
                    "Reports that everything in the universe points to a"
                    " Single Unique God (Wahid-i Ahad)."
                ),
            },
            {
                "ref": "Muslim, Birr",
                "title": "Voices of Conscience",
                "text": (
                    "Righteousness is good character, and wrongdoing is that"
                    " which wavers in your soul and which you dislike people"
                    " to know about."
                ),
                "desc": (
                    "Shows the unshakability of universal conscience against"
                    " materialistic moral views."
                ),
            },
            {
                "ref": "Tirmidhi, Zuhd",
                "title": "Treasure of Contentment",
                "text": "Contentment is an inexhaustible treasure.",
                "desc": (
                    "Provides spiritual satisfaction against materialistic"
                    " ambition and consumption frenzy."
                ),
            },
            {
                "ref": "Tirmidhi, Zuhd 26",
                "title": "World and Hereafter",
                "text": "The world is the seedbed of the Hereafter.",
                "desc": (
                    "The purposeful creation principle proving that life is"
                    " not limited to matter and the other realm exists."
                ),
            },
            {
                "ref": "Bukhari, Knowledge",
                "title": "Withdrawing of Knowledge",
                "text": (
                    "The decrease of knowledge and increase of ignorance are"
                    " among the signs of the Day of Judgment."
                ),
                "desc": (
                    "Draws attention to end-time movements where truth is"
                    " attempted to be concealed."
                ),
            },
            {
                "ref": "Bukhari, Manners",
                "title": "Mercy",
                "text": "He who does not show mercy will not be shown mercy.",
                "desc": (
                    "Islam's civilization of compassion against the ruthless"
                    " Darwinist claim 'survival of the fittest'."
                ),
            },
            {
                "ref": "Tirmidhi, Birr",
                "title": "Good Character",
                "text": (
                    "The most perfect of the believers in faith are those with"
                    " the best character."
                ),
                "desc": "Shows the practical and moral reflection of faith.",
            },
            {
                "ref": "Bayhaqi, Shu'ab al-Iman",
                "title": "Value of Contemplation",
                "text": (
                    "An hour of contemplation is better than a year of"
                    " worship."
                ),
                "desc": (
                    "Emphasizes the value of looking at the universe with"
                    " insight and examining scientific evidence."
                ),
            },
            {
                "ref": "Tirmidhi, Supplications",
                "title": "Essence of Supplication",
                "text": "Supplication is worship itself.",
                "desc": (
                    "The divine address belief refuting the deist view that"
                    " 'God does not hear prayers'."
                ),
            },
            {
                "ref": "Muslim, Birr 34",
                "title": "Place of God-consciousness",
                "text": "Taqwa is right here (pointing to his heart).",
                "desc": (
                    "Reports the importance of heart and spiritual"
                    " comprehension beyond material measurements."
                ),
            },
            {
                "ref": "Abu Dawud, Malahim",
                "title": "Truthful Word",
                "text": (
                    "The greatest jihad is speaking a word of truth in front"
                    " of an unjust ruler."
                ),
                "desc": "The stance of truth struggle against denialist movements.",
            },
            {
                "ref": "Bukhari, Riqaq",
                "title": "Value of Time",
                "text": (
                    "Two blessings which many people are deceived into losing:"
                    " health and free time."
                ),
                "desc": (
                    "Reminds that life must be lived purposefully and"
                    " productively."
                ),
            },
            {
                "ref": "Bukhari, Manners",
                "title": "Brotherhood",
                "text": "A Muslim is the brother of a Muslim...",
                "desc": (
                    "Social solidarity spirit against individualistic and"
                    " egoistic materialistic philosophies."
                ),
            },
        ],
        "alimler": [
            {
                "name": "Imam al-Ghazali",
                "work": "Tahafut al-Falasifa (Incoherence of the Philosophers)",
                "view": (
                    "Refuted the philosophers' claims of the eternity of the"
                    " universe with rational and logical evidence."
                    " Emphasized the importance of heart vision."
                ),
            },
            {
                "name": "Rumi (Jalal al-Din Rumi)",
                "work": "Mathnawi",
                "view": (
                    "Elaborated on the divine order in the universe with deep"
                    " philosophy by stating, 'Every atom testifies to the"
                    " existence of an artist'."
                ),
            },
            {
                "name": "Ibn Arabi",
                "work": "Futuhat al-Makkiyya",
                "view": (
                    "Proved through the perspective of Wahdat al-Wujud"
                    " (Oneness of Being) that everything in the universe is a"
                    " manifestation of the divine names."
                ),
            },
            {
                "name": "Imam Rabbani",
                "work": "Maktubat (Letters)",
                "view": (
                    "Strongly rejected the naturalists' claims that 'nature"
                    " creates by itself' and defended that nature is merely a"
                    " veil."
                ),
            },
            {
                "name": "Al-Farabi",
                "work": "Ihsan al-Ulum",
                "view": (
                    "Foundationalized the existence of Allah as a logical"
                    " necessity through the concept of Wajib al-Wujud (Necessary"
                    " Existent)."
                ),
            },
            {
                "name": "Avicenna (Ibn Sina)",
                "work": "Kitab al-Shifa (The Book of Healing)",
                "view": (
                    "Proved through his famous 'Flying Man' thought experiment"
                    " that the soul is an independent substance separate from"
                    " matter."
                ),
            },
            {
                "name": "Averroes (Ibn Rushd)",
                "work": "Tahafut al-Tahafut",
                "view": (
                    "Defended evidence of providence and invention in the"
                    " universe, showing that philosophy and religion unite in"
                    " truth."
                ),
            },
            {
                "name": "Shah Waliullah Dehlawi",
                "work": "Hujjatullah al-Baligha",
                "view": (
                    "Presented Islam's rational foundations and wisdom to the"
                    " understanding of the age, writing refutations against"
                    " social denialist movements."
                ),
            },
            {
                "name": "Katip Çelebi",
                "work": "Mizan al-Hakk",
                "view": (
                    "Defended that scientific developments do not contradict"
                    " religious truths, but rather strengthen faith."
                ),
            },
            {
                "name": "Abu Mansur al-Maturidi",
                "work": "Kitab al-Tawhid",
                "view": (
                    "Established that humans can find the existence of Allah"
                    " through reason, emphasizing the balance of reason and"
                    " revelation."
                ),
            },
            {
                "name": "Abu Hasan al-Ash'ari",
                "work": "Al-Luma'",
                "view": (
                    "Proved through atomistic theory that substances are in"
                    " constant need of creation."
                ),
            },
            {
                "name": "Imam Suyuti",
                "work": "Al-Itqan fi Ulum al-Quran",
                "view": (
                    "Compiled scientific and literary miracles of the Quran,"
                    " presenting the greatest evidence against deniers."
                ),
            },
            {
                "name": "Abdul Qadir al-Jilani",
                "work": "Jala al-Khawatir",
                "view": (
                    "Presented the spiritual depths of the heart and the recipe"
                    " for salvation from materialistic ambitions."
                ),
            },
            {
                "name": "Hasan al-Basri",
                "work": "Rasail (Treatises)",
                "view": (
                    "Conducted deep theological analyses on human free will"
                    " and the divine order of justice in the universe."
                ),
            },
            {
                "name": "Ibrahim of Beirut",
                "work": "Treatises on Kalam",
                "view": (
                    "Defended the supremacy of divine power against natural"
                    " philosophy."
                ),
            },
            {
                "name": "Sayyid Sharif al-Jurjani",
                "work": "Sharifiyyah",
                "view": (
                    "Brought to light the ontological impasses of"
                    " materialism in the philosophy of existence and"
                    " non-existence."
                ),
            },
            {
                "name": "Taftazani",
                "work": "Sharh al-Aqaid",
                "view": (
                    "Ensured the defense of Islamic creed with the most"
                    " robust rational evidence."
                ),
            },
            {
                "name": "Jalal al-Din al-Mahalli",
                "work": "Tafsir al-Jalalayn",
                "view": (
                    "Brought creation evidence in verses to the present day in"
                    " the most concise manner."
                ),
            },
            {
                "name": "Al-Zamakhshari",
                "work": "Al-Kashshaf",
                "view": (
                    "Proved that the eloquence of the Quran is super-human and"
                    " cannot be explained by chance."
                ),
            },
            {
                "name": "Ibn Qayyim al-Jawziyya",
                "work": "Miftah Dar al-Sa'ada",
                "view": (
                    "Rejected atheism by examining in detail the wisdoms in"
                    " the universe and miracles in medicine/biology."
                ),
            },
        ],
        "nursi": [
            {
                "category": "Resurrection & Creation",
                "title": (
                    "The Magnificent Palace and Letters (Kasr-ı Nur)"
                ),
                "text": (
                    "A guest coming to a huge palace sees that everything"
                    " inside is in harmony. He says, 'This palace cannot be"
                    " ownerless'."
                ),
                "desc": (
                    "Proves that the universe is a grand palace, man is a"
                    " guest, and the order cannot be a coincidence."
                ),
            },
            {
                "category": "Artist & Art",
                "title": "The Allegory of the Marvelous Factory",
                "text": (
                    "Imagine a colossal factory producing everything. Is it"
                    " not contrary to reason to say that irons in this factory"
                    " came together by themselves to establish it?"
                ),
                "desc": (
                    "Proves that biological cells and the factory of living"
                    " beings cannot form through blind coincidences."
                ),
            },
            {
                "category": "Book of Universe",
                "title": "The Enormous Book and Letters",
                "text": (
                    "Who would believe if it were said that the letters of all"
                    " books in a library flew in the air by themselves and"
                    " formed encyclopedias?"
                ),
                "desc": (
                    "Proves that atoms cannot unconsciously write the book of"
                    " the universe and that there is an Author behind it."
                ),
            },
            {
                "category": "Prophethood",
                "title": "The Miracle of Ahmad (PBUH)",
                "text": (
                    "The miracles of prophets are the helping hand of divine"
                    " power at points where humanity is helpless."
                ),
                "desc": (
                    "Explains the necessity of prophetic guidance against the"
                    " irrationality of deists denying prophets."
                ),
            },
            {
                "category": "Tawhid (Oneness)",
                "title": "Factory of Flowers and Flies",
                "text": (
                    "The thousands of varieties of flower carpets woven on the"
                    " loom of earth in spring cannot be the work of"
                    " unconscious soil and water."
                ),
                "desc": (
                    "Resolves the superstition of naturalists that 'nature"
                    " made it' by stating, 'Nature is a printing press, not"
                    " the printer'."
                ),
            },
            {
                "category": "Order",
                "title": "Coffee Grinder and Order",
                "text": (
                    "Where there is order and discipline, there is certainly"
                    " will and knowledge. Even a self-rotating mill is the work"
                    " of a master."
                ),
                "desc": (
                    "Explains that physical laws are not unconscious and"
                    " will-less, and that there is divine will behind them."
                ),
            },
            {
                "category": "Divine Names",
                "title": "Mirrors of Asma-ul Husna",
                "text": (
                    "The universe is a magnificent collection of mirrors"
                    " where Allah's beautiful names (Al-Khaliq, Al-Razzaq,"
                    " Al-Musawwir) are manifested."
                ),
                "desc": (
                    "Answers the atheists' question 'Why was it created?'"
                    " through the manifestation of divine names."
                ),
            },
            {
                "category": "Hereafter",
                "title": "Death and Resurrection (Treatise on Resurrection)",
                "text": (
                    "The death of trees in autumn and their exact"
                    " resurrection in spring is evidence that man will also"
                    " be resurrected after death."
                ),
                "desc": (
                    "Presents rational and visible evidence for resurrection"
                    " after death."
                ),
            },
            {
                "category": "Art",
                "title": "Representation of Eye and Camera",
                "text": (
                    "Even the most advanced man-made camera remains a toy"
                    " compared to the magnificent function alongside the eye."
                ),
                "desc": "Brings miraculous design in biological organs to light.",
            },
            {
                "category": "Power",
                "title": "Miracle of Acid and Seed",
                "text": (
                    "The power that fits the program of a giant tree inside a"
                    " tiny seed belongs only to the All-Powerful Being."
                ),
                "desc": (
                    "Proves the divine knowledge behind DNA and genetic"
                    " codes."
                ),
            },
            {
                "category": "Faith & Disbelief",
                "title": "Story of Two Travelers",
                "text": (
                    "During a journey, one of two travelers gives everything"
                    " to its owner and finds peace, while the other attributes"
                    " everything to nature and suffers torment."
                ),
                "desc": (
                    "Compares the peace of believers with the psychological"
                    " depression of deniers."
                ),
            },
            {
                "category": "Rububiyyah (Lordship)",
                "title": "Captain and the Passenger on the Ship",
                "text": (
                    "Can a colossal ship swim in a stormy sea without a"
                    " captain and a helm? The ship of the universe cannot be"
                    " ownerless either."
                ),
                "desc": "Explains perfection in the management of the universe.",
            },
            {
                "category": "Nature",
                "title": "Soup Cauldron and Nature",
                "text": (
                    "What they call nature is merely a manifestation ledger"
                    " of divine art; it is created, not creating."
                ),
                "desc": "Destroys the fundamental fallacy of naturalism.",
            },
            {
                "category": "Eternity",
                "title": "Infinite Capacities of Man",
                "text": (
                    "Man has an infinite desire for paradise. The mortal"
                    " world cannot satisfy these desires; therefore, there"
                    " is an eternal realm."
                ),
                "desc": (
                    "Proves that human spiritual structure demands the"
                    " hereafter."
                ),
            },
            {
                "category": "Essence of Majesty",
                "title": "Duty of Particles",
                "text": (
                    "Every particle is like a soldier acting by the command"
                    " of the Lord. They work in harmony like armies."
                ),
                "desc": "Explains the flawless order in the subatomic world.",
            },
            {
                "category": "Scientific Evidence",
                "title": "Confession of the Western Philosopher",
                "text": (
                    "The confession of some honest Western philosophers that"
                    " the universe cannot be explained by chance."
                ),
                "desc": (
                    "Emphasizes objective science approaching faith."
                ),
            },
            {
                "category": "Supplication",
                "title": "Infinite Needs and Helplessness",
                "text": (
                    "Man has infinite needs and helplessness. Thus, he must"
                    " seek refuge in a Refuge Who is capable of everything."
                ),
                "desc": (
                    "Analyzes human psychology that cannot live without"
                    " supplication."
                ),
            },
            {
                "category": "Soul",
                "title": "Dream and Relativity of Time",
                "text": (
                    "Seeing years of dreams in a few seconds during sleep"
                    " shows that the soul is not bound to matter."
                ),
                "desc": "Refutes materialist denial of the soul.",
            },
            {
                "category": "Blessing",
                "title": "Bee, Silkworm, and Cow",
                "text": (
                    "The cow giving milk and the bee giving honey are divine"
                    " officials; they cannot know this art themselves."
                ),
                "desc": (
                    "Reports that marvelous production in animals is a grant"
                    " from the Creator."
                ),
            },
            {
                "category": "Order",
                "title": "Sun Stove and Universe Lamp",
                "text": (
                    "The Being Who made the sun our stove warming our world"
                    " and night our quilt is capable of everything."
                ),
                "desc": (
                    "Proves that ecological balance in the universe is a"
                    " work of mercy."
                ),
            },
        ],
    }

# ----------------- SIDEBAR KONTROLÜ -----------------
st.sidebar.markdown(f"# {t['sidebar_title']}")
st.sidebar.markdown(f"### {t['sidebar_sub']}")

menu = st.sidebar.radio(t["nav"], t["menu"])

st.sidebar.markdown("---")
search_query = st.sidebar.text_input(
    t["search_label"], placeholder=t["search_ph"]
)

st.sidebar.markdown("---")
st.sidebar.info(t["sleep_note"])

# ----------------- İÇERİK EKRANLARI -----------------

if menu == t["menu"][0]:
    st.markdown(
        f"""
    <div class="main-header">
        <h1 style="color: white; margin-bottom: 0.5rem;">{t['main_title']}</h1>
        <p style="color: #d1fae5; font-size: 1.1rem;">{t['main_desc']}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            f'<div class="metric-card"><h3>📖 20+</h3><p'
            f' style="color:#64748b; margin:0;">{t["c_ayet"]}</p></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="metric-card"><h3>📜 20+</h3><p'
            f' style="color:#64748b; margin:0;">{t["c_hadis"]}</p></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f'<div class="metric-card"><h3>🎓 20+</h3><p'
            f' style="color:#64748b; margin:0;">{t["c_alim"]}</p></div>',
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            f'<div class="metric-card"><h3>💡 20+</h3><p'
            f' style="color:#64748b; margin:0;">{t["c_nursi"]}</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown(f"""
    ### {t['scope_title']}
    {t['scope_desc']}
    """)

elif menu == t["menu"][1]:
    st.markdown(f"## {t['section_ayet_title']}")
    st.markdown(t["section_ayet_desc"])

    # 20+ Genişletilmiş Ayet Listesi Entegrasyonu
    ayetler_genisletilmis = [
        {
            "ref": "Bakara Suresi, 164",
            "title": "Kainattaki İlahi Deliller",
            "text": "Şüphesiz göklerin ve yerin yaratılışında, gece ile gündüzün artarda gelişinde, insanlara fayda veren şeylerle denizde yürüye Allah'ın yük taşıyan gemilerinde, Allah'ın gökten indirip de ölü haldeki toprağı canlandırdığı suda, yeryüzünde her çeşit canlıyı yaymasında, rüzgarları ve gökle yer arasında emre amade bekleyen bulutları döndürmesinde düşünen bir topluluk için elbette deliller vardır.",
            "desc": "Kainattaki her bir nizam ve intizam, tesadüfe yer bırakmayacak derecede usta bir Yaratıcı'nın varlığını ve birliğini açıkça ilan eder.",
        },
        {
            "ref": "Âl-i İmrân Suresi, 190-191",
            "title": "Göklerin ve Yerin Yaratılışı",
            "text": "Şüphesiz göklerin ve yerin yaratılışında, gece ile gündüzün değişmesinde akıl sahipleri için ibretler vardır. Onlar ayaktayken, otururken, yanları üzerine yatarken Allah'ı zrederler; göklerin ve yerin yaratılışı üzerinde düşünürler.",
            "desc": "Hakiki ilim ve iman, kainat kitabını dikkatle okumaktan ve tesadüf inancını aklen reddetmekten geçer.",
        },
        {
            "ref": "Rûm Suresi, 22",
            "title": "Yaratılıştaki Çeşitlilik",
            "text": "Göklerin ve yerin yaratılması, dillerinizin ve renklerinizin farklı olması da O'nun delillerindendir. Şüphesiz bunda bilenler için ibretler vardır.",
            "desc": "İnsan kimliğindeki ve dillerindeki çeşitlilik, sonsuz bir irade ve planlamanın eseridir.",
        },
        {
            "ref": "Mülk Suresi, 3-4",
            "title": "Kainattaki Kusursuzluk",
            "text": "O, birbiriyle uyumlu yedi göğü yaratmıştır. Rahman'ın yaratmasında hiçbir uyumsuzluk göremezsin. Gözünü çevir de bak, bir bozukluk görüyor musun? Sonra gözünü tekrar tekrar çevir bak; göz aradığını bulamamış ve yorgun olarak sana dönecektir.",
            "desc": "Kainatta hiçbir kusur, çelişki veya başıboşluk yoktur; her şey hikmetle ve muazzam bir ölçüyle kurulmuştur.",
        },
        {
            "ref": "Nahl Suresi, 68-69",
            "title": "Arı Mucizesi ve İlahi Program",
            "text": "Rabbin bal arısına: 'Dağlardan, ağaçlardan ve insanların kurdukları çardaklardan kendine evler edin, sonra her türlü meyveden ye, sonra da Rabbinin sana kolaylaştırdığı yollara boyun eğerek gir' diye ilham etti. Onların karınlarından çeşitli renklerde bir şurup çıkar ki, onda insanlar için şifa vardır. Şüphesiz bunda düşünen bir topluluk için kesin bir ibret vardır.",
            "desc": "Küçük bir böceğe ilham edilen bu devasa organizasyon, tabiatın değil, mutlak bir İrade sahibinin işidir.",
        },
        {
            "ref": "Zâriyât Suresi, 20-21",
            "title": "Kainatta ve Nefislerdeki Ayetler",
            "text": "Yeryüzünde kesin olarak inananlar için ibretler vardır. Kendi nefislerinizde de öyle. Hâlâ görmüyor musunuz?",
            "desc": "İnsanın kendi iç dünyasındaki ruhî, kalbî ve biyolojik mucizeler Allah'ı tanıttıran en büyük delillerdendir.",
        },
        {
            "ref": "Fâtır Suresi, 27-28",
            "title": "Renk Çeşitliliği ve İlim",
            "text": "Görmedin mi Allah gökten su indirdi. Onunla renkleri çeşit çeşit meyveler çıkardık. Dağlarda da yollar, beyaz, kırmızı, değişik renklerde ve simsiyah katmanlar vardır. İnsanlardan, hareketli canlılardan ve hayvanlardan da yine böyle türlü renkte olanlar vardır. Kulleri içinde ancak alimler, Allah'ın büyüklüğünü derinden hissederler.",
            "desc": "Bilim ve fen, kainattaki hakikatleri keşfettikçe Yaratıcı'nın azametini daha iyi anlar.",
        },
        {
            "ref": "Yâsîn Suresi, 33-40",
            "title": "Ölü Toprağın Canlanması ve Yörüngeler",
            "text": "Ölü toprak onlar için bir delildir; biz onu dirilttik, ondan taneler çıkardık da ondan yemektedirler... Güneş de yörüngesinde akıp gitmektedir. Bu, mutlak güç sahibi, hakkıyla bilen Allah'ın takdiridir.",
            "desc": "Güneşin ve ayın hassas dengelerle hareket etmesi, kör tesadüflerin değil, şuur ve kudretin sonucudur.",
        },
        {
            "ref": "Hacc Suresi, 73",
            "title": "Sinek Misali ve Acizlik",
            "text": "Ey insanlar! Bir misal verildi; şimdi onu dinleyin: Allah'ı bırakıp da yalvardıklarınız, hepsi bir araya gelseler bile bir sinek dahi yaratamazlar. Sinek onlardan bir şey kopsa, bunu ondan kurtaramazlar. İsteyen de aciz, istenen de.",
            "desc": "Madde ve tabiatın kendi kendine ilahlaşamayacağını, her şeyin mutlak bir kudrete muhtaç olduğunu bildirir.",
        },
        {
            "ref": "En'âm Suresi, 59",
            "title": "Gaybın Anahtarları",
            "text": "Gaybın anahtarları O'nun katındadır, onları O'ndan başkası bilmez. Karada ve denizde olanları bilir. O'nun ilmi dışında bir yaprak bile düşmez...",
            "desc": "Kainattaki her bir zerre, ilâhî ilim ve gözetim altındadır.",
        },
        {
            "ref": "Tâhâ Suresi, 50",
            "title": "Yaratılışın Gayesi",
            "text": "Musa, 'Bizim Rabbimiz, her şeye yaratılışını veren, sonra da yolunu gösterendir' dedi.",
            "desc": "Her varlığa ne yapacağı, nasıl yaşayacağı ilahi bir programla önceden tayin edilmiştir.",
        },
        {
            "ref": "İsrâ Suresi, 44",
            "title": "Kainatın Tesbihi",
            "text": "Yedi gök, yer ve bunlarda bulunanlar O'nu tesbih ederler. O'nu övgü ile tesbih etmeyen hiçbir şey yoktur. Ne var ki siz onların tesbihini anlamazsınız. O, halimdir, çok bağışlayandır.",
            "desc": "Kainattaki her varlık kendi lisan-ı hal ile Yaratıcı'sını zikreder ve anar.",
        },
        {
            "ref": "Nur Suresi, 35",
            "title": "Göklerin ve Yerin Nuru",
            "text": "Allah, göklerin ve yerin nurudur...",
            "desc": "Kainattaki bütün aydınlıklar, hayat ve şuur pırıltıları O'nun nurunun tecellisidir.",
        },
        {
            "ref": "A'râf Suresi, 54",
            "title": "Yaratılış ve Emir",
            "text": "Şüphesiz sizin Rabbiniz, gökleri ve yeri altı günde yaratan, sonra Arş'a istiva eden, geceyi durmaksızın kendisini kovalayan gündüze bürüyen Allah'tır. Güneş, ay ve yıldızlar O'nun buyruğuna boyun eğmişlerdir. İyi bilin ki yaratmak da emretmek de O'na mahsustur. Alemlerin Rabbi olan Allah ne yücedir!",
            "desc": "Kainatın sahibi kimse, kanun koyucu da odur; tabiat ve madde emir kuludur.",
        },
        {
            "ref": "Câsiye Suresi, 3-4",
            "title": "Müminler İçin Deliller",
            "text": "Şüphesiz göklerde ve yerde müminler için elbette deliller vardır. Sizin yaratılışınızda ve yayılan canlılarda kesin olarak inanan bir topluluk için ibretler vardır.",
            "desc": "İman edenler kainattaki delilleri görerek yakin derecelerini artırırlar.",
        },
        {
            "ref": "Lokman Suresi, 10-11",
            "title": "Direksiz Gökler ve Dağlar",
            "text": "O, gökleri gördüğünüz gibi direksiz yaratmıştır. Yeryüzüne de sizi sarsmasın diye sabit dağlar koymuş ve orada her türlü canlıyı yaymıştır...",
            "desc": "Madde ötesinden gelen bir kudret eli olmadan bu muazzam dengeler ayakta duramaz.",
        },
        {
            "ref": "Gāfir Suresi, 64",
            "title": "Güzel Suret",
            "text": "Allah, yeryüzünü sizin için karar kılavuzu, göğü de bina yapan, size şekil verip de şeklinizi güzel kılan ve sizi temiz rızıklarla rızıklandıran Allah'tır...",
            "desc": "İnsana en mükemmel simayı ve bedeni veren O'dur.",
        },
        {
            "ref": "Kāf Suresi, 6-8",
            "title": "Göğün Donatılması",
            "text": "Üstlerindeki göğe bakmadılar mı? Onu nasıl bina ettik, onu nasıl donattık! Onda hiçbir çatlak yoktur. Yeryüzünü de döşedik, ona sabit dağlar attık ve orada göz alıcı her çift bitki bitirdik.",
            "desc": "Estetik ve kusursuz mimari, kör tesadüflerin mahsulü olamaz.",
        },
        {
            "ref": "Enbiya Suresi, 30",
            "title": "Kainatın Başlangıcı",
            "text": "İnkar edenler, göklerle yer bitişik iken onları ayırdığımızı ve her canlı şeyi sudan yarattığımızı görmediler mi? Hâlâ inanmayacaklar mı?",
            "desc": "Modern bilimin Big Bang teorisiyle doğruladığı başlangıç noktası, ilahi yaratılışın açık bir delilidir.",
        },
        {
            "ref": "Mülk Suresi, 19",
            "title": "Kuşların Uçuş Kanunları",
            "text": "Üstlerinde kanatlarını açıp kapatarak uçan kuşları görmediler mi? Onları havada ancak Rahman tutmaktadır. Şüphesiz O, her şeyi hakkıyla görendir.",
            "desc": "Aerodinamik kanunları ve yer çekimine karşı uçuş mucizesi ilahi kudretin eseridir.",
        }
    ]

    filtered = (
        [
            a
            for a in ayetler_genisletilmis
            if search_query.lower() in a["title"].lower()
            or search_query.lower() in a["text"].lower()
            or search_query.lower() in a["desc"].lower()
            or search_query.lower() in a["ref"].lower()
        ]
        if search_query
        else ayetler_genisletilmis
    )

    for item in filtered:
        st.markdown(
            f"""
        <div class="card">
            <span class="badge">{item['ref']}</span>
            <h4 style="margin-top: 0.25rem; color: #1e293b;">{item['title']}</h4>
            <div class="arabic-text">"{item['text']}"</div>
            <p style="font-size: 0.9rem; color: #475569; margin-top: 0.5rem;"><b>{t['analysis_label']}:</b> {item['desc']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

elif menu == t["menu"][2]:  # Peygamberimize Ait Ayetler (Diyanet) [YENİ BÖLÜM]
    st.markdown(f"## {t['section_hz_ayet_title']}")
    st.markdown(t["section_hz_ayet_desc"])
    st.markdown("---")

    for item in diyanet_hz_muhammed_ayetleri:
        st.markdown(f"<div class='card'>", unsafe_allow_html=True)
        st.markdown(
            f"<span class='badge'>📖 {item['sure']} - Ayet"
            f" {item['ayet_no']}</span>",
            unsafe_allow_html=True,
        )
        baslik_str = (
            item["baslik"]
            if lang == "Türkçe"
            else item.get("english_title", item["baslik"])
        )
        meal_str = item["meal"] if lang == "Türkçe" else item["english_meal"]

        st.markdown(f"### {baslik_str}")
        st.markdown(
            f"<div class='arabic-text'>\"{meal_str}\"</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<small><b>Kaynak:</b> {item['kaynak']}</small>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == t["menu"][3]:
    st.markdown(f"## {t['section_hadis_title']}")
    st.markdown(t["section_hadis_desc"])

    # 20+ Genişletilmiş Hadis Listesi Entegrasyonu
    hadisler_genisletilmis = [
        {
            "ref": "Buhârî, Tevhîd, 22",
            "title": "Yaratanın Sanatı Üzerine Düşünmek",
            "text": "Allahü Teala şöyle buyurmuştur: 'Ademoğlu beni yalanlar ki bu onun hakkı değildir; bana söver ki bu da onun hakkı yokken yaptığı şeydir. Beni yalanlaması, 'O beni ilk yarattığı gibi tekrar diriltmeyecektir' demesidir...'",
            "desc": "İnsanın ölümden sonraki dirilişi inkar etmesi, kainattaki ilk yaratılış sanatını ve hikmetini okuyamamasından kaynaklanır.",
        },
        {
            "ref": "Müslim, İman, 147",
            "title": "Kalpteki İman ve Tefekkür",
            "text": "İmanın en zayıf mertebesi, kalple buğzetmek (kötülüğü reddetmek) ve yaratılıştaki hikmetleri tefekkür etmektir.",
            "desc": "Tefekkür, kalbi uyanık tutan ve imanı takviye eden en önemli manevi ibadettir.",
        },
        {
            "ref": "Tirmizî, Zühd, 17",
            "title": "Dünya ve Ahiret Dengesi",
            "text": "Dünya ahirete göre ancak birinizin denize daldırdığı parmağının, o denizden ne kadar su alabileceğine benzer; parmağının suya batıp çıktığına bir baksın.",
            "desc": "Geçici madde perdesine takılıp kalmamak, ebedi hayatı esas almak gerekir.",
        },
        {
            "ref": "Ebû Dâvûd, Edeb, 42",
            "title": "İlim ve Hikmet Arayışı",
            "text": "Hikmet, müminin yitiğidir; nerede bulursa onu alır.",
            "desc": "Hakikat ve bilim nerede bulunursa oradan alınır; çünkü tüm doğru ilimler Yaratıcı'nın sıfatlarının yansımasıdır.",
        },
        {
            "ref": "Buhârî, İlim, 10",
            "title": "İlim Öğrenmenin Fazileti",
            "text": "Allah, kimin için hayır dilerse onu dinde fakih (derin anlayış sahibi) kılar.",
            "desc": "Hakiki anlamda dini ve kâinatı okuyan alimler, olayların perde arkasındaki ilahi kudreti görürler.",
        },
        {
            "ref": "Müslim, Zikir, 38",
            "title": "Allah'ı Zikretmek ve Hatırlamak",
            "text": "Allah'ı zikreden kimse ile zikretmeyen kimsenin misali, diri ile ölü gibidir.",
            "desc": "Kâinatı manasız ve tesadüfi gören zihniyet ölü gibidir; onu Yaratıcı'nın eseri bilen ruh ise diridir.",
        },
        {
            "ref": "Tirmizî, Kader, 10",
            "title": "İlahi Takdir ve Rıza",
            "text": "Kaderine razı ol ki insanların en zengini olasın.",
            "desc": "Kainattaki her şeyi en mükemmel ölçüyle idare eden bir Yaratıcı'ya teslim olmak huzur getirir.",
        },
        {
            "ref": "İbn Mâce, Mukaddime, 17",
            "title": "İlim Yolculuğu",
            "text": "İlim öğrenmek her müslümana farzdır.",
            "desc": "Hem dinsel hem de fen bilimlerini öğrenmek, alemi tanıma adına büyük bir sorumluluktur.",
        },
        {
            "ref": "Nesâî, Zînet, 51",
            "title": "Güzellik ve İnce Sanat",
            "text": "Şüphesiz Allah güzeldir, güzelliği sever.",
            "desc": "Kainattaki tüm estetik ve sanat, o mukaddes ve sonsuz güzelliğin birer perdesidir.",
        },
        {
            "ref": "Buhârî, Rikāk, 3",
            "title": "Nimetlerin Kıymeti",
            "text": "İki nimet vardır ki insanların çoğu onlar hususunda aldanmıştır: Sıhhat ve boş vakit.",
            "desc": "Hayatın ve zamanın tesadüfen verilmediği, insan sınavı için büyük birer emanet olduğu unutulmamalıdır.",
        },
        {
            "ref": "Müslim, Birr, 59",
            "title": "Merhamet ve Şefkat",
            "text": "Merhamet etmeyene merhamet olunmaz.",
            "desc": "Kainattaki tüm canlılara şefkatle yaklaşmak, Rububiyet kanunlarına uygun bir ahlaktır.",
        },
        {
            "ref": "Tirmizî, Kıyamet, 49",
            "title": "Amel ve Sorumluluk",
            "text": "İnsanoğlu kıyamet gününde beş şeyden hesaba çekilmedikçe yerinden ayrılmaz...",
            "desc": "Hayatın her saniyesi ve verilen aklın nerede kullanıldığı hesaba tabi tutulacaktır.",
        },
        {
            "ref": "Ebû Dâvûd, Sünnet, 1",
            "title": "Hakikate Sarılmak",
            "text": "Sizden kim yaşarsa, pek çok ihtilaflar görecektir. Size sünnetimi ve hulefa-i raşidinin yolunu tavsiye ederim.",
            "desc": "Fikir akımlarının ve sapmaların çoğaldığı asırlarda ana kaynaklara sımsıkı sarılmak kurtuluştur.",
        },
        {
            "ref": "Buhârî, İman, 7",
            "title": "Doğruluk ve Dürüstlük",
            "text": "Doğruluk insanı iyiliğe, iyilik de cennete götürür.",
            "desc": "Ahlaki erdemler kainattaki fıtrat kanunları ile tam bir uyum içerisindedir.",
        },
        {
            "ref": "Müslim, Müsâfirîn, 26",
            "title": "Tevekkül ve Çalışmak",
            "text": "Eğer siz Allah'a gereği gibi tevekkül etseydiniz, kuşun rızıklandırıldığı gibi rızıklandırılırdınız...",
            "desc": "Sebep dairesinde çalışıp neticeyi Yaratıcı'dan beklemek akli ve nakli bir kuraldır.",
        },
        {
            "ref": "Tirmizî, Edeb, 70",
            "title": "İnsanlara Teşekkür",
            "text": "İnsanlara teşekkür etmeyen, Allah'a şükretmemiş olur.",
            "desc": "Vasıta olan sebepleri bilmek ve hakiki Verici'ye minnettar olmak gerekir.",
        },
        {
            "ref": "İbn Mâce, Zühd, 24",
            "title": "Dünyaya Aldanmamak",
            "text": "Dünyada sanki bir yabancı veya bir yolcu gibi ol.",
            "desc": "Maddeye taparcasına bağlanmamak, dünyanın geçici bir misafirhane olduğunu idrak etmek önemlidir.",
        },
        {
            "ref": "Buhârî, Edeb, 18",
            "title": "Komşuluk ve Toplumsal Düzen",
            "text": "Cebrail bana komşuya iyilik etmeyi o kadar çok tavsiye etti ki, onu mirasçı kılacak sandı.",
            "desc": "Sosyal ilişkilerdeki ince ölçüler, toplumsal huzurun teminatıdır.",
        },
        {
            "ref": "Müslim, Selâm, 11",
            "title": "Sevgi ve Barış",
            "text": "İman etmedikçe cennete giremezsiniz; birbirinizi sevmedikçe de iman etmiş olmazsınız...",
            "desc": "Kalplerin sevgiyle bağlanması ilahi muhabbetin tecellisidir.",
        },
        {
            "ref": "Tirmizî, İlim, 19",
            "title": "Alimin Değeri",
            "text": "Alimin abide üstünlüğü, dolunayın diğer yıldızlara üstünlüğü gibidir.",
            "desc": "Gerçek ilim sahipleri kainattaki esrarı çözerek insanlığa rehberlik ederler.",
        }
    ]

    filtered = (
        [
            h
            for h in hadisler_genisletilmis
            if search_query.lower() in h["title"].lower()
            or search_query.lower() in h["text"].lower()
            or search_query.lower() in h["desc"].lower()
            or search_query.lower() in h["ref"].lower()
        ]
        if search_query
        else hadisler_genisletilmis
    )

    for item in filtered:
        st.markdown(
            f"""
        <div class="card">
            <span class="badge" style="background-color: #eff6ff; color: #1d4ed8;">{item['ref']}</span>
            <h4 style="margin-top: 0.25rem; color: #1e293b;">{item['title']}</h4>
            <p style="font-style: italic; color: #334155; background-color: #f8fafc; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid #3b82f6;">"{item['text']}"</p>
            <p style="font-size: 0.9rem; color: #475569; margin-top: 0.5rem;"><b>{t['wisdom_label']}:</b> {item['desc']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

elif menu == t["menu"][4]:
    st.markdown(f"## {t['section_alim_title']}")
    st.markdown(t["section_alim_desc"])

    # 20+ Genişletilmiş Alimler Listesi Entegrasyonu
    alimler_genisletilmis = [
        {
            "name": "İmâm-ı Gazâlî",
            "work": "Tehâfütü'l-Felâsife & İhyâu Ulûmi'd-Dîn",
            "view": "Felsefi akımların ve maddeciliğin iddialarını akli delillerle çürütmüş, kainattaki her zerrerinin ilahi kudretle hareket ettiğini ispat etmiştir."
        },
        {
            "name": "İbn Sînâ",
            "work": "Kitâbü'ş-Şifâ & El-Kānûn fî't-Tıbb",
            "view": "Maddenin ezeliliğini reddetmiş, Vacibü'l-Vücud (zorunlu varlık) akidesiyle kainatın yaratıcısının varlığını felsefi temellere oturtmuştur."
        },
        {
            "name": "Fahreddin Râzî",
            "work": "Mefâtîhu'l-Ğayb (Tefsir-i Kebîr)",
            "view": "Ayetlerin tefsirinde astronomi, tıp ve fen bilimlerini yoğun şekilde kullanarak kainat kitabının okunmasının imanî delillerini ortaya koymuştur."
        },
        {
            "name": "İbn Rüşd",
            "work": "Tehâfütü't-Tehâfüt",
            "view": "Din ve felsefenin asla çelişmeyeceğini, hakiki bilimin insanı Allah'ın sanatını anlamaya sevk edeceğini savunmuştur."
        },
        {
            "name": "Mâtürîdî",
            "work": "Kitâbü't-Tevhîd",
            "view": "İnsanın akıl ve vicdanıyla Yaratıcı'yı bulabileceğini, kainattaki hikmetli nizamın şüpheleri bertaraf ettiğini savunmuştur."
        },
        {
            "name": "Eş'arî",
            "work": "Lüma'ü'l-Edille",
            "view": "Atomcu (cevher-i ferd) teoriyle maddelerin her an ilahi irade ile varlıkta durduğunu, tesadüfe yer olmadığını savunmuştur."
        },
        {
            "name": "İbn Teymiye",
            "work": "Der'ü Teârüzi'l-Akl ve'n-Nakl",
            "view": "Akli delillerle nakli delillerin tam bir uyum içinde olduğunu, sağlıklı bir aklın asla vahye ve yaratılış gerçeğine ters düşmeyeceğini vurgulamıştır."
        },
        {
            "name": "Mevlânâ Celâleddîn-i Rûmî",
            "work": "Mesnevî",
            "view": "Kainattaki her şeyin ilahi aşkla ve nizamla hareket ettiğini, maddenin manaya açılan bir pencere olduğunu şiirsel bir dille anlatmıştır."
        },
        {
            "name": "Muhyiddin İbn Arabî",
            "work": "Fütûhât-ı Mekkiyye",
            "view": "Kainatın ilahi isimlerin ve sıfatların birer ayna ve tecelligahı olduğunu ifade etmiştir."
        },
        {
            "name": "Sühreverdî",
            "work": "Hikmetü'l-İşrâk",
            "view": "Işık (nur) felsefesiyle varlık alemini açıklayarak, tüm mevcudatın Hak'tan yansıyan nurlar olduğunu savunmuştur."
        },
        {
            "name": "Abdülkâdir Geylânî",
            "work": "Fethu'r-Rabbânî",
            "view": "Kalbin ancak Allah'ın marifetiyle huzur bulacağını, maddi hırsların insanı hakikatten uzaklaştıracağını belirtmiştir."
        },
        {
            "name": "Şah Veliyullah Dehlevî",
            "work": "Hüccetüllahi'l-Balıga",
            "view": "Şeriatın hükümlerinin ve kainattaki kanunların hikmetlerini akli ve toplumsal temellerle açıklamıştır."
        },
        {
            "name": "Birûnî",
            "work": "Tahkîk Ma li-l-Hind & Âsâru'l-Bâkiye",
            "view": "Astronomi ve doğa bilimlerinde yaptığı hassas gözlemlerle, tabiat kanunlarının kusursuz bir ilahi nizama dayandığını göstermiştir."
        },
        {
            "name": "İbn Heysem",
            "work": "Kitâbü'l-Menâzır",
            "view": "Optik ve fizik alanındaki öncü çalışmalarıyla görme olayındaki muazzam ilahi sanatı ve geometriyi gözler önüne sermiştir."
        },
        {
            "name": "Harezmî",
            "work": "Kitâbül-Hülasa fi Hesâbi'l-Cebr ve'l-Mukābele",
            "view": "Matematikteki kusursuz denklemlerin evrendeki ilahi nizamın dilini yansıttığını ortaya koymuştur."
        },
        {
            "name": "Akşemseddin",
            "work": "Maddetü'l-Hayat",
            "view": "Tıp ve mikro biyoloji alanındaki görüşleriyle hastalıkların tesadüfi olmadığını, ilahi kanunlar çerçevesinde işlediğini belirtmiştir."
        },
        {
            "name": "Kâtip Çelebi",
            "work": "Keşfü'z-Zunûn",
            "view": "İlimlerin tasnifini yaparak fen ve din ilimlerinin birbirini tamamlayan iki hakikat kolu olduğunu savunmuştur."
        },
        {
            "name": "İzmirli İsmail Hakkı",
            "work": "Yeni İlm-i Kelâm",
            "view": "Modern dönemde ortaya çıkan materyalist ve pozitivist akımlara karşı İslam kelamını güncel bilimsel verilerle yeniden inşa etmiştir."
        },
        {
            "name": "Elmalılı M. Hamdi Yazır",
            "work": "Hak Dini Kur'ân Dili",
            "view": "Tefsirinde modern fen bilimlerinin verileri ile ayetleri harmanlayarak kainat kitabının okunuşunu muazzam bir şekilde açıklamıştır."
        }
    ]

    filtered = (
        [
            a
            for a in alimler_genisletilmis
            if search_query.lower() in a["name"].lower()
            or search_query.lower() in a["view"].lower()
            or search_query.lower() in a["work"].lower()
        ]
        if search_query
        else alimler_genisletilmis
    )

    for item in filtered:
        st.markdown(
            f"""
        <div class="card">
            <span class="badge" style="background-color: #faf5ff; color: #7e22ce;">{item['work']}</span>
            <h4 style="margin-top: 0.25rem; color: #1e293b;">{item['name']}</h4>
            <p style="color: #334155; background-color: #fcf8ff; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid #a855f7;">{item['view']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

elif menu == t["menu"][5]:
    st.markdown(f"## {t['section_nursi_title']}")
    st.markdown(t["section_nursi_desc"])

    # 20+ Genişletilmiş Risale-i Nur Listesi Entegrasyonu
    nursi_genisletilmis = [
        {
            "category": "Tabiat Risalesi",
            "title": "Fabrika ve Saray Misali (Tesadüfün Reddi)",
            "text": "Kainat muazzam bir saray ve kusursuz çalışan bir fabrika gibidir. Harika bir fabrikada ya da sarayda en küçük bir çark dahi ustasız ve kitapsız olamazken, kainatın tesadüfe veya tabiata verilmesi aklen imkansızdır.",
            "desc": "Hiçbir sanat eseri ustasız olamayacağı gibi, kainat da sahipsiz ve tesadüfi olamaz.",
        },
        {
            "category": "Sözler (3. Söz)",
            "title": "Güzel Sanat ve Sani' Mesele",
            "text": "İnsan kainata baktığında hayranlık uyandıran bir sanat görür. Sanat, Sani'yi (sanatkârı) gösterir; esersiz ustasız olamaz.",
            "desc": "Gördüğümüz her eser, arkasındaki mutlak bir ilim ve irade sahibini haber verir.",
        },
        {
            "category": "Asâ-yı Musa",
            "title": "DNA ve Hikmet Kodları",
            "text": "Küçücük bir çekirdekte devasa bir ağacın programının yazılması, mucizevi bir kudret kaleminin ve sonsuz bir ilmin eseridir.",
            "desc": "Bilgi ve kodlar, ancak bir İrade sahibinin kaleminden çıkabilir; madde kendi kendine bilgi üretemez.",
        },
        {
            "category": "Lem'alar (23. Lem'a)",
            "title": "Tabiatın Maskesi",
            "text": "Tabiat, kudret-i ilahiyenin bir defteri veya kanunları mecmuasıdır; icra edici bir kudret değildir. Matbaa basıcıdır, yazar değildir.",
            "desc": "Tabiat kanunları sadece işleyiş nizamıdır; icra eden ise Allah'ın kudretidir.",
        },
        {
            "category": "Mektubat (20. Mektup)",
            "title": "Hadsiz Acizlik ve Sonsuz Kudret",
            "text": "İnsan, kainattaki hadsiz hadiselere karşı acizdir; lakin sonsuz bir Kudret Sahibine iman ederek bütün sıkıntılara karşı sığınabilir.",
            "desc": "İmanın kazandırdığı manevi güç ve huzur, insanı ruhsal bunalımlardan korur.",
        },
        {
            "category": "Şualar (7. Şua - Ayetü'l-Kübra)",
            "title": "Kainatın lisanıyla Yaratıcı'yı Aramak",
            "text": "Gökler, yer, yıldızlar, nebatlar ve zerrat hep bir ağızdan Yaratıcı'nın varlığını ve birliğini şahitlik ederler.",
            "desc": "Kainattaki her mevcudat birer dildir ve Sani'sini tanıttırır.",
        },
        {
            "category": "Sözler (22. Söz)",
            "title": "İman ve Küfrün Neticesi",
            "text": "İman insanı insan eder, belki sultan eder; küfür ise insanı canavar bir hayvana veya en aşağı bir dereceye düşürür.",
            "desc": "İnançsızlık insan ruhunu tatminsizlik ve yalnızlık girdabına sürükler.",
        },
        {
            "category": "Barikası (11. Şua)",
            "title": "İhlas ve Hakikat",
            "text": "Amellerde rıza-i ilahi esas olmalıdır. Hakiki başarı ve huzur ancak Allah'ın rızasına yönelmekle elde edilir.",
            "desc": "Maneviyatın temel direği ihlas ve samimiyettir.",
        },
        {
            "category": "Mesnevî-i Nuriye",
            "title": "Zerrelerin Şahitliği",
            "text": "Kainattaki en küçük zerreler bile muntazam hareketleriyle ilahi birer ordu mensubu gibi çalışırlar.",
            "desc": "Hiçbir zerre başıboş hareket etmez, ilahi kanunlara itaat eder.",
        },
        {
            "category": "Tılsımlar Mecmuası",
            "title": "Ölümün Hakikati",
            "text": "Ölüm yok olmak değil, bir terhis tezkeresi ve ebedi alem seyahatinin başlangıcıdır.",
            "desc": "Ölüm korkusunu gideren en büyük hakikat iman ile gelen ahiret inancıdır.",
        },
        {
            "category": "Sözler (32. Söz)",
            "title": "Mahlukatta Hikmet ve Faydalar",
            "text": "Kainatta hiçbir şey lüzumsuz ve hikmetsiz yaratılmamıştır; en küçük mahlukta bile binler fayda vardır.",
            "desc": "İsrafsız ve kusursuz bir tasarruf hakimdir.",
        },
        {
            "category": "Lem'alar (17. Lem'a)",
            "title": "İbadetin Hayattaki Yeri",
            "text": "İbadet, ruhun gıdası ve kalbin anahtarıdır; hayatın manasını anlamanın tek yoludur.",
            "desc": "İbadet eden insan hayatın yükünden kurtulur ve huzur bulur.",
        },
        {
            "category": "Mektubat (29. Mektup)",
            "title": "Ruhun Bekası",
            "text": "İnsandaki baki kalma arzusu ve sonsuzluk isteği, ebedi bir alem varlığının en büyük delilidir.",
            "desc": "İnsanın fıtratındaki sonsuzluk arzusu ahireti müjdeler.",
        },
        {
            "category": "Asâ-yı Musa",
            "title": "Kur'an'ın Mucizekarlığı",
            "text": "Kur'an-ı Hakim kainatın müzikası ve ulu bir hazinenin anahtarıdır.",
            "desc": "Kur'an insanlığın akli ve kalbi sorularına tam cevap verir.",
        },
        {
            "category": "Şualar",
            "title": "Haşrin Delilleri",
            "text": "Baharda yeryüzünde ölü tohumların diriltilmesi, haşrin ve ahiretin ne kadar kolay olduğunu gösteren somut bir delildir.",
            "desc": "Bahar misali, ölümden sonra diriliş aklen ve mantıken mümkündür.",
        },
        {
            "category": "Sözler (10. Söz)",
            "title": "Haşir ve Ahiret",
            "text": "Sonsuz bir adalet ve merhamet, bu dünyadaki mazlumların haklarının alınacağı bir mahkeme-i kübrayı iktiza eder.",
            "desc": "Ahiret inancı evrensel adaletin temelidir.",
        },
        {
            "category": "Barla Lahikası",
            "title": "Dua ve İbadet Münasebeti",
            "text": "Dua, kulun Cenâb-ı Hakk'a olan aczini ve fakrını ilan etmesinin en güzel yoludur.",
            "desc": "Dua eden insan asla yalnızlık hissetmez.",
        },
        {
            "category": "Kastamonu Lahikası",
            "title": "Nübüvvetin Lüzumu",
            "text": "İnsan aklı her şeyi tek başına idrak edemez; peygamberlerin rehberliği hayati önem taşır.",
            "desc": "İnsanlık ilahi rehberliğe muhtaçtır.",
        },
        {
            "category": "Emirdağ Lahikası",
            "title": "İman Hizmeti ve Sabır",
            "text": "Hakikat yolunda çekilen sıkıntılar, iman hizmetinin manevi lezzetiyle hafifler.",
            "desc": "Manevi hizmet sabır ve metanet gerektirir.",
        },
        {
            "category": "Muhakemat",
            "title": "Akıl ve Nakil Uyumu",
            "text": "Hakiki akıl ile sahih nakil asla birbiriyle çelişmez; aksine birbirini tasdik eder.",
            "desc": "Bilim ve din ittifak halindedir.",
        }
    ]

    filtered = (
        [
            n
            for n in nursi_genisletilmis
            if search_query.lower() in n["title"].lower()
            or search_query.lower() in n["text"].lower()
            or search_query.lower() in n["category"].lower()
        ]
        if search_query
        else nursi_genisletilmis
    )

    for item in filtered:
        st.markdown(
            f"""
        <div class="card">
            <span class="badge" style="background-color: #fffbeb; color: #b45309;">{item['category']}</span>
            <h4 style="margin-top: 0.25rem; color: #1e293b;">{item['title']}</h4>
            <p style="color: #334155; background-color: #fffefb; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid #f59e0b;">{item['text']}</p>
            <p style="font-size: 0.9rem; color: #475569; margin-top: 0.5rem;"><b>{t['conclusion_label']}:</b> {item['desc']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

elif menu == t["menu"][6]:
    st.markdown(f"## {t['section_akim_title']}")
    st.markdown(t["section_akim_desc"])

    # 20+ Genişletilmiş Felsefi Akımlar ve Cevapları Tablosu Entegrasyonu
    if lang == "Türkçe":
        df = pd.DataFrame(
            [
                ["Ateizm", "Kainat ve canlılar tesadüfen var olmuştur.", "Sanat eseri sanatkârsız olamaz. En basit saat bile ustasız olmazken kainat sahipsiz olamaz.", "Bediüzzaman (Fabrika ve Saray misali)"],
                ["Deizm", "Allah alemi yarattı fakat müdahale etmez, kitap göndermez.", "Yaratan her an yarattığını görür, gözetir ve rızkını verir. Rububiyet bunu gerektirir.", "İmam-ı Gazali & Kur'an (Mülk Suresi)"],
                ["Materyalizm", "Her şey maddeden ibarettir; ruh ve ahiret yoktur.", "Madde şuursuzdur; şuurlu hayat, vicdan ve akıl maddeden doğamaz.", "İbn Sina & Bediüzzaman"],
                ["Natüralizm", "Tabiat kanunları her şeyi yapar, ilahi iradeye gerek yoktur.", "Tabiat bir kanunlar mecmuasıdır; icra edici kudret değildir. Matbaa basıcıdır, yazar değildir.", "Bediüzzaman (Tabiat Risalesi)"],
                ["Darvinizm", "Canlılar kör mekanizmalarla tesadüfen çeşitlenmiştir.", "Hücredeki kusursuz DNA bilgi kodları tesadüfen oluşamaz; şuur ve irade ister.", "İslam Alimleri ve Asrın Kelamcıları"],
                ["Pozitivizm", "Sadece deney ve gözlemle bilinen şeyler gerçektir, metafizik yoktur.", "İnsan ruhu, vicdanı, sevgi ve adalet gibi soyut gerçekler de deneyüstü hakikatlerdir.", "İzmirli İsmail Hakkı"],
                ["Agnostisizm", "Yaratanın varlığı veya yokluğu bilinemez, bilinemezcilik esastır.", "İnsanın fıtratındaki sığınma ve ilahi adalet duygusu bu gerçeği fıtri olarak bilir.", "İslam Kelamcıları"],
                ["Nihilizm", "Hiçbir değer, anlam ve amaç yoktur; hayat boşluktan ibarettir.", "Her varlık gayelidir ve hikmetle yaratılmıştır; hiçbir şey manasız değildir.", "Mevlânâ & Nur Risaleleri"],
                ["Egzistansiyalizm", "İnsan önce var olur, sonra kendi anlamını kendi yaratır.", "İnsan kendi başına anlam üretemez; o ancak Yaratıcı'sını tanımakla gerçek anlamını bulur.", "Alimler ve Düşünürler"],
                ["Sekülarizm", "Din hayatın dışına çıkarılmalı, sadece bireysel vicdana hapsedilmelidir.", "Yaratıcı kainatın her alanında hükümrandır; hayatın bütünü ilahi kanunlara tabidir.", "İslam Hukuku ve Felsefesi"],
                ["Panteizm", "Allah ve kainat aynı şeydir; kainatın kendisi ilahdır.", "Yaratan ile yaratılan tamamen ayrıdır. Usta eserinin içine hapsolamaz, ustası başkadır.", "İmam Rabbani"],
                ["Panenteizm", "Kainat Allah'ın içindedir ama O'ndan ibaret değildir.", "Varlık alemi ilahi isimlerin aynasıdır; O dışarıdan müdahale eden müstakil bir Yaratıcı'dır.", "Muhyiddin İbn Arabî"],
                ["Fatalizm (Cebriyye)", "İnsanın iradesi yoktur, her şey zorunlu olarak önceden belirlenmiştir.", "İnsana cüzi irade verilmiştir; insan yaptıklarından ve tercihlerinden mesuldür.", "Ehl-i Sünnet Kelamcıları"],
                ["Hedonizm", "Hayatın yegane amacı haz almak ve acıdan kaçmaktır.", "Geçici hazlar ruhu doyurmaz; kalbin hakiki tatmini ancak sonsuz olanı sevmekle mümkündür.", "İmam-ı Gazali"],
                ["Rasyonalizm", "Tek hakikat kaynağı akıldır; duyu organları yanılttığı için güvenilmez.", "Akıl ve nakil (vahiy) birbirinin zıddı değil, iki müttefik nurdur.", "Fahreddin Râzî"],
                ["Ampirizm", "Tüm bilgi duyu organlarıyla ve deneyle elde edilir, zihinde önsel bilgi yoktur.", "Duyu ötesi (gaybi) hakikatler vahiyle ve akli istidlallerle bilinir.", "İbn Rüşd"],
                ["Pragmatizm", "Bir şeyin doğruluğu sağladığı faydaya ve işlevselliğe göre ölçülür.", "Hakikat faydalı olandan ibaret değildir; faydalı olan şey hakikatin ta kendisi olabilir.", "İslam Düşüncesi"],
                ["Evrimcilik (Genel)", "Canlı türleri sabit değildir, sürekli başka türlere dönüşmüştür.", "Yaratılış kademeli olabilir; ancak her kademe ilahi irade ve kudretle gerçekleşir.", "Elmalılı Hamdi Yazır"],
                ["Materyalist Tarih", "Tarihi belirleyen yegane unsur ekonomik ve maddesel şartlardır.", "Tarih ve kainat, ilahi hikmetlerin ve kader planının tecelli ettiği bir yazgı sahnesidir.", "İbn Haldun"],
                ["Solipsizm", "Yalnızca ben ve zihnim vardır, dış dünya bir yanılsamadan ibarettir.", "Kainatın dışarıda somut ve hakiki bir varlığı vardır; zira milyarlarca insan aynı nizamı görmektedir.", "İmam Mâtürîdî"]
            ],
            columns=t["table_columns"],
        )
    else:
        df = pd.DataFrame(
            [
                ["Atheism", "Universe and living beings came to be by chance.", "An artwork cannot exist without an artist. Even the simplest clock cannot exist without a maker; the universe cannot be ownerless.", "Bediuzzaman (Factory and Palace allegory)"],
                ["Deism", "God created the universe but does not intervene or send books.", "The Creator sees, oversees, and sustains His creation at every moment. Lordship requires this.", "Imam al-Ghazali & Quran (Surah Al-Mulk)"],
                ["Materialism", "Everything consists of matter; there is no soul or hereafter.", "Matter is unconscious; conscious life, conscience, and intellect cannot originate from matter.", "Avicenna & Bediuzzaman"],
                ["Naturalism", "Laws of nature do everything; divine will is not necessary.", "Nature is a collection of laws, not an executing power. The printing press is the printer, not the author.", "Bediuzzaman (Treatise on Nature)"],
                ["Darwinism", "Living beings diversified by chance through blind mechanisms.", "Flawless DNA information codes in the cell cannot form by chance; they require consciousness and will.", "Islamic Scholars & Contemporary Theologians"],
                ["Positivism", "Only things known by experience and observation are real, metaphysics does not exist.", "Human soul, conscience, love, and justice are also transcendental realities.", "Izmirli Ismail Hakki"],
                ["Agnosticism", "The existence or non-existence of the Creator cannot be known.", "The innate human inclination for refuge and divine justice knows this truth inherently.", "Islamic Theologians"],
                ["Nihilism", "There is no value, meaning, or purpose; life consists of emptiness.", "Every entity has a purpose and is created with wisdom; nothing is meaningless.", "Rumi & Risale-i Nur"],
                ["Existentialism", "Man exists first, then creates his own meaning.", "Man cannot produce meaning on his own; he finds true meaning only by knowing his Creator.", "Scholars and Thinkers"],
                ["Secularism", "Religion should be kept out of public life and confined to individual conscience.", "The Creator reigns over every sphere of the universe; life is subject to divine laws.", "Islamic Law and Philosophy"],
                ["Pantheism", "God and the universe are the same; the universe itself is the divine.", "The Creator and creation are entirely separate. The artisan cannot be trapped inside his artwork.", "Imam Rabbani"],
                ["Panentheism", "The universe is within God but not identical to Him.", "The realm of existence is a mirror of divine names; He is an independent Creator intervening from beyond.", "Muhyiddin Ibn Arabi"],
                ["Fatalism (Jabriyya)", "Man has no will, everything is predetermined strictly.", "Man is given partial free will; he is responsible for his choices.", "Ahl al-Sunnah Theologians"],
                ["Hedonism", "The ultimate purpose of life is to seek pleasure and avoid pain.", "Temporary pleasures do not satisfy the soul; true satisfaction comes from loving the Eternal.", "Imam al-Ghazali"],
                ["Rationalism", "The sole source of truth is reason; senses are deceptive.", "Reason and revelation are not opposites, but two allied lights.", "Fakhr al-Din al-Razi"],
                ["Empiricism", "All knowledge is acquired through senses and experience.", "Transcendental truths are known through revelation and rational deduction.", "Ibn Rushd"],
                ["Pragmatism", "The truth of something is measured by its utility and functionality.", "Truth is not limited to what is useful; what is useful may be the truth itself.", "Islamic Thought"],
                ["Evolutionism", "Living species transform constantly into other species.", "Creation can be gradual, but every stage occurs through divine will and power.", "Elmalili Hamdi Yazir"],
                ["Historical Materialism", "The sole determinant of history is economic and material conditions.", "History and the universe are the stage of divine wisdom and destiny.", "Ibn Khaldun"],
                ["Solipsism", "Only I and my mind exist; the external world is an illusion.", "The universe has an objective and real existence; billions witness the same order.", "Imam Maturidi"]
            ],
            columns=t["table_columns"],
        )

    st.dataframe(df, use_container_width=True, hide_index=True)

elif menu == t["menu"][7]:
    st.markdown(f"## {t['legal_title']}")
    st.markdown(
        f"""
    <div class="card">
        <p style="line-height: 1.8; white-space: pre-line;">{t['legal_text']}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )# ----------------- ALT BİLGİ (FOOTER) -----------------
st.markdown(f'<div class="footer-text">{t["footer"]}</div>', unsafe_allow_html=True)