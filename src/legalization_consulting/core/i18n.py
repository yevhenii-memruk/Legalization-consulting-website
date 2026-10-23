"""Translated landing-page content."""

from typing import Any

DEFAULT_LANGUAGE = "pl"

LANGUAGES = (
    {"code": "pl", "label": "PL", "name": "Polski", "locale": "pl_PL"},
    {"code": "uk", "label": "UA", "name": "Українська", "locale": "uk_UA"},
    {"code": "ru", "label": "RU", "name": "Русский", "locale": "ru_RU"},
    {"code": "en", "label": "EN", "name": "English", "locale": "en_US"},
)

PAGE_CONTENT: dict[str, dict[str, Any]] = {
    "pl": {
        "meta_title": "legalizacja i dokumenty w Polsce",
        "meta_description": (
            "Non-Stop Documents — profesjonalne wsparcie w legalizacji pobytu "
            "i sprawach urzędowych w Polsce."
        ),
        "skip_link": "Przejdź do treści",
        "home_label": "Non-Stop Documents — strona główna",
        "menu_open": "Otwórz menu",
        "menu_close": "Zamknij menu",
        "navigation_label": "Główna nawigacja",
        "language_label": "Wybór języka",
        "nav": {
            "services": "Usługi",
            "about": "O nas",
            "process": "Jak działamy",
            "faq": "FAQ",
            "consultation": "Konsultacja",
        },
        "hero": {
            "eyebrow": "Legalizacja pobytu i dokumenty w Polsce",
            "title_1": "Twoje dokumenty.",
            "title_2": "Nasze doświadczenie.",
            "lead": (
                "Pomagamy cudzoziemcom przejść przez formalności spokojnie, "
                "przejrzyście i z profesjonalnym wsparciem na każdym etapie."
            ),
            "values_label": "Nasze wartości",
            "values": [
                "Jasny plan działania",
                "Indywidualne podejście",
                "Wsparcie w Warszawie i online",
            ],
        },
        "form": {
            "kicker": "Bezpłatny pierwszy kontakt",
            "title": "Zostaw zapytanie",
            "intro": "Wypełnij formularz, a skontaktujemy się z Tobą.",
            "name_label": "Imię i nazwisko",
            "name_placeholder": "Jan Kowalski",
            "phone_label": "Numer telefonu",
            "comment_summary": "Dodaj komentarz",
            "optional": "opcjonalnie",
            "comment_label": "Twój komentarz",
            "comment_placeholder": "Opisz krótko swoją sprawę...",
            "honeypot_label": "Strona internetowa firmy",
            "privacy": "Informacje o przetwarzaniu danych:",
            "submit": "Wyślij zapytanie",
            "status_pending": "Wysyłanie zapytania…",
            "status_success": (
                "Dziękujemy. Twoje zapytanie zostało zapisane — skontaktujemy się z Tobą."
            ),
            "status_rate_limit": "Zbyt wiele prób. Spróbuj ponownie za kilka minut.",
            "status_validation": "Sprawdź poprawność imienia i numeru telefonu.",
            "status_unavailable": (
                "Formularz jest chwilowo niedostępny. Spróbuj ponownie później."
            ),
            "status_connection": (
                "Nie udało się połączyć z serwerem. Sprawdź połączenie i spróbuj ponownie."
            ),
        },
        "trust": {
            "label": "Zakres wsparcia",
            "items": [
                "Wsparcie w sprawach urzędowych",
                "Dokumenty przygotowane krok po kroku",
                "Konsultacje stacjonarne i online",
            ],
        },
        "services": {
            "kicker": "Nasze usługi",
            "title": "Pomoc w najważniejszych formalnościach",
            "intro": (
                "Każdą sprawę zaczynamy od poznania Twojej sytuacji i ustalenia "
                "jasnego zakresu dalszych działań."
            ),
            "cta": "Zapytaj o usługę",
            "items": [
                {
                    "title": "Karta pobytu",
                    "description": (
                        "Wsparcie przy przygotowaniu dokumentów i przejściu przez "
                        "kolejne etapy postępowania."
                    ),
                },
                {
                    "title": "PESEL",
                    "description": (
                        "Pomoc w przygotowaniu danych i dokumentów potrzebnych do złożenia wniosku."
                    ),
                },
                {
                    "title": "Niebieska Karta UE",
                    "description": (
                        "Uporządkowanie dokumentacji i wsparcie informacyjne dla "
                        "wykwalifikowanych pracowników."
                    ),
                },
                {
                    "title": "Obywatelstwo",
                    "description": (
                        "Wstępna analiza sytuacji oraz pomoc w skompletowaniu "
                        "wymaganej dokumentacji."
                    ),
                },
                {
                    "title": "Tłumaczenie prawa jazdy",
                    "description": (
                        "Wsparcie w organizacji tłumaczenia oraz przygotowaniu "
                        "dokumentów do dalszych formalności."
                    ),
                },
            ],
        },
        "about": {
            "image_alt": "Panorama centrum Warszawy",
            "photo": "Zdjęcie",
            "kicker": "O nas",
            "title": "Formalności bez niepotrzebnego chaosu",
            "lead": (
                "Non-Stop Documents wspiera cudzoziemców w sprawach związanych "
                "z pobytem i dokumentami w Polsce."
            ),
            "body": (
                "Zamiast uniwersalnych obietnic oferujemy uporządkowany proces: "
                "poznajemy sytuację, wyjaśniamy kolejne kroki i pomagamy "
                "przygotować potrzebne dokumenty."
            ),
            "values": [
                {"title": "Przejrzystość", "text": "Wiesz, jaki jest następny krok."},
                {"title": "Uważność", "text": "Każda sytuacja wymaga osobnej analizy."},
                {
                    "title": "Kontakt",
                    "text": "Pozostajemy w kontakcie podczas współpracy.",
                },
            ],
        },
        "process": {
            "kicker": "Jak działamy",
            "title": "Cztery przejrzyste kroki",
            "intro": "Od pierwszego kontaktu do uporządkowanego planu dalszego działania.",
            "items": [
                {
                    "title": "Zostaw zapytanie",
                    "text": "Podaj podstawowe dane i krótko opisz swoją sprawę.",
                },
                {
                    "title": "Konsultacja",
                    "text": "Poznajemy sytuację i odpowiadamy na najważniejsze pytania.",
                },
                {
                    "title": "Przygotowanie",
                    "text": "Ustalamy listę dokumentów oraz kolejne działania.",
                },
                {
                    "title": "Wsparcie",
                    "text": "Pomagamy przejść przez uzgodniony zakres formalności.",
                },
            ],
        },
        "reviews": {
            "kicker": "Opinie klientów",
            "title": "Zaufanie budujemy na realnych doświadczeniach",
            "placeholder": (
                "W tym miejscu opublikujemy wyłącznie zweryfikowane opinie klientów. "
                "Nie tworzymy fikcyjnych rekomendacji."
            ),
        },
        "faq": {
            "kicker": "FAQ",
            "title": "Najczęściej zadawane pytania",
            "intro": "Nie widzisz odpowiedzi? Zostaw zapytanie, a wrócimy do Ciebie.",
            "cta": "Przejdź do formularza",
            "items": [
                {
                    "question": "Jakie dokumenty będą potrzebne?",
                    "answer": (
                        "Lista zależy od rodzaju sprawy i Twojej sytuacji. Po pierwszym "
                        "kontakcie przygotujemy indywidualną listę dokumentów."
                    ),
                },
                {
                    "question": "Czy konsultacja może odbyć się online?",
                    "answer": (
                        "Tak. Zakres i dogodną formę konsultacji ustalamy podczas "
                        "pierwszego kontaktu."
                    ),
                },
                {
                    "question": "Ile trwa załatwienie sprawy?",
                    "answer": (
                        "Czas zależy od rodzaju postępowania, kompletności dokumentów "
                        "oraz pracy właściwego urzędu. Nie obiecujemy nierealnych terminów."
                    ),
                },
                {
                    "question": "W jakich językach dostępna jest obsługa?",
                    "answer": (
                        "Strona i formularz są dostępne po polsku, ukraińsku, rosyjsku i angielsku."
                    ),
                },
            ],
        },
        "final_cta": {
            "kicker": "Zacznijmy od rozmowy",
            "title": "Opowiedz nam o swojej sprawie",
            "button": "Zostaw zapytanie",
        },
        "footer": {
            "description": "Wsparcie w legalizacji pobytu i dokumentach w Polsce.",
            "navigation": "Nawigacja",
            "contact": "Kontakt",
            "location": "Warszawa, Polska",
            "privacy": "Polityka prywatności",
        },
    },
    "uk": {
        "meta_title": "легалізація та документи в Польщі",
        "meta_description": (
            "Non-Stop Documents — професійна підтримка в легалізації перебування "
            "та вирішенні офіційних питань у Польщі."
        ),
        "skip_link": "Перейти до вмісту",
        "home_label": "Non-Stop Documents — головна сторінка",
        "menu_open": "Відкрити меню",
        "menu_close": "Закрити меню",
        "navigation_label": "Головна навігація",
        "language_label": "Вибір мови",
        "nav": {
            "services": "Послуги",
            "about": "Про нас",
            "process": "Як ми працюємо",
            "faq": "FAQ",
            "consultation": "Консультація",
        },
        "hero": {
            "eyebrow": "Легалізація перебування та документи в Польщі",
            "title_1": "Ваші документи.",
            "title_2": "Наш досвід.",
            "lead": (
                "Допомагаємо іноземцям пройти формальності спокійно, зрозуміло "
                "та з професійною підтримкою на кожному етапі."
            ),
            "values_label": "Наші цінності",
            "values": [
                "Чіткий план дій",
                "Індивідуальний підхід",
                "Підтримка у Варшаві та онлайн",
            ],
        },
        "form": {
            "kicker": "Безкоштовний перший контакт",
            "title": "Залиште запит",
            "intro": "Заповніть форму, і ми зв’яжемося з вами.",
            "name_label": "Ім’я та прізвище",
            "name_placeholder": "Іван Коваленко",
            "phone_label": "Номер телефону",
            "comment_summary": "Додати коментар",
            "optional": "необов’язково",
            "comment_label": "Ваш коментар",
            "comment_placeholder": "Коротко опишіть вашу справу...",
            "honeypot_label": "Вебсайт компанії",
            "privacy": "Інформація про обробку даних:",
            "submit": "Надіслати запит",
            "status_pending": "Надсилання запиту…",
            "status_success": "Дякуємо. Ваш запит збережено — ми зв’яжемося з вами.",
            "status_rate_limit": "Забагато спроб. Спробуйте ще раз за кілька хвилин.",
            "status_validation": "Перевірте правильність імені та номера телефону.",
            "status_unavailable": "Форма тимчасово недоступна. Спробуйте пізніше.",
            "status_connection": (
                "Не вдалося з’єднатися із сервером. Перевірте з’єднання та спробуйте ще раз."
            ),
        },
        "trust": {
            "label": "Сфера підтримки",
            "items": [
                "Підтримка в офіційних питаннях",
                "Підготовка документів крок за кроком",
                "Особисті та онлайн-консультації",
            ],
        },
        "services": {
            "kicker": "Наші послуги",
            "title": "Допомога з найважливішими формальностями",
            "intro": (
                "Кожну справу починаємо зі знайомства з вашою ситуацією та "
                "визначення чіткого плану подальших дій."
            ),
            "cta": "Запитати про послугу",
            "items": [
                {
                    "title": "Карта побиту",
                    "description": (
                        "Підтримка в підготовці документів і проходженні наступних "
                        "етапів процедури."
                    ),
                },
                {
                    "title": "PESEL",
                    "description": (
                        "Допомога в підготовці даних і документів, необхідних для подання заяви."
                    ),
                },
                {
                    "title": "Блакитна карта ЄС",
                    "description": (
                        "Упорядкування документів та інформаційна підтримка "
                        "кваліфікованих працівників."
                    ),
                },
                {
                    "title": "Громадянство",
                    "description": (
                        "Попередній аналіз ситуації та допомога в підготовці необхідних документів."
                    ),
                },
                {
                    "title": "Переклад водійського посвідчення",
                    "description": (
                        "Підтримка в організації перекладу та підготовці документів "
                        "для подальших формальностей."
                    ),
                },
            ],
        },
        "about": {
            "image_alt": "Панорама центру Варшави",
            "photo": "Фото",
            "kicker": "Про нас",
            "title": "Формальності без зайвого хаосу",
            "lead": (
                "Non-Stop Documents підтримує іноземців у питаннях перебування "
                "та документів у Польщі."
            ),
            "body": (
                "Замість універсальних обіцянок ми пропонуємо впорядкований процес: "
                "вивчаємо ситуацію, пояснюємо наступні кроки та допомагаємо "
                "підготувати необхідні документи."
            ),
            "values": [
                {"title": "Прозорість", "text": "Ви знаєте, яким буде наступний крок."},
                {"title": "Уважність", "text": "Кожна ситуація потребує окремого аналізу."},
                {
                    "title": "Зв’язок",
                    "text": "Ми залишаємося на зв’язку під час співпраці.",
                },
            ],
        },
        "process": {
            "kicker": "Як ми працюємо",
            "title": "Чотири зрозумілі кроки",
            "intro": "Від першого контакту до впорядкованого плану подальших дій.",
            "items": [
                {
                    "title": "Залиште запит",
                    "text": "Вкажіть основні дані та коротко опишіть вашу справу.",
                },
                {
                    "title": "Консультація",
                    "text": "Вивчаємо ситуацію та відповідаємо на головні запитання.",
                },
                {
                    "title": "Підготовка",
                    "text": "Визначаємо перелік документів і наступні дії.",
                },
                {
                    "title": "Підтримка",
                    "text": "Допомагаємо пройти погоджений обсяг формальностей.",
                },
            ],
        },
        "reviews": {
            "kicker": "Відгуки клієнтів",
            "title": "Ми будуємо довіру на реальному досвіді",
            "placeholder": (
                "Тут ми публікуватимемо лише перевірені відгуки клієнтів. "
                "Ми не створюємо вигаданих рекомендацій."
            ),
        },
        "faq": {
            "kicker": "FAQ",
            "title": "Поширені запитання",
            "intro": "Не знайшли відповіді? Залиште запит, і ми зв’яжемося з вами.",
            "cta": "Перейти до форми",
            "items": [
                {
                    "question": "Які документи будуть потрібні?",
                    "answer": (
                        "Перелік залежить від виду справи та вашої ситуації. Після "
                        "першого контакту ми підготуємо індивідуальний список документів."
                    ),
                },
                {
                    "question": "Чи може консультація відбутися онлайн?",
                    "answer": (
                        "Так. Обсяг і зручний формат консультації узгодимо під час "
                        "першого контакту."
                    ),
                },
                {
                    "question": "Скільки часу займає вирішення справи?",
                    "answer": (
                        "Строк залежить від виду процедури, повноти документів і роботи "
                        "відповідної установи. Ми не обіцяємо нереалістичних строків."
                    ),
                },
                {
                    "question": "Якими мовами доступне обслуговування?",
                    "answer": (
                        "Сайт і форма доступні польською, українською, російською "
                        "та англійською мовами."
                    ),
                },
            ],
        },
        "final_cta": {
            "kicker": "Почнімо з розмови",
            "title": "Розкажіть нам про вашу справу",
            "button": "Залишити запит",
        },
        "footer": {
            "description": "Підтримка в легалізації перебування та документах у Польщі.",
            "navigation": "Навігація",
            "contact": "Контакти",
            "location": "Варшава, Польща",
            "privacy": "Політика конфіденційності",
        },
    },
    "ru": {
        "meta_title": "легализация и документы в Польше",
        "meta_description": (
            "Non-Stop Documents — профессиональная поддержка в легализации пребывания "
            "и решении официальных вопросов в Польше."
        ),
        "skip_link": "Перейти к содержимому",
        "home_label": "Non-Stop Documents — главная страница",
        "menu_open": "Открыть меню",
        "menu_close": "Закрыть меню",
        "navigation_label": "Основная навигация",
        "language_label": "Выбор языка",
        "nav": {
            "services": "Услуги",
            "about": "О нас",
            "process": "Как мы работаем",
            "faq": "FAQ",
            "consultation": "Консультация",
        },
        "hero": {
            "eyebrow": "Легализация пребывания и документы в Польше",
            "title_1": "Ваши документы.",
            "title_2": "Наш опыт.",
            "lead": (
                "Помогаем иностранцам пройти формальности спокойно, понятно "
                "и с профессиональной поддержкой на каждом этапе."
            ),
            "values_label": "Наши ценности",
            "values": [
                "Понятный план действий",
                "Индивидуальный подход",
                "Поддержка в Варшаве и онлайн",
            ],
        },
        "form": {
            "kicker": "Бесплатный первый контакт",
            "title": "Оставьте заявку",
            "intro": "Заполните форму, и мы свяжемся с вами.",
            "name_label": "Имя и фамилия",
            "name_placeholder": "Иван Коваленко",
            "phone_label": "Номер телефона",
            "comment_summary": "Добавить комментарий",
            "optional": "необязательно",
            "comment_label": "Ваш комментарий",
            "comment_placeholder": "Кратко опишите вашу ситуацию...",
            "honeypot_label": "Сайт компании",
            "privacy": "Информация об обработке данных:",
            "submit": "Отправить заявку",
            "status_pending": "Отправка заявки…",
            "status_success": "Спасибо. Ваша заявка сохранена — мы свяжемся с вами.",
            "status_rate_limit": "Слишком много попыток. Повторите через несколько минут.",
            "status_validation": "Проверьте правильность имени и номера телефона.",
            "status_unavailable": "Форма временно недоступна. Попробуйте позже.",
            "status_connection": (
                "Не удалось подключиться к серверу. Проверьте соединение и повторите попытку."
            ),
        },
        "trust": {
            "label": "Область поддержки",
            "items": [
                "Поддержка в официальных вопросах",
                "Подготовка документов шаг за шагом",
                "Очные и онлайн-консультации",
            ],
        },
        "services": {
            "kicker": "Наши услуги",
            "title": "Помощь с важнейшими формальностями",
            "intro": (
                "Каждое дело мы начинаем с изучения вашей ситуации и определения "
                "понятного плана дальнейших действий."
            ),
            "cta": "Спросить об услуге",
            "items": [
                {
                    "title": "Карта побыту",
                    "description": (
                        "Поддержка в подготовке документов и прохождении следующих "
                        "этапов процедуры."
                    ),
                },
                {
                    "title": "PESEL",
                    "description": (
                        "Помощь в подготовке данных и документов, необходимых для подачи заявления."
                    ),
                },
                {
                    "title": "Голубая карта ЕС",
                    "description": (
                        "Упорядочивание документов и информационная поддержка "
                        "квалифицированных работников."
                    ),
                },
                {
                    "title": "Гражданство",
                    "description": (
                        "Предварительный анализ ситуации и помощь в подготовке "
                        "необходимых документов."
                    ),
                },
                {
                    "title": "Перевод водительского удостоверения",
                    "description": (
                        "Помощь в организации перевода и подготовке документов "
                        "для дальнейших формальностей."
                    ),
                },
            ],
        },
        "about": {
            "image_alt": "Панорама центра Варшавы",
            "photo": "Фото",
            "kicker": "О нас",
            "title": "Формальности без лишнего хаоса",
            "lead": (
                "Non-Stop Documents поддерживает иностранцев в вопросах пребывания "
                "и документов в Польше."
            ),
            "body": (
                "Вместо универсальных обещаний мы предлагаем упорядоченный процесс: "
                "изучаем ситуацию, объясняем следующие шаги и помогаем подготовить документы."
            ),
            "values": [
                {"title": "Прозрачность", "text": "Вы знаете, каким будет следующий шаг."},
                {"title": "Внимательность", "text": "Каждая ситуация требует анализа."},
                {"title": "Связь", "text": "Мы остаёмся на связи во время сотрудничества."},
            ],
        },
        "process": {
            "kicker": "Как мы работаем",
            "title": "Четыре понятных шага",
            "intro": "От первого контакта до упорядоченного плана дальнейших действий.",
            "items": [
                {
                    "title": "Оставьте заявку",
                    "text": "Укажите основные данные и кратко опишите вашу ситуацию.",
                },
                {
                    "title": "Консультация",
                    "text": "Изучаем ситуацию и отвечаем на главные вопросы.",
                },
                {
                    "title": "Подготовка",
                    "text": "Определяем список документов и последующие действия.",
                },
                {
                    "title": "Поддержка",
                    "text": "Помогаем пройти согласованный объём формальностей.",
                },
            ],
        },
        "reviews": {
            "kicker": "Отзывы клиентов",
            "title": "Мы строим доверие на реальном опыте",
            "placeholder": (
                "Здесь мы опубликуем только проверенные отзывы клиентов. "
                "Мы не создаём вымышленных рекомендаций."
            ),
        },
        "faq": {
            "kicker": "FAQ",
            "title": "Часто задаваемые вопросы",
            "intro": "Не нашли ответ? Оставьте заявку, и мы свяжемся с вами.",
            "cta": "Перейти к форме",
            "items": [
                {
                    "question": "Какие документы потребуются?",
                    "answer": (
                        "Список зависит от типа дела и вашей ситуации. После первого "
                        "контакта мы подготовим индивидуальный перечень документов."
                    ),
                },
                {
                    "question": "Можно ли провести консультацию онлайн?",
                    "answer": (
                        "Да. Объём и удобный формат консультации согласуем во время "
                        "первого контакта."
                    ),
                },
                {
                    "question": "Сколько времени занимает решение вопроса?",
                    "answer": (
                        "Срок зависит от вида процедуры, полноты документов и работы "
                        "соответствующего учреждения. Мы не обещаем нереалистичных сроков."
                    ),
                },
                {
                    "question": "На каких языках доступно обслуживание?",
                    "answer": (
                        "Сайт и форма доступны на польском, украинском, русском "
                        "и английском языках."
                    ),
                },
            ],
        },
        "final_cta": {
            "kicker": "Начнём с разговора",
            "title": "Расскажите нам о вашей ситуации",
            "button": "Оставить заявку",
        },
        "footer": {
            "description": "Поддержка в легализации пребывания и документах в Польше.",
            "navigation": "Навигация",
            "contact": "Контакты",
            "location": "Варшава, Польша",
            "privacy": "Политика конфиденциальности",
        },
    },
    "en": {
        "meta_title": "legalization and documents in Poland",
        "meta_description": (
            "Non-Stop Documents — professional support with residence legalization "
            "and official matters in Poland."
        ),
        "skip_link": "Skip to content",
        "home_label": "Non-Stop Documents — home page",
        "menu_open": "Open menu",
        "menu_close": "Close menu",
        "navigation_label": "Main navigation",
        "language_label": "Choose language",
        "nav": {
            "services": "Services",
            "about": "About us",
            "process": "How we work",
            "faq": "FAQ",
            "consultation": "Consultation",
        },
        "hero": {
            "eyebrow": "Residence legalization and documents in Poland",
            "title_1": "Your documents.",
            "title_2": "Our experience.",
            "lead": (
                "We help foreigners handle formalities calmly and clearly, with "
                "professional support at every stage."
            ),
            "values_label": "Our values",
            "values": [
                "A clear plan of action",
                "An individual approach",
                "Support in Warsaw and online",
            ],
        },
        "form": {
            "kicker": "Free initial contact",
            "title": "Send an enquiry",
            "intro": "Complete the form and we will contact you.",
            "name_label": "Full name",
            "name_placeholder": "John Smith",
            "phone_label": "Phone number",
            "comment_summary": "Add a comment",
            "optional": "optional",
            "comment_label": "Your comment",
            "comment_placeholder": "Briefly describe your case...",
            "honeypot_label": "Company website",
            "privacy": "Information about personal data processing:",
            "submit": "Send enquiry",
            "status_pending": "Sending your enquiry…",
            "status_success": "Thank you. Your enquiry has been saved — we will contact you.",
            "status_rate_limit": "Too many attempts. Please try again in a few minutes.",
            "status_validation": "Check your name and phone number.",
            "status_unavailable": "The form is temporarily unavailable. Please try again later.",
            "status_connection": (
                "Could not connect to the server. Check your connection and try again."
            ),
        },
        "trust": {
            "label": "Scope of support",
            "items": [
                "Support with official matters",
                "Documents prepared step by step",
                "In-person and online consultations",
            ],
        },
        "services": {
            "kicker": "Our services",
            "title": "Help with essential formalities",
            "intro": (
                "We begin every case by understanding your situation and defining "
                "a clear scope for the next steps."
            ),
            "cta": "Ask about this service",
            "items": [
                {
                    "title": "Residence permit",
                    "description": (
                        "Support with preparing documents and navigating each stage "
                        "of the procedure."
                    ),
                },
                {
                    "title": "PESEL",
                    "description": (
                        "Help with preparing the information and documents required "
                        "for an application."
                    ),
                },
                {
                    "title": "EU Blue Card",
                    "description": (
                        "Document organization and practical guidance for qualified professionals."
                    ),
                },
                {
                    "title": "Citizenship",
                    "description": (
                        "An initial assessment of your situation and help assembling "
                        "the required documents."
                    ),
                },
                {
                    "title": "Driving licence translation",
                    "description": (
                        "Support with arranging a translation and preparing documents "
                        "for the next formal steps."
                    ),
                },
            ],
        },
        "about": {
            "image_alt": "Panorama of central Warsaw",
            "photo": "Photo",
            "kicker": "About us",
            "title": "Formalities without unnecessary confusion",
            "lead": (
                "Non-Stop Documents supports foreigners with residence and document "
                "matters in Poland."
            ),
            "body": (
                "Instead of one-size-fits-all promises, we offer an organized process: "
                "we understand your situation, explain the next steps and help prepare "
                "the necessary documents."
            ),
            "values": [
                {"title": "Clarity", "text": "You know what the next step is."},
                {"title": "Attention", "text": "Every situation requires its own assessment."},
                {"title": "Communication", "text": "We stay in touch throughout our work."},
            ],
        },
        "process": {
            "kicker": "How we work",
            "title": "Four clear steps",
            "intro": "From initial contact to an organized plan for what comes next.",
            "items": [
                {
                    "title": "Send an enquiry",
                    "text": "Provide your basic details and briefly describe your case.",
                },
                {
                    "title": "Consultation",
                    "text": "We learn about your situation and answer the key questions.",
                },
                {
                    "title": "Preparation",
                    "text": "We define the document list and the next steps.",
                },
                {
                    "title": "Support",
                    "text": "We help you through the agreed scope of formalities.",
                },
            ],
        },
        "reviews": {
            "kicker": "Client reviews",
            "title": "We build trust on real experiences",
            "placeholder": (
                "Only verified client reviews will be published here. "
                "We do not create fictional recommendations."
            ),
        },
        "faq": {
            "kicker": "FAQ",
            "title": "Frequently asked questions",
            "intro": "Cannot find the answer? Send an enquiry and we will get back to you.",
            "cta": "Go to the form",
            "items": [
                {
                    "question": "Which documents will I need?",
                    "answer": (
                        "The list depends on the type of case and your circumstances. "
                        "After the initial contact, we will prepare an individual document list."
                    ),
                },
                {
                    "question": "Can the consultation take place online?",
                    "answer": (
                        "Yes. We agree on the scope and a convenient consultation format "
                        "during the initial contact."
                    ),
                },
                {
                    "question": "How long does the process take?",
                    "answer": (
                        "The timing depends on the procedure, completeness of the documents "
                        "and the relevant authority. We do not promise unrealistic deadlines."
                    ),
                },
                {
                    "question": "Which languages are supported?",
                    "answer": (
                        "The website and enquiry form are available in Polish, Ukrainian, "
                        "Russian and English."
                    ),
                },
            ],
        },
        "final_cta": {
            "kicker": "Let’s start with a conversation",
            "title": "Tell us about your case",
            "button": "Send an enquiry",
        },
        "footer": {
            "description": "Support with residence legalization and documents in Poland.",
            "navigation": "Navigation",
            "contact": "Contact",
            "location": "Warsaw, Poland",
            "privacy": "Privacy policy",
        },
    },
}


def get_page_content(language: str | None) -> tuple[str, dict[str, Any]]:
    """Return a supported language and its content, falling back to Polish."""
    selected_language = language if language in PAGE_CONTENT else DEFAULT_LANGUAGE
    return selected_language, PAGE_CONTENT[selected_language]
