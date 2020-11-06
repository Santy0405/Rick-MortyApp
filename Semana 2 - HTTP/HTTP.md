

### Las peticiones http más usados son los siguientes: 

**GET:** El método GET  solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.

**HEAD:** El método HEAD pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.

**POST:** El método POST se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

**PUT:** El modo PUT reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.

**DELETE:** El método DELETE borra un recurso en específico.

**CONNECT:** El método CONNECT establece un túnel hacia el servidor identificado por el recurso.

**OPTIONS:** El método OPTIONS es utilizado para describir las opciones de comunicación para el recurso de destino.

**TRACE:** El método TRACE  realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino.

**PATCH:** El método PATCH  es utilizado para aplicar modificaciones parciales a un recurso.
## Respuestas
Para la respuestas se tiene que se dividen en 5 grandes grupos cada una con un rango para ser inidentificadas, estas son: 

Respuestas informativas (100–199), respuestas satisfactorias (200–299), redirecciones (300–399), errores de los clientes (400–499), y errores de los servidores (500–599).

**100 Continue:** Esta respuesta provisional indica que todo hasta ahora está bien y que el cliente debe continuar con la solicitud o ignorarla si ya está terminada.
**101 Switching Protocol:** Este código se envía en respuesta a un encabezado de solicitud Upgrade por el cliente e indica que el servidor acepta el cambio de protocolo propuesto por el agente de usuario.

**200 OK:** La solicitud ha tenido éxito. El significado de un éxito varía dependiendo del método HTTP:
**201 Created:** La solicitud ha tenido éxito y se ha creado un nuevo recurso como resultado de ello. Ésta es típicamente la respuesta enviada después de una petición PUT.
**202 Accepted:** La solicitud se ha recibido, pero aún no se ha actuado. Es una petición "sin compromiso", lo que significa que no hay manera en HTTP que permite enviar una respuesta asíncrona que indique el resultado del procesamiento de la solicitud. Está pensado para los casos en que otro proceso o servidor maneja la solicitud, o para el procesamiento por lotes.

**301 Moved Permanently:** Este código de respuesta significa que la URI  del recurso solicitado ha sido cambiado. Probablemente una nueva URI sea devuelta en la respuesta.
**302 Found:** Este código de respuesta significa que el recurso de la URI solicitada ha sido cambiado temporalmente. Nuevos cambios en la URI serán agregados en el futuro. Por lo tanto, la misma URI debe ser usada por el cliente en futuras solicitudes.

**403 Forbidden:** El cliente no posee los permisos necesarios para cierto contenido, por lo que el servidor está rechazando otorgar una respuesta apropiada.
**404 Not Found:** El servidor no pudo encontrar el contenido solicitado. Este código de respuesta es uno de los más famosos dada su alta ocurrencia en la web

**500 Internal Server Error:** El servidor ha encontrado una situación que no sabe cómo manejarla.
**502 Bad Gateway:** Esta respuesta de error significa que el servidor, mientras trabaja como una puerta de enlace para obtener una respuesta necesaria para manejar la petición, obtuvo una respuesta inválida.
