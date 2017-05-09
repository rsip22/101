// Escreva um trecho de código para imprimir os números pares definidos por um intervalo de valores inteiros não-negativos, inicio e fim.

function imprimirPares(num1, num2) {
  console.log("Início")
  if(isNaN(num1) || isNaN(num2)){
    console.log("Você precisa digitar números inteiros!")
    } else {
    console.log("Números pares no intervalo entre "+ num1 + " e " + num2 + ":")
    for (i = num1; i <= num2; i++){
      if(i%2 === 0){
        console.log(i)
      }
    }
    console.log("Fim.")
  }
}

imprimirPares(1, 10)
