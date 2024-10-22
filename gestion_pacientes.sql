-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-10-2024 a las 14:45:09
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_pacientes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `id` int(11) NOT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `medico_id` int(11) DEFAULT NULL,
  `fecha_hora` datetime DEFAULT NULL,
  `motivo` varchar(255) DEFAULT NULL,
  `estado` enum('confirmada','cancelada') DEFAULT 'confirmada'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `citas`
--

INSERT INTO `citas` (`id`, `paciente_id`, `medico_id`, `fecha_hora`, `motivo`, `estado`) VALUES
(1, 1, 1, '2024-10-15 10:00:00', 'Chequeo general', 'confirmada'),
(2, 2, 2, '2024-10-16 11:00:00', 'Consulta pediátrica', 'confirmada'),
(3, 3, 3, '2024-10-17 09:30:00', 'Revisión de piel', 'confirmada'),
(4, 4, 4, '2024-10-18 14:00:00', 'Evaluación neurológica', 'confirmada'),
(5, 5, 5, '2024-10-19 16:00:00', 'Chequeo de vista', 'confirmada'),
(6, 6, 6, '2024-10-20 13:00:00', 'Consulta ginecológica', 'confirmada'),
(7, 7, 7, '2024-10-21 15:30:00', 'Consulta oncológica', 'confirmada'),
(8, 8, 8, '2024-10-22 08:00:00', 'Terapia psicológica', 'confirmada'),
(9, 9, 9, '2024-10-23 12:00:00', 'Chequeo ortopédico', 'confirmada'),
(10, 10, 10, '2024-10-24 10:00:00', 'Consulta endocrinológica', 'confirmada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicos`
--

CREATE TABLE `medicos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `especialidad` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medicos`
--

INSERT INTO `medicos` (`id`, `nombre`, `apellido`, `especialidad`, `telefono`, `correo`, `username`, `password`) VALUES
(1, 'Lizeth', 'Pérez', 'Cardiología', '123456789', 'juan@example.com', 'j.perez', '$2y$10$F.xR.h/XkEd0B9.AsR2w9enKktcEnjViSRBw2kWnJu53pOzek.wdq'),
(2, 'Dr. Laura', 'Fernández', 'Pediatría', '123456789', 'laura.fernandez@example.com', 'laura', '$2y$10$cbQDKgVzXew5a8FlVUhIXOv/QSatJALyopXPzreqDa57qnTr3fD9u'),
(3, 'Dr. Juan', 'Fernández', 'Dermatología', '123456789', 'juan.gomez@example.com', 'laura', '$2y$10$PwFiSa0i/0xmcj7fdyW0YeBuzgIvUFVzey8C/2.k1ieI5Sd6MMz2u'),
(4, 'Dra. María', 'Pérez', 'Pediatría', '987654321', 'maria.perez@example.com', 'maria_pediatra', '$2y$10$T4RNeK4BKfcrSp.RgXMSi.73I894yvz0pkAY.cE9dSSgylSK7X3pa'),
(5, 'Dr. Carlos', 'Gómez', 'Cardiología', '456789123', 'carlos.gomez@example.com', 'c_gomez', '$2y$10$CIzTt5d4N1zobkaE9xyYievjwREfPa8Z.UnxMw74F1o5SWEDScUWO'),
(6, 'Dra. Ana', 'Lopez', 'Ginecología', '321654987', 'ana.lopez@example.com', 'ana_ginecologa', '$2y$10$toqTht1dWbtVYL/knYOU3.wGXuDaEdioAwxnGC.hamqFyhbokkJn.'),
(7, 'Dr. Luis', 'Martínez', 'Oftalmología', '654321789', 'luis.martinez@example.com', 'luis_oftalmo', '$2y$10$k4Gj/47CdywjB1KIXhzd8e9pSSkWES/8PNpaFYRTgebwMV8SKgs5m'),
(8, 'Dra. Sofía', 'Ramírez', 'Psicología', '789123456', 'sofia.ramirez@example.com', 'sofia_psicologa', '$2y$10$qnNblCThRKdeocEVk3bRSunc88f6Qw.JvwFj5m72u2DXsQQ7VHyNO'),
(9, 'Dr. Felipe', 'Torres', 'Ortopedia', '159753486', 'felipe.torres@example.com', 'felipe_ortopedista', '$2y$10$ma3CUPJARq5tYVEJelM4oe2XVd5rOGcb5pL/xSneSUDI75HgKwvt.'),
(10, 'Dra. Valentina', 'Hernández', 'Nutrición', '753159486', 'valentina.hernandez@example.com', 'valentina_nutri', '$2y$10$tsC0bWGH3btdFju7dQ1YROIQsCmPEh/TpMCRT3PvXauz8k3ygfmsG');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`id`, `nombre`, `apellido`, `fecha_nacimiento`, `direccion`, `telefono`, `correo`) VALUES
(1, 'Juan', 'Pérez', '1985-02-15', 'Calle Falsa 123', '1234567890', 'juan.perez@example.com'),
(2, 'María', 'González', '1990-03-10', 'Avenida Siempre Viva 742', '0987654321', 'maria.gonzalez@example.com'),
(3, 'Luis', 'Martínez', '1988-07-20', 'Calle Real 456', '5551234567', 'luis.martinez@example.com'),
(4, 'Ana', 'Lopez', '1995-12-30', 'Calle de la Luna 101', '6669876543', 'ana.lopez@example.com'),
(5, 'Carlos', 'Hernández', '1982-11-25', 'Avenida del Sol 987', '7776543210', 'carlos.hernandez@example.com'),
(6, 'Lucía', 'Ramírez', '1993-09-05', 'Calle del Río 135', '8885432109', 'lucia.ramirez@example.com'),
(7, 'Fernando', 'Torres', '1980-05-18', 'Calle de la Paz 456', '9994321098', 'fernando.torres@example.com'),
(8, 'Sofía', 'Díaz', '1991-04-14', 'Avenida Libertad 321', '3216549870', 'sofia.diaz@example.com'),
(9, 'Pedro', 'Morales', '1987-08-22', 'Calle del Bosque 654', '2345678901', 'pedro.morales@example.com'),
(10, 'Valentina', 'Suárez', '1994-01-30', 'Calle de las Flores 789', '3456789012', 'valentina.suarez@example.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'testuser', 'e16b2ab8d12314bf4efbd6203906ea6c');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `paciente_id` (`paciente_id`),
  ADD KEY `medico_id` (`medico_id`);

--
-- Indices de la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citas`
--
ALTER TABLE `citas`
  ADD CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`medico_id`) REFERENCES `medicos` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
