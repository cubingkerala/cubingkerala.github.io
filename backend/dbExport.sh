curl -O https://www.worldcubeassociation.org/results/misc/WCA_export.sql.zip
unzip ./WCA_export.sql.zip -d db
mysql -u dany -pemmaus wca < db/WCA_export.sql
rm WCA_export.sql.zip
rm db/*
mysql -u dany -pemmaus wca << EOF
create table KeralaCubers (id varchar(10));
EOF