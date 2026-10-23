const header = document.querySelector("[data-site-header]");
const navToggle = document.querySelector("[data-nav-toggle]");
const navigation = document.querySelector("[data-navigation]");
const leadForm = document.querySelector("[data-lead-form]");
const leadSubmit = document.querySelector("[data-lead-submit]");
const formStatus = document.querySelector("[data-form-status]");

function closeNavigation() {
  if (!navToggle || !navigation || !header) return;

  navToggle.setAttribute("aria-expanded", "false");
  navToggle.setAttribute("aria-label", "Otwórz menu");
  navigation.classList.remove("is-open");
  header.classList.remove("is-menu-open");
}

navToggle?.addEventListener("click", () => {
  if (!navigation || !header) return;

  const isOpen = navToggle.getAttribute("aria-expanded") === "true";
  navToggle.setAttribute("aria-expanded", String(!isOpen));
  navToggle.setAttribute("aria-label", isOpen ? "Otwórz menu" : "Zamknij menu");
  navigation.classList.toggle("is-open", !isOpen);
  header.classList.toggle("is-menu-open", !isOpen);
});

navigation?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", closeNavigation);
});

window.addEventListener(
  "scroll",
  () => header?.classList.toggle("is-scrolled", window.scrollY > 24),
  { passive: true },
);

function setFormStatus(message, state) {
  if (!formStatus) return;

  formStatus.textContent = message;
  formStatus.dataset.state = state;
}

leadForm?.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (!leadForm.reportValidity() || !leadSubmit || leadSubmit.disabled) return;

  const formData = new FormData(leadForm);
  const comment = String(formData.get("comment") || "").trim();
  const payload = {
    full_name: String(formData.get("full_name") || ""),
    phone: String(formData.get("phone") || ""),
    comment: comment || null,
    language: document.documentElement.lang || "pl",
    company_website: String(formData.get("company_website") || ""),
  };

  leadSubmit.disabled = true;
  leadSubmit.setAttribute("aria-busy", "true");
  setFormStatus("Wysyłanie zapytania…", "pending");

  try {
    const response = await fetch(leadForm.action, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (response.ok) {
      leadForm.reset();
      leadForm.querySelector("details")?.removeAttribute("open");
      setFormStatus(
        "Dziękujemy. Twoje zapytanie zostało zapisane — skontaktujemy się z Tobą.",
        "success",
      );
      return;
    }

    if (response.status === 429) {
      setFormStatus("Zbyt wiele prób. Spróbuj ponownie za kilka minut.", "error");
      return;
    }

    if (response.status === 422) {
      setFormStatus("Sprawdź poprawność imienia i numeru telefonu.", "error");
      return;
    }

    setFormStatus("Formularz jest chwilowo niedostępny. Spróbuj ponownie później.", "error");
  } catch {
    setFormStatus("Nie udało się połączyć z serwerem. Sprawdź połączenie i spróbuj ponownie.", "error");
  } finally {
    leadSubmit.disabled = false;
    leadSubmit.removeAttribute("aria-busy");
  }
});
