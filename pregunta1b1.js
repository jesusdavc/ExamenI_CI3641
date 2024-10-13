/* CI-3641 - Lenguajes de Programación I
 * Estudiante: Jesús Cuéllar Carnet: 15-10345. 
 * Pregunta 1b Parte i */
var a = 3;
var b = 2;
var c = 2;
/*La función module_pot tiene como parametros a,b,c que son 
enteros los cuales se usan para calcular
la potencia modulada dada la forma expresada en el enunciado */
function module_pot(a, b, c) {
    if (b == 0) {
        return 1;
    } else {
        return ((a % c) * ((a ** (b - 1)) % c)) % c;
    }
};

//Código de prueba
z = module_pot(3,2,2);
console.log(`El valor de la potencia modulada ${a}^${b} mod ${c} es ${z}.`);

