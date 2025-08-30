import streamlit as st
from datetime import datetime


animals_data = {
    0: {
        "name": "Sıçgan (Sıçan/Fare)",
        "image": "🐭",
        "years": [2032, 2020, 2008, 1996, 1984, 1972, 1960, 1948, 1936, 1924, 1912, 1900],
        "description": "Bu yılın ilk aylarında ve ortalarında ferahlık, halk arasında bir mutluluk gözlenir. Aynı zamanda zenginlik olur. Ama yılın sonbaharında halklar ve padişahlar arasında fitne başlar. Kışın salgın olur, yaz günleri yağmurlu olur. Sıçanlar çok olur ve buğdaylara hücum ederler.",
        "characteristics": "Zeki, çevik, uyumlu, pratik düşünen"
    },
    1: {
        "name": "Ud (Öküz/Sığır)",
        "image": "🐂", 
        "years": [2033, 2021, 2009, 1997, 1985, 1973, 1961, 1949, 1937, 1925, 1913, 1901],
        "description": "Bu yılda yıldırımlar ve gök gürültülü yağmurlar olur. Kışın tipiler çok olur, kar çok yağar, kış uzun sürer. Buğday ve her çeşit meyve çok olur. Doğal olarak afetler olmasına rağmen bereketli bir yıldır.",
        "characteristics": "Sabırlı, çalışkan, güvenilir, kararlı"
    },
    2: {
        "name": "Bars (Pars/Kaplan)",
        "image": "🐆",
        "years": [2034, 2022, 2010, 1998, 1986, 1974, 1962, 1950, 1938, 1926, 1914, 1902],
        "description": "Bu yılda halk arasında düşmanlık ve adaletsiz işler olur. Padişahlar arasında geçimsizlik olur, sükûnet yoktur. Yazın buğday ve meyvelere afet gelir, yani kuvvetli zelzeleler olur. Denizde dalgalı tufanlar olur. Kısaca bireysel ve toplumsal anlamda kötü bir yıldır.",
        "characteristics": "Cesur, güçlü, lider ruhlu, bağımsız"
    },
    3: {
        "name": "Tavışgan (Tavşan)",
        "image": "🐰",
        "years": [2035, 2023, 2011, 1999, 1987, 1975, 1963, 1951, 1939, 1927, 1915, 1903],
        "description": "Bu yıl tam bir bolluk yılıdır. Bu yılda her çeşit nimet çok olur. Yaz ve kış ılıman olur, havalar iyi olur. Halk arasında sükûnet ve rahatlık olur.",
        "characteristics": "Nazik, diplomatik, sanatçı ruhlu, barışsever"
    },
    4: {
        "name": "Nek (Ejder/Ejderha)",
        "image": "🐉",
        "years": [2036, 2024, 2012, 2000, 1988, 1976, 1964, 1952, 1940, 1928, 1916, 1904],
        "description": "Bu yıl mutsuz bir yıldır. Bu yılda halk arasında husumet, fitne, çatışma ve savaş peyda olur. Yaz günleri yıldırım ve gök gürültülü yağmurlar çok olur. Kışın tipi ve kar çok olur; ağaçları soğuk alır.",
        "characteristics": "Güçlü, karizmatik, enerjik, lider"
    },
    5: {
        "name": "Yılan (Yılan)",
        "image": "🐍",
        "years": [2037, 2025, 2013, 2001, 1989, 1977, 1965, 1953, 1941, 1929, 1917, 1905],
        "description": "Bu yıl kıtlık yılıdır. Bu yılda yazın yağmur az, havalar kuru olur; buğday az olur. Çoğu yerde açlık ve pahalılık olur. Kışın kar az yağar; rutubet olur. Halk arasında kaygı ve hasret olur.",
        "characteristics": "Bilge, gizemli, derin düşünen, sezgileri güçlü"
    },
    6: {
        "name": "Yund (At)",
        "image": "🐎",
        "years": [2038, 2026, 2014, 2002, 1990, 1978, 1966, 1954, 1942, 1930, 1918, 1906],
        "description": "Bereket ve huzursuzluğun birlikte ortaya çıktığı bir yıldır. Bu yılda yazın hava ılık, yağmurlu olur. Buğday ve meyveler boldur. Kışın kar fazla yağmaz. Halk ve padişahlar arasında fitne çıkar, savaş ve çatışmalar ortaya çıkar. Dört ayaklı hayvanlara hastalık bulaşır.",
        "characteristics": "Özgür ruhlu, hızlı, maceraperest, bağımsız"
    },
    7: {
        "name": "Koy (Koyun)",
        "image": "🐑",
        "years": [2039, 2027, 2015, 2003, 1991, 1979, 1967, 1955, 1943, 1931, 1919, 1907],
        "description": "Bu yılda büyük oranda insanların mutlu olacağı bir yıldır. Bu yılda yaz sıcak olur, kış soğuk ve uzun geçer. Halk arasında zenginlik ve rahatlık olup, padişahlar arasında savaş başladığı halde barış hemen sağlanır. Ancak deniz ve gemilerde birtakım olumsuzluklarla karşılaşılır.",
        "characteristics": "Uysal, barışçıl, yaratıcı, sanatçı ruhlu"
    },
    8: {
        "name": "Biçin (Maymun)",
        "image": "🐵",
        "years": [2040, 2028, 2016, 2004, 1992, 1980, 1968, 1956, 1944, 1932, 1920, 1908],
        "description": "Bu ay da oldukça kötü bir yıldır. Halk arasında haset ve düşmanlık olur. Yazın yağmur, kışın kar çok olur. Halk arasında hastalıklar yayılır. Hayvanlar arasından deve ve yılkı hastalığa yakalanır.",
        "characteristics": "Zeki, esprili, sosyal, problem çözen"
    },
    9: {
        "name": "Tagaku (Tavuk/Horoz)",
        "image": "🐓",
        "years": [2041, 2029, 2017, 2005, 1993, 1981, 1969, 1957, 1945, 1933, 1921, 1909],
        "description": "Bu yılda yaz yağmurlu ve sıcak geçer; buğday ve çeşitli meyveler çok olur. Kış karlı ve soğuk olur. Hamile kadınlara ağırlık gelir. Darı, karabuğdaylar erken dikilmelidir.",
        "characteristics": "Dikkatli, düzenli, çalışkan, güvenilir"
    },
    10: {
        "name": "İt (Köpek)",
        "image": "🐕",
        "years": [2042, 2030, 2018, 2006, 1994, 1982, 1970, 1958, 1946, 1934, 1922, 1910],
        "description": "Ölümler diğer yıllara göre fazladır. Bu yılda yazın yağmurlar az olur. Buğdaylar az olup, fiyatlar pahalı olur. Kış yumuşak geçer. Meyveler ucuz olur.",
        "characteristics": "Sadık, dürüst, adil, koruyucu"
    },
    11: {
        "name": "Tonguz (Domuz/Geyik)",
        "image": "🐗",
        "years": [2043, 2031, 2019, 2007, 1995, 1983, 1971, 1959, 1947, 1935, 1923, 1911],
        "description": "Bu yılın adını Türkler söylemek istemediklerinden bu yıla 'geyik yılı' da denilmektedir. Bu yılda yaz yağmurlu, kış uzun ve soğuk olur. Buğday çok ve ucuz olur. Padişahlar arasında muhalefet, savaş ve çatışmalar olur. Halk arasında geçimsizlik olur; çeşitli afetler meydana gelir.",
        "characteristics": "Cömert, samimi, güçlü, kararlı"
    }
}

def calculate_animal_year(birth_year):

    animal_index = (birth_year - 1984) % 12
    return animals_data[animal_index]

def main():
    st.set_page_config(
        page_title="12 Hayvanlı Türk Takvimi",
        page_icon="🌙",
        layout="wide"
    )
    
    st.title("🌙 12 Hayvanlı Türk Takvimi")
    
    st.markdown("""
    Bu kadim takvim sistemi Türk kavimlerinin özgün buluşudur ve M.Ö. 2367'de başlamıştır. 
    12 yıllık döngülerle işleyen bu sistem, Gök Türkler, Uygur Türkleri, Tuna-Bulgar Türkleri 
    ve Hun Türkleri tarafından kullanılmış, Orhun Yazıtları ve Manas Destanı'nda da yer almıştır. 
    Her hayvan yılının kendine özgü özellikleri ve o yıla dair kehanetleri vardır. 
    Yılbaşı 21 Mart'ta gece-gündüz eşitliği ile başlar ve dünya'nın 3.600.000 yıllık 
    ömrünün bir parçası olarak görülür.
    """)
    
    st.markdown("---")
    st.subheader("✨ Hangi Hayvan Yılında Doğduğunuzu Keşfedin")
    
    st.markdown("""
    ### 🧮 Hesaplama Yöntemi
    **Örnek:** 2000 doğumlu bir kişi için:
    - 2000 + 9 = 2009
    - 2009 ÷ 12 = 167, **Kalan: 5**
    - Kalan 5 = **Ejder Yılı** (5. hayvan)
    
    *Bu şekilde doğduğunuz hayvan yılını bulabilirsiniz.*
    """)
    
    col_input, col_button = st.columns([2, 1])
    
    with col_input:
        current_year = datetime.now().year
        birth_year = st.number_input(
            "📅 Doğum Yılınız:",
            min_value=1900,
            max_value=current_year + 20,
            value=2000,
            step=1
        )
    
    with col_button:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 Hesapla", type="primary", use_container_width=True):
            st.session_state.birth_year_result = birth_year
    
    if hasattr(st.session_state, 'birth_year_result'):
        year = st.session_state.birth_year_result
        animal = calculate_animal_year(year)
        
        st.markdown("---")
        st.markdown(f"### 🎯 {year} Yılı Sonucunuz")
        
        col_left, col_right = st.columns([1, 2])
        
        with col_left:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px; background: linear-gradient(45deg, #ff6b6b, #ee5a24); border-radius: 15px; color: white; margin-bottom: 15px;">
                <div style="font-size: 80px; margin-bottom: 10px;">{animal['image']}</div>
                <h3 style="margin-bottom: 10px;">{animal['name']}</h3>
                <p style="font-style: italic;">{animal['characteristics']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if 2025 in animal['years']:
                st.markdown("### ⭐ 2025 YILI! ⭐")
                st.success("Bu yıl şu anda yaşadığımız yıl!")
        
        with col_right:
            st.markdown("### 📖 Yıl Özellikleri")
            st.info(animal['description'])
            
            st.markdown("### 📅 Bu Hayvana Ait Yıllar")
            
            years = animal['years']
            current_year = datetime.now().year
            
            year_cols = st.columns(4)
            for idx, year_item in enumerate(years):
                with year_cols[idx % 4]:
                    if year_item == current_year:
                        st.markdown(f"""
                        <div style="text-align: center; padding: 10px; background: #28a745; color: white; border-radius: 8px; margin: 2px;">
                            <strong>🎯 {year_item}</strong><br><small>ŞU AN</small>
                        </div>
                        """, unsafe_allow_html=True)
                    elif year_item < current_year:
                        if st.button(f"📚 {year_item}", key=f"result_year_{year_item}", help="Geçmiş yıl"):
                            st.balloons()
                            st.toast(f"{year_item} yılı {animal['name']} yılıydı!", icon="🎉")
                    else:
                        if st.button(f"🔮 {year_item}", key=f"result_year_{year_item}", help="Gelecek yıl"):
                            st.success(f"{year_item} yılı {animal['name']} yılı olacak!")
    
    st.markdown("---")
    st.subheader("🌟 12 Kutsal Hayvan Yılları ve Kadim Bilgileri")
    st.markdown("*Her hayvana tıklayarak o yıla ait bilgileri görün*")
    
    for i in range(12):
        animal = animals_data[i]
        
        with st.expander(f"{animal['image']} {i+1}. {animal['name']}", expanded=False):
            
            col_left, col_right = st.columns([1, 2])
            
            with col_left:
                st.markdown(f"""
                <div style="text-align: center; padding: 20px; background: linear-gradient(45deg, #ff6b6b, #ee5a24); border-radius: 15px; color: white; margin-bottom: 15px;">
                    <div style="font-size: 80px; margin-bottom: 10px;">{animal['image']}</div>
                    <h3 style="margin-bottom: 10px;">{animal['name']}</h3>
                    <p style="font-style: italic;">{animal['characteristics']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if 2025 in animal['years']:
                    st.markdown("### ⭐ 2025 YILI! ⭐")
                    st.success("Bu yıl şu anda yaşadığımız yıl!")
            
            with col_right:
                st.markdown("### 📖 Yıl Özellikleri")
                st.info(animal['description'])
                
                st.markdown("### 📅 Bu Hayvana Ait Yıllar")
                
                years = animal['years']
                current_year = datetime.now().year
                
                year_cols = st.columns(4)
                for idx, year in enumerate(years):
                    with year_cols[idx % 4]:
                        if year == current_year:
                            st.markdown(f"""
                            <div style="text-align: center; padding: 10px; background: #28a745; color: white; border-radius: 8px; margin: 2px;">
                                <strong>🎯 {year}</strong><br><small>ŞU AN</small>
                            </div>
                            """, unsafe_allow_html=True)
                        elif year < current_year:
                            if st.button(f"📚 {year}", key=f"year_{i}_{year}", help="Geçmiş yıl"):
                                st.balloons()
                                st.toast(f"{year} yılı {animal['name']} yılıydı!", icon="🎉")
                        else:
                            if st.button(f"🔮 {year}", key=f"year_{i}_{year}", help="Gelecek yıl"):
                                st.success(f"{year} yılı {animal['name']} yılı olacak!")
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">
        <h3 style="text-align: left; margin-bottom: 20px; color: white;">⚙️ Takvim Sistemi</h3>
        <p style="font-size: 16px; line-height: 1.8; margin: 0;">
            🌍 <strong>Dünya'nın Ömrü:</strong> 3.600.000 yıl &nbsp;&nbsp;&nbsp; 
            🔄 <strong>Bir Devir:</strong> 12 yıl &nbsp;&nbsp;&nbsp; 
            📅 <strong>Yılbaşı:</strong> 21 Mart &nbsp;&nbsp;&nbsp; 
            🎊 <strong>Başlangıç:</strong> Gece-gündüz eşitliği
        </p>
    </div>
    """, unsafe_allow_html=True)
    


if __name__ == "__main__":
    main()