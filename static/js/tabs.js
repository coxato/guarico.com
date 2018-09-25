
(function(d){
    let t = d.querySelectorAll(".tabs__item");
    let tabs = [...t];
    let p = d.querySelectorAll(".panel__item");
    let panels = [...p];
    
    //delegacion de eventos para 
    d.getElementById('ulPadreLi').addEventListener('click',e => {
        if(e.target.classList.contains('tabs__item')){
        //obtener el indice
            let i = tabs.indexOf(e.target);
         //recorre todos los tabs y quita la clase active
         //luego la coloca solo al elemento pulsado[i]  
        tabs.map(tab => tab.classList.remove('active'));
        tabs[i].classList.add('active');

        //recorre los paneles, le quita la clase 'active'
        //y solo agrega a el indice[i]
        panels.map(pan => pan.classList.remove('active'));
        panels[i].classList.add('active');
            
        }
    })

})(document);

