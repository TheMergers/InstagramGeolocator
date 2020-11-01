const L = require("leaflet");
const axios = require("axios");

document.addEventListener("DOMContentLoaded", function () {
  const sendButton = document.getElementById("send");
  const username = document.getElementById("username");
  const loading = document.getElementById("loading");
  const app = document.getElementById("app");

  sendButton.addEventListener("click", (event) => {
    event.preventDefault();
    loading.classList.add("loading");

    axios
      .get("/run", {
        params: {
          iguser: username.value,
        },
      })
      .then(function ({ data }) {
        loading.classList.remove("loading");
        console.log(data);
        app.classList.add("app");
        // initialize Leaflet
        var map = L.map("map").setView({ lon: 0, lat: 0 }, 2);

        // add the OpenStreetMap tiles
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          maxZoom: 19,
          attribution:
            '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>',
        }).addTo(map);

        // show the scale bar on the lower left corner
        L.control.scale().addTo(map);
      });
  });
});
