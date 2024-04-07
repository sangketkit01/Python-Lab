const fs = require("fs");
function checkFile() {
  try {
    fs.readFileSync("Lab/Lab13/product.txt", "utf8");
  } catch (error) {
    console.log("Cannot open product.txt");
  }
}
function notComplete() {
  const file = fs.readFileSync("Lab/Lab13/product.txt", "utf8");
  const lines = file.split("\n");
  let round = 0;
  for (let line of lines) {
      round++;
      const lineParts = line.split(", ");
      print(lineParts)
    lineParts[3] = lineParts[3].replace("\n", "");
    const price = lineParts[3];
    if (round === 1) continue;
    if (lineParts.length !== 5) {
      console.log(
        `At line ${round}, an invalid data is found and it was skipped. ${lineParts}`
      );
    }
    try {
      if (!(price.endsWith("99") || lineParts.length !== 5)) {
        throw new Error("The price should end with .99");
      }
    } catch (error) {
      console.log(`Check data at line ${round} ${lineParts}`);
    }
  }
}
function complete() {
  const file = fs.readFileSync("Lab/Lab13/product.txt", "utf8");
  const lines = file.split("\n");
  const all_category = {};
  const camping = [];
  const kitchen = [];
  const toilet = [];
  let campingCount = 0;
  let kitchenCount = 0;
  let toiletCount = 0;
  let round = 0;
  let sumItem = 0;
  for (let line of lines) {
    round++;
    const lineParts = line.split(", ");
    const category = lineParts[1];
    const name = lineParts[2];
    const quantity = lineParts[4].replace("\n", "");
    if (round === 1) continue;
    if (lineParts.length === 5) {
      sumItem += parseInt(quantity);
      if (category === "Camping") {
        camping.push(name);
        campingCount++;
      } else if (category === "Kitchen") {
        kitchen.push(name);
        kitchenCount++;
      } else if (category === "Toilet") {
        toilet.push(name);
        toiletCount++;
      }
      if (!(category in all_category)) {
        if (category === "Camping") {
          all_category[category] = camping;
        } else if (category === "Kitchen") {
          all_category[category] = kitchen;
        } else if (category === "Toilet") {
          all_category[category] = toilet;
        }
      }
    }
  }
  console.log(
    `The data in file contains ${round} product\n=================================================\nThere are ${
      Object.keys(all_category).length
    } categories.`
  );
  for (let [k, v] of Object.entries(all_category)) {
    if (k === "Camping") {
      console.log(`Camping ${campingCount} product: ${v.join(", ")}`);
    } else if (k === "Kitchen") {
      console.log(`Kitchen ${kitchenCount} product: ${v.join(", ")}`);
    } else if (k === "Toilet") {
      console.log(`Toilet ${toiletCount} product: ${v.join(", ")}`);
    }
  }
  console.log(
    `=================================================\ntotal contains ${sumItem} items`
  );
}
checkFile();
notComplete();
complete();
