document.addEventListener("DOMContentLoaded", function () {
    let jobCards = document.querySelectorAll(".single_jobs");
    jobCards.forEach((card, index) => {
        card.style.opacity = "0"; // التأكد من أن البطاقات مخفية في البداية
        card.style.transform = "translateY(20px)"; // إضافة حركة بسيطة
        setTimeout(() => {
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
            card.style.transition = "all 0.5s ease"; // إضافة انتقال سلس
        }, index * 200);
    });
});