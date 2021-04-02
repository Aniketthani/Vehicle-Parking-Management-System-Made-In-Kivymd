-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 02, 2021 at 11:25 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pms`
--

-- --------------------------------------------------------

--
-- Table structure for table `parking`
--

CREATE TABLE `parking` (
  `SNO` int(255) NOT NULL,
  `Emp_Name` varchar(100) NOT NULL,
  `Emp_Id` int(20) NOT NULL,
  `Owner_Name` varchar(100) NOT NULL,
  `Mobile` varchar(15) NOT NULL,
  `V_Type` varchar(30) NOT NULL,
  `V_Number` varchar(20) NOT NULL,
  `Check_In` varchar(20) NOT NULL,
  `Check_Out` varchar(20) NOT NULL,
  `DATE` date NOT NULL,
  `Fare` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `parking`
--

INSERT INTO `parking` (`SNO`, `Emp_Name`, `Emp_Id`, `Owner_Name`, `Mobile`, `V_Type`, `V_Number`, `Check_In`, `Check_Out`, `DATE`, `Fare`) VALUES
(1, 'Aniket Thani', 1111, 'svhvsh', 'ssss', 'Car', 'sssss', '04:04:33pm', '0', '2021-03-29', '30'),
(2, 'Aniket Thani', 1111, 'ffffff', 'ffffffff', 'Car', 'fffffff', '04:07:13pm', '0', '2021-03-29', '30'),
(3, 'Aniket Thani', 1111, 'hello', '541511', '2Wheeler', 'hsvhvd', '04:18:11pm', '0', '2021-03-29', '20'),
(4, 'Aniket Thani', 1111, 'helloworld', 'sssssssss', 'Truck', 'dddddd', '04:22:09pm', '0', '2021-03-29', '70'),
(5, 'Aniket Thani', 1111, 'hsdvhd', 'sssss', '2Wheeler', 'sssssssss', '04:23:24pm', '0', '2021-03-29', '20'),
(6, 'Aniket Thani', 1111, 'aniket thani', '1234567895', 'Car', 'mp09ds2345', '04:24:10pm', '0', '2021-03-29', '30'),
(7, 'Aniket Thani', 1111, 'Aniket Thani', '4562255', '2Wheeler', '6646cgcg', '04:25:43pm', '0', '2021-03-29', '20'),
(8, 'Aniket Thani', 1111, 'aniket thani', '989661115', 'Bus', 'mp09fd2341', '04:27:03pm', '0', '2021-03-29', '50'),
(9, 'Aniket Thani', 1111, 'advhvd', 'ddddddd', '2Wheeler', 'dddddd', '04:28:15pm', '0', '2021-03-29', '20'),
(10, 'Aniket Thani', 1111, 'sdddddd', 'ddddddd', 'Car', 'ffffffff', '04:29:41pm', '0', '2021-03-29', '30'),
(11, 'Aniket Thani', 1111, 'shdvdv', 'ddddd', 'Car', 'ddddddddddd', '04:30:10pm', '0', '2021-03-29', '30'),
(12, 'Aniket Thani', 1111, 'sssss', 'sssssssss', 'Car', 'ssssss', '05:22:10pm', '01:01:29pm', '2021-03-29', '30'),
(13, 'Aniket Thani', 1111, 'ddddddddd', 'dddddd', 'Car', 'dddddd', '05:22:55pm', '01:12:31pm', '2021-03-29', '30'),
(14, 'Aniket Thani', 1111, 'dddddd', 'dddd', 'Car', 'ddddddd', '05:23:47pm', '0', '2021-03-29', '30'),
(15, 'Aniket Thani', 1111, 'dddddd', 'ddddd', 'Car', 'ddddd', '05:24:29pm', '0', '2021-03-29', '30'),
(16, 'Aniket Thani', 1111, 'Aniket Thani', '944545445', 'Car', 'ccfcgcgc', '05:33:52pm', '0', '2021-03-29', '30'),
(17, 'Aniket Thani', 1111, 'ddd', 'dddd', 'Bus', 'dddddd', '06:02:35pm', '12:56:17pm', '2021-03-29', '50'),
(18, 'Aniket Thani', 1111, 'dddddd', 'aniket', 'Car', 'helloworld', '06:10:07pm', '01:11:25pm', '2021-03-29', '30'),
(19, 'Aniket Thani', 1111, 'bjdb', 'vhvhv', 'Truck', 'hhvv', '06:40:05pm', '0', '2021-03-29', '70'),
(20, 'Aniket Thani', 1111, 'ydhvhd', 'hvvhv', 'Car', 'hvhvvhv', '06:41:26pm', '0', '2021-03-29', '30'),
(21, 'Aniket Thani', 1111, 'hello', 'dvdhvdhv', 'Car', 'hvhdvvd', '06:47:32pm', '01:26:32pm', '2021-03-29', '30'),
(22, 'Aniket Thani', 1111, 'final', '91164442', '2Wheeler', 'djjdbjdd', '06:53:59pm', '0', '2021-03-29', '20'),
(23, 'Aniket Thani', 1111, 'aniket thani', '9893vvhvdg', 'Bus', 'mp09fd2341', '01:17:16am', '01:18:19am', '2021-03-31', '50'),
(24, 'Aniket Thani', 1111, 'thani', '985355scss', 'Car', '123fd243', '09:05:02am', '0', '2021-03-31', '30'),
(25, 'Aniket Thani', 1111, 'test owner', 'testmobile', 'HCV', 'testvnumber', '09:49:37am', '0', '2021-03-31', '120'),
(26, 'Aniket Thani', 1111, 'aniket thani', 'testmobile', 'HCV', 'testvnumber', '09:50:09am', '0', '2021-03-31', '120'),
(27, 'Aniket Thani', 1111, 'Notapp', 'Notapp', 'Car', '', '09:55:15am', '0', '2021-03-31', '30'),
(28, 'Aniket Thani', 1111, 'anikettest', 'test', '2Wheeler', '00000001', '09:55:15am', '0', '2021-03-31', '20'),
(29, 'Aniket Thani', 1111, 'jaya', 'jayamobile', '2Wheeler', 'jayavno', '09:59:15am', '0', '2021-03-31', '20'),
(30, 'Aniket Thani', 1111, 'gvdhhv', 'jbjjb', 'Car', 'jbjbb', '10:01:06am', '0', '2021-03-31', '30'),
(31, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:01am', '0', '2021-03-31', '70'),
(32, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:34am', '0', '2021-03-31', '70'),
(33, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:36am', '0', '2021-03-31', '70'),
(34, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:37am', '0', '2021-03-31', '70'),
(35, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:40am', '0', '2021-03-31', '70'),
(36, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:42am', '0', '2021-03-31', '70'),
(37, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:43am', '0', '2021-03-31', '70'),
(38, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:44am', '0', '2021-03-31', '70'),
(39, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:43am', '0', '2021-03-31', '70'),
(40, 'Aniket Thani', 1111, 'aaaaa', 'bbbbb', 'Truck', 'cccccc', '10:03:44am', '0', '2021-03-31', '70'),
(41, 'Aniket Thani', 1111, 'hsvh', 'sdeeee', 'Car', '', '10:06:19am', '0', '2021-03-31', '30'),
(42, 'Aniket Thani', 1111, 'qqqq1', 'wwww2', 'Car', 'rrrrr3', '10:06:19am', '0', '2021-03-31', '30'),
(43, 'Aniket Thani', 1111, 'eeeee', 'eeddd', 'Car', '', '10:17:42am', '0', '2021-03-31', '30'),
(44, 'Aniket Thani', 1111, 'zzzz1', 'xxxx1', 'Car', 'cccc1', '10:17:42am', '0', '2021-03-31', '30'),
(45, 'Aniket Thani', 1111, 'pppp2', 'oooo2', 'Truck', 'iiiii2', '10:21:22am', '0', '2021-03-31', '70'),
(46, 'Aniket Thani', 1111, 'llll3', 'kkkk2', 'Bus', 'jjjjj2', '10:22:59am', '0', '2021-03-31', '50'),
(47, 'Aniket Thani', 1111, 'ww', 'ww', 'Car', 'ww', '10:23:43am', '0', '2021-03-31', '30'),
(48, 'Aniket Thani', 1111, '1111', '2222', 'Car', '5555', '10:25:18am', '0', '2021-03-31', '30'),
(49, 'Aniket Thani', 1111, '777', '888', 'Car', '5555', '10:26:21am', '0', '2021-03-31', '30'),
(50, 'Aniket Thani', 1111, '111', '222', 'Car', '9999', '10:27:03am', '0', '2021-03-31', '30'),
(51, 'Aniket Thani', 1111, 'aaaa', 'sssss', 'Car', 'dddddddd', '10:27:37am', '0', '2021-03-31', '30'),
(52, 'Aniket Thani', 1111, 'ddddd123', 'dddddddd', '2Wheeler', 'dddddddddd', '10:28:27am', '0', '2021-03-31', '20'),
(53, 'Aniket Thani', 1111, '2', 'ee', 'Car', 'rr', '08:44:57pm', '0', '2021-03-31', '30'),
(54, 'Aniket Thani', 1111, 'helloaniket', 'mobileno', 'Truck', 'vno1234', '08:49:08pm', '0', '2021-03-31', '70'),
(55, 'Aniket Thani', 1111, 'aniketishere', '1234abcd', '2Wheeler', 'helloakt', '08:50:04pm', '0', '2021-03-31', '20'),
(56, 'Aniket Thani', 1111, 'yshsh', 'vhvjv', 'Car', 'jjjb', '08:50:32pm', '0', '2021-03-31', '30'),
(57, 'Aniket Thani', 1111, 'aniketthani', 'mob12345', 'Car', '12346', '08:58:34pm', '0', '2021-03-31', '30'),
(58, 'Aniket Thani', 1111, 'helloakt', 'hsvhvsjb', 'Car', 'jbbkk', '08:59:05pm', '0', '2021-03-31', '30'),
(60, 'Aniket Thani', 1111, 'normal', 'normal', '2Wheeler', 'normal', '10:23:02pm', '10:36:38pm', '2021-03-31', '20'),
(61, 'Aniket Thani', 1111, 'normal2', 'normal2', '2Wheeler', 'normal2', '10:27:55pm', '10:35:58pm', '2021-03-31', '20'),
(62, 'Aniket Thani', 1111, 'dddd', 'dddd', 'Car', 'wwerrrr', '10:29:57pm', '0', '2021-03-31', '30'),
(63, 'Aniket Thani', 1111, 'dvdvd', 'hvjvjv', 'Car', 'vjvvjvjv', '10:30:31pm', '0', '2021-03-31', '30');

-- --------------------------------------------------------

--
-- Table structure for table `slots`
--

CREATE TABLE `slots` (
  `SNO` int(11) NOT NULL,
  `Type` varchar(30) NOT NULL,
  `Total` int(255) NOT NULL,
  `Available` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `slots`
--

INSERT INTO `slots` (`SNO`, `Type`, `Total`, `Available`) VALUES
(1, 'Car', 10, 3),
(2, 'Truck', 10, 8),
(3, '2Wheeler', 10, 10),
(4, 'Bus', 10, 10),
(5, 'LCV', 10, 9),
(6, 'HCV', 10, 9);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `SNO` int(255) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Type` varchar(100) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `Mobile` int(10) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Emp_Id` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`SNO`, `Name`, `Type`, `Gender`, `Mobile`, `Address`, `Username`, `Password`, `Emp_Id`) VALUES
(1, 'Aniket Thani', 'Staff', 'M', 1234567890, 'hello iam here ', 'aniket', '1562206543da764123c21bd524674f0a8aaf49c8a89744c97352fe677f7e4006', 1111),
(2, 'Administrator AKT', 'Administrator', 'M', 1245789686, 'krishna nagar , Vrindavan,UP', 'admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 7777);

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `SNO` int(100) NOT NULL,
  `V_Type` varchar(100) NOT NULL,
  `Fare` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`SNO`, `V_Type`, `Fare`) VALUES
(1, 'Car', '30'),
(2, 'Truck', '70'),
(3, '2Wheeler', '20'),
(4, 'Bus', '50'),
(5, 'LCV', '100'),
(6, 'HCV', '120');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `parking`
--
ALTER TABLE `parking`
  ADD PRIMARY KEY (`SNO`);

--
-- Indexes for table `slots`
--
ALTER TABLE `slots`
  ADD PRIMARY KEY (`SNO`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`SNO`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`SNO`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `parking`
--
ALTER TABLE `parking`
  MODIFY `SNO` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `slots`
--
ALTER TABLE `slots`
  MODIFY `SNO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `SNO` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `vehicles`
--
ALTER TABLE `vehicles`
  MODIFY `SNO` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
