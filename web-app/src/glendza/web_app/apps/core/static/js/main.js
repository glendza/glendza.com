/* -------------- Constants -------------- */

const SHRUGGIE = "¯\\_(ツ)_/¯";

const THEMING_ATTRIBUTE_NAME = "data-theme";

const THEMES = {
  light: "light",
  dark: "dark",
};

const THEME_ICONS = {
  [THEMES.light]: "🌞",
  [THEMES.dark]: "🌚",
};

const CSS_VARIABLES = {
  headerBgOpacity: "--header-bg-opacity",
};

const LOCAL_STORAGE_PREFIX = "glendza";

const LOCAL_STORAGE_KEYS = {
  theme: `${LOCAL_STORAGE_PREFIX}:theme`,
  scrollPosition: `${LOCAL_STORAGE_PREFIX}:scrollPosition`,
};

// Example of a scroll position at which the header should be fully opaque
const HEADER_FULL_OPACITY_SCROLL_POSITION = 300;

const ELEMENT_IDS = {
  navigationMenu: "navmenu",
  navmenuContent: "navmenu-content",
  navigationMenuToggleButton: "navmenu-toggle-button",
  navigationMenuCloseButton: "navmenu-close-button",
  themeToggleButton: "theme-toggle-button",
};

const ELEMENT_CLASSES = {
  // Utils:
  noScroll: "no-scroll",
  // Navmenu:
  navmenuCurrentPageLink: "navmenu__menu-link--current-page",
  navmenuOpenModifier: "navmenu--open",
  navmenuMenuLink: "navmenu__menu-link",
};

/* -------------- Utils -------------- */

/**
 * Tries to get an element by its id, throwing an error if it doesn't exist.
 * @param {string} id
 * @returns {HTMLElement}
 */
function tryGetElementById(id) {
  const element = document.getElementById(id);
  if (!element) {
    throw new Error(`No element found with id "${id}"`);
  }
  return element;
}

/* -------------- Theme utils -------------- */

function getTheme() {
  // First check if the user has already declared a preference:.
  const configuredTheme = localStorage.getItem(LOCAL_STORAGE_KEYS.theme);
  if (configuredTheme && Object.values(THEMES).includes(configuredTheme)) {
    return configuredTheme;
  }

  // If not, check if the user has a system preference:
  const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
  return prefersDarkScheme.matches ? THEMES.dark : THEMES.light;
}

/**
 * Sets the page theme.
 * @param {string} theme
 */
function setTheme(theme) {
  document.documentElement.setAttribute(THEMING_ATTRIBUTE_NAME, theme);
}

/**
 * Sets the attributes of the theme toggle button.
 * @param {HTMLButtonElement} themeToggleButton
 * @param {string} theme
 */
function setThemeButtonAttributes(themeToggleButton, theme) {
  const inverseTheme = theme === THEMES.light ? THEMES.dark : THEMES.light;
  const label = `Switch to ${inverseTheme} mode`;
  themeToggleButton.title = label;
  themeToggleButton.ariaLabel = label;
  themeToggleButton.textContent = THEME_ICONS[theme];
}

/**
 * Toggles the theme between light and dark.
 * @param {HTMLButtonElement} themeToggleButton
 * @returns {void}
 */
function toggleTheme(themeToggleButton) {
  const currentTheme = document.documentElement.getAttribute(THEMING_ATTRIBUTE_NAME);
  const newTheme = currentTheme === THEMES.light ? THEMES.dark : THEMES.light;
  document.documentElement.setAttribute(THEMING_ATTRIBUTE_NAME, newTheme);
  localStorage.setItem(LOCAL_STORAGE_KEYS.theme, newTheme);
  setThemeButtonAttributes(themeToggleButton, newTheme);
}

function setUpTheming() {
  // First, set up the theme from the user's preference:
  const themeSetting = getTheme();
  setTheme(themeSetting);

  // Then, set up the toggle button:
  const themeToggleButton = tryGetElementById(ELEMENT_IDS.themeToggleButton);

  themeToggleButton.addEventListener("click", function () {
    toggleTheme(themeToggleButton);
  });
  setThemeButtonAttributes(themeToggleButton, themeSetting);
}

/* -------------- Navigation menu -------------- */

/**
 * Handles the click event outside of the sidebar.
 * @param {MouseEvent} event
 * @returns {void}
 */
function handleSidebarOutsideClick(event) {
  const sidebar = tryGetElementById(ELEMENT_IDS.navmenuContent);
  if (!sidebar.contains(event.target)) {
    closeSidebar(navmenu);
  }
}

/**
 * Sets up the conditions for the sidebar to be open.
 * @param {HTMLElement} navmenu
 * @returns {void}
 */
function openSidebar(navmenu) {
  navmenu.classList.add(ELEMENT_CLASSES.navmenuOpenModifier);
  document.body.classList.add(ELEMENT_CLASSES.noScroll);
  navmenu.addEventListener("click", handleSidebarOutsideClick);
}

/**
 * Removes the conditions for the sidebar to be open.
 * @param {HTMLElement} navmenu
 */
function closeSidebar(navmenu) {
  navmenu.classList.remove(ELEMENT_CLASSES.navmenuOpenModifier);
  document.body.classList.remove(ELEMENT_CLASSES.noScroll);
  navmenu.removeEventListener("click", handleSidebarOutsideClick);
}

function setUpNavigationMenu() {
  const navmenu = tryGetElementById(ELEMENT_IDS.navigationMenu);
  const navmenuToggleButton = tryGetElementById(ELEMENT_IDS.navigationMenuToggleButton);
  const navmenuCloseButton = tryGetElementById(ELEMENT_IDS.navigationMenuCloseButton);

  // Set up the event listeners:

  navmenuToggleButton.addEventListener("click", openSidebar.bind(null, navmenu));

  navmenuCloseButton.addEventListener("click", closeSidebar.bind(null, navmenu));

  document.addEventListener("keyup", function (event) {
    if (event.key === "Escape") {
      closeSidebar(navmenu);
      document.removeEventListener("keyup", closeSidebar);
    }
  });
}

/* -------------- Header opacity -------------- */

function setHeaderBgOpacity() {
  const opacityValue = window.scrollY / HEADER_FULL_OPACITY_SCROLL_POSITION;
  document.documentElement.style.setProperty(CSS_VARIABLES.headerBgOpacity, opacityValue);
}

/* -------------- Scroll position -------------- */

function saveScrollPosition() {
  localStorage.setItem(LOCAL_STORAGE_KEYS.scrollPosition, window.scrollY);
}

function restoreScrollPosition() {
  const scrollPosition = localStorage.getItem(LOCAL_STORAGE_KEYS.scrollPosition);

  if (scrollPosition) {
    window.scrollTo(0, scrollPosition);
    localStorage.removeItem(LOCAL_STORAGE_KEYS.scrollPosition);
  }
}

/* -------------- Navmenu -------------- */

const highlightCurrentPageLink = () => {
  const navLinks = document.querySelectorAll(`.${ELEMENT_CLASSES.navmenuMenuLink}`);
  navLinks.forEach((link) => {
    const url = new URL(link.href);
    if (url.origin == window.location.origin && url.pathname === window.location.pathname) {
      link.classList.add(ELEMENT_CLASSES.navmenuCurrentPageLink);
    }
  });
};

/* -------------- Event handlers -------------- */

function onDOMContentLoaded() {
  setUpTheming();
  setHeaderBgOpacity();
  setUpNavigationMenu();
  highlightCurrentPageLink();

  console.log(`%c${SHRUGGIE}`, "font-size: 30px; color: red; font-weight: bold;");
}

function onWindowLoad() {
  restoreScrollPosition();
}

function onBeforeUnload() {
  saveScrollPosition();
}

function onScroll() {
  setHeaderBgOpacity();
}

/* -------------- Event listeners -------------- */

window.addEventListener("load", onWindowLoad);
document.addEventListener("DOMContentLoaded", onDOMContentLoaded);
window.addEventListener("scroll", onScroll);
window.addEventListener("beforeunload", onBeforeUnload);
