--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Debian 14.5-2.pgdg110+2)
-- Dumped by pg_dump version 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1)

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
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

-- *not* creating schema, since initdb creates it


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: buckets; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.buckets (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL,
    amount integer NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    bucket_type character varying,
    properties json
);


--
-- Name: buckets_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.buckets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: buckets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.buckets_id_seq OWNED BY public.buckets.id;


--
-- Name: events; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.events (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL,
    trigger_datetime timestamp without time zone NOT NULL,
    frequency character varying NOT NULL,
    event_type character varying NOT NULL,
    properties json NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    bucket_id integer
);


--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- Name: logs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.logs (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL,
    event_id integer NOT NULL,
    event_type character varying NOT NULL,
    event_properties json NOT NULL,
    bucket_id integer NOT NULL,
    bucket_name character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    log_type character varying
);


--
-- Name: logs_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.logs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.logs_id_seq OWNED BY public.logs.id;


--
-- Name: buckets id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buckets ALTER COLUMN id SET DEFAULT nextval('public.buckets_id_seq'::regclass);


--
-- Name: events id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- Name: logs id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.logs ALTER COLUMN id SET DEFAULT nextval('public.logs_id_seq'::regclass);


--
-- Data for Name: buckets; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.buckets (id, name, description, amount, created_at, updated_at, bucket_type, properties) FROM stdin;
1	Start	Starting Bucket	5000	2025-05-08 11:10:33.951	2025-05-08 11:10:33.951	STORE	\N
2	Household	Household Expenses	0	2025-05-08 11:11:04.558	2025-05-08 11:11:04.558	STORE	\N
3	Necessity	Necessary Spending	0	2025-05-08 11:11:55.448	2025-05-08 11:11:55.448	STORE	\N
4	Lifestyle	Lifestyle personal uses	0	2025-05-08 11:11:55.448	2025-05-08 11:11:55.448	STORE	\N
5	Savings	Savings that are accumulated	0	2025-05-08 11:12:50.965	2025-05-08 11:12:50.965	STORE	\N
6	Debt	Debts I owe people	-500	2025-05-08 11:13:23.688	2025-05-08 11:13:23.688	INVSB	\N
7	Rent	Rent cost and portioning	0	2025-05-08 11:13:23.688	2025-05-08 11:13:23.688	STORE	\N
8	Bills	Utility Bills and Spending	0	2025-05-08 11:14:20.036	2025-05-08 11:14:20.036	STORE	\N
9	Health Insurance	Medical Health Insurance	0	2025-05-08 11:14:36.08	2025-05-08 11:14:36.08	STORE	\N
11	Weekly Spending	Grocery and Eating out spending	0	2025-05-08 11:15:03.186	2025-05-08 11:15:03.186	STORE	\N
12	Gym	Spending at the Gym	0	2025-05-08 11:17:12.596	2025-05-08 11:17:12.596	STORE	\N
10	Fun Fund	Spending for wants	0	2025-05-08 11:18:51.831	2025-05-08 11:18:51.831	STORE	\N
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.events (id, name, description, trigger_datetime, frequency, event_type, properties, created_at, updated_at, bucket_id) FROM stdin;
1	Salary	Monthly Salary, paid on the last working day of the month	2025-03-01 11:26:42.614	1m	ADD	{"amount": 5500}	2025-05-08 11:26:42.614	2025-05-08 11:26:42.614	1
2	Household Transfer	Monthly Transfer of household stuff	2025-03-02 11:28:02.028	1m	MOVE	{"to_bucket_id": 2, "amount": 2400}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	1
3	Necessity Transfer	Monthly Transfer for necessity	2025-03-02 11:28:02.028	1m	MOVE	{"to_bucket_id": 3, "amount": 150}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	1
4	Lifestyle Transfer	Monthly Transfer for lifestyle	2025-03-02 11:28:02.028	1m	MOVE	{"to_bucket_id": 4, "amount": 1260}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	1
5	Savings Transfer	Monthly Transfer for to savings account	2025-03-02 11:28:02.028	1m	MOVE	{"to_bucket_id": 5, "amount": 1690}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	1
6	Rent Transfer	Monthly Transfer for rent	2025-03-03 11:28:02.028	1m	MOVE	{"to_bucket_id": 6, "amount": 2000}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	2
7	Bill Transfer	Monthly Transfer for utilities: Gas, Electric, Internet	2025-03-03 11:28:02.028	1m	MOVE	{"to_bucket_id": 7, "amount": 200}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	2
13	Auto Rental Payment	Fortnightly rental payment	2025-03-14 11:28:02.028	2w	SUB	{"amount": 1000}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	2
8	Health Insurance Transfer	Monthly Transfer for medicare health insurance	2025-03-03 11:28:02.028	1m	MOVE	{"to_bucket_id": 9, "amount": 150}	2025-05-08 11:40:12.202	2025-05-08 11:40:12.202	3
14	Health Insurance Payment	Monthly Medicare payment	2025-03-07 11:28:02.028	1m	SUB	{"amount": 150}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	3
9	Fun Fund Transfer	Weekly Transfer for fun stuff fund	2025-03-03 11:28:02.028	1w	MOVE	{"to_bucket_id": 10, "amount": 50}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	4
10	Weekly Spending Transfer	Weekly Transfer for Groceries and what not	2025-03-03 11:28:02.028	1w	MOVE	{"to_bucket_id": 11, "amount": 200}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	4
11	Gym Transfer	Weekly Transfer for gym membership	2025-03-03 11:28:02.028	1w	MOVE	{"to_bucket_id": 12, "amount": 15}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	4
12	PT Transfer	Weekly Transfer for Personal Trainer	2025-03-03 11:28:02.028	2w	MOVE	{"to_bucket_id": 12, "amount": 100}	2025-05-08 11:28:02.028	2025-05-08 11:28:02.028	4
\.


--
-- Data for Name: logs; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.logs (id, name, description, event_id, event_type, event_properties, bucket_id, bucket_name, created_at, updated_at, log_type) FROM stdin;
\.


--
-- Name: buckets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.buckets_id_seq', 12, true);


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.events_id_seq', 14, true);


--
-- Name: logs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.logs_id_seq', 1, false);


--
-- Name: buckets buckets_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buckets
    ADD CONSTRAINT buckets_pkey PRIMARY KEY (id);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- Name: logs logs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_pkey PRIMARY KEY (id);


--
-- Name: ix_buckets_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_buckets_id ON public.buckets USING btree (id);


--
-- Name: ix_events_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_events_id ON public.events USING btree (id);


--
-- Name: ix_logs_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_logs_id ON public.logs USING btree (id);


--
-- Name: events events_bucket_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_bucket_id_fkey FOREIGN KEY (bucket_id) REFERENCES public.buckets(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: -
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

