var basebuttonElement = document.getElementById("base");
var basePlay = document.getElementById("Base");
var tinkPlay = document.getElementById("Tink");

basebuttonElement.addEventListener("click",function()
{
  basePlay.play()
});
basebuttonElement.addEventListener("mouseenter",function()
{
  tinkPlay.play()
});

var clapbuttonElement = document.getElementById("clap");
var clapPlay = document.getElementById("Clap");
var snarePlay = document.getElementById("Snare");

clapbuttonElement.addEventListener("click",function()
{
  clapPlay.play()
});
clapbuttonElement.addEventListener("mouseenter",function()
{
  snarePlay.play()
});

var hatbuttonElement = document.getElementById("hihat");
var hihatPlay = document.getElementById("Hihat");
var openhatPlay = document.getElementById("Openhat");

hatbuttonElement.addEventListener("click",function()
{
  hihatPlay.play()
});
hatbuttonElement.addEventListener("mouseenter",function()
{
  openhatPlay.play()
});
