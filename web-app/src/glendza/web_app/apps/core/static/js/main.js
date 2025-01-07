/* -------------- Constants -------------- */

const SHRUGGIE = "¯\\_(ツ)_/¯";

const THEMING_ATTRIBUTE_NAME = "data-theme";
const THEMES = {
  light: "light",
  dark: "dark",
};

const LOCAL_STORAGE_KEYS = {
  theme: "theme",
};

const ELEMENT_IDS = {
  themeToggleButton: "theme-toggle-button",
};

/* -------------- Theme utils -------------- */

function getTheme() {
  // First check if the user has already declared a preference:.
  const configuredTheme = localStorage.getItem(LOCAL_STORAGE_KEYS.theme);
  if (configuredTheme) {
    return configuredTheme;
  }

  // If not, check if the user has a system preference:
  const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
  return prefersDarkScheme.matches ? THEMES.dark : THEMES.light;
}

function setTheme(theme) {
  document.documentElement.setAttribute(THEMING_ATTRIBUTE_NAME, theme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute(
    THEMING_ATTRIBUTE_NAME
  );
  const newTheme = currentTheme === THEMES.light ? THEMES.dark : THEMES.light;
  document.documentElement.setAttribute(THEMING_ATTRIBUTE_NAME, newTheme);
  localStorage.setItem(LOCAL_STORAGE_KEYS.theme, newTheme);
}

function setUpTheming() {
  // First, set up the theme from the user's preference:
  const themeSetting = getTheme();
  setTheme(themeSetting);

  // Then, set up the toggle button:
  const themeToggleButton = document.getElementById(
    ELEMENT_IDS.themeToggleButton
  );

  if (!themeToggleButton) {
    console.warn(
      `No theme toggle button found with id "${ELEMENT_IDS.themeToggleButton}"`
    );
    return;
  }

  themeToggleButton.addEventListener("click", toggleTheme);
}

/* -------------- App init -------------- */

function onDOMContentLoaded() {
  setUpTheming();

  console.log(
    `%c${SHRUGGIE}`,
    "font-size: 30px; color: red; font-weight: bold;"
  );
}

document.addEventListener("DOMContentLoaded", onDOMContentLoaded);
