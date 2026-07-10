let sidebarOpen = false;

function openSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');

    sidebarOpen = !sidebarOpen;

    sidebar.classList.toggle('open', sidebarOpen);
    overlay.classList.toggle('open', sidebarOpen);
}

const revealElements = document.querySelectorAll('.reveal');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        } else {
            entry.target.classList.remove('visible'); // 위로 다시 스크롤하면 재생 초기화하고 싶으면 유지
        }
    });
}, {
    threshold: 0.3 // 요소가 30% 보이면 트리거 (원하는 비율로 조절)
});

revealElements.forEach(el => observer.observe(el));