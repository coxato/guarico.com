#Django
from django.shortcuts import render

#variables/context

guarico = {
	'map_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4037147.022085074!2d-68.64835128784135!3d8.83048407594819!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8c2aaa20760411b1%3A0x26780acd818f797b!2zR3XDoXJpY28!5e0!3m2!1ses-419!2sve!4v1537059792639'
}

pascua = {
	'name': 'Valle de La Pascua',
	'apodo': 'la pricesa del llano',
	'map_url': 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d86447.28842336252!2d-66.00665738338795!3d9.212289214591927!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e1!3m2!1ses-419!2sve!4v1537062750728',
	#la imagen está en 'static' 
	'image': '../static/images/catedrales/catedralPascua.jpg',
	'image_portada': '../static/images/cities/pascua.jpg',
	'historical_description': 'Valle de la Pascua es la ciudad capital del municipio autónomo de Leonardo Infante, en el estado Guárico, Venezuela. La ciudad se encuentra en los llanos centrales de Venezuela y fue fundada el 25 de febrero de 1785 por el padre Mariano Martí. Es junto a San Juan de Los Morros, Calabozo y Zaraza una de las ciudades más importantes de estado, Las inmediaciones de la ciudad fueron escenario de la Batalla de Valle de la Pascua en febrero de 1814.',
}

tucupido = {
	'name': 'Tucupido',
	'apodo': 'El granero del Llano',
	#la imagen está en 'static' 
	'image': '../static/images/miniMaps/tucupido.jpg',
	'image_portada': '../static/images/cities/tucupido.jpg',
	'historical_description': 'Tucupido es una población venezolana, capital del Municipio José Félix Ribas del Estado Guárico en Los Llanos, se estima que cuenta con una población de más de 55.000 habitantes. Ocupa la divisoria de aguas entre el río Tamanaco y la quebrada Jabillal. El río Tucupido afluye al Tamanaco al noreste de la localidad. La quebrada Jabillal forma el embalse Tucupido situado al sur de la población. Está a 130 m de altitud. Temperatura media de 28 °C y precipitaciones medias anuales de 950 mm .',
	'map_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d21418.607480906372!2d-65.78855373279674!3d9.276916403007915!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8dd363eca1e3910f%3A0x81000f5e6e6c46d6!2sTucupido+2330%2C+Gu%C3%A1rico!5e1!3m2!1ses-419!2sve!4v1537062607514'
}

zaraza = {
	'name': 'zaraza',
	'apodo': 'La flor del Llano',
	#la imagen está en 'static' 
	'image': '../static/images/catedrales/catedralZaraza.png',
	'image_portada': '../static/images/cities/zaraza.jpg',
	'historical_description': 'Zaraza es una ciudad de Venezuela, la capital del Autónomo Municipio Pedro Zaraza en el oriente del estado de Guárico, en la región de Los Llanos. Tiene una población de unos 78.642 habitantes. Para el 2010 se convierte oficialmente en una ciudad universitaria formando parte de las principales Ciudades del Estado Guárico, junto con Calabozo, San Juan de los Morros y Valle de la Pascua. Originalmente fue fundada en el año 1646 con el nombre de "La Ciudad de San Miguel de La Nueva Tarragona del Batey".',
	'map_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d43195.98373829821!2d-65.36308905303291!3d9.35525522251281!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8dd317d8bf5fe571%3A0x108a8f9a4f2216d7!2sZaraza+2332%2C+Gu%C3%A1rico!5e1!3m2!1ses-419!2sve!4v1537062847983'
}
mercedes = {
	'name': 'Las mercedes del llano',
	'apodo': '',
	'image': '../static/images/miniMaps/mercedes.jpg',
	'image_portada': '../static/images/cities/mercedes.jpg',
	'historical_description': 'El Municipio Las Mercedes es uno de los 15 municipios del Estado Guárico, Venezuela. Su capital es la población de Las Mercedes. Tiene una superficie de 7.691 km² siendo el tercer municipio de mayor extensión del Estado Guárico, se estima que para 2011 su población sea de 33.025 habitantes​ según el Instituto Nacional de Estadística de Venezuela pero esta cifra podría elevarse considerablemente por el desarrollo comercial e industrial que se espera desde ese año para este municipio. Éste municipio está conformado por 3 parroquias, Cabruta, Santa Rita de Manapire y Las Mercedes.',
	'map_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d21626.3701891038!2d-66.41758951690178!3d9.10662995691886!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8dd4f7c0f99f119f%3A0x67efb676ce3a08e7!2sLas+Mercedes+del+Llano+2356%2C+Gu%C3%A1rico!5e1!3m2!1ses-419!2sve!4v1537078356965'
}
altagracia = {
	'name': 'Altagracia de Orituco',
	'apodo': '',
	'image': '../static/images/miniMaps/altagracia.jpg',
	'image_portada': '../static/images/cities/altagracia.jpg',
	'historical_description': 'Altagracia de Orituco, fundada como Nuestra Señora de Altagracia de Orituco es una ciudad de Venezuela, situada en el nor-oriente del Estado Guárico, capital del Municipio José Tadeo Monagas y antigua capital del estado. Su población era de 107295 habitantes, según censo de 2011',
	'map_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d43158.474223941295!2d-66.3950917961796!3d9.85517131185564!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8c2b310af6eb2683%3A0xe812450ef745240c!2sAltagracia+De+Orituco%2C+Gu%C3%A1rico!5e1!3m2!1ses-419!2sve!4v1537078618994'
}

SanJuan = {
	'name': 'San Juan de los Morros',
	'apodo': '',
	'image': '../static/images/catedrales/catredralSanJuan.jpg',
	'image_portada': '../static/images/cities/sanJuan4.jpg',
	'historical_description': 'San Juan de Los Morros, es la capital del Estado Guárico en Venezuela, es prácticamente la puerta de entrada a los Llanos Centrales pero sin llegar a ser propiamente llano. Tiene una geografía muy particular donde prevalecen espectaculares montañas. Su población es de 160.248 habitantes, siendo la segunda ciudad más poblada del estado Guárico después de Calabozo y la primera en densidad de población.',
	'map_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d86305.06175451352!2d-67.4153321007081!3d9.900486713631638!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8c2aaa20760411b1%3A0x80d974a28823a010!2sSan+Juan+de+Los+Morros%2C+Gu%C3%A1rico!5e1!3m2!1ses-419!2sve!4v1537079006935'
}

calabozo = {
	'name': 'Calabozo',
	'apodo': '',
	'image': '../static/images/miniMaps/calabozo.jpg',
	'image_portada': '../static/images/cities/calabozo.jpg',
	'historical_description': 'Calabozo, oficialmente Villa de Todos los Santos de Calabozo, es una ciudad de Venezuela situada en el estado Guárico, capital del municipio Francisco de Miranda y antigua capital del estado. Tiene una población de 131.989 habitantes, según el Instituto Nacional De Estadística (INE) en el censo 2011. Se ubica en el centro-oeste del estado Guárico, es uno de los principales productores de arroz del país. Cuenta con el sistema de riego más grande de Venezuela. Es la primera ciudad más poblada del estado y la trigésima primera más poblada del país.',
	'map_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d86551.5948062959!2d-67.48529985902415!3d8.914065444377172!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e7f63cccfa810bb%3A0x36250624c1080db0!2sCalabozo+2312%2C+Gu%C3%A1rico!5e1!3m2!1ses-419!2sve!4v1537078939682'
}
# Create your views here.

#template for the cities
template = 'cities/simple_city_template/city_template.html'

def principal_page(request):
	return render(request,'cities/index.html',{'ciudad_context': guarico})

def pascua_page(request):
	return render(
		request,
		template,
		{'ciudad_context': pascua}
	)

def tucupido_page(request):
	return render(
		request,
		template,
		{'ciudad_context': tucupido}
	)

def zaraza_page(request):
	return render(
		request,
		template,
		{'ciudad_context': zaraza}
	)

def mercedes_page(request):
	return render(
		request,
		template,
		{'ciudad_context': mercedes}
		)

def altagracia_page(request):
	return render(
		request,
		template,
		{'ciudad_context': altagracia}
		)

def SanJuan_page(request):
	return render(
		request,
		template,
		{'ciudad_context': SanJuan}
		)

def calabozo_page(request):
	return render(
		request,
		template,
		{'ciudad_context': calabozo}
		)