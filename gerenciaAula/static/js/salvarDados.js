var buttonSaveCSV = document.querySelector(".btn-save-csv");

buttonSaveCSV.onclick = () => {
    var csvContent = document.querySelector('#csvContent').value;
    var blob = new Blob([csvContent], {type: 'text/csv'});
    var link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = 'dados.csv';
    link.click();
}