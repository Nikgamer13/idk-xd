document.addEventListener('DOMContentLoaded', function() {
    const tipoResiduo = document.getElementById('tipo-residuo');
    const subtipoResiduo = document.getElementById('subtipo-residuo');

    const subtipos = {
        plastico: ['Botellas', 'Bolsas', 'Envases'],
        papel: ['Cartón', 'Papel de oficina', 'Revistas'],
        vidrio: ['Botellas', 'Frascos'],
        metal: ['Latas', 'Tuberías'],
        electronico: ['Computadoras', 'Teléfonos', 'Baterías']
    };

    tipoResiduo.addEventListener('change', function() {
        const selectedTipo = this.value;
        subtipoResiduo.innerHTML = '<option value="">Seleccione un subtipo</option>';

        if (subtipos[selectedTipo]) {
            subtipos[selectedTipo].forEach(function(subtipo) {
                const option = document.createElement('option');
                option.value = subtipo.toLowerCase();
                option.textContent = subtipo;
                subtipoResiduo.appendChild(option);
            });
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-reciclaje');

    if (form) {
        form.addEventListener('submit', function(event) {
            const nombre = document.getElementById('nombre').value.trim();
            const email = document.getElementById('email').value.trim();
            const direccion = document.getElementById('direccion').value.trim();
            const cantidad = document.getElementById('cantidad').value.trim();
            let valido = true;

            if (nombre.length < 1) {
                alert('Por favor, ingresa un nombre válido de al menos 2 caracteres.');
                valido = false;
            }

            const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$/;
            if (!emailPattern.test(email)) {
                alert('Por favor, ingresa un correo electrónico válido.');
                valido = false;
            }

            if (direccion.length < 1) {
                alert('Por favor, ingresa una dirección válida de al menos 5 caracteres.');
                valido = false;
            }

            if (isNaN(cantidad) || cantidad <= 0) {
                alert('Por favor, ingresa una cantidad válida de residuos mayor que 0.');
                valido = false;
            }

            if (!valido) {
                event.preventDefault();
            }
        });
    }
});

function confirmar() {
    return confirm("¿Estas seguro de que deseas enviar la solicitud?");
}