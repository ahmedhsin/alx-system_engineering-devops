#!/bin/bash
STR="6-multiple_permissions"
echo -e "#!/bin/bash" >> $STR;
echo -e "chmod 777 hello">>$STR;
chmod a+r,ug+x $STR;
git add *
git commit -m "blablabla"
git push