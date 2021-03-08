id = 1

function makeForm() {
    var x = document.getElementById('form');
    var submit_button = document.getElementById('result-submit');
    var new_field = document.createElement('input');
    new_field.setAttribute("type", "text");
    new_field.setAttribute("name", "name[]");
    new_field.setAttribute("class", "form-control");
    new_field.setAttribute("placeholder", "Enter link");
    new_field.setAttribute("id", id);
    id += 1;
    var divadd = document.createElement('div');
    divadd.setAttribute("class", "form-group");
    divadd.appendChild(new_field);
    x.insertBefore(divadd, submit_button);

}

function makeFormResult(splitted) {
    console.log(splitted)
    for (i=0; i < splitted.length; i++){
        var x = document.getElementById('form');
        var submit_button = document.getElementById('result-submit');
        var new_field = document.createElement('input');
        new_field.setAttribute("type", "text");
        new_field.setAttribute("name", "name[]");
        new_field.setAttribute("class", "form-control");
        new_field.setAttribute("placeholder", "Enter link");
        new_field.setAttribute("id", id);
        var divadd = document.createElement('div');
        divadd.setAttribute("class", "form-group");
        divadd.appendChild(new_field);
        x.insertBefore(divadd, submit_button);
        document.getElementById(id).value = splitted[id-1];
        id += 1;
    }
}

function delForm() {

    var y = document.getElementById(id-1);
    y.remove();
    id -= 1;
}

function resultrender(data) {
    document.getElementById('result-table').style.display = 'table';
    var tbodyresult = document.getElementById("result-body");
    tbodyresult.textContent = '';
    for(i = 0; i < data.length; i++){
        var a = document.createElement('a');
        var linkText = document.createTextNode(data[i].title);
        a.appendChild(linkText);
        a.href = data[i].link;
        a.title = data[i].title;
        var new_tr = document.createElement('TR');
        tbodyresult.appendChild(new_tr);
        var th_1 = document.createElement('TH');
        th_1.setAttribute("scope", "col");
        var node = document.createTextNode(i+1);
        new_tr.appendChild(th_1);
        th_1.appendChild(node);
        var th_2 = document.createElement('TH');
        th_2.setAttribute("scope", "col");
        new_tr.appendChild(th_2);
        th_2.appendChild(a);
        var th_3 = document.createElement('TH');
        th_3.setAttribute("scope", "col");
        var node3 = document.createTextNode(data[i].subjecttag);
        new_tr.appendChild(th_3);
        th_3.appendChild(node3);
        var th_4 = document.createElement('TH');
        th_4.setAttribute("scope", "col");
        var node4 = document.createTextNode(data[i].date);
        new_tr.appendChild(th_4);
        th_4.appendChild(node4);

    }


}

function submitfunc() {
    event.preventDefault();
    var inputs = document.getElementsByName('name[]');
    var linklist = [];
    for(i = 0; i < inputs.length; i++){
        var e = inputs[i].value;
        if (e == ""){
            inputs[i].remove();
            i--;
        } else {
            linklist.push(e);
        }
    }
    console.log(linklist);
    var url = `http://127.0.0.1:8000/api/detail-view/${linklist}`;
    fetch(url)
    .then(response => response.json())
    .then(data => resultrender(data));

}

function submitalt() {
    event.preventDefault();
    var inputs = document.getElementsByName('name[]');
    var linklist = [];
    for(i = 0; i < inputs.length; i++){
        var e = inputs[i].value;
        if (e == ""){
            inputs[i].remove();
            i--;
        } else {
            linklist.push(e);
        }
    }
    console.log(linklist);
    var url = `http://127.0.0.1:8000/result/${linklist}`;
    window.location.href = url;

}

