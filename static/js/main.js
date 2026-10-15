document.addEventListener("DOMContentLoaded", function () {
    const cursorDot = document.getElementById("cursorDot");
    const cursorRing = document.getElementById("cursorRing");

    if (cursorDot && cursorRing) {
        let mouseX = -100;
        let mouseY = -100;
        let ringX = -100;
        let ringY = -100;

        window.addEventListener("mousemove", function (e) {
            mouseX = e.clientX;
            mouseY = e.clientY;

            cursorDot.style.left = mouseX + "px";
            cursorDot.style.top = mouseY + "px";
            cursorDot.classList.remove("cursor-hidden");
            cursorRing.classList.remove("cursor-hidden");
        });

        document.addEventListener("mouseleave", function () {
            cursorDot.classList.add("cursor-hidden");
            cursorRing.classList.add("cursor-hidden");
        });

        function animateRing() {
            ringX += (mouseX - ringX) * 0.15;
            ringY += (mouseY - ringY) * 0.15;

            cursorRing.style.left = ringX + "px";
            cursorRing.style.top = ringY + "px";

            requestAnimationFrame(animateRing);
        }
        requestAnimationFrame(animateRing);

        const interactiveSelectors = "a, button, input, select, textarea, .product-card, .category-card, .btn, .icon-link";
        document.querySelectorAll(interactiveSelectors).forEach(function (el) {
            el.addEventListener("mouseenter", function () {
                cursorDot.classList.add("is-hovering");
                cursorRing.classList.add("is-hovering");
            });
            el.addEventListener("mouseleave", function () {
                cursorDot.classList.remove("is-hovering");
                cursorRing.classList.remove("is-hovering");
            });
        });
    }

    const passwordButtons = document.querySelectorAll("[data-password-toggle]");
    passwordButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const input = document.getElementById(button.dataset.passwordToggle);
            if (!input) return;

            const showing = input.type === "text";
            input.type = showing ? "password" : "text";
            button.innerHTML = showing
                ? '<i class="bi bi-eye"></i>'
                : '<i class="bi bi-eye-slash"></i>';

            button.setAttribute("aria-label", showing ? "Show password" : "Hide password");
        });
    });

    document.querySelectorAll(".product-card, .category-card").forEach(function (card) {
        card.addEventListener("mouseenter", function () {
            card.classList.add("is-active");
        });
        card.addEventListener("mouseleave", function () {
            card.classList.remove("is-active");
        });
    });

    document.querySelectorAll("img").forEach(function (img) {
        img.addEventListener("error", function () {
            img.style.display = "none";
            const parent = img.parentElement;
            if (parent && !parent.querySelector(".image-error")) {
                const fallback = document.createElement("div");
                fallback.className = "product-placeholder image-error";
                fallback.innerHTML = '<i class="bi bi-image"></i>';
                parent.appendChild(fallback);
            }
        });
    });
});
