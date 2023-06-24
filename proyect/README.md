# Sistema para clientes de una Clinica
#### video demo: https://youtu.be/qDMqAB_e9Vs
#### Descripción

#### Este es una página web para una clínica, en el cual se le facilitará tanto al cliente como al doctor el manejo de la información; desde poder acceder (como cliente/paciente) a las distintas especialidades, poder chatear con el doctor de su preferencia, poder buscar la especialidad requerida, etc.

## Desarrollo

### Registro

#### Esta es una funcionalidad que permite a los usuarios crear una cuenta personalizada en el sitio web. Esta opción generalmente se encuentra en la página de inicio o en un enlace específico destinado al registro. Cuando un usuario selecciona la opción de registro, se le presenta un formulario que solicita cierta información personal. Los datos típicos solicitados en un formulario de registro pueden incluir:
#### -Usuario
#### -Contraseña
#### -Confirmar contraseña

#### Aparte de eso se incluyó un campo de "Rol", para crear una cuenta como Doctor o como  paciente.
#### En el caso de acceder como doctor, estarán disponibles otras opciones que se especificarán más adelante en este escrito.
#### Una vez que el usuario completa el formulario de registro y lo envía, el sistema web realiza varias verificaciones y validaciones para asegurarse de que la información proporcionada sea correcta y cumpla con los requisitos establecidos. Estas verificaciones pueden incluir la comprobación de la disponibilidad del nombre de usuario, la fortaleza de la contraseña y la validez del Usuario.

#### Si toda la información es válida, se crea una cuenta nueva para el usuario en la base de datos del sitio web.

### Login

#### Una vez que los datos sean validados en en registro, e podrá acceder a la página web por me dio del usuario ya creado.

### Home

#### Esta es la parte de presentación de la clínica a la cual se ha creado esta página, pasarán unas cards con la mesión, visión y propósito de la clínica.

### Especialidades

#### Acá se mostrarán todos los doctores por medio de unas cards responsivas por medio de unos botonoes que redirigirán a una ventana en whatsapp para poderse comunicar con el doctor. Un botón expandir el cual nos mostrará una tarjeta de presentación del doctor, describiendo un poco su carrera y especialidad.

### Admin

#### Al iniciar sesión con el rol de doctor, aparecerán unas opciones nuevas en las cuales podremos actualizar información de los doctores dentro de la base de datos o bien agregara un doctor nuevo, en la misma.

### Logout
#### Colocamos un botón que nos permita cerrar sesión.
#### En el sistema se ha aplicado tecnologías como HTML, CSS, Python, Javascript.