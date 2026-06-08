/* =============================================
   MarketSpace — Vanilla JavaScript
   No frameworks. No libraries. Just JS.
   ============================================= */

document.addEventListener("DOMContentLoaded", () => {

  /* ─── Mobile Navigation Toggle ─── */
  const navToggle = document.getElementById("nav-toggle");
  const navMenu   = document.getElementById("nav-menu");

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      navToggle.classList.toggle("open");
      navMenu.classList.toggle("open");
    });

    // Close on link click
    navMenu.querySelectorAll(".nav__link").forEach(link => {
      link.addEventListener("click", () => {
        navToggle.classList.remove("open");
        navMenu.classList.remove("open");
      });
    });
  }

  /* ─── Header Scroll Effect ─── */
  const header = document.getElementById("header");

  const onScroll = () => {
    if (!header) return;
    if (window.scrollY > 60) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll(); // init

  /* ─── Active Nav Link ─── */
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav__link");

  const highlightNav = () => {
    const scrollY = window.scrollY + 100;

    sections.forEach(section => {
      const top    = section.offsetTop - 80;
      const bottom = top + section.offsetHeight;
      const id     = section.getAttribute("id");

      navLinks.forEach(link => {
        if (link.getAttribute("href") === `#${id}`) {
          if (scrollY >= top && scrollY < bottom) {
            link.classList.add("active");
          } else {
            link.classList.remove("active");
          }
        }
      });
    });
  };

  window.addEventListener("scroll", highlightNav, { passive: true });

  /* ─── Scroll Reveal (IntersectionObserver) ─── */
  const revealElements = document.querySelectorAll(
    ".design__block, .prototype__frame, .section-header, .hmw__vision, .hmw__card, .matrix, .about__text, .about__goals, .persona__tabs, .affinity__box"
  );

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          // Stagger delay based on index within viewport batch
          setTimeout(() => {
            entry.target.classList.add("reveal", "visible");
          }, i * 80);
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: "0px 0px -40px 0px"
    });

    revealElements.forEach(el => {
      el.classList.add("reveal");
      observer.observe(el);
    });
  }

  /* ─── Persona Tab Switching ─── */
  const personaTabs = document.querySelectorAll(".persona__tab");
  const personaPanels = document.querySelectorAll(".persona__panel");

  personaTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      const idx = tab.getAttribute("data-index");

      // Deactivate all tabs & panels
      personaTabs.forEach(t => t.classList.remove("active"));
      personaPanels.forEach(p => p.classList.remove("active"));

      // Activate clicked tab & matching panel
      tab.classList.add("active");
      const target = document.querySelector(`.persona__panel[data-panel="${idx}"]`);
      if (target) {
        target.classList.add("active");
        // Re-trigger animation
        target.style.animation = "none";
        target.offsetHeight; // force reflow
        target.style.animation = "";
      }
    });
  });

});
