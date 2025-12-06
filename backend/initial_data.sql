--
-- PostgreSQL database dump
--

\restrict yB3dvqo4RJF11XTGNQ6bhGOMTdP4d0Aizjlb1YjzzdzseCIeHlk1g2giHpaN3cs

-- Dumped from database version 16.11 (Ubuntu 16.11-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.11 (Ubuntu 16.11-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: library_user
--

INSERT INTO public.alembic_version VALUES ('71f1f07df5a6');


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: library_user
--

INSERT INTO public.books VALUES (1, 'Libro de Prueba 1', 'Autor 1', 'ISBN-BD2-2025-1120', 100, 2000, '2025-12-05 23:25:26.961424-03', '2025-12-05 23:25:26.961429-03', 1, NULL, 'es', 'Editorial 1');
INSERT INTO public.books VALUES (2, 'Libro de Prueba 2', 'Autor 2', 'ISBN-BD2-2025-1125', 120, 2001, '2025-12-05 23:25:26.96143-03', '2025-12-05 23:25:26.961431-03', 2, NULL, 'es', 'Editorial 2');
INSERT INTO public.books VALUES (3, 'Libro de Prueba 3', 'Autor 3', 'ISBN-BD2-2025-1130', 140, 2002, '2025-12-05 23:25:26.961431-03', '2025-12-05 23:25:26.961432-03', 3, NULL, 'es', 'Editorial 3');
INSERT INTO public.books VALUES (4, 'Libro de Prueba 4', 'Autor 4', 'ISBN-BD2-2025-1135', 160, 2003, '2025-12-05 23:25:26.961433-03', '2025-12-05 23:25:26.961433-03', 4, NULL, 'es', 'Editorial 4');
INSERT INTO public.books VALUES (5, 'Libro de Prueba 5', 'Autor 5', 'ISBN-BD2-2025-1140', 180, 2004, '2025-12-05 23:25:26.961434-03', '2025-12-05 23:25:26.961434-03', 5, NULL, 'es', 'Editorial 5');
INSERT INTO public.books VALUES (6, 'Libro de Prueba 6', 'Autor 6', 'ISBN-BD2-2025-1145', 200, 2005, '2025-12-05 23:25:26.961435-03', '2025-12-05 23:25:26.961436-03', 1, NULL, 'es', 'Editorial 6');
INSERT INTO public.books VALUES (7, 'Libro de Prueba 7', 'Autor 7', 'ISBN-BD2-2025-1150', 220, 2006, '2025-12-05 23:25:26.961436-03', '2025-12-05 23:25:26.961437-03', 2, NULL, 'es', 'Editorial 7');
INSERT INTO public.books VALUES (8, 'Libro de Prueba 8', 'Autor 8', 'ISBN-BD2-2025-1155', 240, 2007, '2025-12-05 23:25:26.961437-03', '2025-12-05 23:25:26.961438-03', 3, NULL, 'es', 'Editorial 8');
INSERT INTO public.books VALUES (9, 'Libro de Prueba 9', 'Autor 9', 'ISBN-BD2-2025-1160', 260, 2008, '2025-12-05 23:25:26.961439-03', '2025-12-05 23:25:26.961439-03', 4, NULL, 'es', 'Editorial 9');
INSERT INTO public.books VALUES (10, 'Libro de Prueba 10', 'Autor 10', 'ISBN-BD2-2025-1165', 280, 2009, '2025-12-05 23:25:26.96144-03', '2025-12-05 23:25:26.96144-03', 5, NULL, 'es', 'Editorial 10');


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: library_user
--

INSERT INTO public.categories VALUES (1, 'Ficción', 'Obras literarias de imaginación.', '2025-12-05 23:25:26.274068-03', '2025-12-05 23:25:26.274074-03');
INSERT INTO public.categories VALUES (2, 'No Ficción', 'Obras basadas en hechos y realidad.', '2025-12-05 23:25:26.274076-03', '2025-12-05 23:25:26.274077-03');
INSERT INTO public.categories VALUES (3, 'Ciencia', 'Libros sobre temas científicos y tecnológicos.', '2025-12-05 23:25:26.274078-03', '2025-12-05 23:25:26.274079-03');
INSERT INTO public.categories VALUES (4, 'Historia', 'Libros que exploran eventos pasados.', '2025-12-05 23:25:26.274079-03', '2025-12-05 23:25:26.27408-03');
INSERT INTO public.categories VALUES (5, 'Fantasía', 'Género con elementos mágicos y sobrenaturales.', '2025-12-05 23:25:26.274081-03', '2025-12-05 23:25:26.274081-03');


--
-- Data for Name: book_categories; Type: TABLE DATA; Schema: public; Owner: library_user
--

INSERT INTO public.book_categories VALUES (5, 5);
INSERT INTO public.book_categories VALUES (2, 2);
INSERT INTO public.book_categories VALUES (8, 3);
INSERT INTO public.book_categories VALUES (3, 3);
INSERT INTO public.book_categories VALUES (6, 1);
INSERT INTO public.book_categories VALUES (9, 4);
INSERT INTO public.book_categories VALUES (4, 4);
INSERT INTO public.book_categories VALUES (1, 1);
INSERT INTO public.book_categories VALUES (7, 2);
INSERT INTO public.book_categories VALUES (10, 5);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: library_user
--

INSERT INTO public.users VALUES (1, 'johndoe', 'John Doe', '$argon2id$v=19$m=65536,t=3,p=4$hiL26oTMuzaAalBRt7Z43A$6n5YZnzsHZ0m7IRPKXrKR75YBNbSMtiXGd10JbajJbk', '2025-12-05 23:25:26.934733-03', '2025-12-05 23:25:26.934737-03', 'john.doe@example.com', '123456789', '123 Main St', true);
INSERT INTO public.users VALUES (2, 'janedoe', 'Jane Doe', '$argon2id$v=19$m=65536,t=3,p=4$V5c/cZ1JbU/PSr3uBuxFCQ$ZqKRlUCEgCoXCqesy2XHBS640ELBNClr5GpP0X8XObE', '2025-12-05 23:25:26.934738-03', '2025-12-05 23:25:26.934739-03', 'jane.doe@example.com', '987654321', '456 Oak Ave', true);
INSERT INTO public.users VALUES (3, 'peterjones', 'Peter Jones', '$argon2id$v=19$m=65536,t=3,p=4$+Y28/I8qxwR2QtIdtjo4qA$VySmIjCnEqxK9dYbayz8gtXrz1oB5i6YKMmhVNwoYfs', '2025-12-05 23:25:26.93474-03', '2025-12-05 23:25:26.93474-03', 'peter.jones@example.com', '555111222', '789 Pine Ln', true);
INSERT INTO public.users VALUES (4, 'marysmith', 'Mary Smith', '$argon2id$v=19$m=65536,t=3,p=4$7EA2VaDCOC6YuC3s4enSsg$aIc2zNHPLA9IVZHafFfVC3t6dsHrs6kgUrIo3OiRNPM', '2025-12-05 23:25:26.934741-03', '2025-12-05 23:25:26.934742-03', 'mary.smith@example.com', '555333444', '101 Maple Rd', true);
INSERT INTO public.users VALUES (5, 'admin', 'Admin User', '$argon2id$v=19$m=65536,t=3,p=4$elwOl7vIkg0vGmaGxQIHqw$9DKy3QgnzjBoSXq9NlcdlkZF690W81P9Nk0bSDXBRUQ', '2025-12-05 23:25:26.934742-03', '2025-12-05 23:25:26.934743-03', 'admin@example.com', '555555555', '1 Admin Ct', true);


--
-- Data for Name: loans; Type: TABLE DATA; Schema: public; Owner: library_user
--

INSERT INTO public.loans VALUES (1, '2025-11-30', NULL, 1, 1, '2025-12-05 23:25:26.971922-03', '2025-12-05 23:25:26.971927-03', '2025-12-14', NULL, 'ACTIVE');
INSERT INTO public.loans VALUES (2, '2025-11-15', '2025-11-25', 2, 2, '2025-12-05 23:25:26.971928-03', '2025-12-05 23:25:26.971929-03', '2025-11-29', NULL, 'RETURNED');
INSERT INTO public.loans VALUES (3, '2025-11-05', NULL, 3, 3, '2025-12-05 23:25:26.971931-03', '2025-12-05 23:25:26.971932-03', '2025-11-19', NULL, 'OVERDUE');
INSERT INTO public.loans VALUES (4, '2025-12-03', NULL, 1, 4, '2025-12-05 23:25:26.971933-03', '2025-12-05 23:25:26.971934-03', '2025-12-17', NULL, 'ACTIVE');
INSERT INTO public.loans VALUES (5, '2025-10-26', '2025-11-30', 4, 5, '2025-12-05 23:25:26.971935-03', '2025-12-05 23:25:26.971936-03', '2025-11-09', 10500.00, 'RETURNED');
INSERT INTO public.loans VALUES (6, '2025-11-22', NULL, 5, 6, '2025-12-05 23:25:26.971937-03', '2025-12-05 23:25:26.971938-03', '2025-12-06', NULL, 'ACTIVE');
INSERT INTO public.loans VALUES (7, '2025-11-20', '2025-12-04', 2, 7, '2025-12-05 23:25:26.971939-03', '2025-12-05 23:25:26.971941-03', '2025-12-04', NULL, 'RETURNED');
INSERT INTO public.loans VALUES (8, '2025-12-04', NULL, 3, 8, '2025-12-05 23:25:26.971942-03', '2025-12-05 23:25:26.971943-03', '2025-12-18', NULL, 'ACTIVE');


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: library_user
--

INSERT INTO public.reviews VALUES (1, 5, '¡Excelente libro!', '2025-12-05', 1, 2, '2025-12-05 23:25:26.984406-03', '2025-12-05 23:25:26.984409-03');
INSERT INTO public.reviews VALUES (2, 4, 'Muy bueno, lo recomiendo.', '2025-12-05', 2, 1, '2025-12-05 23:25:26.984416-03', '2025-12-05 23:25:26.984417-03');
INSERT INTO public.reviews VALUES (3, 3, 'Interesante, pero un poco lento.', '2025-12-05', 3, 3, '2025-12-05 23:25:26.984421-03', '2025-12-05 23:25:26.984422-03');
INSERT INTO public.reviews VALUES (4, 5, 'Una obra maestra.', '2025-12-05', 4, 4, '2025-12-05 23:25:26.984425-03', '2025-12-05 23:25:26.984426-03');
INSERT INTO public.reviews VALUES (5, 2, 'No me gustó mucho.', '2025-12-05', 5, 5, '2025-12-05 23:25:26.98443-03', '2025-12-05 23:25:26.984431-03');
INSERT INTO public.reviews VALUES (6, 4, 'Mejor de lo que esperaba.', '2025-12-05', 1, 3, '2025-12-05 23:25:26.984435-03', '2025-12-05 23:25:26.984436-03');
INSERT INTO public.reviews VALUES (7, 5, 'Lo volvería a leer.', '2025-12-05', 2, 4, '2025-12-05 23:25:26.98444-03', '2025-12-05 23:25:26.984441-03');
INSERT INTO public.reviews VALUES (8, 4, 'Sólido.', '2025-12-05', 3, 5, '2025-12-05 23:25:26.984444-03', '2025-12-05 23:25:26.984445-03');
INSERT INTO public.reviews VALUES (9, 1, 'No es para mí.', '2025-12-05', 4, 6, '2025-12-05 23:25:26.984449-03', '2025-12-05 23:25:26.98445-03');
INSERT INTO public.reviews VALUES (10, 5, 'Imprescindible.', '2025-12-05', 5, 7, '2025-12-05 23:25:26.984454-03', '2025-12-05 23:25:26.984455-03');
INSERT INTO public.reviews VALUES (11, 4, 'Buen ritmo.', '2025-12-05', 1, 8, '2025-12-05 23:25:26.984458-03', '2025-12-05 23:25:26.984459-03');
INSERT INTO public.reviews VALUES (12, 3, 'Regular.', '2025-12-05', 2, 9, '2025-12-05 23:25:26.984463-03', '2025-12-05 23:25:26.984464-03');
INSERT INTO public.reviews VALUES (13, 5, 'Fantástico.', '2025-12-05', 3, 10, '2025-12-05 23:25:26.984467-03', '2025-12-05 23:25:26.984468-03');
INSERT INTO public.reviews VALUES (14, 4, 'Me enganchó desde el principio.', '2025-12-05', 4, 1, '2025-12-05 23:25:26.984472-03', '2025-12-05 23:25:26.984473-03');
INSERT INTO public.reviews VALUES (15, 5, 'De mis favoritos.', '2025-12-05', 5, 2, '2025-12-05 23:25:26.984476-03', '2025-12-05 23:25:26.984477-03');


--
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: library_user
--

SELECT pg_catalog.setval('public.books_id_seq', 10, true);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: library_user
--

SELECT pg_catalog.setval('public.categories_id_seq', 5, true);


--
-- Name: loans_id_seq; Type: SEQUENCE SET; Schema: public; Owner: library_user
--

SELECT pg_catalog.setval('public.loans_id_seq', 8, true);


--
-- Name: reviews_id_seq; Type: SEQUENCE SET; Schema: public; Owner: library_user
--

SELECT pg_catalog.setval('public.reviews_id_seq', 15, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: library_user
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict yB3dvqo4RJF11XTGNQ6bhGOMTdP4d0Aizjlb1YjzzdzseCIeHlk1g2giHpaN3cs

