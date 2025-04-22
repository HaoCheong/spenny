--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Debian 14.5-2.pgdg110+2)
-- Dumped by pg_dump version 14.15 (Ubuntu 14.15-0ubuntu0.22.04.1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: buckets; Type: TABLE; Schema: public; Owner: spenny_user
--

CREATE TABLE public.buckets (
    id integer NOT NULL,
    name character varying,
    description character varying,
    current_amount double precision,
    properties json
);


ALTER TABLE public.buckets OWNER TO spenny_user;

--
-- Name: buckets_id_seq; Type: SEQUENCE; Schema: public; Owner: spenny_user
--

CREATE SEQUENCE public.buckets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.buckets_id_seq OWNER TO spenny_user;

--
-- Name: buckets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spenny_user
--

ALTER SEQUENCE public.buckets_id_seq OWNED BY public.buckets.id;


--
-- Name: flowEvents; Type: TABLE; Schema: public; Owner: spenny_user
--

CREATE TABLE public."flowEvents" (
    id integer NOT NULL,
    name character varying,
    description character varying,
    change_amount double precision,
    type character varying,
    frequency character varying,
    next_trigger timestamp without time zone,
    from_bucket_id integer,
    to_bucket_id integer
);


ALTER TABLE public."flowEvents" OWNER TO spenny_user;

--
-- Name: flowEvents_id_seq; Type: SEQUENCE; Schema: public; Owner: spenny_user
--

CREATE SEQUENCE public."flowEvents_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."flowEvents_id_seq" OWNER TO spenny_user;

--
-- Name: flowEvents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spenny_user
--

ALTER SEQUENCE public."flowEvents_id_seq" OWNED BY public."flowEvents".id;


--
-- Name: logs; Type: TABLE; Schema: public; Owner: spenny_user
--

CREATE TABLE public.logs (
    id integer NOT NULL,
    name character varying,
    description character varying,
    type character varying,
    amount double precision,
    date_created timestamp without time zone,
    bucket_id integer
);


ALTER TABLE public.logs OWNER TO spenny_user;

--
-- Name: logs_id_seq; Type: SEQUENCE; Schema: public; Owner: spenny_user
--

CREATE SEQUENCE public.logs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.logs_id_seq OWNER TO spenny_user;

--
-- Name: logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spenny_user
--

ALTER SEQUENCE public.logs_id_seq OWNED BY public.logs.id;


--
-- Name: buckets id; Type: DEFAULT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public.buckets ALTER COLUMN id SET DEFAULT nextval('public.buckets_id_seq'::regclass);


--
-- Name: flowEvents id; Type: DEFAULT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public."flowEvents" ALTER COLUMN id SET DEFAULT nextval('public."flowEvents_id_seq"'::regclass);


--
-- Name: logs id; Type: DEFAULT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public.logs ALTER COLUMN id SET DEFAULT nextval('public.logs_id_seq'::regclass);


--
-- Data for Name: buckets; Type: TABLE DATA; Schema: public; Owner: spenny_user
--

COPY public.buckets (id, name, description, current_amount, properties) FROM stdin;
1	Total	Total amount in account	10000	{"invisible": false}
2	Savings	General Savings	1800	{"invisible": false}
3	Lifestyle	Everything from food to fun	200	{"invisible": false}
4	Food	My crippling eating habits	0	{"invisible": false}
5	Fun	For my hobbies and fun stuff 	0	{"invisible": false}
\.


--
-- Data for Name: flowEvents; Type: TABLE DATA; Schema: public; Owner: spenny_user
--

COPY public."flowEvents" (id, name, description, change_amount, type, frequency, next_trigger, from_bucket_id, to_bucket_id) FROM stdin;
1	Main Job income	My main salary	5000	ADD	5d	2024-01-22 17:10:14.412421	\N	1
2	Savings	Automated saving move	1800	MOV	3d	2024-01-19 17:10:14.412437	1	2
3	Rent	Purely to live at my apartment	560	SUB	5d	2024-01-22 17:10:14.412438	1	\N
4	Gym	Fitness Finance	18	SUB	2d	2024-01-22 17:10:14.41244	1	\N
5	Lifestyle	Money for actually living in the cruel world	240	MOV	4d	2024-01-23 17:10:14.412441	1	3
6	Food	Budget for eating	200	MOV	3d	2024-01-17 17:10:14.412442	3	4
7	Fun	Hobby Funding	40	MOV	1d	2024-01-21 17:10:14.412444	3	5
\.


--
-- Data for Name: logs; Type: TABLE DATA; Schema: public; Owner: spenny_user
--

COPY public.logs (id, name, description, type, amount, date_created, bucket_id) FROM stdin;
1	Main Job income	My main salary	ADD	5000	2024-01-19 17:10:14.412455	1
2	Gym Spending	For exercise	SUB	18	2024-01-22 17:10:14.412456	1
3	Household spending move	Moving Total to household spending	MOV	600	2024-01-20 17:10:14.412458	1
4	Savings Move	Money to be saved on untouched	MOV	2000	2024-01-18 17:10:14.412459	1
5	Woolies shopping	Friday woolies shopping	SUB	65	2024-01-19 17:10:14.41246	5
6	Eating at Cafe de la Cafe	Brekkie	SUB	30	2024-01-23 17:10:14.412461	5
\.


--
-- Name: buckets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spenny_user
--

SELECT pg_catalog.setval('public.buckets_id_seq', 5, true);


--
-- Name: flowEvents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spenny_user
--

SELECT pg_catalog.setval('public."flowEvents_id_seq"', 7, true);


--
-- Name: logs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spenny_user
--

SELECT pg_catalog.setval('public.logs_id_seq', 7, true);


--
-- Name: buckets buckets_pkey; Type: CONSTRAINT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public.buckets
    ADD CONSTRAINT buckets_pkey PRIMARY KEY (id);


--
-- Name: flowEvents flowEvents_pkey; Type: CONSTRAINT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public."flowEvents"
    ADD CONSTRAINT "flowEvents_pkey" PRIMARY KEY (id);


--
-- Name: logs logs_pkey; Type: CONSTRAINT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_pkey PRIMARY KEY (id);


--
-- Name: ix_buckets_id; Type: INDEX; Schema: public; Owner: spenny_user
--

CREATE UNIQUE INDEX ix_buckets_id ON public.buckets USING btree (id);


--
-- Name: ix_flowEvents_id; Type: INDEX; Schema: public; Owner: spenny_user
--

CREATE UNIQUE INDEX "ix_flowEvents_id" ON public."flowEvents" USING btree (id);


--
-- Name: ix_logs_id; Type: INDEX; Schema: public; Owner: spenny_user
--

CREATE UNIQUE INDEX ix_logs_id ON public.logs USING btree (id);


--
-- Name: flowEvents flowEvents_from_bucket_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public."flowEvents"
    ADD CONSTRAINT "flowEvents_from_bucket_id_fkey" FOREIGN KEY (from_bucket_id) REFERENCES public.buckets(id);


--
-- Name: flowEvents flowEvents_to_bucket_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public."flowEvents"
    ADD CONSTRAINT "flowEvents_to_bucket_id_fkey" FOREIGN KEY (to_bucket_id) REFERENCES public.buckets(id);


--
-- Name: logs logs_bucket_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: spenny_user
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_bucket_id_fkey FOREIGN KEY (bucket_id) REFERENCES public.buckets(id);


--
-- PostgreSQL database dump complete
--

