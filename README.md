# wandougongzhu
mysql

CREATE TABLE `wandou` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cat_id` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL,
  `price` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `title` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `name` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `brand` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2901 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


