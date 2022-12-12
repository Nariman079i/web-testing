function GetTest(){
    let url = 'http://127.0.0.1:8000/api/v1/test/'+localStorage.getItem('id');
    let options = {
        method:'get',
        headers:{
            'Content-Type':'application/json'
        }
    }
    fetch(url,options)
    .then(response => response.json())
    .then(result => console.log(result));
}

window.onload = GetTest;