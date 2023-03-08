function logout(){
    window.location.replace("../html/qrcode.html");
}
var logoutButton = document.getElementsByClassName("logout");
console.log(logoutButton);
logoutButton[0].addEventListener("click", logout);
//Todo: 修改本地登录数据