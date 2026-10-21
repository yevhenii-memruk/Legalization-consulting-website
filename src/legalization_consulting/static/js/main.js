const header = document.querySelector("[data-site-header]");
const navToggle = document.querySelector("[data-nav-toggle]");
const navigation = document.querySelector("[data-navigation]");
const demoForm = document.querySelector("[data-demo-form]");
const demoSubmit = document.querySelector("[data-demo-submit]");
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

demoSubmit?.addEventListener("click", () => {
  if (!demoForm.reportValidity() || !formStatus) return;

  formStatus.textContent =
    "Formularz jest gotowy wizualnie. Bezpieczną wysyłkę danych podłączymy w kolejnym etapie.";
});
