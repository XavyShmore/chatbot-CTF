const form = document.getElementById('chat-form');
const input = document.getElementById('chat-input');

document.addEventListener('htmx:beforeRequest', (event) => {
    if (event.target === form) {
        let childNodes = form.childNodes;
        childNodes.forEach(child => child.disabled = true);
        input.value = '';
    }
});

document.addEventListener('htmx:beforeSwap', (event) => {
    const reply = document.querySelector('.loading_message');
    if (event.detail.target === reply) {
        let childNodes = form.childNodes;
        childNodes.forEach(child => child.disabled = false);
    }
});