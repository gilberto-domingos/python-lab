document.getElementById('proximo').addEventListener('click', function() {
        var inputs = document.querySelectorAll('input');
        inputs.forEach(function(input) {
            input.value = '';
        });

        window.location.href = 'cad_pg3.html';
    });

document.querySelector('.back').addEventListener('click', function() {
    window.history.back();
});
