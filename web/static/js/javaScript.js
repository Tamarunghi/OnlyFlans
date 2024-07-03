// Función para deshabilitar el data-bs-toggle="collapse" en pantallas grandes (lg)
function disableCollapseOnLG() {
    const navbarToggle = document.querySelector('.navbar-toggler');
    const screenWidth = window.innerWidth;
    
    if (screenWidth >= 992) { // 992px es el breakpoint de LG en Bootstrap
      navbarToggle.setAttribute('data-bs-toggle', ''); // Deshabilita el data-bs-toggle
    } else {
      navbarToggle.setAttribute('data-bs-toggle', 'collapse'); // Habilita el data-bs-toggle
    }
  }
  
  // Ejecutar al cargar la página y en redimensionamientos
  disableCollapseOnLG();
  window.addEventListener('resize', disableCollapseOnLG);
  