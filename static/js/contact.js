document.addEventListener('DOMContentLoaded', function () {
    const messageBox = document.getElementById('message');
    const wordCount = document.getElementById('wordCount');

    if (messageBox) {
        messageBox.addEventListener('input', function (e) {
            // RegEx splits by spaces, tabs, and newlines while filtering out empty strings
            let words = this.value.trim().split(/\s+/).filter(Boolean);

            if (words.length > 200) {
                // Save the current cursor selection position
                const selectionStart = this.selectionStart;
                const selectionEnd = this.selectionEnd;

                // Trim the word list strictly to 200
                words = words.slice(0, 200);
                this.value = words.join(' ');

                // Restore the cursor position so it doesn't snap to the end
                this.setSelectionRange(selectionStart, selectionEnd);
            }

            // Update the live counter number
            wordCount.textContent = words.length;
        });
    }
}); 