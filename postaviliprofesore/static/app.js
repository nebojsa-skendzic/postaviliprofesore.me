id = 1


function makeForm() {
    try {
        var idstart = document.getElementsByName('name[]');
        id = (+idstart.item(idstart.length - 1).id) + +1;
    }
    catch(err){
        id = 1;
    }
    console.log(idstart);
    var x = document.getElementById('form');
    var submit_button = document.getElementById('result-submit');
    var new_field = document.createElement('input');
    new_field.setAttribute("type", "text");
    new_field.setAttribute("name", "name[]");
    new_field.setAttribute("class", "form-control");
    new_field.setAttribute("placeholder", "Link:");
    new_field.setAttribute("id", id);
    var divadd = document.createElement('div');
    divadd.setAttribute("class", "form-group");
    divadd.appendChild(new_field);
    x.insertBefore(divadd, submit_button);
}

function makeFormResult(splitted) {
    console.log(splitted)
    for (i=0; i < splitted.length; i++){
        try {
            var idstart = document.getElementsByName('name[]');
            id = (+idstart.item(idstart.length - 1).id) + +1;
        }
        catch(err){
            id = 1;
        }
        var x = document.getElementById('form');
        var submit_button = document.getElementById('result-submit');
        var new_field = document.createElement('input');
        new_field.setAttribute("type", "text");
        new_field.setAttribute("name", "name[]");
        new_field.setAttribute("class", "form-control");
        new_field.setAttribute("placeholder", "Link:");
        new_field.setAttribute("id", id);
        var divadd = document.createElement('div');
        divadd.setAttribute("class", "form-group");
        divadd.appendChild(new_field);
        x.insertBefore(divadd, submit_button);
        document.getElementById(id).value = "https://www.ucg.ac.me/objave_spisak/" + splitted[id-1];
    }
}

function delForm() {

    id -= 1;
    var y = document.getElementById(id+1);
    y.remove();

}

function resultrender(data) {
    test = data.sort(function(x, y){
            return y.date - x.date;
        })
    console.log(test);

    var tbodyresult = document.getElementById("result-body");
    tbodyresult.textContent = '';
    for(i = 0; i < test.length; i++){
        var a = document.createElement('a');
        var linkText = document.createTextNode(test[i].title);
        a.appendChild(linkText);
        a.href = test[i].link;
        a.title = test[i].title;
        var new_tr = document.createElement('TR');
        tbodyresult.appendChild(new_tr);
        var th_1 = document.createElement('TH');
        th_1.setAttribute("scope", "row");
        var node = document.createTextNode(i+1);
        new_tr.appendChild(th_1);
        th_1.appendChild(node);
        var th_2 = document.createElement('TD');
        new_tr.appendChild(th_2);
        th_2.appendChild(a);
        var th_3 = document.createElement('TD');
        var node3 = document.createTextNode(test[i].subjecttag);
        new_tr.appendChild(th_3);
        th_3.appendChild(node3);
        var th_4 = document.createElement('TD');
        var node4 = document.createTextNode(convertdate(test[i].date));
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
    var url = `/api/detail-view/${linklist}`;
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
            var shortened = e.replace("https://www.ucg.ac.me/objave_spisak/", "")
            linklist.push(shortened);
            console.log(shortened);
        }
    }
    var url = `/result/${linklist}`;
    console.log(url)
    window.location.href = url;

}

function convertdate(date) {
    var d = new Date(date * 1000); // The 0 there is the key, which sets the date to the epoch
    var dd = d.getDate();
    var mm = d.getMonth()+1;
    var yyyy = d.getFullYear();

    var formattedDate = dd+'.'+mm+'.'+yyyy;

    return formattedDate;
}


/*!
    * Start Bootstrap - Grayscale v6.0.3 (https://startbootstrap.com/theme/grayscale)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
    */
    (function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
                this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top - 70,
                    },
                    1000,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
            $("#mainmast").addClass("masthead");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
})(jQuery); // End of use strict
