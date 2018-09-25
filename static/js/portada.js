	
//traerse todos los divs con clase 'lugar' y meterlos en una variable array
	let places = document.getElementsByClassName('lugar');
	let lugares = [...places];
	let puntoHtml = document.getElementsByClassName('dot');
	let puntos = [...puntoHtml];

	//variable para el elemento que este visible, se utiliza tambien
	//como indicador del elemento del array
	let current = 0;


	//quitarle la clase 'actual' a quien la tenga y asignarsela
	//al elemento pulsado, ya sea por los circulos de navegación o por
	//las flechas previous y next
	function mostrar(num) {
		for(let i = 0; i< lugares.length; i++){
			if(lugares[i].className.includes('actual')){
			lugares[i].className = lugares[i].className.replace('actual','');
			break;
			}
		}
		current = num;
		lugares[num].className += ' actual';
		puntosColoreados(current)
	}


	//quitar y poner clase css a los dots de navegación
	function puntosColoreados(num) {
		for(let i = 0; i< puntos.length; i++){
			if(puntos[i].className.includes('activo')){
			puntos[i].className = puntos[i].className.replace('activo',''); 
			break;
			}
		}
		puntos[num].className += ' activo';
	}

	//avanzar una imagen
	const next = () => {
		current++;
		if(current > lugares.length - 1) current = 0;
		mostrar(current)
	}

	//retroceder una imagen
	const previous = () => {
		current--;
		if (current < 0) current = lugares.length - 1;
		mostrar(current)
	}

	setTimeout(()=> setInterval(()=>{
				next();
				},7000),
		4000)

	// setTimeout(()=> {
	// 	setInterval(()=>{
	// 		return
	// 		next()
	// 	},7000)
	// }
	// ,5000)
