
function chooseColor(){
    var colors=[rgb(107,116,51), rgb(107,134,51) ,rgb(107,101,51) ,rgb(107,145,51)];
    var x=0;
    x=Math.floor(Math.random()*4);
    return colors[x];
}
var story=document.getElementsByClassName("story");
story.forEach(element => {
    element.style.backgroundColor=chooseColor();
    console.log(element);
});