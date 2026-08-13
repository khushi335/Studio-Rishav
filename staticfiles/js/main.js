
    document.addEventListener("DOMContentLoaded", () => {
        const wrapper = document.getElementById("video-wrapper");
        const iframe = document.getElementById("hero-fb-frame");
        const btnPlayPause = document.getElementById("btn-play-pause");
        const btnMute = document.getElementById("btn-mute");
        const btnZoom = document.getElementById("btn-zoom");

        const iconPause = document.getElementById("icon-pause");
        const iconPlay = document.getElementById("icon-play");
        const iconMuted = document.getElementById("icon-muted");
        const iconUnmuted = document.getElementById("icon-unmuted");

        let isPlaying = true;
        let isMuted = true;
        let isZoomed = false;

        // 1. Pause/Play (Toggles opacity overlay smoothly)
        btnPlayPause.addEventListener("click", () => {
            isPlaying = !isPlaying;
            if (isPlaying) {
                iframe.classList.remove("opacity-0");
                iframe.classList.add("opacity-60");
                iconPlay.classList.add("hidden");
                iconPause.classList.remove("hidden");
            } else {
                iframe.classList.remove("opacity-60");
                iframe.classList.add("opacity-0");
                iconPause.classList.add("hidden");
                iconPlay.classList.remove("hidden");
            }
        });

        // 2. Mute/Unmute Switcher for Embedded Reel Source
        btnMute.addEventListener("click", () => {
            isMuted = !isMuted;
            const baseUrl = "https://www.facebook.com/plugins/dvr.php?href=https%3A%2F%2Fwww.facebook.com%2Freel%2F3997848770509472&show_text=false&autoplay=true";
            
            if (isMuted) {
                iframe.src = `${baseUrl}&muted=true&controls=false`;
                iconUnmuted.classList.add("hidden");
                iconMuted.classList.remove("hidden");
            } else {
                iframe.src = `${baseUrl}&muted=false&controls=false`;
                iconMuted.classList.add("hidden");
                iconUnmuted.classList.remove("hidden");
            }
        });

        // 3. Cinematic Scale/Zoom Handler
        btnZoom.addEventListener("click", () => {
            isZoomed = !isZoomed;
            if (isZoomed) {
                wrapper.classList.remove("scale-105");
                wrapper.classList.add("scale-125");
            } else {
                wrapper.classList.remove("scale-125");
                wrapper.classList.add("scale-105");
            }
        });
    });