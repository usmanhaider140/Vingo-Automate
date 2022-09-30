const { By, Key } = require("selenium-webdriver");

exports.login = async (driver) => {
  await driver
    .findElement(By.name("email"))
    .sendKeys("admin@gmail.com", Key.RETURN);
  await driver
    .findElement(By.name("password"))
    .sendKeys("admin@123", Key.RETURN);
  await driver.findElement(By.id("kt_login_signin_submit")).click();
  // await driver.wait(until.titleIs(""), 1000);
  return;
};
