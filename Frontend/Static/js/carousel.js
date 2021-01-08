document.addEventListener('DOMContentLoaded', () => {
    // CHANGE ONLY THIS
    const SLIDETIME = 500; //ms
    // --------------------------

    const backButton = document.querySelector('.wbn-slider-back-btn');
    const forwardButton = document.querySelector('.wbn-slider-next-btn');
    // Select all slides and convert node to array for easy handling
    // const allSlides = Array.from(document.querySelectorAll('.wbn-slide'));
    const allSlides = [...document.querySelectorAll('.wbn-slide')];
    let clickable = true;
    let active = null;
    let newActive = null;

    function initSlider() {
        // Set the CSS transition on the slides to the value we specified in SLIDETIME above
        allSlides.forEach(slide =>
            slide.setAttribute(
                'style',
                `transition: transform ${SLIDETIME}ms ease;
                     animation-duration: ${SLIDETIME}ms`,
            ),
        );
        setInterval(()=>{
            changeSlide(true)
        },5000)
    }

    function changeSlide(forward) {
        if (clickable) {
            clickable = false;
            active = document.querySelector('.active');
            const activeSlideIndex = allSlides.indexOf(active);

            if (forward) {
                newActive = allSlides[(activeSlideIndex + 1) % allSlides.length];
                active.classList.add('slideOutLeft');
                newActive.classList.add('slideInRight', 'active');
            } else {
                newActive =
                    allSlides[
                    (activeSlideIndex - 1 + allSlides.length) % allSlides.length
                        ];
                active.classList.add('slideOutRight');
                newActive.classList.add('slideInLeft', 'active');
            }
        }
    }

    allSlides.forEach(slide => {
        slide.addEventListener('transitionend', e => {
            if (slide === active && !clickable) {
                clickable = true;
                active.className = 'wbn-slide';
            }
        });
    });

    //Event listeners
    // forwardButton.addEventListener('click', () => {
    //     changeSlide(true);
    // });
    // backButton.addEventListener('click', () => {
    //     changeSlide(false);
    // });

    // Init the slider
    initSlider();
});
