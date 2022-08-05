$(document).ready(function () {
    $("#datatable").DataTable({
      ajax: {
        url: "http://127.0.0.1:8000/api/products/",
        dataSrc:"",
        type: "GET",
        datatype: "json",
      },
      columns: [
        { title: "Id", data: "id" },
        { title: "Descripcion", data: "description" },
        { title: "Precio", data: "price" },
        { title: "Stock", data: "stock" },
      ],
      searching: false,
      language: {
        "lengthMenu": "Mostrar _MENU_ registros por página",
        "zeroRecords": "No hay registros para mostrar",
        "info": "Página _PAGE_ of _PAGES_",
        "infoEmpty": "No hay registros para mostrar",
        "paginate": {
          "first": "Primero",
          "last": "Último",
          "next": "Siguiente",
          "previous": "Anterior"
      },

      },   
    });
  });