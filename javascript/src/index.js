const inputText = document.querySelector(`.inputText`);
const button_0 = document.querySelector(`.button_0`);
const button_1 = document.querySelector(`.button_1`);
const button_2 = document.querySelector(`.button_2`);
const button_3 = document.querySelector(`.button_3`);
const button_4 = document.querySelector(`.button_4`);
const button_5 = document.querySelector(`.button_5`);
const button_6 = document.querySelector(`.button_6`);
const button_7 = document.querySelector(`.button_7`);
const button_8 = document.querySelector(`.button_8`);
const button_9 = document.querySelector(`.button_9`);
const addition = document.querySelector(`.addition`);
const subtraction = document.querySelector(`.subtraction`);
const multiplication = document.querySelector(`.multiplication`);
const division = document.querySelector(`.division`);
const equal = document.querySelector(`.equal`);
const reset = document.querySelector(`.reset`);

class Calc {
  constructor() {
    this.initValue = 0;
    this.inputTempText = document.querySelector(`.inputTempText`);
  }

  result(display) {
    try {
      display.value = eval(this.inputTempText.value);
      return display.value;
    } catch (error) {
      console.error(error);
      display.value = "Error! Press the 'C' button";
    }
  }
}

const calc = new Calc();
inputText.value = calc.initValue;
calc.inputTempText.value = calc.initValue;

function ButtonClicked(event) {
  if (
    (inputText.value === "0" || calc.inputTempText.value === "0") &&
    event.target.innerText !== "+" &&
    event.target.innerText !== "-" &&
    event.target.innerText !== "*" &&
    event.target.innerText !== "/" &&
    calc.inputTempText.value.indexOf("+") === -1 &&
    calc.inputTempText.value.indexOf("-") === -1 &&
    calc.inputTempText.value.indexOf("*") === -1 &&
    calc.inputTempText.value.indexOf("/") === -1
  ) {
    inputText.value = event.target.innerText;
    calc.inputTempText.value = event.target.innerText;
  } else if (
    event.target.innerText !== "+" &&
    event.target.innerText !== "-" &&
    event.target.innerText !== "*" &&
    event.target.innerText !== "/" &&
    calc.inputTempText.value.slice(-1) !== "+" &&
    calc.inputTempText.value.slice(-1) !== "-" &&
    calc.inputTempText.value.slice(-1) !== "*" &&
    calc.inputTempText.value.slice(-1) !== "/"
  ) {
    inputText.value += event.target.innerText;
    calc.inputTempText.value += event.target.innerText;
  } else if (
    calc.inputTempText.value !== "0" &&
    calc.inputTempText.value.slice(-1) !== "+" &&
    calc.inputTempText.value.slice(-1) !== "-" &&
    calc.inputTempText.value.slice(-1) !== "*" &&
    calc.inputTempText.value.slice(-1) !== "/" &&
    (event.target.innerText === "+" ||
      event.target.innerText === "-" ||
      event.target.innerText === "*" ||
      event.target.innerText === "/") &&
    calc.inputTempText.value.indexOf("+") === -1 &&
    calc.inputTempText.value.indexOf("-") === -1 &&
    calc.inputTempText.value.indexOf("*") === -1 &&
    calc.inputTempText.value.indexOf("/") === -1
  ) {
    inputText.value += "";
    calc.inputTempText.value += event.target.innerText;
  } else if (
    (calc.inputTempText.value.slice(-1) === "+" ||
      calc.inputTempText.value.slice(-1) === "-" ||
      calc.inputTempText.value.slice(-1) === "*" ||
      calc.inputTempText.value.slice(-1) === "/") &&
    event.target.innerText !== "+" &&
    event.target.innerText !== "-" &&
    event.target.innerText !== "*" &&
    event.target.innerText !== "/"
  ) {
    inputText.value = event.target.innerText;
    calc.inputTempText.value += event.target.innerText;
  } else if (
    (calc.inputTempText.value.slice(-1) === "+" ||
      calc.inputTempText.value.slice(-1) === "-" ||
      calc.inputTempText.value.slice(-1) === "*" ||
      calc.inputTempText.value.slice(-1) === "/") &&
    (event.target.innerText === "+" ||
      event.target.innerText === "-" ||
      event.target.innerText === "*" ||
      event.target.innerText === "/") &&
    (calc.inputTempText.value.indexOf("+") === -1 ||
      calc.inputTempText.value.indexOf("-") === -1 ||
      calc.inputTempText.value.indexOf("*") === -1 ||
      calc.inputTempText.value.indexOf("/") === -1)
  ) {
    calc.inputTempText.value = calc.inputTempText.value.replace(
      calc.inputTempText.value.slice(-1),
      event.target.innerText
    );
  } else if (
    (event.target.innerText === "+" ||
      event.target.innerText === "-" ||
      event.target.innerText === "*" ||
      event.target.innerText === "/") &&
    (calc.inputTempText.value.indexOf("+") !== -1 ||
      calc.inputTempText.value.indexOf("-") !== -1 ||
      calc.inputTempText.value.indexOf("*") !== -1 ||
      calc.inputTempText.value.indexOf("/") !== -1)
  ) {
    const result = calc.result(inputText);
    calc.inputTempText.value = result;
    calc.inputTempText.value += event.target.innerText;
  }
}

button_0.addEventListener(`click`, ButtonClicked);
button_1.addEventListener(`click`, ButtonClicked);
button_2.addEventListener(`click`, ButtonClicked);
button_3.addEventListener(`click`, ButtonClicked);
button_4.addEventListener(`click`, ButtonClicked);
button_5.addEventListener(`click`, ButtonClicked);
button_6.addEventListener(`click`, ButtonClicked);
button_7.addEventListener(`click`, ButtonClicked);
button_8.addEventListener(`click`, ButtonClicked);
button_9.addEventListener(`click`, ButtonClicked);
addition.addEventListener(`click`, ButtonClicked);
subtraction.addEventListener(`click`, ButtonClicked);
multiplication.addEventListener(`click`, ButtonClicked);
division.addEventListener(`click`, ButtonClicked);

function ResetValue() {
  inputText.value = calc.initValue;
  calc.inputTempText.value = calc.initValue;
}

reset.addEventListener(`click`, ResetValue);

function ResultValue() {
  const result = calc.result(inputText);
  calc.inputTempText.value = result;
}

equal.addEventListener(`click`, ResultValue);
