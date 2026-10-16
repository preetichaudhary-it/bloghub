// document.addEventListener('DOMContentLoaded', function () {
//     const messageBox = document.getElementById('id_message');
//     const wordCount = document.getElementById('wordCount');
//     const messageError = document.getElementById('messageError');
//     const contactForm = document.getElementById('contactForm');

//     if (!messageBox || !wordCount) {
//         return;
//     }

//     function updateWordCount() {
//         const text = messageBox.value.trim();
//         const words = text ? text.split(/\s+/).filter(Boolean) : [];
//         const count = words.length;

//         wordCount.textContent = count;
//         wordCount.style.color = count > 200 ? '#e53935' : '';

//         if (messageError) {
//             messageError.textContent = count > 200
//                 ? 'Maximum 200 words allowed.'
//                 : '';
//         }
//     }

//     messageBox.addEventListener('input', updateWordCount);

//     updateWordCount();

//     if (contactForm) {
//         contactForm.addEventListener('submit', function (event) {
//             const text = messageBox.value.trim();
//             const count = text ? text.split(/\s+/).filter(Boolean).length : 0;

//             if (count > 200) {
//                 event.preventDefault();

//                 if (messageError) {
//                     messageError.textContent = 'Maximum 200 words allowed.';
//                 }

//                 messageBox.focus();
//             }
//         });
//     }
// });

document.addEventListener('DOMContentLoaded', function () {
    const messageBox = document.getElementById('id_message') ||
                      document.getElementById('id_feedback');
    const wordCount = document.getElementById('wordCount');
    const messageError = document.getElementById('messageError');
    const contactForm = document.getElementById('contactForm') ||
                        messageBox?.closest('form');

    if (!messageBox || !wordCount) {
        return;
    }

    function updateWordCount() {
        const text = messageBox.value.trim();
        const words = text ? text.split(/\s+/).filter(Boolean) : [];
        const count = words.length;

        wordCount.textContent = count;
        wordCount.style.color = count > 200 ? '#e53935' : '';

        if (messageError) {
            messageError.textContent = count > 200
                ? 'Maximum 200 words allowed.'
                : '';
        }
    }

    messageBox.addEventListener('input', updateWordCount);
    updateWordCount();

    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            const text = messageBox.value.trim();
            const count = text ? text.split(/\s+/).filter(Boolean).length : 0;

            if (count > 200) {
                event.preventDefault();

                if (messageError) {
                    messageError.textContent = 'Maximum 200 words allowed.';
                }

                messageBox.focus();
            }
        });
    }
});