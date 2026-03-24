document.getElementById('enviar').addEventListener('click', function() {
        var inputs = document.querySelectorAll('input');
        inputs.forEach(function(input) {
            input.value = '';
        });

        window.location.href = 'cad_pg4.html';
    });


document.querySelector('.back').addEventListener('click', function() {
    window.history.back();
});
