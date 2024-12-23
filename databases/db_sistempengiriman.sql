-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: db_sistempengiriman
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alamat`
--

DROP TABLE IF EXISTS `alamat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alamat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_alamat` varchar(255) DEFAULT NULL,
  `latitude` decimal(9,6) DEFAULT NULL,
  `longitude` decimal(9,6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alamat`
--

LOCK TABLES `alamat` WRITE;
/*!40000 ALTER TABLE `alamat` DISABLE KEYS */;
INSERT INTO `alamat` VALUES (1,'kediri',1.000000,5.000000),(2,'surabaya',-7.257500,112.752100),(3,'jakarta',-1.000000,9.000000);
/*!40000 ALTER TABLE `alamat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `barang_pengiriman`
--

DROP TABLE IF EXISTS `barang_pengiriman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barang_pengiriman` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_pengirim` varchar(100) DEFAULT NULL,
  `alamat_pengirim` varchar(100) DEFAULT NULL,
  `nama_penerima` varchar(100) DEFAULT NULL,
  `alamat_penerima` varchar(100) DEFAULT NULL,
  `nama_barang` varchar(100) DEFAULT NULL,
  `berat_barang` float DEFAULT NULL,
  `jumlah_barang` int DEFAULT NULL,
  `tanggal_pengiriman` date DEFAULT NULL,
  `tanggal_penerimaan` date DEFAULT NULL,
  `status` enum('Dikemas','Dikirim','Selesai') DEFAULT 'Dikemas',
  `harga` int DEFAULT NULL,
  `voucher` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `status_pembayaran` enum('Belum Dibayar','Sudah Dibayar') DEFAULT 'Belum Dibayar',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barang_pengiriman`
--

LOCK TABLES `barang_pengiriman` WRITE;
/*!40000 ALTER TABLE `barang_pengiriman` DISABLE KEYS */;
INSERT INTO `barang_pengiriman` VALUES (5,'irfan','kediri','dhai','surabaya','kaca',10,2,'2024-10-01','2024-10-03','Dikirim',6016793,'GRATISONGKIR','Sudah Dibayar'),(6,'irfan','kediri','faisal','jakarta','kursi',2,5,NULL,NULL,'Dikemas',NULL,NULL,'Belum Dibayar');
/*!40000 ALTER TABLE `barang_pengiriman` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `makanan_pengiriman`
--

DROP TABLE IF EXISTS `makanan_pengiriman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `makanan_pengiriman` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_pengirim` varchar(100) DEFAULT NULL,
  `alamat_pengirim` varchar(255) DEFAULT NULL,
  `nama_penerima` varchar(100) DEFAULT NULL,
  `alamat_penerima` varchar(255) DEFAULT NULL,
  `nama_makanan` varchar(100) DEFAULT NULL,
  `jumlah_makanan` int DEFAULT NULL,
  `tanggal_pengiriman` date DEFAULT NULL,
  `tanggal_penerimaan` date DEFAULT NULL,
  `status` enum('Dikemas','Dikirim','Selesai') DEFAULT 'Dikemas',
  `harga` decimal(10,2) DEFAULT NULL,
  `voucher` varchar(255) DEFAULT NULL,
  `status_pembayaran` enum('Belum Dibayar','Sudah Dibayar') DEFAULT 'Belum Dibayar',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `makanan_pengiriman`
--

LOCK TABLES `makanan_pengiriman` WRITE;
/*!40000 ALTER TABLE `makanan_pengiriman` DISABLE KEYS */;
/*!40000 ALTER TABLE `makanan_pengiriman` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orang_pengiriman`
--

DROP TABLE IF EXISTS `orang_pengiriman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orang_pengiriman` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_pemesanan` varchar(255) DEFAULT NULL,
  `alamat_pemesanan` text,
  `alamat_tujuan` text,
  `kategori` enum('Bike','Car') DEFAULT 'Bike',
  `status` enum('Penjemputan','Dalam Perjalanan','Selesai') DEFAULT 'Selesai',
  `harga` decimal(10,2) DEFAULT NULL,
  `voucher` varchar(255) DEFAULT NULL,
  `status_pembayaran` enum('Belum Dibayar','Sudah Dibayar') DEFAULT 'Belum Dibayar',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orang_pengiriman`
--

LOCK TABLES `orang_pengiriman` WRITE;
/*!40000 ALTER TABLE `orang_pengiriman` DISABLE KEYS */;
/*!40000 ALTER TABLE `orang_pengiriman` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('admin','pelanggan') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'irfan','123456','pelanggan'),(2,'dhafi','123456','admin'),(4,'bima','123','pelanggan');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voucher`
--

DROP TABLE IF EXISTS `voucher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `voucher` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kode_voucher` varchar(50) DEFAULT NULL,
  `diskon_persen` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kode_voucher` (`kode_voucher`),
  CONSTRAINT `voucher_chk_1` CHECK ((`diskon_persen` between 0 and 100))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voucher`
--

LOCK TABLES `voucher` WRITE;
/*!40000 ALTER TABLE `voucher` DISABLE KEYS */;
INSERT INTO `voucher` VALUES (1,'PROMO30',10),(3,'GRATISONGKIR',50),(5,'aaa',10);
/*!40000 ALTER TABLE `voucher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'db_sistempengiriman'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-19 14:30:08
