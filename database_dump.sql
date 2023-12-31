PGDMP                         {            cse412-project    15.4    15.4 ;    W           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            X           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            Y           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            Z           1262    16488    cse412-project    DATABASE     �   CREATE DATABASE "cse412-project" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
     DROP DATABASE "cse412-project";
                khoi    false                        2615    16963    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            [           0    0    SCHEMA public    COMMENT         COMMENT ON SCHEMA public IS '';
                   postgres    false    5            \           0    0    SCHEMA public    ACL     +   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
                   postgres    false    5            �            1259    16965 
   admin_user    TABLE     �   CREATE TABLE public.admin_user (
    admin_id integer NOT NULL,
    password character varying(20) NOT NULL,
    user_name character varying(20) NOT NULL
);
    DROP TABLE public.admin_user;
       public         heap    postgres    false    5            �            1259    17016    course    TABLE     �   CREATE TABLE public.course (
    course_id integer NOT NULL,
    room_id integer NOT NULL,
    des character varying(30),
    req integer,
    addr character varying(30)
);
    DROP TABLE public.course;
       public         heap    postgres    false    5            �            1259    17021 
   department    TABLE     �   CREATE TABLE public.department (
    dept_id integer NOT NULL,
    des character varying(30),
    capacity integer,
    fund double precision
);
    DROP TABLE public.department;
       public         heap    postgres    false    5            �            1259    17036 
   enrolls_in    TABLE     �   CREATE TABLE public.enrolls_in (
    student_uni_id integer NOT NULL,
    course_id integer NOT NULL,
    room_id integer NOT NULL
);
    DROP TABLE public.enrolls_in;
       public         heap    postgres    false    5            �            1259    16987    faculty    TABLE     v   CREATE TABLE public.faculty (
    uni_id integer NOT NULL,
    fa_id integer NOT NULL,
    salary double precision
);
    DROP TABLE public.faculty;
       public         heap    postgres    false    5            �            1259    17066    has    TABLE     x   CREATE TABLE public.has (
    course_id integer NOT NULL,
    room_id integer NOT NULL,
    dept_id integer NOT NULL
);
    DROP TABLE public.has;
       public         heap    postgres    false    5            �            1259    17026    manages    TABLE     _   CREATE TABLE public.manages (
    admin_id integer NOT NULL,
    system_id integer NOT NULL
);
    DROP TABLE public.manages;
       public         heap    postgres    false    5            �            1259    16999 	   professor    TABLE     y   CREATE TABLE public.professor (
    uni_id integer NOT NULL,
    fa_id integer NOT NULL,
    prof_id integer NOT NULL
);
    DROP TABLE public.professor;
       public         heap    postgres    false    5            �            1259    16975    student    TABLE     �   CREATE TABLE public.student (
    uni_id integer NOT NULL,
    stu_id integer NOT NULL,
    gpa double precision,
    tuition double precision,
    enr_yr character varying(4)
);
    DROP TABLE public.student;
       public         heap    postgres    false    5            �            1259    17051    teaches    TABLE     {   CREATE TABLE public.teaches (
    uni_id integer NOT NULL,
    course_id integer NOT NULL,
    room_id integer NOT NULL
);
    DROP TABLE public.teaches;
       public         heap    postgres    false    5            �            1259    16970    university_person    TABLE       CREATE TABLE public.university_person (
    uni_id integer NOT NULL,
    first_name character varying(15),
    last_name character varying(15),
    phone_number character varying(10),
    email character varying(30),
    addr character varying(30),
    gender character(1)
);
 %   DROP TABLE public.university_person;
       public         heap    postgres    false    5            �            1259    17081    works_in    TABLE     \   CREATE TABLE public.works_in (
    uni_id integer NOT NULL,
    dept_id integer NOT NULL
);
    DROP TABLE public.works_in;
       public         heap    postgres    false    5            I          0    16965 
   admin_user 
   TABLE DATA           C   COPY public.admin_user (admin_id, password, user_name) FROM stdin;
    public          postgres    false    214   KF       N          0    17016    course 
   TABLE DATA           D   COPY public.course (course_id, room_id, des, req, addr) FROM stdin;
    public          postgres    false    219   �F       O          0    17021 
   department 
   TABLE DATA           B   COPY public.department (dept_id, des, capacity, fund) FROM stdin;
    public          postgres    false    220   cG       Q          0    17036 
   enrolls_in 
   TABLE DATA           H   COPY public.enrolls_in (student_uni_id, course_id, room_id) FROM stdin;
    public          postgres    false    222   �G       L          0    16987    faculty 
   TABLE DATA           8   COPY public.faculty (uni_id, fa_id, salary) FROM stdin;
    public          postgres    false    217   H       S          0    17066    has 
   TABLE DATA           :   COPY public.has (course_id, room_id, dept_id) FROM stdin;
    public          postgres    false    224   �H       P          0    17026    manages 
   TABLE DATA           6   COPY public.manages (admin_id, system_id) FROM stdin;
    public          postgres    false    221   'I       M          0    16999 	   professor 
   TABLE DATA           ;   COPY public.professor (uni_id, fa_id, prof_id) FROM stdin;
    public          postgres    false    218   MI       K          0    16975    student 
   TABLE DATA           G   COPY public.student (uni_id, stu_id, gpa, tuition, enr_yr) FROM stdin;
    public          postgres    false    216   �I       R          0    17051    teaches 
   TABLE DATA           =   COPY public.teaches (uni_id, course_id, room_id) FROM stdin;
    public          postgres    false    223   K       J          0    16970    university_person 
   TABLE DATA           m   COPY public.university_person (uni_id, first_name, last_name, phone_number, email, addr, gender) FROM stdin;
    public          postgres    false    215   MK       T          0    17081    works_in 
   TABLE DATA           3   COPY public.works_in (uni_id, dept_id) FROM stdin;
    public          postgres    false    225   pR       �           2606    16969    admin_user admin_user_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.admin_user
    ADD CONSTRAINT admin_user_pkey PRIMARY KEY (admin_id);
 D   ALTER TABLE ONLY public.admin_user DROP CONSTRAINT admin_user_pkey;
       public            postgres    false    214            �           2606    17020    course course_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_pkey PRIMARY KEY (course_id, room_id);
 <   ALTER TABLE ONLY public.course DROP CONSTRAINT course_pkey;
       public            postgres    false    219    219            �           2606    17025    department department_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (dept_id);
 D   ALTER TABLE ONLY public.department DROP CONSTRAINT department_pkey;
       public            postgres    false    220            �           2606    17040    enrolls_in enrolls_in_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.enrolls_in
    ADD CONSTRAINT enrolls_in_pkey PRIMARY KEY (student_uni_id, course_id, room_id);
 D   ALTER TABLE ONLY public.enrolls_in DROP CONSTRAINT enrolls_in_pkey;
       public            postgres    false    222    222    222            �           2606    16993    faculty faculty_fa_id_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_fa_id_key UNIQUE (fa_id);
 C   ALTER TABLE ONLY public.faculty DROP CONSTRAINT faculty_fa_id_key;
       public            postgres    false    217            �           2606    16991    faculty faculty_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (uni_id);
 >   ALTER TABLE ONLY public.faculty DROP CONSTRAINT faculty_pkey;
       public            postgres    false    217            �           2606    17070    has has_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.has
    ADD CONSTRAINT has_pkey PRIMARY KEY (course_id, room_id, dept_id);
 6   ALTER TABLE ONLY public.has DROP CONSTRAINT has_pkey;
       public            postgres    false    224    224    224            �           2606    17030    manages manages_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.manages
    ADD CONSTRAINT manages_pkey PRIMARY KEY (admin_id, system_id);
 >   ALTER TABLE ONLY public.manages DROP CONSTRAINT manages_pkey;
       public            postgres    false    221    221            �           2606    17003    professor professor_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_pkey PRIMARY KEY (uni_id);
 B   ALTER TABLE ONLY public.professor DROP CONSTRAINT professor_pkey;
       public            postgres    false    218            �           2606    17005    professor professor_prof_id_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_prof_id_key UNIQUE (prof_id);
 I   ALTER TABLE ONLY public.professor DROP CONSTRAINT professor_prof_id_key;
       public            postgres    false    218            �           2606    16979    student student_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (uni_id);
 >   ALTER TABLE ONLY public.student DROP CONSTRAINT student_pkey;
       public            postgres    false    216            �           2606    16981    student student_stu_id_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_stu_id_key UNIQUE (stu_id);
 D   ALTER TABLE ONLY public.student DROP CONSTRAINT student_stu_id_key;
       public            postgres    false    216            �           2606    17055    teaches teaches_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.teaches
    ADD CONSTRAINT teaches_pkey PRIMARY KEY (uni_id, course_id, room_id);
 >   ALTER TABLE ONLY public.teaches DROP CONSTRAINT teaches_pkey;
       public            postgres    false    223    223    223            �           2606    16974 (   university_person university_person_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.university_person
    ADD CONSTRAINT university_person_pkey PRIMARY KEY (uni_id);
 R   ALTER TABLE ONLY public.university_person DROP CONSTRAINT university_person_pkey;
       public            postgres    false    215            �           2606    17085    works_in works_in_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.works_in
    ADD CONSTRAINT works_in_pkey PRIMARY KEY (uni_id, dept_id);
 @   ALTER TABLE ONLY public.works_in DROP CONSTRAINT works_in_pkey;
       public            postgres    false    225    225            �           2606    17046 ,   enrolls_in enrolls_in_course_id_room_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.enrolls_in
    ADD CONSTRAINT enrolls_in_course_id_room_id_fkey FOREIGN KEY (course_id, room_id) REFERENCES public.course(course_id, room_id) ON DELETE CASCADE;
 V   ALTER TABLE ONLY public.enrolls_in DROP CONSTRAINT enrolls_in_course_id_room_id_fkey;
       public          postgres    false    3233    219    219    222    222            �           2606    17041 )   enrolls_in enrolls_in_student_uni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.enrolls_in
    ADD CONSTRAINT enrolls_in_student_uni_id_fkey FOREIGN KEY (student_uni_id) REFERENCES public.student(uni_id) ON DELETE CASCADE;
 S   ALTER TABLE ONLY public.enrolls_in DROP CONSTRAINT enrolls_in_student_uni_id_fkey;
       public          postgres    false    216    222    3221            �           2606    16994    faculty faculty_uni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_uni_id_fkey FOREIGN KEY (uni_id) REFERENCES public.university_person(uni_id) ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.faculty DROP CONSTRAINT faculty_uni_id_fkey;
       public          postgres    false    217    215    3219            �           2606    17076    has has_course_id_room_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.has
    ADD CONSTRAINT has_course_id_room_id_fkey FOREIGN KEY (course_id, room_id) REFERENCES public.course(course_id, room_id) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.has DROP CONSTRAINT has_course_id_room_id_fkey;
       public          postgres    false    219    219    3233    224    224            �           2606    17071    has has_dept_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.has
    ADD CONSTRAINT has_dept_id_fkey FOREIGN KEY (dept_id) REFERENCES public.department(dept_id) ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.has DROP CONSTRAINT has_dept_id_fkey;
       public          postgres    false    224    220    3235            �           2606    17031    manages manages_admin_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.manages
    ADD CONSTRAINT manages_admin_id_fkey FOREIGN KEY (admin_id) REFERENCES public.admin_user(admin_id) ON DELETE CASCADE;
 G   ALTER TABLE ONLY public.manages DROP CONSTRAINT manages_admin_id_fkey;
       public          postgres    false    214    3217    221            �           2606    17011    professor professor_fa_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_fa_id_fkey FOREIGN KEY (fa_id) REFERENCES public.faculty(fa_id) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.professor DROP CONSTRAINT professor_fa_id_fkey;
       public          postgres    false    3225    218    217            �           2606    17006    professor professor_uni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_uni_id_fkey FOREIGN KEY (uni_id) REFERENCES public.faculty(uni_id) ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.professor DROP CONSTRAINT professor_uni_id_fkey;
       public          postgres    false    217    3227    218            �           2606    16982    student student_uni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_uni_id_fkey FOREIGN KEY (uni_id) REFERENCES public.university_person(uni_id) ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.student DROP CONSTRAINT student_uni_id_fkey;
       public          postgres    false    216    3219    215            �           2606    17061 &   teaches teaches_course_id_room_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.teaches
    ADD CONSTRAINT teaches_course_id_room_id_fkey FOREIGN KEY (course_id, room_id) REFERENCES public.course(course_id, room_id) ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.teaches DROP CONSTRAINT teaches_course_id_room_id_fkey;
       public          postgres    false    223    3233    219    223    219            �           2606    17056    teaches teaches_uni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.teaches
    ADD CONSTRAINT teaches_uni_id_fkey FOREIGN KEY (uni_id) REFERENCES public.professor(uni_id) ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.teaches DROP CONSTRAINT teaches_uni_id_fkey;
       public          postgres    false    223    3229    218            �           2606    17091    works_in works_in_dept_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.works_in
    ADD CONSTRAINT works_in_dept_id_fkey FOREIGN KEY (dept_id) REFERENCES public.department(dept_id) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.works_in DROP CONSTRAINT works_in_dept_id_fkey;
       public          postgres    false    220    3235    225            �           2606    17086    works_in works_in_uni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.works_in
    ADD CONSTRAINT works_in_uni_id_fkey FOREIGN KEY (uni_id) REFERENCES public.faculty(uni_id) ON DELETE CASCADE;
 G   ALTER TABLE ONLY public.works_in DROP CONSTRAINT works_in_uni_id_fkey;
       public          postgres    false    3227    217    225            I   e   x��;�0���-Pz�?����6�%����l�\?�jR��V�e��g�8���4?���O�LIn�n�&/�#���Z�j��B3�u�[��^#� �G      N   �   x�U�1�@��z�s c��(Z�(QK��8	�C����Nac�W|������)���D�;�Q�9��W�^v�ûHD#�)j�5\RV�,�J��L����A�����%�Ix�EJy�o:����d��s�/�-��s_�3�      O   _   x�370�t��-(-I-RN�L�KNUpI-H,*�M�+�440�45 .s#N�Ē���Ē��bdU�&0EƜ�@%��%E�(p�A���qqq ��"�      Q   $   x�340�450�440�b$��mds��qqq �}/      L   �   x��ˑ1C�5/�\&�8��ou�c���-97���V�Ee��W���;Omx
a7g��QH�xt�W({�UhF@��/9�n�µ��8�!�]��`C*����4CR����I{�ʓ$U�/H��
0� )r��v�HIQ�ٮO9��إO)qw��U��Xep�)1{S��H)�����.RJ�2_�;RJ�z�v�Rr���J)�yk�.9���	��w~��?/J�      S   !   x�350�4bsC.Sc ��6����� E�g      P      x�3�4�2bc ����� (      M   k   x�λ�0�:&0%˟]���5^�S��c��<�\HH�F��:�PYM4C5P���ZV���U�cMtѵh-rK�"Z䖢E��-E�h�[��"�4I�:�7"~�*$�      K   C  x�M�Ǒ�0C�r1�A�����̿�{1=	fF�Y�x�����AF����΢�r�N���_RȊ��K?�`8η�rt)%�2��e���t���:� ��-���.�X-~�9<79{�e��c]Yw�8�V��h	��N��� ���3��� ĸ;��4���v�v:� ��iګsĀ���8ooZt�@Bgo;�����gㆭy?�B(�7<YC(M�|9o���(P���}������'Y��N��E�E�W�TN(���=]���(PԈ�e�brw����z�d����}l�a]N	� >�=���<�7�sw�      R   "   x�342�450�440�24��M�l�=... E�k      J     x�eW�r7<�_�?��p�d�Rd1N�J)I�r!�P�.%3_�ƾlPGv����gz�(%��غ�<�W�6'RAcF��D����K�~��)yU\����ՑOe��nZ���\G$��dJ����䑴,nb���UKV�ɣov�9�`�U��Yɘ�Տ��YEyqӸ�l�ǰd%��YĹ8n\ۓJH�3�G|��@�,n��튯��D6Gn��;"8U�R���΂����������C�-ypmk��$!Q����,�ԪXٶ��c��!fEV��%�ǭ���I57T���,�`�x��-�i���͛�Y�yt(
��*Q(���DIkV\�ַYV�\�`B�ޒ��]��DU�Jk�;�yLY��n?G3$}��Hn]�=6�T�jIKV����,
�[ܞj�-w��d4	ʷ֑_;K8��Ѓ�a��=2^\7�C<�z�b�|��,�p}Lj�
j4*?��_��������'[��I��b���FI�Ў352yi�*�v��P�H�����侉��T�Zk��ς�
ŵ�w��)�E㻝E�	C&�.؄p^�R�1�cq'1I>�~��t�u�ƥS�9߹�ʛ����)�'�z>��<��䈪� %%M�39�b埞�)��mӑ�P�R��+Q��Hd��,�O��F��C�Ps�*�@���N�a�d���<�k����z	eȯ�	�[�o��oñ�7q.����CBD+��\:$��� ���4�*��f	�\��@�{�9����Y���օ�\�bC:C[	�����d.��p�w�����`�q��=���4�.Ln�_ڃ����q-��]�vG�pQ���#>�y��"�`{���./ӗ=��mc:�CQXLB0/�ţs��y�u�[Knm;���,�3�*�WlNa�S��n�z�������71�g����4J�����t�@4ȥԬ21���Ea[��se�I�{k�&rݼ�@0?�PƠ�'b��~����/3?ݺ!7�v�ñIK����9������#%kl
� �_��3-��)F;���������i�;���S��2%�5.�̽�����e�����6����V�](e1�g ��>�!;Z��V�g���o�]�K)!"cFf&�#�]a\���>��C+����D�
v�R��w��%�7��n`��~�&.��$�(��Mԙ��"��|���㔀T1��9�Ja������Y#/V��[�P�S��}riow3�+L]�2S#��UѴ����d9�Mntyj�p%�%��Ѩf �FAů�k7m��y�AƿE��CW���èA@��h$F<��>c#�O�� �Z�PWr]��V�h�h���a�ؿ!��2������zk�'��Q�䌥Ķ�����^�Pǭq>O�!�� ��	S�����Gؙ-�⏷�nA���{}i{,o���5�P]j]i�A3�~J=�Շ��-%)�U��MMo����Je"<�
΋�S�7�+jx�ކ��,�?�*Vъ��Fjf���p,�`�"w)'�}��a�FH���������wG7��8�JLcw��>Z� �q��41���c�_B�]�eڨ!/K�v5ѩGSw�	���ŭ�f�8�{i�g�u>Y_��1�\�:�ڤw̱�{�˸I�0,(�.��VN��z7�p�����{��\c�9���-$~�5����_�)~Ǵ��ы������.���6�¸���Mp�KRο����X�z+�ޅ-�ǉJ��|���*a ��ֈ�> �~���������      T   '   x�342�470�242�F@�Hi��%����� �N     