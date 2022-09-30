require("chromedriver");
const { Builder, Browser, By, until } = require("selenium-webdriver");
const { login } = require("./login/login");
const { addNew } = require("./companies");

async function example() {
  let driver = await new Builder().forBrowser(Browser.CHROME).build();
  try {
    await driver.get("http://localhost:3006");
    await login(driver);
    await driver.wait(until.urlIs("http://localhost:3006/dashboard"));
    await driver
      .findElement(By.xpath('//*[@id="root"]/div/aside/div[1]/ul/li[2]/a'))
      .click();
    await addNew(driver);
    // await driver.wait(until.titleIs(""), 1000);
  } catch (e) {
    console.log(e);
  } finally {
    // await driver.quit();
  }
}

example();
