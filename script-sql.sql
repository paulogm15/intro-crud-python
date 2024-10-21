create database facsenac;
use facsenac; -- ativa o db
show databases;

drop table if exists alunos;

create table if not exists alunos (
	matricula int not null primary key,
	nome char(20) not null,
	cod_curso int not null,
	idade int,
	data datetime
);

select * from alunos;

show tables;

insert into alunos values(10, 'Cleiton Tavares', 21, 19, now());
insert into alunos values(11, 'Ana Paula', 21, 20, now());

update alunos set idade=30 where matricula=10;

delete from alunos where matricula=11;


create table usuarios(
	cod int not null auto_increment primary key,
	nome char(30) not null,
	cidade char(20) not null default "Brasilia",
	uf char(3) default "DF",
	data_cadastro datetime
);

insert into usuarios values(
  null,
  'Lando Norris',
  default,
  default,
  now()
);

select * from usuarios order by nome;

update usuarios set nome="Emerson Fittipaldi" where cod=1;

delete from usuarios where cod=1;





