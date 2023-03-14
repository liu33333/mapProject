function logout() {
    window.location.href="qrcode/";
}

var logoutButton = document.getElementsByClassName("logout");
console.log(logoutButton);
logoutButton[0].addEventListener("click", logout);
//Todo: 修改本地登录数据