--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4 (Debian 14.4-1.pgdg110+1)
-- Dumped by pg_dump version 14.4 (Debian 14.4-1.pgdg110+1)

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
-- Data for Name: api_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_product (id, description, price, stock) FROM stdin;
1	Producto 1	2567	3
2	Producto 2	8500	1
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$320000$5tQL21gfwKGGAL7pNVf64n$oPdGrGBXlvDncJ/XF3DdiFTlAefytKmnWarTXKNVvvs=	2022-08-06 03:03:47.403436+00	f	marianela				f	t	2022-08-03 17:12:07+00
1	pbkdf2_sha256$320000$q7BrvQdJSvmJMuEynxUBi6$pJKogB8higHLqdZ6zDfywze5hkdFSrMjv1Rxr7udxrA=	2022-08-07 19:47:38.10586+00	t	admin				t	t	2022-08-03 17:10:51.314387+00
\.


--
-- Name: api_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_product_id_seq', 2, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

