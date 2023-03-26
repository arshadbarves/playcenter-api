// Email Validation
function validateEmail(email) {
  var re = /\S+@\S+\.\S+/;
  return re.test(email);
}

// Password Validation
function validatePassword(password) {
  var re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
  return re.test(password);
}

// Login Form Validation with Error Messages in form of Alerts
function validateLoginForm() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  if (!validateEmail(email)) {
    alert("Please enter a valid email address.");
    return false;
  }
  if (!validatePassword(password)) {
    alert("Please enter a valid password.");
    return false;
  }
  return true;
}

// Create Account Form Validation with Error Messages in form of Alerts
function validateCreateAccountForm() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var confirmPassword = document.getElementById("confirmPassword").value;
  if (!validateEmail(email)) {
    alert("Please enter a valid email address.");
    return false;
  }
  if (!validatePassword(password)) {
    alert("Please enter a valid password.");
    return false;
  }
  if (password != confirmPassword) {
    alert("Passwords do not match.");
    return false;
  }
  return true;
}

/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2023 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

// (() => {
//   "use strict";

//   const storedTheme = localStorage.getItem("theme");

//   const getPreferredTheme = () => {
//     if (storedTheme) {
//       return storedTheme;
//     }

//     return window.matchMedia("(prefers-color-scheme: dark)").matches
//       ? "dark"
//       : "light";
//   };

//   const setTheme = function (theme) {
//     if (
//       theme === "auto" &&
//       window.matchMedia("(prefers-color-scheme: dark)").matches
//     ) {
//       document.documentElement.setAttribute("data-bs-theme", "dark");
//     } else {
//       document.documentElement.setAttribute("data-bs-theme", theme);
//     }
//   };

//   setTheme(getPreferredTheme());

//   const showActiveTheme = (theme, focus = false) => {
//     const themeSwitcher = document.querySelector("#bd-theme");

//     if (!themeSwitcher) {
//       return;
//     }

//     const themeSwitcherText = document.querySelector("#bd-theme-text");
//     const activeThemeIcon = document.querySelector(".theme-icon-active use");
//     const btnToActive = document.querySelector(
//       `[data-bs-theme-value="${theme}"]`
//     );
//     const svgOfActiveBtn = btnToActive
//       .querySelector("svg use")
//       .getAttribute("href");

//     document.querySelectorAll("[data-bs-theme-value]").forEach((element) => {
//       element.classList.remove("active");
//       element.setAttribute("aria-pressed", "false");
//     });

//     btnToActive.classList.add("active");
//     btnToActive.setAttribute("aria-pressed", "true");
//     activeThemeIcon.setAttribute("href", svgOfActiveBtn);
//     const themeSwitcherLabel = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`;
//     themeSwitcher.setAttribute("aria-label", themeSwitcherLabel);

//     if (focus) {
//       themeSwitcher.focus();
//     }
//   };

//   window
//     .matchMedia("(prefers-color-scheme: dark)")
//     .addEventListener("change", () => {
//       if (storedTheme !== "light" || storedTheme !== "dark") {
//         setTheme(getPreferredTheme());
//       }
//     });

//   window.addEventListener("DOMContentLoaded", () => {
//     showActiveTheme(getPreferredTheme());

//     document.querySelectorAll("[data-bs-theme-value]").forEach((toggle) => {
//       toggle.addEventListener("click", () => {
//         const theme = toggle.getAttribute("data-bs-theme-value");
//         localStorage.setItem("theme", theme);
//         setTheme(theme);
//         showActiveTheme(theme, true);
//       });
//     });
//   });
// })();
