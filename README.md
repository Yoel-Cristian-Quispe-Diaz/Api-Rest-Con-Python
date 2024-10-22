# API de Gestión de Pacientes

API REST para la gestión de pacientes, médicos y citas médicas.

## Índice
- [Autenticación](#autenticación)
  - [Registro de Usuario](#registro-de-usuario)
  - [Inicio de Sesión](#inicio-de-sesión)
- [Pacientes](#pacientes)
  - [Obtener Todos los Pacientes](#obtener-todos-los-pacientes)
  - [Crear Paciente](#crear-paciente)
  - [Obtener Paciente](#obtener-paciente)
  - [Actualizar Paciente](#actualizar-paciente)
  - [Eliminar Paciente](#eliminar-paciente)
- [Médicos](#médicos)
  - [Obtener Todos los Médicos](#obtener-todos-los-médicos)
  - [Crear Médico](#crear-médico)
  - [Obtener Médico](#obtener-médico)
  - [Actualizar Médico](#actualizar-médico)
  - [Eliminar Médico](#eliminar-médico)
- [Citas](#citas)
  - [Obtener Todas las Citas](#obtener-todas-las-citas)
  - [Crear Cita](#crear-cita)
  - [Obtener Cita](#obtener-cita)
  - [Actualizar Cita](#actualizar-cita)
  - [Eliminar Cita](#eliminar-cita)

## Autenticación

> **Nota sobre el token**: En los ejemplos se utiliza `localStorage.getItem('token')` para obtener el token. Sin embargo, el método de almacenamiento puede variar según la implementación (sessionStorage, cookies, variables de estado, etc.).

### Registro de Usuario

```http
POST http://tu-servidor/register
```

**Body**:
```json
{
  "username": "nuevo_usuario",
  "password": "contraseña_segura"
}
```

**Respuesta**:
```json
{
  "message": "Usuario creado exitosamente"
}
```

### Inicio de Sesión

```http
POST http://tu-servidor/login
```

**Body**:
```json
{
  "username": "usuario_existente",
  "password": "contraseña_correcta"
}
```

**Respuesta**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## Pacientes

### Obtener Todos los Pacientes

```http
GET http://tu-servidor/pacientes
Authorization: Bearer <token>
```

**Respuesta**:
```json
[
  {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "fecha_nacimiento": "1990-01-15",
    "direccion": "Calle 123, Ciudad",
    "telefono": "1234567890",
    "correo": "juan@example.com"
  }
]
```

### Crear Paciente

```http
POST http://tu-servidor/pacientes
Authorization: Bearer <token>
```

**Body**:
```json
{
  "nombre": "Ana",
  "apellido": "Martínez",
  "fecha_nacimiento": "1995-08-10",
  "direccion": "Plaza 789, Villa",
  "telefono": "1122334455",
  "correo": "ana@example.com"
}
```

**Respuesta**:
```json
{
  "mensaje": "Paciente creado exitosamente"
}
```

### Obtener Paciente

```http
GET http://tu-servidor/pacientes/{id}
Authorization: Bearer <token>
```

**Respuesta**:
```json
{
  "id": 1,
  "nombre": "Juan",
  "apellido": "Pérez",
  "fecha_nacimiento": "1990-01-15",
  "direccion": "Calle 123, Ciudad",
  "telefono": "1234567890",
  "correo": "juan@example.com"
}
```

### Actualizar Paciente

```http
PUT http://tu-servidor/pacientes/{id}
Authorization: Bearer <token>
```

**Body**:
```json
{
  "nombre": "Juan Carlos",
  "apellido": "Pérez",
  "fecha_nacimiento": "1990-01-15",
  "direccion": "Nueva Calle 456, Ciudad",
  "telefono": "9876543210",
  "correo": "juancarlos@example.com"
}
```

**Respuesta**:
```json
{
  "mensaje": "Paciente actualizado exitosamente"
}
```

### Eliminar Paciente

```http
DELETE http://tu-servidor/pacientes/{id}
Authorization: Bearer <token>
```

**Respuesta**:
```json
{
  "mensaje": "Paciente eliminado exitosamente"
}
```

## Médicos

### Obtener Todos los Médicos

```http
GET http://tu-servidor/medicos
Authorization: Bearer <token>
```

**Respuesta**:
```json
[
  {
    "id": 1,
    "nombre": "Carlos",
    "apellido": "Rodríguez",
    "especialidad": "Cardiología",
    "telefono": "9876543210",
    "correo": "carlos@hospital.com"
  }
]
```

### Crear Médico

```http
POST http://tu-servidor/medicos
Authorization: Bearer <token>
```

**Body**:
```json
{
  "nombre": "Elena",
  "apellido": "Gómez",
  "especialidad": "Neurología",
  "telefono": "5544332211",
  "correo": "elena@hospital.com"
}
```

**Respuesta**:
```json
{
  "mensaje": "Médico creado exitosamente"
}
```

### Obtener Médico

```http
GET http://tu-servidor/medicos/{id}
Authorization: Bearer <token>
```

**Respuesta**:
```json
{
  "id": 1,
  "nombre": "Carlos",
  "apellido": "Rodríguez",
  "especialidad": "Cardiología",
  "telefono": "9876543210",
  "correo": "carlos@hospital.com"
}
```

### Actualizar Médico

```http
PUT http://tu-servidor/medicos/{id}
Authorization: Bearer <token>
```

**Body**:
```json
{
  "nombre": "Carlos Alberto",
  "apellido": "Rodríguez",
  "especialidad": "Cardiología",
  "telefono": "9876543210",
  "correo": "carlosalberto@hospital.com"
}
```

**Respuesta**:
```json
{
  "mensaje": "Médico actualizado exitosamente"
}
```

### Eliminar Médico

```http
DELETE http://tu-servidor/medicos/{id}
Authorization: Bearer <token>
```

**Respuesta**:
```json
{
  "mensaje": "Médico eliminado exitosamente"
}
```

## Citas

### Obtener Todas las Citas

```http
GET http://tu-servidor/citas
Authorization: Bearer <token>
```

**Respuesta**:
```json
[
  {
    "id": 1,
    "paciente_id": 1,
    "medico_id": 2,
    "fecha_hora": "2023-05-15 10:00:00",
    "motivo": "Consulta de rutina",
    "estado": "Programada"
  }
]
```

### Crear Cita

```http
POST http://tu-servidor/citas
Authorization: Bearer <token>
```

**Body**:
```json
{
  "paciente_id": 1,
  "medico_id": 2,
  "fecha_hora": "2024-10-25T10:00:00",
  "motivo": "Consulta general",
  "estado": "Pendiente"
}
```

**Respuesta**:
```json
{
  "mensaje": "Cita creada exitosamente"
}
```

### Obtener Cita

```http
GET http://tu-servidor/citas/{id}
Authorization: Bearer <token>
```

**Respuesta**:
```json
{
  "id": 1,
  "paciente_id": 1,
  "medico_id": 2,
  "fecha_hora": "2024-10-25T10:00:00",
  "motivo": "Consulta general",
  "estado": "Pendiente"
}
```

### Actualizar Cita

```http
PUT http://tu-servidor/citas/{id}
Authorization: Bearer <token>
```

**Body**:
```json
{
  "paciente_id": 1,
  "medico_id": 2,
  "fecha_hora": "2024-10-25T11:00:00",
  "motivo": "Consulta de seguimiento",
  "estado": "Confirmada"
}
```

**Respuesta**:
```json
{
  "mensaje": "Cita actualizada exitosamente"
}
```

### Eliminar Cita

```http
DELETE http://tu-servidor/citas/{id}
Authorization: Bearer <token>
```

**Respuesta**:
```json
{
  "mensaje": "Cita eliminada exitosamente"
}
```
