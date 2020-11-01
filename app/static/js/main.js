const L = require("leaflet");
const axios = require("axios");

document.addEventListener("DOMContentLoaded", function () {
  // initialize Leaflet
  var map = L.map("mapid").setView({ lon: 0, lat: 0 }, 2);

  // add the OpenStreetMap tiles
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>',
  }).addTo(map);

  // show the scale bar on the lower left corner
  L.control.scale().addTo(map);

  const sendButton = document.getElementById("send");
  const username = document.getElementById("username");

  sendButton.addEventListener("click", (event) => {
    event.preventDefault();
    console.log(username.value);
    axios
      .get("/run:5000", {
        iguser: username.value,
      })
      .then(function (response) {
        console.log(response);
      });
  });
});
