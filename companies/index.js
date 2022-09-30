const { By, Key, until } = require("selenium-webdriver");

exports.addNew = async (driver) => {
  await driver
    .findElement(By.xpath('//*[@id="root"]/div/aside/div[1]/ul/li[2]/a'))
    .click();
  await driver.wait(until.urlIs("http://localhost:3006/companies"));

  await driver
    .findElement(
      By.xpath("/html/body/div[1]/div/div/main/div/div/div/div[3]/div[2]/a[2]")
    )
    .click();
  // await driver.wait(until.titleIs(""), 1000);
  return;
};
