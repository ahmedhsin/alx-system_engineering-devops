#!/bin/bash
STR="6-multiple_permissions"
echo -e "#!/bin/bash" >> $STR;
echo -e "chmod ug+x,o+r hello">>$STR;
chmod u+x $STR;
git add *
git commit -m "blablabla"
git push