##### addusers script
takes either a count or a file to generate users.
```
#!/bin/bash
# ./addusers suffix count outfile.txt
USAGE="
usage example:
./addusers suffix count/input_file.txt output_file.txt
suffix: will have the counter added after it during username creation
count: number of users thatll be created
input_file: a file containing plaintext 'username:password' in each row
output_file: file thatll store the users and their password hashes"
(( $# == 3 )) || echo "There are some missing parameters." "$USAGE"
add_from_file () {
	INPUT_FILE=$1
	for row in $(IFS=: cat $INPUT_FILE 2> /dev/null)
	do
		IFS=: read username password <<< $row
		password=$(openssl passwd $password)
		useradd $username"_"$SUFFIX -p $password
		echo $username:$password >> $OUTPUT
	done
}
add_from_counter () {
	COUNT=$1
	for num in $(seq 1 $COUNT)
	do
		username="$SUFFIX"_"$num"
		password=$(openssl rand -base64 8)
		id $username 2> /dev/null || useradd $username -p $password
		echo $username:$password >> $OUTPUT
	done
}
SUFFIX=$1
[ "$2" -eq "$2" 2>/dev/null ] && FUNC=add_from_counter || FUNC=add_from_file
OUTPUT=$3

$FUNC $2
```

#### greetings script
```
#!/bin/bash
#
question="What's your name?
> "
read -p "$question" name
echo "Hello $name"
```

#### s2 script
```
#!/bin/bash
#first method
source s1.sh
echo x=$x
#second method
env $(cat s1.sh | xargs) &> /dev/null
echo x=$x
```
#### s1 env file / script
```
x=5
```
#### mycp
```
#!/bin/bash
cp -r $*
```
#### mycd
```
#!/bin/bash
cd $1
bash
```
#### myls
```
#!/bin/bash
ls $*
```
#### mytest.sh
```
#!/bin/bash

TARGET=$1
echo -e "type\t\tpermissions"
stat -c "%F   %A" $1
```
#### myinfo.sh
```
#!/bin/bash
#
USERNAME="Whats your username?
> "
read -p "$USERNAME" username 
home="/home/$username"
[ -d $home ] || exit 1
ls -alh $home
mkdir /tmp/$username
cp -r $home /tmp/$username
top > /tmp/$username/process_status
```
#### mycase.sh
```
#!/bin/bash

read -p "Enter a char / sttring: " char
if [[ ${#char} == 1 ]]
then
	echo "you wrote a char."
	case $char in
	  [A-Z])
	      echo "upper case"
	      ;;
	  [a-z])
	      echo "lower case"
	      ;;
	  [0-9])
	      echo "number"
	      ;;
	  "")
	      echo "nothing"
	      ;;
	esac
else
	echo "you wrote a string."
	str=$char
	if [[ $str =~ ^[A-Z]+$ ]]; then
	   echo "upper cases string"
	elif [[ $str =~ ^[a-z]+$ ]]; then
	   echo "lower cases string"
	elif [[ $str =~ ^[0-9]+$ ]]; then
	   echo "numbers"
	else
	   echo "mix"
	fi
fi
```

#### mychmod.sh
```
#!/bin/bash
chmod -R +x $HOME
```

#### mybackup.sh
```
#!/bin/bash
tar cvf /tmp/$USER_home_backup.tar $HOME
```
