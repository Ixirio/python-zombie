window.onload = () => {
    if (window.location.href.includes('?full=1')) {
        document.getElementById('fullBody').checked = true;
    }
}

function manageFullBody() {
    if (window.location.href.includes('?full=1')) {
        return window.location.href = window.location.href.replace('?full=1', '');
    }
    return window.location.href += '?full=1';
}
