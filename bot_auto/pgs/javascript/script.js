document.getElementById('proximo').addEventListener('click', function() {
        var inputs = document.querySelectorAll('input');
        inputs.forEach(function(input) {
            input.value = '';
        });

        window.location.href = 'cad_pg2.html';
    });