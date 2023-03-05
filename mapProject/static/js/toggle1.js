var shapeName1=document.currentScript.getAttribute("shapeName1");
var shapeName2=document.currentScript.getAttribute("shapeName2");
var control=document.getElementById(shapeName1);
var controler=document.getElementById(shapeName2);
controler.onclick=function(){
    if (control.style.visibility=="hidden"){
        control.style.visibility="visible";
    }
    else{
        control.style.visibility="hidden";
    }
}