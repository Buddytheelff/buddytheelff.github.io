//Author Buddy Collins
"use strict"


var year = ["1900","1910","1920","1930","1940","1950","1960","1970","1980","1990","2000","2010"];
var data;
// append the svg object to the body of the page

function createChart(){
  var svg = d3.select("#chartid").append("svg:svg")
  .attr("width", 800)//canvasWidth)
  .attr("height", 300),//canvasHeight);
  margin = { top: 20, right: 20, bottom: 30, left: 70 },
  width = +svg.attr("width") - margin.left - margin.right,
  height = +svg.attr("height") - margin.top - margin.bottom;


  var scale_x = d3.scaleBand()
  .domain(year)
  .range([0,width]);

  var scale_y = d3.scaleLinear()
  .domain([0,100])
  .range([height,0]);

  var x_axis = d3.axisBottom()
  .scale(scale_x);

  var y_axis = d3.axisLeft()
  .scale(scale_y);
  svg.append("g")
  .attr("transform", "translate(50, 10)")
  .call(y_axis);

  var xAxisTranslate = height + 10;
  svg.append("g")
  .attr("transform", "translate(50, " + xAxisTranslate  +")")
  .call(x_axis);



  svg.append("path")
  .datum(data)
  .attr("fill", "none")
  .attr("stroke", "steelblue")
  .attr("stroke-width", 1.5)
  .attr("d", d3.line()
  .x(function(d) {return x(data.x) })
  .y(function(d) {return y(data.y) })
)


};

function createLine(properties){

  data = [
    {x:"1900", y:properties.F1900_mean * 100},
    {x:"1910", y:properties.F1910_mean * 100},
    {x:"1920", y:properties.F1920_mean * 100},
    {x:"1930", y:properties.F1930_mean * 100},
    {x:"1940", y:properties.F1940_mean * 100},
    {x:"1950", y:properties.F1950_mean * 100},
    {x:"1960", y:properties.F1960_mean * 100},
    {x:"1970", y:properties.F1970_mean * 100},
    {x:"1980", y:properties.F1980_mean * 100},
    {x:"1990", y:properties.F1990_mean * 100},
    {x:"2000", y:properties.F2000_mean * 100},
    {x:"2010", y:properties.F2010_mean * 100}];
    console.log(data);


}
