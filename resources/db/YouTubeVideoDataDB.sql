--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

-- Started on 2023-02-05 02:04:09

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
-- TOC entry 6 (class 2615 OID 16399)
-- Name: VideoData; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA IF NOT EXISTS "VideoData";


ALTER SCHEMA "VideoData" OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16400)
-- Name: Video; Type: TABLE; Schema: VideoData; Owner: postgres
--

CREATE TABLE  IF NOT EXISTS "VideoData"."Video"(
    video_id character varying(50) NOT NULL,
    thubmnail_default character varying(250),
    thumbnail_medium character varying(250),
    thumbnail_high character varying(250),
    title character varying(250),
    description character varying(1000),
    published_at date,
    "timestamp" date
);


ALTER TABLE "VideoData"."Video" OWNER TO postgres;

--
-- TOC entry 3317 (class 0 OID 16400)
-- Dependencies: 215
-- Data for Name: Video; Type: TABLE DATA; Schema: VideoData; Owner: postgres
--

COPY "VideoData"."Video" (video_id, thubmnail_default, thumbnail_medium, thumbnail_high, title, description, published_at, "timestamp") FROM stdin;
\.


--
-- TOC entry 3174 (class 2606 OID 16406)
-- Name: Video Video_pkey; Type: CONSTRAINT; Schema: VideoData; Owner: postgres
--

ALTER TABLE ONLY "VideoData"."Video"
    ADD CONSTRAINT "Video_pkey" PRIMARY KEY (video_id);


-- Completed on 2023-02-05 02:04:09

--
-- PostgreSQL database dump complete
--

