

const colors = [
  'azul',
  'amarelo',
  'preto',
  'verde',
  'roxo',
  'rosa'
]
const ColorValues = [
  '#0A01FF',
  '#FFF201',
  '#000000',
  '#34FF01',
  '#8901FF',
  '#ED5ED'
]
const dark = [
  2

]
let animation = false
function end(){
  console.log('hi')
  
}
const socorro = document.getElementById("socorro")
const root = document.documentElement
let element = document.getElementById('socorro')
let computedstyle = window.getComputedStyle(element)
let backgroundcolor = computedstyle.backgroundColor
function color(target ){
  if (!animation){
    animation = true
    root.style.setProperty('--TargetColor', ColorValues[target])

    if (ColorValues[target] == 2){
      console.log('cominggggg')
      socorro.classList.add('forwards')
    } 
    else{
      console.log('stoppppp')
      socorro.classList.add('backwards')
    }
    socorro.classList.remove('ColorChange')
    socorro.classList.add('ColorChange')

    setTimeout( function(){
      socorro.style.setProperty('--MainColor', ColorValues[target]);socorro.classList.remove('forwards');
      socorro.classList.remove('backwards'); socorro.classList.remove('ColorChange'); animation = false
    },2000)
    
    console.log(backgroundcolor)
    console.log("target is :", colors[target])
    
  }
}
