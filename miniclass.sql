-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 18, 2022 at 02:13 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `miniclass`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendancetbl`
--

CREATE TABLE `attendancetbl` (
  `studentNo` int(11) NOT NULL,
  `date` text NOT NULL,
  `attendance` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendancetbl`
--

INSERT INTO `attendancetbl` (`studentNo`, `date`, `attendance`) VALUES
(1, '18-08-2022', 'P'),
(2, '18-08-2022', 'P'),
(3, '18-08-2022', 'A');

-- --------------------------------------------------------

--
-- Table structure for table `studentstbl`
--

CREATE TABLE `studentstbl` (
  `studentNo` int(11) NOT NULL,
  `firstName` text NOT NULL,
  `lastName` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentstbl`
--

INSERT INTO `studentstbl` (`studentNo`, `firstName`, `lastName`) VALUES
(3, 'rhett', 'andrew'),
(4, 'leo', 'james'),
(5, 'walker', 'william');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `studentstbl`
--
ALTER TABLE `studentstbl`
  ADD PRIMARY KEY (`studentNo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
