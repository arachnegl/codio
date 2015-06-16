//console.log('event listener loaded');
//var button = $('codio-button');
//console.log(button);

window.addEventListener('codio-button-custom', function (ev) {

    //if (codio) {
    //    console.log('codio is defined');
    //}

    var path;

    switch (ev.cmd) {

        case 'hi':
            path = 'hi';
            break;

        case 'hiName':
            path = 'hi_name';
            break;

    }

    $.get(window.location.origin + ':9500/' + path, function (data, err) {
        console.log(data);
    });

});

