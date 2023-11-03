echo "which build do you want to generate?"
echo "1. teacher"
echo "2. student"
echo "3. full"
set /p choice="your choice: "
if %choice%==1 goto teacher
if %choice%==2 goto student
if %choice%==3 goto full
goto end

:teacher
python -m nuitka ^
          --mingw64 ^
          --follow-imports ^
          --output-dir=build\teacher\ ^
          --assume-yes-for-download ^
          --windows-product-version=1.0 ^
          --include-data-dir=database=database,File_template=File_template ^
          --onefile ^
          --plugin-enable=pyqt5 ^
          --windows-disable-console ^
          --windows-icon-from-ico=icon\icon.ico ^
          teacher_entry.py

echo "add File_template"
mkdir build\teacher\File_template
xcopy File_template build\teacher\File_template /s /y
echo "add database"
mkdir build\teacher\database
xcopy database build\teacher\database /s /y
echo "finished generating teacher.exe"
goto end

:student
python -m nuitka ^
          --mingw64 ^
          --follow-imports ^
          --output-dir=build\student\ ^
          --assume-yes-for-download ^
          --windows-product-version=1.0 ^
          --include-data-dir=database=database,File_template=File_template ^
          --onefile ^
          --plugin-enable=pyqt5 ^
          --windows-disable-console ^
          --windows-icon-from-ico=icon\icon.ico ^
            student_entry.py

echo "add File_template"
mkdir build\student\File_template
xcopy File_template build\student\File_template /s /y
echo "add database"
mkdir build\student\database
xcopy database build\student\database /s /y
echo "finished generating student.exe"

goto end

:full
python -m nuitka ^
          --mingw64 ^
          --follow-imports ^
          --output-dir=build\full\ ^
          --assume-yes-for-download ^
          --windows-product-version=1.0 ^
          --include-data-dir=database=database,File_template=File_template ^
          --onefile ^
          --plugin-enable=pyqt5 ^
          --windows-disable-console ^
          --windows-icon-from-ico=icon\icon.ico ^
          full_entry.py

echo "add File_template"
mkdir build\full\File_template
xcopy File_template build\full\File_template /s /y
echo "add database"
mkdir build\full\database
xcopy database build\full\database /s /y
echo "finished generating full.exe"

goto end