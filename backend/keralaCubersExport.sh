members=()
while read -r line
do
members+=("$line")
done < "../membersID.dat"
echo ${members[@]}
mysql -u dany -pemmaus wca << EOF
delete from KeralaCubers;
EOF
for i in $(seq 0 ${#members[@]})
do
id="${members[$i]}"
if [ ${#id} -ge 10 ]
then
mysql -u dany -pemmaus wca << EOF
insert into KeralaCubers values ('$id');
EOF
fi
done