var fecha = 0,
    compra = 0,
    venta = 0,
    anho = 0,
    mes = 0,
    arrayTC = [];
anho = document.getElementsByTagName("h3")[0].innerText.toString().split("-")[1].trim()
mesTexto = document.getElementsByTagName("h3")[0].innerText.toString().split("-")[0].trim().toUpperCase()
switch (mesTexto) {
    case "ENERO":
        mes = "01";
        break;
    case "FEBRERO":
        mes = "02";
        break;
    case "MARZO":
        mes = "03";
        break;
    case "ABRIL":
        mes = "04";
        break;
    case "MAYO":
        mes = "05";
        break;
    case "JUNIO":
        mes = "06";
        break;
    case "JULIO":
        mes = "07";
        break;
    case "AGOSTO":
        mes = "08";
        break;
    case "SETIEMBRE":
        mes = "09";
        break;
    case "OCTUBRE":
        mes = "10";
        break;
    case "NOVIEMBRE":
        mes = "11";
        break;
    case "DICIEMBRE":
        mes = "12";
        break;
}

for (j = 1; j < document.getElementsByClassName('class="form-table"')[0].children[0].children.length; j++) {
    for (i = 0; i < document.getElementsByClassName('class="form-table"')[0].children[0].children[j].children.length; i++) {
        if (i % 3 == 0) {
            fecha = anho + '-' + mes + '-' + document.getElementsByClassName('class="form-table"')[0].children[0].children[j].children[i].innerText
        } else if (i % 3 == 1) {
            compra = document.getElementsByClassName('class="form-table"')[0].children[0].children[j].children[i].innerText
        } else if (i % 3 == 2) {
            venta = document.getElementsByClassName('class="form-table"')[0].children[0].children[j].children[i].innerText
            arrayTC.push({ fecha, compra, venta })
            fecha = 0, compra = 0, venta = 0;
        }
    }
}
console.log(JSON.stringify(arrayTC))