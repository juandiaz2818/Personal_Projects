// Crear variables que contengan todo lo de los contendores del html
// Creamos las variables

// Contenedor de palabras
const ContenedorPalabras = document.getElementById('wordContainer');
// Contenedor de boton iniciar
const startButton = document.getElementById('startButton');
// Contenedor de palabras del usuarios
const PalabrasUsuarioElement = document.getElementById('usedLetters');
// Obetenemos el canvas
const canvas = document.getElementById('canvas');
// Inicializamos canvas
let ctx = canvas.getContext('2d');
// Establecemos Ancho y Alto del canvas
ctx.canvas.width = 0;
ctx.canvas.heiht = 0;
// Dibujo del muñequito ahorcado

const bodyParts = [
    [4,2,1,1],
    [4,3,1,2],
    [3,5,1,1],
    [5,5,1,1],
    [3,3,1,1],
    [5,3,1,1]
];
// Variables del juego

// Selecciona la palabra del archivo palabras.js
let PalabraSeleccionada;
// Guardar la palabra hecha por el usuario
let PalabrasUsuario;
// Errores del usuario
let Errores;
// Aciertos del usuario
let Aciertos;

// Funcion para añadir palabras
const addPalabra = Palabra => {
    // Crear un elemento span
    const PalabraElement = document.createElement('span');
    // Convertir en mayusculas
    PalabraElement.innerHTML = Palabra.toUpperCase();
    // Agregar la palabra al nuevo elemento creado
    PalabrasUsuarioElement.appendChild(PalabraElement);
}
// Funcion para añadir partes del muñequito
const addBodyPart = bodyPart => {
    // Establecer un color al muñeco
    ctx.fillStyle = '#9638D8';
    // Dibujamos con fillrect el muñequito
    ctx.fillRect(...bodyPart)
}
// Funcion para palabras incorrectas
const wrongPalabra = () =>{
    // Agregar un bodypart para generar a la persina de ahorcado
    addBodyPart(bodyParts[Errores]);
    // Sumamos los errores
    Errores++;
    // Verificar si los errores son igual a las partes del muñequito
    if(Errores === bodyParts.length)endGame();
}
// Funcion de Finalizacion de videojuego
const endGame = () =>{
    // Eliminaremso todos los eventos de la teclas
    document.removeEventListener('keydown',PalabraEvent);
    // Ejecutamos el boton de inicio
    startButton.style.display = 'block';
};
// Funcion para  la palabra correcta
const correctPalabra = Palabra => {
    // Obtenemos todos los span
    const {children} = ContenedorPalabras;
    // Iteramos cada letra que se esta obteniendo
    for(let i = 0; i < children.length; i++){
        // Sacamos de la clase hiden la letra que ingreso el usuario
        if(children[i].innerHTML === Palabra){
        children[i].classList.toggle('hidden');
        Aciertos++; 
        }
    }
    if(Aciertos === PalabraSeleccionada.length)endGame()
}
// Funcion para ingresar  la palabra del usuario
const PalabraInput = Palabra => {
    // Evaluamos los valores que se tratan de adivinar
    if (PalabraSeleccionada.includes(Palabra)){
        correctPalabra(Palabra)
    }
    else{
        // Llamamos a una funcion la cual me dira si la palabra es incorrecta
        wrongPalabra()
    }
    // Agregamos la letra que ingrese el usuario
    addPalabra(Palabra)
    // Agregar la palabra establecida en la funcion
    PalabrasUsuario.push(Palabra)
}
// Funcion para evaluar la gramatica del usuario
const PalabraEvent = event => {
    // Recoger la palabra y convertirla en mayuscula
    let newPalabra = event.key.toUpperCase();
    // Evaluar si esa palabra cumple ciertos requerimientos
    if(newPalabra.match(/^[a-zñ]$/i) && !PalabrasUsuario.includes(newPalabra)){
        PalabraInput(newPalabra)
    }
};
// Funcion para dibujar la palabra
const drawWord = () =>{
    // Seleccionamos la palabra 
    PalabraSeleccionada.forEach(Palabra => {
        // Creamos un elemento de tipo span
        const PalabraElement = document.createElement('span');
        // Guardamos la palabra en mayuscula
        PalabraElement.innerHTML = Palabra.toUpperCase();
        // Añadimos clases a los nuevos elementos
        PalabraElement.classList.add('letter');
        PalabraElement.classList.add('hidden');
        // Asignamos la letra en el contenedor de palabras
        ContenedorPalabras.appendChild(PalabraElement)
        
    });
};
// Funcion para escoger palabra random :D
const selectRandomWord = () => {
    // Crear variable que me guarde la palabra
    let palabra = words[Math.floor((Math.random()* words.length))].toUpperCase();
    // Aplicamos la separacion de caracteres
    PalabraSeleccionada = palabra.split('');
};


// Funcion para dibujar al ahorcado
const DrawHangMan = ()=>{
    // Dimensiones al ahorcado

    // Alto
    ctx.canvas.width = 240;
    // Ancho
    ctx.canvas.height = 360;
    // Tamaño de pixeles
    ctx.scale(40,40)
    // Borramos todo lo que se encuentre en si dibujado
    ctx.clearRect(0,0, canvas.width, canvas.height)
    // Empezamos a dibujar al hombrecito
    ctx.fillStyle = '#9C2222';
    // Posicionamos el muñeco segun las coordenadas

    ctx.fillRect(0, 7, 4 ,1);
    ctx.fillRect(1, 0, 1, 8);
    ctx.fillRect(2, 0, 3, 1);
    ctx.fillRect(4, 1, 1, 1);
};
// Funcion para inicializar videojuego
const IniciodeVideojuego = ()=>{
    // Reseteamos todas las variables
    
    // Reseteamos palabras de usuario
    PalabrasUsuario = [];
    // Reseteamos los errores del usuario
    Errores = 0;
    // Reseteamos lo que son los aciertos
    Aciertos =  0;
    // Reseteamos contenedor de palabra
    ContenedorPalabras.innerHTML = '';
    // Reseteamos el contenedor de las letras
    PalabrasUsuarioElement.innerHTML = '';
    // Escondemos el boton de Start o inicio
    startButton.style.display = 'none'
    DrawHangMan();
    selectRandomWord()
    drawWord()
    // Cuando el usuario presione una tecla cualquiera se ejecutara una funcion
    document.addEventListener('keydown',PalabraEvent)
}
// Evento para iniciar el juego
startButton.addEventListener('click',IniciodeVideojuego)
//Funcion para mostrar el texto inferior
function texto_mostrar() {
        document.getElementById(texto)
        texto.style.display = "block"
}
