let map = L.map('mapid', {zoomControl: false}).setView([51.505, -0.09], 12);
L.tileLayer(`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${MAP_KEY}`, {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' + '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' + 'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: MAP_KEY,
    tap: true
}).addTo(map);
let marker = L.marker()
L.control.zoom({
    position: 'topright'
}).addTo(map);

for (const place of added_place_json){
    L.marker([place.fields.lat, place.fields.long]).bindPopup(
        `<div class="card" style="width: 15rem;">\n` +
        ` <h6 class="card-header">Название места:<br>${place.fields.name}</h6>\n` +
        `  <div class="card-body">\n` +
        `    <p class="card-text" style="overflow: scroll">Комментарий места:<br>${place.fields.comment}</p>\n` +
        `  </div>\n` +
        `</div>`
    ).addTo(map)
};
