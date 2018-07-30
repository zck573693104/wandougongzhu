# wandougongzhu
mysql

CREATE TABLE `wandou` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `price` varchar(10) COLLATE utf8mb4_bin DEFAULT NULL,
  `title` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `name` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `brand` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;