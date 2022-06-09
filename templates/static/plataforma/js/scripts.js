$(document).ready(function(){

    var searchBtn = $('#search-botao');
    var searchForm = $('#search-formulario');

    $(searchBtn).on('click', function(){
        searchForm.submit();

    });


});