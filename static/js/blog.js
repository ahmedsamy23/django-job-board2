document.addEventListener("DOMContentLoaded", function () {
    var textarea = document.querySelector(".auto-expand");

    if (textarea) {
        textarea.addEventListener("input", function () {
            this.style.height = "auto";
            this.style.height = (this.scrollHeight) + "px";
        });
    }
});
