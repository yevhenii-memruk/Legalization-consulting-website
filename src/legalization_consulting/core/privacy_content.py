"""Localized privacy information for the public website."""

from typing import Any

PRIVACY_CONTENT: dict[str, dict[str, Any]] = {
    "pl": {
        "meta_title": "Polityka prywatności",
        "title": "Polityka prywatności",
        "intro": (
            "Poniżej wyjaśniamy, jakie dane zbieramy przez formularz kontaktowy, "
            "w jakim celu je wykorzystujemy oraz jakie prawa Ci przysługują."
        ),
        "updated": "Ostatnia aktualizacja: 23 października 2026 r.",
        "back_home": "Wróć na stronę główną",
        "controller": {
            "title": "1. Administrator danych",
            "text": "Administratorem danych osobowych jest:",
        },
        "data": {
            "title": "2. Jakie dane przetwarzamy",
            "intro": "Za pośrednictwem formularza możemy otrzymać:",
            "items": [
                "imię i nazwisko",
                "numer telefonu",
                "opcjonalny komentarz dotyczący sprawy",
                "język wybrany na stronie",
            ],
            "technical": (
                "Adres sieciowy urządzenia jest wykorzystywany krótkotrwale w pamięci "
                "aplikacji wyłącznie do ograniczania nadużyć. Nie zapisujemy go w arkuszu z zapytaniami."
            ),
        },
        "purpose": {
            "title": "3. Cele i podstawy przetwarzania",
            "items": [
                (
                    "udzielenie odpowiedzi na zapytanie i podjęcie działań na Twoje "
                    "żądanie przed ewentualnym zawarciem umowy — art. 6 ust. 1 lit. b RODO"
                ),
                (
                    "ochrona formularza przed nadużyciami oraz ustalenie, dochodzenie "
                    "lub obrona roszczeń — uzasadniony interes administratora, "
                    "art. 6 ust. 1 lit. f RODO"
                ),
            ],
        },
        "retention": {
            "title": "4. Okres przechowywania",
            "text": (
                "Dane z zapytania przechowujemy maksymalnie przez 12 miesięcy od "
                "ostatniego kontaktu. Możemy usunąć je wcześniej, gdy nie są już potrzebne "
                "lub gdy skutecznie zażądasz usunięcia. Jeśli rozpocznie się współpraca, "
                "dane związane z umową mogą podlegać innym terminom wynikającym z prawa "
                "lub potrzeby ochrony roszczeń."
            ),
        },
        "recipients": {
            "title": "5. Odbiorcy danych",
            "text": (
                "Dostęp do danych mogą otrzymać osoby upoważnione przez administratora "
                "oraz dostawcy wspierający działanie strony. Zapytania są przechowywane "
                "w usłudze Google Sheets. Po publikacji strony odbiorcą technicznym może "
                "być również wybrany dostawca hostingu."
            ),
        },
        "rights": {
            "title": "6. Twoje prawa",
            "intro": "W zakresie przewidzianym przez RODO możesz żądać:",
            "items": [
                "dostępu do danych i otrzymania ich kopii",
                "sprostowania lub uzupełnienia danych",
                "usunięcia danych lub ograniczenia przetwarzania",
                "przeniesienia danych, jeżeli ma zastosowanie",
                "wniesienia sprzeciwu wobec przetwarzania opartego na uzasadnionym interesie",
            ],
            "complaint": (
                "Masz również prawo wnieść skargę do Prezesa Urzędu Ochrony Danych "
                "Osobowych (UODO)."
            ),
        },
        "required": {
            "title": "7. Dobrowolność podania danych",
            "text": (
                "Podanie danych jest dobrowolne, ale imię i nazwisko oraz numer telefonu "
                "są potrzebne, abyśmy mogli odpowiedzieć na zapytanie. Komentarz jest opcjonalny."
            ),
        },
        "automation": {
            "title": "8. Automatyczne decyzje i analityka",
            "text": (
                "Nie podejmujemy wobec Ciebie decyzji w sposób zautomatyzowany i nie "
                "profilujemy użytkowników. Obecnie strona nie korzysta z narzędzi "
                "analitycznych ani marketingowych plików cookie."
            ),
        },
        "contact": {
            "title": "9. Kontakt w sprawach danych",
            "text": (
                "Aby skorzystać ze swoich praw lub zadać pytanie dotyczące prywatności, "
                "napisz na adres:"
            ),
        },
    },
    "uk": {
        "meta_title": "Політика конфіденційності",
        "title": "Політика конфіденційності",
        "intro": (
            "Нижче пояснюємо, які дані збираємо через контактну форму, навіщо їх "
            "використовуємо та які права ви маєте."
        ),
        "updated": "Останнє оновлення: 23 жовтня 2026 року",
        "back_home": "Повернутися на головну",
        "controller": {
            "title": "1. Адміністратор даних",
            "text": "Адміністратором персональних даних є:",
        },
        "data": {
            "title": "2. Які дані ми обробляємо",
            "intro": "Через форму ми можемо отримати:",
            "items": [
                "ім’я та прізвище",
                "номер телефону",
                "необов’язковий коментар щодо справи",
                "мову, обрану на сайті",
            ],
            "technical": (
                "Мережева адреса пристрою короткочасно використовується в пам’яті "
                "застосунку лише для обмеження зловживань. Ми не записуємо її до таблиці запитів."
            ),
        },
        "purpose": {
            "title": "3. Цілі та правові підстави",
            "items": [
                (
                    "відповідь на запит і вчинення дій на вашу вимогу до можливого "
                    "укладення договору — ст. 6(1)(b) GDPR"
                ),
                (
                    "захист форми від зловживань, а також встановлення, заявлення або "
                    "захист правових вимог — законний інтерес адміністратора, ст. 6(1)(f) GDPR"
                ),
            ],
        },
        "retention": {
            "title": "4. Строк зберігання",
            "text": (
                "Дані із запиту зберігаються не довше 12 місяців від останнього контакту. "
                "Ми можемо видалити їх раніше, якщо вони більше не потрібні або якщо ви "
                "обґрунтовано попросите про видалення. Якщо почнеться співпраця, до даних, "
                "пов’язаних із договором, можуть застосовуватися інші строки, передбачені "
                "законом або необхідністю захисту правових вимог."
            ),
        },
        "recipients": {
            "title": "5. Одержувачі даних",
            "text": (
                "Доступ до даних можуть мати уповноважені адміністратором особи та "
                "постачальники, які забезпечують роботу сайту. Запити зберігаються в "
                "Google Sheets. Після публікації сайту технічним одержувачем також може "
                "бути обраний постачальник хостингу."
            ),
        },
        "rights": {
            "title": "6. Ваші права",
            "intro": "У межах, передбачених GDPR, ви можете вимагати:",
            "items": [
                "доступу до даних та отримання їх копії",
                "виправлення або доповнення даних",
                "видалення даних або обмеження обробки",
                "перенесення даних, якщо це застосовно",
                "заперечення проти обробки на підставі законного інтересу",
            ],
            "complaint": (
                "Ви також маєте право подати скаргу Голові Управління захисту "
                "персональних даних Польщі (UODO)."
            ),
        },
        "required": {
            "title": "7. Добровільність надання даних",
            "text": (
                "Надання даних є добровільним, але ім’я, прізвище та номер телефону "
                "потрібні, щоб ми могли відповісти на запит. Коментар необов’язковий."
            ),
        },
        "automation": {
            "title": "8. Автоматичні рішення та аналітика",
            "text": (
                "Ми не приймаємо щодо вас автоматизованих рішень і не профілюємо "
                "користувачів. Наразі сайт не використовує аналітичних інструментів "
                "або маркетингових cookie."
            ),
        },
        "contact": {
            "title": "9. Контакт із питань даних",
            "text": (
                "Щоб скористатися своїми правами або поставити запитання щодо "
                "конфіденційності, напишіть на адресу:"
            ),
        },
    },
    "ru": {
        "meta_title": "Политика конфиденциальности",
        "title": "Политика конфиденциальности",
        "intro": (
            "Ниже мы объясняем, какие данные собираем через контактную форму, "
            "для чего их используем и какие права у вас есть."
        ),
        "updated": "Последнее обновление: 23 октября 2026 года",
        "back_home": "Вернуться на главную",
        "controller": {
            "title": "1. Администратор данных",
            "text": "Администратором персональных данных является:",
        },
        "data": {
            "title": "2. Какие данные мы обрабатываем",
            "intro": "Через форму мы можем получить:",
            "items": [
                "имя и фамилию",
                "номер телефона",
                "необязательный комментарий по вопросу",
                "выбранный на сайте язык",
            ],
            "technical": (
                "Сетевой адрес устройства кратковременно используется в памяти "
                "приложения только для ограничения злоупотреблений. Мы не записываем "
                "его в таблицу с заявками."
            ),
        },
        "purpose": {
            "title": "3. Цели и правовые основания",
            "items": [
                (
                    "ответ на заявку и действия по вашему запросу до возможного "
                    "заключения договора — ст. 6(1)(b) GDPR"
                ),
                (
                    "защита формы от злоупотреблений, а также установление, предъявление "
                    "или защита правовых требований — законный интерес администратора, "
                    "ст. 6(1)(f) GDPR"
                ),
            ],
        },
        "retention": {
            "title": "4. Срок хранения",
            "text": (
                "Данные заявки хранятся не более 12 месяцев с момента последнего контакта. "
                "Мы можем удалить их раньше, если они больше не нужны или если вы "
                "обоснованно потребуете удаления. Если начнётся сотрудничество, для данных, "
                "связанных с договором, могут действовать другие сроки, установленные "
                "законом или необходимые для защиты правовых требований."
            ),
        },
        "recipients": {
            "title": "5. Получатели данных",
            "text": (
                "Доступ к данным могут иметь уполномоченные администратором лица и "
                "поставщики, поддерживающие работу сайта. Заявки хранятся в Google Sheets. "
                "После публикации сайта техническим получателем также может стать "
                "выбранный поставщик хостинга."
            ),
        },
        "rights": {
            "title": "6. Ваши права",
            "intro": "В предусмотренных GDPR случаях вы можете потребовать:",
            "items": [
                "доступ к данным и получение их копии",
                "исправление или дополнение данных",
                "удаление данных или ограничение обработки",
                "перенос данных, если это применимо",
                "возражение против обработки на основании законного интереса",
            ],
            "complaint": (
                "Вы также вправе подать жалобу Председателю Управления по защите "
                "персональных данных Польши (UODO)."
            ),
        },
        "required": {
            "title": "7. Добровольность предоставления данных",
            "text": (
                "Предоставление данных добровольно, но имя, фамилия и номер телефона "
                "необходимы, чтобы мы могли ответить на заявку. Комментарий необязателен."
            ),
        },
        "automation": {
            "title": "8. Автоматические решения и аналитика",
            "text": (
                "Мы не принимаем в отношении вас автоматизированных решений и не "
                "профилируем пользователей. Сейчас сайт не использует аналитические "
                "инструменты или маркетинговые cookie."
            ),
        },
        "contact": {
            "title": "9. Контакт по вопросам данных",
            "text": (
                "Чтобы воспользоваться своими правами или задать вопрос о "
                "конфиденциальности, напишите по адресу:"
            ),
        },
    },
    "en": {
        "meta_title": "Privacy policy",
        "title": "Privacy policy",
        "intro": (
            "This page explains what data we collect through the enquiry form, "
            "why we use it and what rights you have."
        ),
        "updated": "Last updated: 23 October 2026",
        "back_home": "Return to the home page",
        "controller": {
            "title": "1. Data controller",
            "text": "The controller of your personal data is:",
        },
        "data": {
            "title": "2. Data we process",
            "intro": "Through the form we may receive:",
            "items": [
                "your full name",
                "your phone number",
                "an optional comment about your case",
                "the language selected on the website",
            ],
            "technical": (
                "Your device network address is used briefly in application memory only "
                "to limit abuse. We do not save it in the enquiry spreadsheet."
            ),
        },
        "purpose": {
            "title": "3. Purposes and legal bases",
            "items": [
                (
                    "responding to your enquiry and taking steps at your request before "
                    "a possible contract — Article 6(1)(b) GDPR"
                ),
                (
                    "protecting the form against abuse and establishing, exercising or "
                    "defending legal claims — the controller’s legitimate interest, "
                    "Article 6(1)(f) GDPR"
                ),
            ],
        },
        "retention": {
            "title": "4. Retention period",
            "text": (
                "We keep enquiry data for no longer than 12 months after the last contact. "
                "We may delete it sooner when it is no longer needed or when you make a "
                "valid erasure request. If we begin working together, contract-related data "
                "may be subject to different periods required by law or needed to protect claims."
            ),
        },
        "recipients": {
            "title": "5. Data recipients",
            "text": (
                "Data may be accessed by people authorized by the controller and providers "
                "supporting the website. Enquiries are stored in Google Sheets. Once the "
                "website is published, the selected hosting provider may also be a technical recipient."
            ),
        },
        "rights": {
            "title": "6. Your rights",
            "intro": "Where provided by the GDPR, you may request:",
            "items": [
                "access to your data and a copy of it",
                "correction or completion of your data",
                "erasure or restriction of processing",
                "data portability, where applicable",
                "an objection to processing based on legitimate interests",
            ],
            "complaint": (
                "You also have the right to lodge a complaint with the President of the "
                "Polish Personal Data Protection Office (UODO)."
            ),
        },
        "required": {
            "title": "7. Voluntary provision of data",
            "text": (
                "Providing data is voluntary, but your full name and phone number are "
                "necessary for us to respond. The comment is optional."
            ),
        },
        "automation": {
            "title": "8. Automated decisions and analytics",
            "text": (
                "We do not make automated decisions about you or profile users. The website "
                "currently uses no analytics tools or marketing cookies."
            ),
        },
        "contact": {
            "title": "9. Privacy contact",
            "text": ("To exercise your rights or ask a privacy question, contact us at:"),
        },
    },
}


def get_privacy_content(language: str | None) -> tuple[str, dict[str, Any]]:
    """Return localized privacy content, falling back to Polish."""
    selected_language = language if language in PRIVACY_CONTENT else "pl"
    return selected_language, PRIVACY_CONTENT[selected_language]
