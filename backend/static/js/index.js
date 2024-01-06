let li = document.querySelectorAll('.logo_son ul li')
let login = document.querySelector('.login')
let register = document.querySelector('.register')
let ipt1 = document.querySelectorAll('.login input')
let ipt2 = document.querySelectorAll('.register input')
let but1 = document.querySelector('.login button')
let but2 = document.querySelector('.register button')
function fun(){
    li[0].className = 'nav_active'
    li[1].className = ''
    login.style.display = 'block'
    register.style.display = 'none'
}
li[0].onclick = () => {
    fun()
}
li[1].onclick = () => {
    li[0].className = ''
    li[1].className = 'nav_active'
    login.style.display = 'none'
    register.style.display = 'block'
}
but1.onclick = () => {
    if (ipt1[0].value == '') {
        alert('请输入账号！')
    } else if (ipt1[1].value == '') {
        alert('请输入密码！')
    } else {
        window.location.href = 'center.html'
    }
}
but2.onclick = () => {
    if (ipt2[0].value == '') {
        alert('请输入账号！')
    } else if (ipt2[1].value == '') {
        alert('请输入密码！')
    } else if (ipt2[2].value == '') {
        alert('请再次输入密码！')
    } else if (ipt2[1].value != ipt2[2].value) {
        alert('两次密码输入不一致！')
    } else {
        alert('注册成功！')
        fun()
    }
}