const terminal = document.querySelector(".terminal pre");

if (terminal) {
    const originalText = terminal.innerText;

    terminal.innerText = "";

    let index = 0;

    function typeTerminal() {
        if (index < originalText.length) {
            terminal.innerText += originalText.charAt(index);
            index++;

            setTimeout(typeTerminal, 18);
        }
    }

    setTimeout(typeTerminal, 700);
}

/*
 * CYBERTEC8 deployment monitor
 * Production status is checked separately.
 * Internal monitoring endpoint:
 * /deploy-status
 */