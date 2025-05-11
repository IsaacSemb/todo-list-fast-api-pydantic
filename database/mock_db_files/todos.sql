-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Generation Time: May 11, 2025 at 04:43 PM
-- Server version: 9.1.0
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `todo_api`
--

-- --------------------------------------------------------

--
-- Table structure for table `todos`
--

CREATE TABLE `todos` (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `expected_completion` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `todos`
--

INSERT INTO `todos` (`id`, `title`, `description`, `created_at`, `expected_completion`, `status`) VALUES
(1, 'Learn FastAPI', 'Keep pushing!', '2025-04-09 20:00:50', '2025-04-12 10:00:00', 0),
(2, 'Wake Up', 'You need to read your books!', '2025-04-09 20:01:28', '2025-04-12 10:00:00', 0),
(3, 'Its saturday baby', 'Gotta live life!', '2025-04-12 15:03:53', '2025-04-13 18:00:00', 0),
(4, 'Drink Water Bro', 'Hydrate or diedrate 😅', '2025-04-13 08:30:00', '2025-04-13 09:00:00', 0),
(5, 'Push That Code', 'FastAPI isn\'t gonna write itself!', '2025-04-13 08:45:00', '2025-04-13 12:00:00', 0),
(6, 'Stretch Yo Legs', 'Get up, walk around. You ain\'t a potato 🥔', '2025-04-13 09:00:00', '2025-04-13 09:15:00', 0),
(7, 'Reflect for 5 Mins', 'What went well? What needs work?', '2025-04-13 09:10:00', '2025-04-13 09:20:00', 0),
(8, 'Chill Time', 'You\'ve earned it. Breathe.', '2025-04-13 09:30:00', '2025-04-13 18:00:00', 0),
(9, 'Review PRs', 'Give feedback and merge the good stuff.', '2025-04-12 11:00:00', '2025-04-12 13:00:00', 1),
(10, 'Write Blog Post', 'Share that FastAPI wisdom with the world.', '2025-04-12 14:30:00', '2025-04-13 18:00:00', 0),
(11, 'Call Mom', 'She misses you.', '2025-04-11 19:00:00', '2025-04-11 20:00:00', 1),
(12, 'Clean Desk', 'Clear space, clear mind.', '2025-04-13 07:45:00', '2025-04-13 08:15:00', 1),
(13, 'Plan the Week', 'Map it out. Don\'t wing it.', '2025-04-13 09:00:00', '2025-04-13 10:00:00', 0),
(14, 'Update Resume', 'Even if you\'re not job hunting, stay ready.', '2025-04-13 10:30:00', '2025-04-13 11:30:00', 0),
(15, 'Meditate', 'Just 10 mins. You got this.', '2025-04-13 11:00:00', '2025-04-13 11:10:00', 1),
(16, 'Read 20 Pages', 'Knowledge ain\'t gonna jump in your brain.', '2025-04-13 12:00:00', '2025-04-13 13:00:00', 0),
(17, 'Prep Lunch', 'Fuel up, chef style 🍽️', '2025-04-13 12:30:00', '2025-04-13 13:30:00', 1),
(18, 'Debug That Error', 'Yeah, the one that’s been haunting you.', '2025-04-13 13:00:00', '2025-04-13 15:00:00', 0),
(19, 'Quick Workout', '15 mins. No excuses. Move!', '2025-04-13 15:15:00', '2025-04-13 15:30:00', 1),
(20, 'Wind Down Routine', 'Low lights, chill music, no screens.', '2025-04-13 21:00:00', '2025-04-13 22:00:00', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `todos`
--
ALTER TABLE `todos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_todos_id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `todos`
--
ALTER TABLE `todos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
