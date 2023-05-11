create database tiendita;
use tiendita;

INSERT INTO inicio_categoria (nombre) VALUES ("Computadoras y portátiles");
INSERT INTO inicio_categoria (nombre) VALUES ("Dispositivos móviles");
INSERT INTO inicio_categoria (nombre) VALUES ("Componentes");
INSERT INTO inicio_categoria (nombre) VALUES ("Accesorios");

INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("NOKIA 3390", "puedes noquear a tus oponentes de uno solo golpe", 45990, 23, "https://down-cl.img.susercontent.com/file/fa54bdc66f22810eb6c6e426230bb538_tn", 2);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("PC Gamer del Gobierno", "lo corre todo, garantizado", 23990, 4, "https://http2.mlstatic.com/D_NQ_NP_638891-MLC49833505357_052022-O.webp", 1);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Acer Nitro 5", "Notebook Intel® Core i5 16GB Ram 512GB SSD 15.6 FHD", 899990, 32, "https://home.ripley.cl/store/Attachment/WOP/D113/2000395850981/2000395850981-1.jpg", 1);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("ASUS VIVOBOOK M413IA", "Notebook AMD Ryzen 7 16GB Ram 512GB SSD 14 FHD", 629990, 21, "https://home.ripley.cl/store/Attachment/WOP/D113/2000396273802/2000396273802-2.jpg", 1);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("NOTEBOOK ELITEBOOK 840 G4", "Windows 10 Pro 64 Intel Core i5-7200U con Intel HD Graphics 620 8 GB RAM DDR4 14", 329990, 3, "https://outlet.ofilink.cl/1457-medium_default/notebook-hp-elitebook-840-g4-i7-8gb-500gb-250gb-m2.jpg", 1);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Lenovo All in One 3 - 24ITL6", "23.8 FHD / Intel Core i5 / Win 11 / 16 GB RAM / 512 GB SSD / Intel Iris Xe Graphics / White", 699990, 6, "https://centrale.cl/wp-content/uploads/Lenovo-AIO-3-24ITL6-24-Core-i3-8GB-RAM-512GB-SSD-Full-HD-F0G000P7CL_xKwH9R0.jpeg", 1);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Samsung Galaxy A34", "5G 128Gb Negro Android 13.0", 269990, 10, "https://cdn.kemik.gt/2023/03/SM-A346M-DS-SAMSUNG-A345G-BK-1200X1200-1.jpg", 2);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Apple iPhone 14 Pro", "6 GB RAM / 128 GB / Gold", 799990, 8, "https://falabella.scene7.com/is/image/Falabella/16563300_1?wid=800&hei=800&qlt=70", 2);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Procesador AMD Ryzen 5 5600G", "Frecuencia 3900 MHz / 6 núcleos / 12 hilos / Socket AM4", 131490, 37, "https://media.solotodo.com/media/products/1436922_picture_1628622735.png", "3");
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Procesador Intel Core i3-10105F", "3700 MHz / 4 núcleos / 8 hilos / Socket LGA 1200", 73990, 21, "https://media.solotodo.com/media/products/1370730_picture_1618586101.jpg", "3");
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("RAM Crucial CB8GU2666", "1 x 8 GB / DDR4 / 2666 MHz", 13990, 45, "https://media.solotodo.com/media/products/1344630_picture_1615637537.jpg", 3);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("RAM Kingston KCP426NS6/8", "1 x 8 GB / DDR4 / 2666 MHz", 17990, 22, "https://media.solotodo.com/media/products/1257498_picture_1603801331.jpg", 3);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("HDD Toshiba 1 TB (DT01ACA100)", "HDD / 1TB / 7200rpm / SATA 3 (6Gb/s)", 19990, 2, "https://media.solotodo.com/media/products/Toshiba.jpg", 3);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("SSD Western Digital Green 240 GB", "240 GB / M.2 / SATA 3", 13990, 6, "https://media.solotodo.com/media/products/1622633_picture_1657178247.jpg", 3);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("GPU Gigabyte GeForce GTX 1660 Ti OC 6G", "6 GB GDDR6 (192 bit) / PCI Express 3.0 x16", 295990, 3, "https://media.solotodo.com/media/products/887460_picture_1551143244.jpg", 3);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Mouse Logitech G203 Lightsync Black", "6 botones / 8000DPI / Alámbrico", 16990, 28, "https://media.solotodo.com/media/products/1169320_picture_1590763819.jpg", 4);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Teclado Redragon Kumara K552 Rainbow", "Mecanico / 80% / RBG / Outemu Red / Alambrico", 25300, 6, "https://media.solotodo.com/media/products/1508732_picture_1639576617.jpg", 4);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Teclado Philips G605", "Mecanico / 100% / RGB / Cyan Switch / Alambrico", 39990, 10, "https://media.solotodo.com/media/products/1366478_picture_1679685352.jpg", 4);
INSERT INTO inicio_producto (name, description, price, stock, img_url, categoria_id) VALUES ("Audifonos Kingston HyperX Cloud Flight", "Headset / 20 - 20000 Hz / Alambrico", 69990, 12, "https://media.solotodo.com/media/products/1008759_picture_1675692800.webp", 4);
