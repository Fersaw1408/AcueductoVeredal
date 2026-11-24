-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-11-2026 a las 17:17:09
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
-- Base de datos: `acueducto_veredal`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `conexiones`
--

CREATE TABLE `conexiones` (
  `id` int(11) NOT NULL,
  `origen_id` int(11) NOT NULL,
  `destino_id` int(11) NOT NULL,
  `distancia` decimal(10,2) NOT NULL
) ;

--
-- Volcado de datos para la tabla `conexiones`
--

INSERT INTO `conexiones` (`id`, `origen_id`, `destino_id`, `distancia`) VALUES
(1, 1, 2, 4.00),
(2, 1, 3, 2.00),
(3, 2, 3, 1.00),
(4, 2, 4, 5.00),
(5, 3, 4, 8.00),
(6, 3, 5, 10.00),
(7, 4, 5, 2.00),
(8, 4, 6, 6.00),
(9, 5, 6, 3.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `veredas`
--

CREATE TABLE `veredas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `veredas`
--

INSERT INTO `veredas` (`id`, `nombre`) VALUES
(1, 'A'),
(2, 'B'),
(3, 'C'),
(4, 'D'),
(5, 'E'),
(6, 'F');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `conexiones`
--
ALTER TABLE `conexiones`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `origen_id` (`origen_id`,`destino_id`),
  ADD KEY `destino_id` (`destino_id`);

--
-- Indices de la tabla `veredas`
--
ALTER TABLE `veredas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `conexiones`
--
ALTER TABLE `conexiones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `veredas`
--
ALTER TABLE `veredas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `conexiones`
--
ALTER TABLE `conexiones`
  ADD CONSTRAINT `conexiones_ibfk_1` FOREIGN KEY (`origen_id`) REFERENCES `veredas` (`id`),
  ADD CONSTRAINT `conexiones_ibfk_2` FOREIGN KEY (`destino_id`) REFERENCES `veredas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
