echo "Whats your name"
read var
if [ `echo $var | wc -c` -eq 2 ]
then
if [[ $var == [a-z] ]]
then 
echo "true"
else 
echo "false"
fi
else 
echo " your entry is invalid"
fi
fi
