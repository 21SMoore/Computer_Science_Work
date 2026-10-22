let lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10];
console.log(lst)

lst.sort(function(a,b){return a-b});
console.log('Sorted list:', lst);

// Calculate total and mean
function mean() {
let total = 0
for(let x of lst) {
    total += x;
}
console.log("Total:", total);
let mean = total / lst.length;
console.log("Mean:", mean);
return mean;
}


// Calculate median
function median() {
if (lst.length % 2 === 0) {
    let mid1 = lst[lst.length / 2 - 1];
    let mid2 = lst[lst.length / 2];
    let median = (mid1 + mid2) / 2;
    console.log("Median:", median);
} else {
    let median = lst[Math.floor(lst.length / 2)];
}
console.log("Median:", median);
return median;
}


//calculate mode
function mode() {
let check = 0;
let often = 0;
let frequency = [];
for (let x of lst) {
    if (x == check) {
        often += 2
        check == x
        frequency.push(x);
    } else {
        check = x;
    }
    return frequency;
    console.log("Mode:", mode);
}
}


//frequency
function frequency() {
    empty = []
    freq = []

for (let x of lst) {
    if (empty.includes(x)) {
        let index = empty.indexOf(x);
        freq[index] += 1;
    } else {
        empty.push(x);
        freq.push(1);
    }
console.log("Frequency:", frequency());
return freq;
}
}

//range
function range() {
    let min = Math.min(...lst);
    let max = Math.max(...lst);
    let range = max - min;
    console.log("Range:", range);
    return range;
}