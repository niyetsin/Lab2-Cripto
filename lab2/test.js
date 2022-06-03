const { Builder } = require("selenium-webdriver");
const chrome = require('selenium-webdriver/chrome');

let options = new chrome.Options();
options.setChromeBinaryPath("C:/Users/milox/AppData/Local/Programs/Opera/launcher.exe");

let driver = await new Builder()
  .forBrowser('chrome')
  .setChromeOptions(options)
  .build();

await driver.quit();