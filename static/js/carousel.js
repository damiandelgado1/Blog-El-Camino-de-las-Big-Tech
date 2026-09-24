let currentIndex = 0;

const track = document.querySelector('.carousel-track');
const images = track.querySelectorAll('img');

function moveCarousel() {
    currentIndex = (currentIndex + 1) % images.length;

    const offset = -currentIndex * images[0].offsetWidth;

    track.style.transform = `translateX(${offset}px)`;
}

setInterval(moveCarousel, 3000);