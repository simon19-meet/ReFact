
function chooseColor(){
    var colors=["#6B7433","#6B8633" ,"#6B6533" ,"#6B9133"];
    var x=0;
    x=Math.floor(Math.random()*4);
    return colors[x];
}
function setBackground(){
    var story=document.getElementsByClassName("story");
    story.forEach(element => {
        element.style.backgroundColor=chooseColor();
        console.log(element);
    });
}