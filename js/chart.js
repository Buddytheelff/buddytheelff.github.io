//Author Buddy Collins
"use strict"

var name = "Click on an area from the map"
var data =  [
  {"x":"1900", "y":0.1 * 100},
  {"x":"1910", "y":0.2 * 100},
  {"x":"1920", "y":0.3 * 100},
  {"x":"1930", "y":0.35 * 100},
  {"x":"1940", "y":0.4 * 100},
  {"x":"1950", "y":0.45 * 100},
  {"x":"1960", "y":0.5 * 100},
  {"x":"1970", "y":0.55 * 100},
  {"x":"1980", "y":0.6 * 100},
  {"x":"1990", "y":0.65 * 100},
  {"x":"2000", "y":0.7 * 100},
  {"x":"2010", "y":0.75 * 100}];
  var width = 430 -80;
  var height = 350 -120;
  var areasSelected = 0;
  var chartYOne = 0;
// append the svg object to the body of the page

function createChart(){
  var chartMax = d3.max(data, function(d) { return +d.y; })
  if (chartMax > chartYOne || chartMax === chartYOne){
    chartMax = chartMax;
  }else{
    chartMax = chartYOne;
  }

  var svg = d3.select("#chartid")
  .append("svg:svg")
  .attr("id","chartsvg")
  .attr("preserveAspectRatio", "xMinYMin meet")
  .attr("viewBox", "0 0 430 390")
  .classed("svg-content", true);
  //title
  svg.append('text')
  .attr('x', width/2 + 50)
  .attr('y', height-height+20)
  .attr('text-anchor', 'middle')
  .style('font-family', 'Helvetica')
  .style('font-size', 8)
  .text(name);



  var scale_x = d3.scaleBand()
  .domain(data.map(function(d) {return d.x}))
  .range([0,width]);

  var scale_y = d3.scaleLinear()
  .domain([0, chartMax + 10])
  .range([height,0]);

  var x_axis = d3.axisBottom()
  .scale(scale_x);

  var y_axis = d3.axisLeft()
  .scale(scale_y);
  svg.append("g")
  .attr("transform", "translate(50, 50)")
  .call(y_axis);

  var xAxisTranslate = height + 50;
  svg.append("g")
  .attr("transform", "translate(50, " + xAxisTranslate  +")")
  .call(x_axis);

  svg.append('g')
  .selectAll("dot")
  .data(data)
  .enter()
  .append("circle")
  .attr("cx", function (d) { return scale_x(d.x) } )
  .attr("cy", function (d) { return scale_y(d.y) } )
  .attr("r", 2)
  .attr("transform", "translate(65,50)")
  .style("fill", "steelblue");

  svg.append("path")
  .datum(data)
  .attr("fill", "none")
  .attr("stroke", "steelblue")
  .attr("stroke-width", 1.5)
  .attr("d", d3.line()
  .x(function(d) { return scale_x(d.x) })
  .y(function(d) { return scale_y(d.y) })
  )
  .attr("transform", "translate(65,50)");

  // X label
  svg.append('text')
  .attr('x', width/2 + 50)
  .attr('y', height + 90)
  .attr('text-anchor', 'middle')
  .style('font-family', 'Helvetica')
  .style('font-size', 8)
  .text('Year');

  // Y label
  var yAxistranslate = height/2 + 50
  svg.append('text')
  .attr('text-anchor', 'middle')
  .attr('transform', 'translate(15,' + yAxistranslate + ')rotate(-90)')
  .style('font-family', 'Helvetica')
  .style('font-size', 8)
  .text('% Built Up Area');


};

function createLine(properties){
  d3.select("#chartsvg").remove();

  chartYOne = d3.max(data, function(d) { return +d.y; })
  name = properties.NAME10;
  data = [
    {"x":"1900", "y":properties.F1900_mean * 100},
    {"x":"1910", "y":properties.F1910_mean * 100},
    {"x":"1920", "y":properties.F1920_mean * 100},
    {"x":"1930", "y":properties.F1930_mean * 100},
    {"x":"1940", "y":properties.F1940_mean * 100},
    {"x":"1950", "y":properties.F1950_mean * 100},
    {"x":"1960", "y":properties.F1960_mean * 100},
    {"x":"1970", "y":properties.F1970_mean * 100},
    {"x":"1980", "y":properties.F1980_mean * 100},
    {"x":"1990", "y":properties.F1990_mean * 100},
    {"x":"2000", "y":properties.F2000_mean * 100},
    {"x":"2010", "y":properties.F2010_mean * 100}];
    createChart();
    areasSelected = areasSelected + 1;

}
