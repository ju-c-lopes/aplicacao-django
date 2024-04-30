var buttonSaveCSV = document.querySelectorAll(".btn-save-csv");
var buttonSaveGraph = document.querySelectorAll(".btn-save-grafico");

for (let i = 0; i < buttonSaveCSV.length; i++) {
    buttonSaveCSV[i].onclick = () => {
        var csvContent = document.querySelector(`#csvContent${i}`).value;
        var blob = new Blob([csvContent], {type: 'text/csv'});
        let link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = 'dados.csv';
        link.click();
    };
}

for (let i = 0; i < buttonSaveGraph.length; i++) {
    buttonSaveGraph[i].onclick = () => {
        var grafico = document.querySelector(`#imagem-grafico${i}`);
        var imageBase64 = grafico.src;
        var link = document.createElement('a');
        link.href = imageBase64;
        link.download = 'grafico.png'
        link.click();
    };
}