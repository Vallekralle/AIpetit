const spinnerWrapperEl = document.querySelector(".spinner-wrapper");

window.addEventListener("load", () => {
    spinnerWrapperEl.style.opacity = "0";

    setTimeout(() => {
        spinnerWrapperEl.style.display = "none";
    }, 200);
});

function showSpinner() {
    const spinnerWrapperEl = document.querySelector(".spinner-wrapper");
    spinnerWrapperEl.style.opacity = "1";
    spinnerWrapperEl.style.display = "flex";
}