document.addEventListener("DOMContentLoaded", function () {
    const messagesContainer = document.querySelector(".messages-container");

    if (messagesContainer) {
        setTimeout(function () {
            messagesContainer.style.transition = "opacity 0.5s ease, max-height 0.5s ease,margin 0.5s ease, padding 0.5s ease";
            messagesContainer.style.opacity = "0px";
            messagesContainer.style.maxHeight = "0px";
            messagesContainer.style.marginTop = "0px";
            messagesContainer.style.marginBottom = "0px";
            messagesContainer.style.paddingTop = "0px";
            messagesContainer.style.paddingBottom = "0px";
            messagesContainer.style.overflow = "hidden";
            setTimeout(function () {
                messagesContainer.remove();
            }, 500);
        }, 4000); // time in milliseconds
    };
    console.log("Success Messages Added")
});