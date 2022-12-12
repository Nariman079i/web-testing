function $id(id){
    return document.getElementById(id);
}
function GetTest(){
    let url = 'http://127.0.0.1:8000/api/v1/test/';
    let options = {
        method:'get',
        headers:{
            'Content-Type':'application/json'
        }
    }
    fetch(url,options)
    .then(response => {
        response.json().then(result => {
            result.forEach(element => {
                let name = element.title;
                let id = element.id;
                function gett(){
                    localStorage.setItem(`id`, id);
                    window.location.replace('./quetions.html');
                }
                 
                let template = `<div class="test ${id}"><span>${name}</span> <button id="${id}" type="button" onclick="${gett}">Go</button></div><br>`;
                
                $id('content').innerHTML += template;
                
            });
        })
    });
}

window.onload = GetTest;