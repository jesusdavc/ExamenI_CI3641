/**
 * CI-3641 - Lenguajes de Programación I
 * Estudiante: Jesús Cuéllar Carnet: 15-10345. 
 * Pregunta 1b Parte ii */
var isValid = true;
var aux_row = 0;
var aux_column = 0;
var aux_diagonal = 0;
var values = [];
var matrix_example = [[8,1,6],[3,5,7],[4,9,2]];
/**Función que recibe una matrix N*N e indica si es Mágica o no */
function its_magic_matrix(matrix){
    for(let i = 0; i < matrix.length; i++){
        for(let j = 0 ; j < matrix.length; j++){
            if(Number.isInteger(matrix[i][j])){
                aux_row = aux_row + matrix[i][j];
                aux_column = aux_column + matrix[j][i];
                aux_diagonal = aux_diagonal + matrix[j][j];
            };
        };
        values.push(aux_row)
        values.push(aux_column);
        values.push(aux_diagonal);
        aux_row = 0;
        aux_column = 0;
        aux_diagonal = 0;
    };
    if(isValid){
        let isMagic = true;
        let comparation = values[0];
        for(let i = 0; i < values.length; i++){
            if(values[i] == comparation){
                continue
            }else{
                isMagic = false;
            }
        }
        if(isMagic){
            console.log('La matriz: ')
            console.log(matrix);
            console.log('Es mágica')
        }else{
            console.log('La matriz: ')
            console.log(matrix);
            console.log('No es mágica')
        };
    }
};
//Código de prueba
its_magic_matrix(matrix_example);
