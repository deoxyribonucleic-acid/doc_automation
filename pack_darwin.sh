python -m PyInstaller -w -D --upx -y  main_teacher.py     
echo "add File_template"
cp -r File_template dist/main_teacher.app/
echo "add database"
cp -r database dist/main_teacher.app/
echo "all done"
open dist/main_teacher.app