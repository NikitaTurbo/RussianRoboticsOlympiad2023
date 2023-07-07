const $node =             document.getElementById('breaken')
const $file =             document.getElementById('file')

const processTextByLine = text => {
    const arr = text.split(/\r?\n/gm)
    arr.map(line => console.log(line))
}

const openFile = async event => {
    const input = event.target
    if (!input) throw new Error('null input')
    const [file] = input.files
    const text = await file.text()
    $node.innerHTML += '<p class="text">' + text + "</p>"
    DrawBreaken(text, "pipe1")
    processTextByLine(text)
}

$file.onchange = openFile

const $nod =             document.getElementById('object')
const $filee =             document.getElementById('file1')

const processText = text => {
    const arr = text.split(/\r?\n/gm)
    arr.map(line => console.log(line))
}

const openFilee = async event => {
    const input = event.target
    if (!input) throw new Error('null input')
    const [file] = input.files
    const text = await file.text()
    $nod.innerHTML += '<p class="text">' + text + "</p>"
    DrawOb(text, "pipe2")
    processText(text)
}

$filee.onchange = openFilee

var loadFile = function(event) {
    var image =             document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
    var image1 =             document.getElementById('output1');
    image1.src = URL.createObjectURL(event.target.files[1]);
};

function DrawBreaken(texta, id) {

    var text = texta.split('\n', 2);

    var dote1 = text[0];
    var dote2 = text[1];

    console.log(Number(dote1.substr(0, dote1.length - 3)))

    //1
    if (Number(dote1.substr(0, dote1.length - 3)) <= 85) {

        if (Number(dote1.substr(0, dote1.length - 3)) <= 43) {

            document.getElementById(id).innerHTML += '<div class="dote1"></div>';
            document.getElementsByClassName("dote1")[0].style.position = "absolute";
            document.getElementsByClassName("dote1")[0].style.color = "red";
            document.getElementsByClassName("dote1")[0].style.right = String((Number(dote1.substr(0, dote1.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("dote1")[0].style.bottom = String(((42 - Number(dote1.substr(0, dote1.length - 3))) * 2.35)) + 'px';

        }

        else {

            document.getElementById(id).innerHTML += '<div class="dote1"></div>';
            document.getElementsByClassName("dote1")[0].style.position = "absolute";
            document.getElementsByClassName("dote1")[0].style.color = "red";
            document.getElementsByClassName("dote1")[0].style.right = String((Number(dote2.substr(0, dote2.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("dote1")[0].style.bottom = String(-((42 - Number(dote2.substr(0, dote2.length - 3))) * 2.35)) + 'px';

        }

    }

    if (Number(dote1.substr(0, dote1.length - 3)) > 85) {

        if (Number(dote1.substr(0, dote1.length - 3)) >= 128) {

            document.getElementById(id).innerHTML += '<div class="dote1"></div>';
            document.getElementsByClassName("dote1")[0].style.position = "absolute";
            document.getElementsByClassName("dote1")[0].style.color = "red";
            document.getElementsByClassName("dote1")[0].style.left = String(50 + (Number(dote1.substr(0, dote1.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("dote1")[0].style.top = String((Number(dote1.substr(0, dote1.length - 3))) * 2.35) + 'px';

        }

        else {

            document.getElementById(id).innerHTML += '<div class="dote1"></div>';
            document.getElementsByClassName("dote1")[0].style.position = "absolute";
            document.getElementsByClassName("dote1")[0].style.color = "red";
            document.getElementsByClassName("dote1")[0].style.left = String((Number(dote1.substr(0, dote1.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("dote1")[0].style.top = String((Number(dote1.substr(0, dote1.length - 3))) * 2.35) + 'px';

        }

    }

    //2
    if (Number(dote2.substr(0, dote2.length - 3)) <= 85) {

        if (Number(dote2.substr(0, dote2.length - 3)) <= 43) {

            document.getElementById(id).innerHTML += '<div class="dote2"></div>';
            document.getElementsByClassName("dote2")[0].style.position = "absolute";
            document.getElementsByClassName("dote2")[0].style.color = "red";
            document.getElementsByClassName("dote2")[0].style.right = String((Number(dote2.substr(0, dote2.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("dote2")[0].style.bottom = String(((42 - Number(dote2.substr(0, dote2.length - 3))) * 2.35)) + 'px';

        }

        else {

            document.getElementById(id).innerHTML += '<div class="dote2"></div>';
            document.getElementsByClassName("dote2")[0].style.position = "absolute";
            document.getElementsByClassName("dote2")[0].style.color = "red";
            document.getElementsByClassName("dote2")[0].style.right = String((Number(dote2.substr(0, dote2.length - 3))) * 1.17 - 4) + '%';
            document.getElementsByClassName("dote2")[0].style.bottom = String(-((42 - Number(dote2.substr(0, dote2.length - 3))) * 2.35) + 6) + 'px';

        }

    }

    if (Number(dote2.substr(0, dote2.length - 3)) > 85) {

        if (Number(dote2.substr(0, dote2.length - 3)) > 128) {

            console.log(1);
            document.getElementById(id).innerHTML += '<div class="dote2"></div>';
            document.getElementsByClassName("dote2")[0].style.position = "absolute";
            document.getElementsByClassName("dote2")[0].style.color = "red";
            document.getElementsByClassName("dote2")[0].style.left = String((Number(dote2.substr(0, dote2.length - 3)) - 85) * 1.17) + '%';
            document.getElementsByClassName("dote2")[0].style.bottom = String(-((Number(dote2.substr(0, dote2.length - 3)) - 85) * 2.35)) + 'px';

        }

        else {

            document.getElementById(id).innerHTML += '<div class="dote2"></div>';
            document.getElementsByClassName("dote2")[0].style.position = "absolute";
            document.getElementsByClassName("dote2")[0].style.color = "red";
            document.getElementsByClassName("dote2")[0].style.right = String((Number(dote2.substr(0, dote2.length - 3)) - 85) * 1.17) + '%';
            document.getElementsByClassName("dote2")[0].style.bottom = String(((Number(dote2.substr(0, dote2.length - 3)) - 50 - 10) * 2.35)) + 'px';

        }

    }

}

function DrawOb(texta, id) {

    var text = texta.split('\n', 2);

    var dote1 = text[0];
    var dote2 = text[1];

    console.log(Number(dote1.substr(0, dote1.length - 3)))

    //1
    if (Number(dote1.substr(0, dote1.length - 3)) <= 85) {

        if (Number(dote1.substr(0, dote1.length - 3)) <= 43) {

            document.getElementById(id).innerHTML += '<div class="obj1"></div>';
            document.getElementsByClassName("obj1")[0].style.position = "absolute";
            document.getElementsByClassName("obj1")[0].style.color = "red";
            document.getElementsByClassName("obj1")[0].style.right = String((Number(dote1.substr(0, dote1.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("obj1")[0].style.bottom = String(((42 - Number(dote1.substr(0, dote1.length - 3))) * 2.35 + 15)) + 'px';

        }

        else {

            document.getElementById(id).innerHTML += '<div class="obj1"></div>';
            document.getElementsByClassName("obj1")[0].style.position = "absolute";
            document.getElementsByClassName("obj1")[0].style.color = "red";
            document.getElementsByClassName("obj1")[0].style.right = String((Number(dote2.substr(0, dote2.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("obj1")[0].style.bottom = String(-((42 - Number(dote2.substr(0, dote2.length - 3))) * 2.35)) + 'px';

        }

    }

    if (Number(dote1.substr(0, dote1.length - 3)) > 85) {

        if (Number(dote1.substr(0, dote1.length - 3)) >= 128) {

            document.getElementById(id).innerHTML += '<div class="obj1"></div>';
            document.getElementsByClassName("obj1")[0].style.position = "absolute";
            document.getElementsByClassName("obj1")[0].style.color = "red";
            document.getElementsByClassName("obj1")[0].style.left = String(50 + (Number(dote1.substr(0, dote1.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("obj1")[0].style.top = String((Number(dote1.substr(0, dote1.length - 3))) * 2.35) + 'px';

        }

        else {

            document.getElementById(id).innerHTML += '<div class="obj1"></div>';
            document.getElementsByClassName("obj1")[0].style.position = "absolute";
            document.getElementsByClassName("obj1")[0].style.color = "red";
            document.getElementsByClassName("obj1")[0].style.left = String((Number(dote1.substr(0, dote1.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("obj1")[0].style.top = String((Number(dote1.substr(0, dote1.length - 3))) * 2.35) + 'px';

        }

    }

    //2
    if (Number(dote2.substr(0, dote2.length - 3)) <= 85) {

        if (Number(dote2.substr(0, dote2.length - 3)) <= 43) {

            document.getElementById(id).innerHTML += '<div class="obj2"></div>';
            document.getElementsByClassName("obj2")[0].style.position = "absolute";
            document.getElementsByClassName("obj2")[0].style.color = "red";
            document.getElementsByClassName("obj2")[0].style.right = String((Number(dote2.substr(0, dote2.length - 3))) * 1.17) + '%';
            document.getElementsByClassName("obj2")[0].style.bottom = String(((42 - Number(dote2.substr(0, dote2.length - 3))) * 2.35)) + 'px';

        }

        else {

            document.getElementById(id).innerHTML += '<div class="obj2"></div>';
            document.getElementsByClassName("obj2")[0].style.position = "absolute";
            document.getElementsByClassName("obj2")[0].style.color = "red";
            document.getElementsByClassName("obj2")[0].style.right = String((Number(dote2.substr(0, dote2.length - 3))) * 1.17 - 4) + '%';
            document.getElementsByClassName("obj2")[0].style.bottom = String(-((42 - Number(dote2.substr(0, dote2.length - 3))) * 2.35) + 6) + 'px';

        }

    }

    if (Number(dote2.substr(0, dote2.length - 3)) > 85) {

        if (Number(dote2.substr(0, dote2.length - 3)) > 128) {

            console.log(1);
            document.getElementById(id).innerHTML += '<div class="dobj2"></div>';
            document.getElementsByClassName("obj2")[0].style.position = "absolute";
            document.getElementsByClassName("obj2")[0].style.color = "red";
            document.getElementsByClassName("obj2")[0].style.left = String((Number(dote2.substr(0, dote2.length - 3)) - 85) * 1.17) + '%';
            document.getElementsByClassName("obj2")[0].style.bottom = String(-((Number(dote2.substr(0, dote2.length - 3)) - 85) * 2.35)) + 'px';

        }

        else {

            document.getElementById(id).innerHTML += '<div class="obj2"></div>';
            document.getElementsByClassName("obj2")[0].style.position = "absolute";
            document.getElementsByClassName("obj2")[0].style.color = "red";
            document.getElementsByClassName("obj2")[0].style.right = String((Number(dote2.substr(0, dote2.length - 3)) - 85) * 1.17) + '%';
            document.getElementsByClassName("obj2")[0].style.bottom = String(((Number(dote2.substr(0, dote2.length - 3)) - 50 - 10) * 2.35)) + 'px';

        }

    }

}
