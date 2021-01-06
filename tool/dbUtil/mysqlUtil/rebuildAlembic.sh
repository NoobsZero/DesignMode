python3 -m emCollect.service.install_init

if [ -d "./alembic"  ];then
	echo "删除 alembic"
	rm -rf alembic	
fi
alembic init alembic
cp alembicInit/env.py  ./alembic/
 



