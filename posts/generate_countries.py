from .models import Country

file_path = '../countries.json'

countries = {
    "1": {
        "en": "Uzbekistan",
        "uz": "O'zbekiston",
        "ru": "Узбекистан"
    },
    "2": {
        "en": "Russian",
        "uz": "Rossiya",
        "ru": "Россия"
    },
    "3": {
        "en": "Germany",
        "uz": "Germaniya",
        "ru": "Германия"
    },
    "4": {
        "en": "Albania",
        "uz": "Albaniya",
        "ru": "Албания"
    },
    "5": {
        "en": "Algeria",
        "uz": "Fazilat",
        "ru": "Алжир"
    },
    "6": {
        "en": "Samo",
        "uz": "Samo",
        "ru": "Само"
    },
    "7": {
        "en": "Andorra",
        "uz": "Antarora",
        "ru": "Андорра"
    },
    "8": {
        "en": "Angola",
        "uz": "Angol",
        "ru": "Ангола"
    },
    "9": {
        "en": "Angilla",
        "uz": "Angilla",
        "ru": "Ангилья"
    },
    "10": {
        "en": "Antigua and Barbuda",
        "uz": "Antigua va barbuda",
        "ru": "Антигуа и Барбуда"
    },
    "11": {
        "en": "Argentina",
        "uz": "Argentina",
        "ru": "Аргентина"
    },
    "12": {
        "en": "Armenia",
        "uz": "Armeniya",
        "ru": "Армения"
    },
    "13": {
        "en": "Aruba",
        "uz": "Aruba",
        "ru": "Аруба"
    },
    "14": {
        "en": "Australia",
        "uz": "Avstraliya",
        "ru": "Австралия"
    },
    "15": {
        "en": "Austria",
        "uz": "Avstriya",
        "ru": "Австрия"
    },
    "16": {
        "en": "Azerbaijan",
        "uz": "Ozarbayjon",
        "ru": "Азербайджан"
    },
    "17": {
        "en": "Bahrain",
        "uz": "Bahrayn",
        "ru": "Бахрейн"
    },
    "18": {
        "en": "Bangladesh",
        "uz": "Bangladesh",
        "ru": "Бангладеш"
    },
    "19": {
        "en": "Barbados",
        "uz": "Barbados",
        "ru": "Барбадос"
    },
    "20": {
        "en": "Belarus",
        "uz": "Bemor",
        "ru": "Беларусь"
    },
    "21": {
        "en": "Belgium",
        "uz": "Belgiya",
        "ru": "Бельгия"
    },
    "22": {
        "en": "Benin",
        "uz": "Benin",
        "ru": "Бенин"
    },
    "23": {
        "en": "Bermud",
        "uz": "Bermud",
        "ru": "Бермуд"
    },
    "24": {
        "en": "Butane",
        "uz": "Butan",
        "ru": "Бутан"
    },
    "25": {
        "en": "Bolivia",
        "uz": "Bolijon",
        "ru": "Боливия"
    },
    "26": {
        "en": "Bosnia and Gersegovina",
        "uz": "Bosniya va Geregovina",
        "ru": "Босния и Герсеговина"
    },
    "27": {
        "en": "Bottlene",
        "uz": "Butillat",
        "ru": "Утолженное"
    },
    "28": {
        "en": "Brazil",
        "uz": "Braziliya",
        "ru": "Бразилия"
    },
    "29": {
        "en": "Broi",
        "uz": "Bovul",
        "ru": "Брои"
    },
    "30": {
        "en": "Bulgaria",
        "uz": "Bulgariya",
        "ru": "Болгария"
    },
    "31": {
        "en": "Burkina-Faso",
        "uz": "Burkina-faso",
        "ru": "Буркина-Фасо"
    },
    "32": {
        "en": "Burmah (Myanma)",
        "uz": "Burma (Myanma)",
        "ru": "Берма (Мьянма)"
    },
    "33": {
        "en": "Burundi",
        "uz": "Burundi",
        "ru": "Бурунди"
    },
    "34": {
        "en": "Cambodia",
        "uz": "Kambodja",
        "ru": "Камбоджа"
    },
    "35": {
        "en": "Cameroon",
        "uz": "Kamerun",
        "ru": "Камерун"
    },
    "36": {
        "en": "Canada",
        "uz": "Kanada",
        "ru": "Канада"
    },
    "37": {
        "en": "Canary Islands",
        "uz": "Kanar orollari",
        "ru": "Канарские острова"
    },
    "38": {
        "en": "Cabo-Berde",
        "uz": "Kabo-berde",
        "ru": "Кабо-берде"
    },
    "39": {
        "en": "Central African Republic",
        "uz": "Markaziy Afrika Respublikasi",
        "ru": "Центральноафриканская Республика"
    },
    "40": {
        "en": "Smoke",
        "uz": "Tutun",
        "ru": "Дымка"
    },
    "41": {
        "en": "Chili",
        "uz": "Chili",
        "ru": "Чили"
    },
    "42": {
        "en": "China",
        "uz": "Xitoy",
        "ru": "Китай"
    },
    "43": {
        "en": "Colombia",
        "uz": "Kolumbiya",
        "ru": "Колумбия"
    },
    "44": {
        "en": "Comory",
        "uz": "Kulgili",
        "ru": "Коморы"
    },
    "45": {
        "en": "Congo",
        "uz": "Kongo",
        "ru": "Конго"
    },
    "46": {
        "en": "Costa Rica",
        "uz": "Kosta-Rika",
        "ru": "Коста-Рика"
    },
    "47": {
        "en": "Croatia",
        "uz": "Xorvatiya",
        "ru": "Хорватия"
    },
    "48": {
        "en": "Cuba",
        "uz": "Kubalik",
        "ru": "Куба"
    },
    "49": {
        "en": "Cyprus",
        "uz": "Kipr",
        "ru": "Кипр"
    },
    "50": {
        "en": "Czech Republic",
        "uz": "Chex Respublikasi",
        "ru": "Чешская Республика"
    },
    "51": {
        "en": "Denmark",
        "uz": "Denmark",
        "ru": "Дания"
    },
    "52": {
        "en": "Jibuts",
        "uz": "Jibutlar",
        "ru": "Jibuts"
    },
    "53": {
        "en": "Dominica",
        "uz": "Domini",
        "ru": "Доминика"
    },
    "54": {
        "en": "Dominican Republic",
        "uz": "Dominika Respublikasi",
        "ru": "Доминиканская Республика"
    },
    "55": {
        "en": "Ecuador",
        "uz": "Ekvador",
        "ru": "Эквадор"
    },
    "56": {
        "en": "Egypt",
        "uz": "Misr",
        "ru": "Египет"
    },
    "57": {
        "en": "Suclador",
        "uz": "So'm",
        "ru": "Сукрадор"
    },
    "58": {
        "en": "Equatorial Guinea",
        "uz": "Ekvator Gvineya",
        "ru": "Экваториальная Гвинея"
    },
    "59": {
        "en": "Us",
        "uz": "Biz",
        "ru": "Нас"
    },
    "60": {
        "en": "Estonia",
        "uz": "Estoniya",
        "ru": "Эстония"
    },
    "61": {
        "en": "Ethiopia",
        "uz": "Efiopiya",
        "ru": "Эфиопия"
    },
    "62": {
        "en": "Falkland Islands",
        "uz": "Falklend orollari",
        "ru": "Фолклендские острова"
    },
    "63": {
        "en": "Fiji",
        "uz": "Fiji",
        "ru": "Фиджи"
    },
    "64": {
        "en": "Finland",
        "uz": "Finlyandiya",
        "ru": "Финляндия"
    },
    "65": {
        "en": "France",
        "uz": "Frantsiya",
        "ru": "Франция"
    },
    "66": {
        "en": "French Guvian",
        "uz": "Frantsuz Guvyan",
        "ru": "Французская Гвиана"
    },
    "67": {
        "en": "French Polynesia",
        "uz": "Fransuz Polinesia",
        "ru": "Французская Полинезия"
    },
    "68": {
        "en": "Gabon",
        "uz": "Gabon",
        "ru": "Габон"
    },
    "69": {
        "en": "Georgia",
        "uz": "Gruziya",
        "ru": "Грузия"
    },
    "70": {
        "en": "Ghana",
        "uz": "Gana",
        "ru": "Гана"
    },
    "71": {
        "en": "Gibraltar",
        "uz": "Gibraltar",
        "ru": "Гибралтар"
    },
    "72": {
        "en": "Greece",
        "uz": "Gretsiya",
        "ru": "Греция"
    },
    "73": {
        "en": "Greenland",
        "uz": "Yashil rang",
        "ru": "Гренландия"
    },
    "74": {
        "en": "Grenada",
        "uz": "Grenada",
        "ru": "Гренада"
    },
    "75": {
        "en": "Guadeloupe",
        "uz": "Guadeluce",
        "ru": "Гваделупа"
    },
    "76": {
        "en": "Guam",
        "uz": "Guman",
        "ru": "Гуам"
    },
    "77": {
        "en": "Guatemala",
        "uz": "Gvatemala",
        "ru": "Гватемала"
    },
    "78": {
        "en": "Guinea",
        "uz": "Gvineya",
        "ru": "Гвинея"
    },
    "79": {
        "en": "Guinea-Bisau",
        "uz": "Gvineya-Bisau",
        "ru": "Гвинея-бисау"
    },
    "80": {
        "en": "Gayana",
        "uz": "Geyana",
        "ru": "Гаяна"
    },
    "81": {
        "en": "Haiti",
        "uz": "Gayt",
        "ru": "Гаити"
    },
    "82": {
        "en": "Honduras",
        "uz": "Gonduras",
        "ru": "Гондурас"
    },
    "83": {
        "en": "Hungary",
        "uz": "Osma",
        "ru": "Венгрия"
    },
    "84": {
        "en": "Iceland",
        "uz": "Mohir",
        "ru": "Исландия"
    },
    "85": {
        "en": "India",
        "uz": "Hindiston",
        "ru": "Индия"
    },
    "86": {
        "en": "Indonesia",
        "uz": "Indoneziya",
        "ru": "Индонезия"
    },
    "87": {
        "en": "Iranian",
        "uz": "Eronlik",
        "ru": "Иранский"
    },
    "88": {
        "en": "Iraq",
        "uz": "Iroqlik",
        "ru": "Ирак"
    },
    "89": {
        "en": "Ireland",
        "uz": "Irlandiyalik",
        "ru": "Ирландия"
    },
    "90": {
        "en": "Israel",
        "uz": "Isroillik",
        "ru": "Израиль"
    },
    "91": {
        "en": "Italy",
        "uz": "Italiya",
        "ru": "Италия"
    },
    "92": {
        "en": "Cat-d’Ivoire",
        "uz": "Mushuk drivuare",
        "ru": "Кот-д’Ивуар"
    },
    "93": {
        "en": "Jamaica",
        "uz": "Yamayka",
        "ru": "Ямайка"
    },
    "94": {
        "en": "Japan",
        "uz": "Yapon",
        "ru": "Япония"
    },
    "95": {
        "en": "Johnston (Atall)",
        "uz": "Jonston (ATAL)",
        "ru": "Джонстон (атолл)"
    },
    "96": {
        "en": "Juthania",
        "uz": "Jarangdor",
        "ru": "Ютания"
    },
    "97": {
        "en": "Turkish Republic of Northern Cyprus",
        "uz": "Shimoliy Kipr Turk Respublikasi",
        "ru": "Турецкая Республика Северного Кипра"
    },
    "98": {
        "en": "Kazakhstan",
        "uz": "Qozog'iston",
        "ru": "Казахстан"
    },
    "99": {
        "en": "Kenya",
        "uz": "Keniya",
        "ru": "Кения"
    },
    "100": {
        "en": "French southern and Antarctic territories",
        "uz": "Frantsuz janubi va Antarktika hududlari",
        "ru": "Французские Южные и Антарктические Территории"
    },
    "101": {
        "en": "Crying",
        "uz": "Yig'lash",
        "ru": "Плачет"
    },
    "102": {
        "en": "Kuwait",
        "uz": "Kuvayt",
        "ru": "Кувейт"
    },
    "103": {
        "en": "Kyrgyzstan",
        "uz": "Qirg'iziston",
        "ru": "Кыргизстан"
    },
    "104": {
        "en": "La",
        "uz": "Lazzat",
        "ru": "Ла"
    },
    "105": {
        "en": "Latvia",
        "uz": "Latviya",
        "ru": "Латвия"
    },
    "106": {
        "en": "Lebanon",
        "uz": "Lebanon",
        "ru": "Ливан"
    },
    "107": {
        "en": "Lesotho",
        "uz": "Lesoto",
        "ru": "Лесото"
    },
    "108": {
        "en": "Liberia",
        "uz": "Liberiya",
        "ru": "Либерия"
    },
    "109": {
        "en": "Libya",
        "uz": "Libya",
        "ru": "Ливия"
    },
    "110": {
        "en": "Lithuania",
        "uz": "Litva",
        "ru": "Литва"
    },
    "111": {
        "en": "Luxembourg",
        "uz": "Lyuksemburg",
        "ru": "Люксембург"
    },
    "112": {
        "en": "Macedonia's resolution",
        "uz": "Makedoniya rezolyutsiyasi",
        "ru": "Резолюция Македонии"
    },
    "113": {
        "en": "Madagascar",
        "uz": "Maqtanchoqlik",
        "ru": "Мадагаскар"
    },
    "114": {
        "en": "Malawi",
        "uz": "Madaviy",
        "ru": "Малави"
    },
    "115": {
        "en": "Malaysia",
        "uz": "Malayziya",
        "ru": "Малайзия"
    },
    "116": {
        "en": "Maldives",
        "uz": "Maldiv orollari",
        "ru": "Мальдивы"
    },
    "117": {
        "en": "Small",
        "uz": "Kichik",
        "ru": "Маленький"
    },
    "118": {
        "en": "Malta",
        "uz": "Malta",
        "ru": "Мальта"
    },
    "119": {
        "en": "Marshalls of the island",
        "uz": "Orolning marshalllari",
        "ru": "Маршалловы Острова"
    },
    "120": {
        "en": "Martinique",
        "uz": "Martinika",
        "ru": "Мартиника"
    },
    "121": {
        "en": "Mauritania",
        "uz": "Mauritaniya",
        "ru": "Мавритания"
    },
    "122": {
        "en": "Mauritius",
        "uz": "Mauritius",
        "ru": "Маврикий"
    },
    "123": {
        "en": "Mexico",
        "uz": "Meksika",
        "ru": "Мексика"
    },
    "124": {
        "en": "Federal states of micronzia",
        "uz": "Mikronziya federal davlatlari",
        "ru": "Федеративные Штаты Микронезии"
    },
    "125": {
        "en": "Midway",
        "uz": "O'rtada",
        "ru": "Мидуэй"
    },
    "126": {
        "en": "Moldova",
        "uz": "Moldova",
        "ru": "Молдова"
    },
    "127": {
        "en": "Monaco",
        "uz": "Monaco",
        "ru": "Монако"
    },
    "128": {
        "en": "Mongolia",
        "uz": "Mo'g'ul",
        "ru": "Монголия"
    },
    "129": {
        "en": "Montserrat",
        "uz": "Montserrrat",
        "ru": "Монтсеррат"
    },
    "130": {
        "en": "Morocco",
        "uz": "Marokash",
        "ru": "Марокко"
    },
    "131": {
        "en": "Mozambique",
        "uz": "Mozambik",
        "ru": "Мозамбик"
    },
    "132": {
        "en": "Widget",
        "uz": "Vidjet",
        "ru": "Виджет"
    },
    "133": {
        "en": "Nepal",
        "uz": "Nepal",
        "ru": "Непал"
    },
    "134": {
        "en": "The Netherlands",
        "uz": "Gollandiya",
        "ru": "Нидерланды"
    },
    "135": {
        "en": "Netherlands Antille Islands",
        "uz": "Gollandiya Anille orollar",
        "ru": "Нидерландские Антильские острова"
    },
    "136": {
        "en": "New Caledonia",
        "uz": "Yangi Kaledoniya",
        "ru": "Новая Каледония"
    },
    "137": {
        "en": "New Zealand",
        "uz": "Yangi Zelandiya",
        "ru": "Новая Зеландия"
    },
    "138": {
        "en": "Nicaragua",
        "uz": "Nikaragua",
        "ru": "Никарагуа"
    },
    "139": {
        "en": "Nyore",
        "uz": "Nyor",
        "ru": "Ньор"
    },
    "140": {
        "en": "Nigeria",
        "uz": "Nigeriya",
        "ru": "Нигерия"
    },
    "141": {
        "en": "Korean People's Democratic Republic",
        "uz": "Koreys Xalq Demokratik Respublikasi",
        "ru": "Корейская Народно-Демократическая Республика"
    },
    "142": {
        "en": "Northern Ireland",
        "uz": "Shimoliy Irlandiya",
        "ru": "Северная Ирландия"
    },
    "143": {
        "en": "Northern Mariana Islands",
        "uz": "Shimoliy Mariana orollari",
        "ru": "Северные Марианские острова"
    },
    "144": {
        "en": "Norway",
        "uz": "Norveg",
        "ru": "Норвегия"
    },
    "145": {
        "en": "Oman",
        "uz": "Omil",
        "ru": "Оман"
    },
    "146": {
        "en": "Pakistan",
        "uz": "Pokiston",
        "ru": "Пакистан"
    },
    "147": {
        "en": "Pilaf",
        "uz": "Palov",
        "ru": "Плов"
    },
    "148": {
        "en": "Palmyra",
        "uz": "Palmamir",
        "ru": "Пальмира"
    },
    "149": {
        "en": "Panama",
        "uz": "Panama",
        "ru": "Панама"
    },
    "150": {
        "en": "Papua - New Guinea",
        "uz": "Papua - yangi Gvineya",
        "ru": "Папуа — Новая Гвинея"
    },
    "151": {
        "en": "Paraguay",
        "uz": "Paragvay",
        "ru": "Парагвай"
    },
    "152": {
        "en": "Peru",
        "uz": "Peru",
        "ru": "Перу"
    },
    "153": {
        "en": "Philippines",
        "uz": "Filippin",
        "ru": "Филиппины"
    },
    "154": {
        "en": "Poland",
        "uz": "Podsho",
        "ru": "Польша"
    },
    "155": {
        "en": "Portugal",
        "uz": "Portugalcha",
        "ru": "Португалия"
    },
    "156": {
        "en": "Puerto Rico",
        "uz": "Puerto riko",
        "ru": "Пуэрто-Рико"
    },
    "157": {
        "en": "Line up",
        "uz": "Qator",
        "ru": "Расстановка"
    },
    "158": {
        "en": "Reunon",
        "uz": "Orqaga surmoq",
        "ru": "Reunon"
    },
    "159": {
        "en": "Romania",
        "uz": "Ruminiya",
        "ru": "Румыния"
    },
    "160": {
        "en": "Rwanda",
        "uz": "Ruanda",
        "ru": "Руанда"
    },
    "161": {
        "en": "The island of St. Helena",
        "uz": "Sent-Helena oroli",
        "ru": "Остров Святой Елены"
    },
    "162": {
        "en": "Saint-Vincent and Grenadines",
        "uz": "Sent-Vinsent va Granadinlar",
        "ru": "Сент-Винсент и Гренадины"
    },
    "163": {
        "en": "San-Marino",
        "uz": "Sandiq",
        "ru": "Сан-Марино"
    },
    "164": {
        "en": "Saudi Arabia",
        "uz": "Saudiya Arabistoni",
        "ru": "Саудовская Аравия"
    },
    "165": {
        "en": "Senegal",
        "uz": "Senegal",
        "ru": "Сенегал"
    },
    "166": {
        "en": "Seychelles",
        "uz": "Soyarlar",
        "ru": "Сейшельские Острова"
    },
    "167": {
        "en": "Sierra Leone",
        "uz": "Syerra-Leone",
        "ru": "Сьерра-Леоне"
    },
    "168": {
        "en": "Singapac record",
        "uz": "Singapak yozuvi",
        "ru": "Сингапак"
    },
    "169": {
        "en": "Slovakia",
        "uz": "Slovakiya",
        "ru": "Словакия"
    },
    "170": {
        "en": "Slovenia",
        "uz": "Sloveniya",
        "ru": "Словения"
    },
    "171": {
        "en": "Solomon Islands",
        "uz": "Sulaymon orollari",
        "ru": "Соломоновы Острова"
    },
    "172": {
        "en": "Somalia",
        "uz": "Soma",
        "ru": "Сомали"
    },
    "173": {
        "en": "South African Republic",
        "uz": "Janubiy Afrika Respublikasi",
        "ru": "Южно-Африканская Республика"
    },
    "174": {
        "en": "South George and Southern Sandwichev Islands",
        "uz": "Janubiy Jorj va Janubiy Sandvichev orollari",
        "ru": "Южная Георгия и Южные Сандвичевы острова"
    },
    "175": {
        "en": "Republic of Korea",
        "uz": "Koreya Respublikasi",
        "ru": "Республика Корея"
    },
    "176": {
        "en": "Spain",
        "uz": "Ispaniya",
        "ru": "Испания"
    },
    "177": {
        "en": "Sri-lanka",
        "uz": "Sri-lanka",
        "ru": "Шри-Ланка"
    },
    "178": {
        "en": "Saint-Kits and Nevis",
        "uz": "Sent-Kits va Nevis",
        "ru": "Сен-Кит и Невис"
    },
    "179": {
        "en": "Saint-Lusia",
        "uz": "Isy't-lusiya",
        "ru": "Сент-Люсия"
    },
    "180": {
        "en": "Saint-Pierre and Michelon",
        "uz": "Sankt-Per va Mishelon",
        "ru": "Сен-Пьер и Микелон"
    },
    "181": {
        "en": "Sudan",
        "uz": "Sudan",
        "ru": "Судан"
    },
    "182": {
        "en": "Suriname",
        "uz": "Surma",
        "ru": "Суринам"
    },
    "183": {
        "en": "Swaziland",
        "uz": "Schayg'iyun",
        "ru": "Свазиленд"
    },
    "184": {
        "en": "Sweden",
        "uz": "Shvetsiya",
        "ru": "Швеция"
    },
    "185": {
        "en": "Switzerland",
        "uz": "Shvitserland",
        "ru": "Швейцария"
    },
    "186": {
        "en": "Syria",
        "uz": "Suriya",
        "ru": "Сирия"
    },
    "187": {
        "en": "To calm",
        "uz": "Tinchlanmoq",
        "ru": "Чтобы успокоиться"
    },
    "188": {
        "en": "Tajikistan",
        "uz": "Tojikiston",
        "ru": "Таджикистан"
    },
    "189": {
        "en": "Tanzania",
        "uz": "Tanzaniya",
        "ru": "Танзания"
    },
    "190": {
        "en": "Thailand",
        "uz": "Tirnoq",
        "ru": "Таиланд"
    },
    "191": {
        "en": "Bahamas",
        "uz": "Baxamalar",
        "ru": "Багамские Острова"
    },
    "192": {
        "en": "Gambium",
        "uz": "Gambiya",
        "ru": "Гамбий"
    },
    "193": {
        "en": "That",
        "uz": "Bu",
        "ru": "Что"
    },
    "194": {
        "en": "Persuore",
        "uz": "Ishontirmoq",
        "ru": "Убедить"
    },
    "195": {
        "en": "Trinidad and Tobago",
        "uz": "Trinidad va Tobago",
        "ru": "Тринидад и Тобаго"
    },
    "196": {
        "en": "Tunisia",
        "uz": "Tungi",
        "ru": "Тунис"
    },
    "197": {
        "en": "Turkey",
        "uz": "Kurka",
        "ru": "Турция"
    },
    "198": {
        "en": "Turkmenistan",
        "uz": "Turkmaniston",
        "ru": "Туркмения"
    },
    "199": {
        "en": "Terx and Kaikos",
        "uz": "Terx va kayikos",
        "ru": "Теркс и Кайкос"
    },
    "200": {
        "en": "United Arab Emirates",
        "uz": "Birlashgan Arab Amirliklari",
        "ru": "Объединённые Арабские Эмираты"
    },
    "201": {
        "en": "Britain",
        "uz": "Britaniya",
        "ru": "Британия"
    },
    "202": {
        "en": "USA",
        "uz": "AQSh",
        "ru": "США"
    },
    "203": {
        "en": "Uganda",
        "uz": "Uganda",
        "ru": "Уганда"
    },
    "204": {
        "en": "Ukraine",
        "uz": "Ukrainalik",
        "ru": "Украина"
    },
    "205": {
        "en": "Uruguay",
        "uz": "Urugvay",
        "ru": "Уругвай"
    },
    "207": {
        "en": "Vanuatu",
        "uz": "VuNuatu",
        "ru": "Вануату"
    },
    "208": {
        "en": "Venezuela",
        "uz": "Venesuela",
        "ru": "Венесуэла"
    },
    "209": {
        "en": "Vietnam",
        "uz": "Vetnam",
        "ru": "Вьетнам"
    },
    "210": {
        "en": "Wake",
        "uz": "Uyg'onmoq",
        "ru": "Уэйк"
    },
    "211": {
        "en": "Pull",
        "uz": "Torting",
        "ru": "Тянуть"
    },
    "212": {
        "en": "Samo",
        "uz": "Samo",
        "ru": "Само"
    },
    "213": {
        "en": "Yemen",
        "uz": "Yaman",
        "ru": "Йемен"
    },
    "214": {
        "en": "Democratic Republic of Congo",
        "uz": "Kongo demokratik Respublikasi",
        "ru": "Демократическая Республика Конго"
    },
    "215": {
        "en": "Zambia",
        "uz": "Zambiya",
        "ru": "Замбия"
    },
    "216": {
        "en": "Zimbabwe",
        "uz": "Zimbabve",
        "ru": "Зимбабве"
    },
    "217": {
        "en": "Lichenstein",
        "uz": "Lichenshteyn",
        "ru": "Лишенштейн"
    },
    "218": {
        "en": "Kaymanov Islands",
        "uz": "Kaymanov orollari",
        "ru": "Каймановы острова"
    },
    "219": {
        "en": "Christmas Island",
        "uz": "Rojdestvo oroli",
        "ru": "Остров Рождества"
    },
    "220": {
        "en": "Kosovo",
        "uz": "Kosovo",
        "ru": "Косово"
    },
    "221": {
        "en": "Macao",
        "uz": "Makkao",
        "ru": "Макао"
    },
    "222": {
        "en": "In Mayotte",
        "uz": "Mayotte",
        "ru": "В Mayotte"
    },
    "223": {
        "en": "Montenegro",
        "uz": "Cherkov",
        "ru": "Черногория"
    },
    "224": {
        "en": "Niu",
        "uz": "Nova",
        "ru": "Ниу"
    },
    "225": {
        "en": "Palace",
        "uz": "Saroy",
        "ru": "Дворец"
    },
    "226": {
        "en": "Saint-Marten",
        "uz": "Sershom",
        "ru": "Сен-Мартен"
    },
    "227": {
        "en": "San-Tome and Principi",
        "uz": "San-Tome va tamoyil",
        "ru": "Сан-Томе и Принцип"
    },
    "228": {
        "en": "Serbia",
        "uz": "Serbiya",
        "ru": "Сербия"
    },
    "229": {
        "en": "Spitzbergen and Yang-Mayenne",
        "uz": "Spitzbergen va Yang-Mayenne",
        "ru": "Спитцберген и Ян-Майенн"
    },
    "230": {
        "en": "East Timor",
        "uz": "Sharqiy Timor",
        "ru": "Восточный Тимор"
    },
    "231": {
        "en": "Tuvala",
        "uz": "Tuvala",
        "ru": "Тувала"
    },
    "232": {
        "en": "Virgin Islands America",
        "uz": "Virjiniya orollari Amerika",
        "ru": "Виргинские острова Америка"
    },
    "233": {
        "en": "Virgin Islands",
        "uz": "Virjiniya orollari",
        "ru": "Виргинские острова"
    },
    "234": {
        "en": "Wallis and Futuna",
        "uz": "Wallis va Futuna",
        "ru": "Уоллис и Футуна"
    },
    "235": {
        "en": "Belly",
        "uz": "Qorin",
        "ru": "Живот"
    },
    "236": {
        "en": "Nauru",
        "uz": "Nobuk",
        "ru": "Науру"
    }
}


def load_countries():
    for code, names in countries.items():
        slug = names['en'].lower().replace(" ", "-").replace("_", "-")

        country, created = Country.objects.get_or_create(
            slug=slug,
            defaults={
                'name_en': names['en'],
                'name_ru': names['ru'],
                'name_uz': names['uz'],
            }
        )

        if created:
            print(f'Добавлена страна: {country.name_en} (Slug: {country.slug})')
        else:
            print(f'Обновлена страна: {country.name_en} (Slug: {country.slug})')
