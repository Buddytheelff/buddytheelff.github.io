//Author Buddy Collins
"use strict"
var geojson;
var map;
var index = 0;
var info = L.control();
var polygonStyle = {
  "weight": 3,
  "color": "#6699ff"};
var year = ["1900","1910","1920","1930","1940","1950","1960","1970","1980","1990","2000","2010"];
var slideArr = [];
window.onload = function () {
    createMap();
    createChart();
};


//-------------------------------------------------------------------------------------------------------------------
function createMap(){
// create a leaflet map with a dark basemap
map = L.map('mapid').setView([39.1839102,-95.9745134], 4.45);

// creates the map from mapbox api
L.tileLayer('https://api.mapbox.com/styles/v1/buddytheelf/ckvsqoj1h11xk14oafqc8fdcm/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYnVkZHl0aGVlbGYiLCJhIjoiY2p2czYxbHNlMndjdzN5cGI3ejI4aWJ5dyJ9.5IPoN9dD2-6boYGfX4ondQ', {
  maxZoom:7,
  minZoom:4,
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
}).addTo(map);


// adds the geojson data
$.getJSON("data/MSA.geojson", function(response){
    geojson = L.geoJSON(response, {
          style: polygonStyle,
          onEachFeature: onEachFeature

    }).addTo(map);

    info.addTo(map);
    createSlider(response);
});
};

//When adding the info
info.onAdd = function (map) {
    //"this" returns to info.
    this._div = L.DomUtil.create('div', 'info');
    //the following line calls info.update(props) function. Again, this refers to 'info' here
    this.update();
    return this._div;
};

//Update the info based on what state user has clicked on
info.update = function (props) {
    this._div.innerHTML = '<h4>Built up area</h4>' + (props ?
        '<b>' + props.NAME10 + '</b><br />' + Math.round(slideArr[index]) + '% BUA in ' + year[index]
        : 'Hover over area');
};

//------------------------------------------------------------------------------------------------------------------
function sliderArray(props){
  slideArr = [
    props.F1900_mean * 100,
    props.F1910_mean * 100,
    props.F1920_mean * 100,
    props.F1930_mean * 100,
    props.F1940_mean * 100,
    props.F1950_mean * 100,
    props.F1960_mean * 100,
    props.F1970_mean * 100,
    props.F1980_mean * 100,
    props.F1990_mean * 100,
    props.F2000_mean * 100,
    props.F2010_mean * 100

  ];
};

function createSlider(response){
    var Slider = L.Control.extend({
      options: {
          position: 'bottomleft'
      },
      onAdd: function () {
        var container = L.DomUtil.create('div', 'sequence-control-container');
          $(container).append('<input class="range-slider" type="range">');
          L.DomEvent.disableClickPropagation(container);
        return container;
        }
    });
map.addControl(new Slider());

$('.range-slider').attr({
  max: 11,
  min: 0,
  value: 0,
  step: 1
});
index = $('.range-slider').val();

$('.range-slider').on('input', function(){
  //Step 6: get the new index value
  index = $(this).val();
  });

};
//-----------------------------------------------------------------------------------------------------------------
function hoverOn(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '	#66ff66',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
    info.update(layer.feature.properties);
    sliderArray(layer.feature.properties);
}


function hoverOff(e) {
    geojson.resetStyle(e.target);
    info.update();

}
function onClick(e) {
    map.fitBounds(e.target.getBounds());
    createLine(e.target.feature.properties);
}
function onEachFeature(feature, layer) {
    layer.on({
      mouseover: hoverOn,
      mouseout: hoverOff,
      click: onClick
    });
}
