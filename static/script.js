document.querySelector('.reg-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    btn.textContent = "Procesando...";
    
    setTimeout(() => {
        alert("¡Registro exitoso para Perla & César!");
        btn.textContent = "Crear Cuenta";
        e.target.reset();
    }, 1500);
});
