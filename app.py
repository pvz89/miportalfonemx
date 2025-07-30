import streamlit as st

def main():
    # Configure page
    st.set_page_config(
        page_title="Mi Portal Fone - Guía Completa SEP 2025",
        layout="centered"
    )
    
    # Header with primary backlink
    st.title("🔥 Mi Portal Fone SEP - Gestión de Recibos Educativos 2025")
    st.markdown("Plataforma oficial de la Secretaría de Educación Pública (SEP) para profesionales del sector educativo")
    st.markdown("[Acceso Directo al Portal Oficial](https://miportal.fone.sep.gob.mx)")
    st.markdown("---")
    
    # Main content sections
    st.header("¿Qué es Mi Portal Fone?")
    st.markdown("""
    **Mi Portal FONE** es la plataforma digital oficial de la Secretaría de Educación Pública (SEP) de México, diseñada para:
    - Gestionar nóminas y comprobantes de pago del sector educativo
    - Centralizar operaciones del Fondo de Aportaciones para la Nómina Educativa (FONE)
    - Proporcionar acceso instantáneo a recibos desde 2015
    - Digitalizar trámites administrativos para docentes y personal educativo
    """)
    
    st.markdown("""
    ### 🔑 Beneficios Clave:
    - Descarga inmediata de recibos SEP 2025
    - Consulta de detalles financieros (bonos, deducciones)
    - Verificación de datos fiscales (RFC, CURP)
    - Acceso desde cualquier dispositivo con internet
    - Soporte técnico 24/7
    """)
    
    # Feature table
    st.subheader("Características de Mi Portal Fone")
    st.table({
        "Función": ["Acceso", "Seguridad", "Disponibilidad", "Soporte", "Formatos"],
        "Detalle": [
            "Dispositivos con internet",
            "Autenticación con CURP y contraseña",
            "Recibos desde 2015 hasta actual",
            "Asistencia 24/7 vía correo/teléfono",
            "Descarga en PDF (archivos RAR)"
        ]
    })
    
    # Registration section
    st.markdown("---")
    st.header("📝 Registro en Mi Portal Fone")
    st.markdown("""
    ### Requisitos para acceso:
    1. **CURP válida** (verificar en [gob.mx/curp](https://www.gob.mx/curp))
    2. **Correo electrónico** personal accesible
    3. **Contraseña segura** (8+ caracteres, números y símbolos)
    4. **Datos del acta de nacimiento** (libro, número, año)
    """)
    
    # Registration process
    st.subheader("Proceso de Registro:")
    st.markdown("""
    1. Ingresa al [portal oficial Mi Portal Fone](https://miportal.fone.sep.gob.mx)
    2. Haz clic en **"Regístrate aquí"**
    3. Completa los campos obligatorios (*):
    """)
    
    # Registration table
    st.table({
        "Campo": ["CURP", "Correo Electrónico", "Contraseña", "Año de Registro", "Número de Libro", "Número de Acta"],
        "Obligatorio": ["Sí", "Sí", "Sí", "Sí", "Sí", "Sí"],
        "Ejemplo": [
            "ABCD123456HDFXXX00",
            "usuario@correo.com",
            "Educ2025!",
            "1980",
            "123",
            "456"
        ]
    })
    
    st.markdown("""
    4. Verifica tu correo electrónico (revisa bandeja de spam)
    5. ¡Comienza a gestionar tus recibos!
    """)
    
    # Security and importance
    st.markdown("---")
    st.header("🔒 Seguridad e Importancia")
    st.markdown("""
    ### Consejos de Seguridad:
    - Siempre verifica que la URL sea: **https://miportal.fone.sep.gob.mx**
    - Nunca compartas tu CURP o contraseña
    - Cambia tu contraseña cada 3 meses
    - Cierra sesión después de cada uso
    
    ### ¿Por qué es esencial Mi Portal Fone?
    > "Esta plataforma ha transformado la gestión educativa en México, eliminando trámites presenciales y proporcionando acceso instantáneo a información financiera crítica para más de 1.2 millones de profesionales de la educación."
    """)
    
    # Additional resources
    st.markdown("---")
    st.header("📚 Recursos Adicionales")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Soporte Técnico")
        st.markdown("""
        - Teléfono: 55 3601 7599
        - Email: soporte@fone.sep.gob.mx
        - Horario: 24/7
        """)
    
    with col2:
        st.subheader("Enlaces Oficiales")
        st.markdown("""
        - [Verificar CURP](https://www.gob.mx/curp)
        - [Preguntas Frecuentes](https://miportal.fone.sep.gob.mx/preguntas-frecuentes)
        - [Descargar WinRAR](https://www.rarlab.com/)
        """)
    
    # Backlink-rich footer
    st.markdown("---")
    st.markdown("### Plataforma Oficial de Gestión Educativa")
    st.markdown("[Acceda ahora a Mi Portal Fone](https://miportal.fone.sep.gob.mx)")
    st.markdown("© 2025 Secretaría de Educación Pública - Todos los derechos reservados")
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p>Recurso proporcionado por el portal educativo líder de México</p>
        <h3><a href="https://miportalfonemx.com.mx/" target="_blank">Mi Portal Fone</a></h3>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
