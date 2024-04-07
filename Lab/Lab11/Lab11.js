let list_input = ["aloha", "wow", "Level", "step on no pets"];

const checkMirror = word => {
    let revlist = [];
    word.forEach(i => {
        let rev = i.split("").reverse().join("");
        if (i.toLowerCase() === rev.toLowerCase()) {
            revlist.push(i);
        }
    });
    console.log("Mirror word : ", revlist.join(","));
}
checkMirror(list_input);
const findLost = (list) => {
    let lostNumber = []
    for (let i = Math.min(...list); i <= Math.max(...list); i++){
        if (!list.includes(i)) {
            lostNumber.push(i);
        }
    }
    return lostNumber.join(",");
}
console.log(findLost([1, 3, 8]))
const countColor = (color) => {
  const colorList = color.split("-");
  const sortedColorList = colorList.sort().join("-");
  const colorDict = {};

  colorList.forEach((color) => {
    if (!colorDict[color]) {
      colorDict[color] = 1;
    } else {
      colorDict[color] += 1;
    }
  });

    return colorDict.sort(), sortedColorList
};