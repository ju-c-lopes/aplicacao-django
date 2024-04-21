var buttonSaveCSV = document.querySelector(".btn-save-csv");
var buttonSaveGraph = document.querySelector(".btn-save-grafico");

buttonSaveCSV.onclick = () => {
    var csvContent = document.querySelector('#csvContent').value;
    var blob = new Blob([csvContent], {type: 'text/csv'});
    let link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = 'dados.csv';
    link.click();
};

buttonSaveGraph.onclick = () => {
    console.log("tentando salvar")
    var grafico = document.querySelector("#imagem-grafico");
    var imageBase64 = grafico.src;
    var link = document.createElement('a');
    link.href = imageBase64;
    link.download = 'grafico.png'
    link.click();
};