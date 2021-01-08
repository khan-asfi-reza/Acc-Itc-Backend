const isInViewport = function (elem) {
    const distance = elem.getBoundingClientRect();
    return (
        distance.top >= 0 &&
        distance.left >= 0 &&
        distance.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        distance.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
};


const onViewPort = (element, callback) => {
    window.addEventListener('scroll', function(event) {
        // add event on scroll

        if (isInViewport(element)) {
            //if in Viewport
            callback()
        }

    }, false);
};
