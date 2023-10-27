python -m nuitka ^
          --mingw64 ^
          --follow-imports ^
          --output-dir=build ^
          --assume-yes-for-download ^
          --windows-product-version=1.0 ^
          --include-data-dir=database=database,File_template=File_template ^
          --onefile ^
          --plugin-enable=pyqt5 ^
          --windows-disable-console ^
          --windows-icon-from-ico=icon\icon.ico ^
          main_teacher.py

echo "add File_template"
mkdir build\File_template
xcopy File_template build\File_template /s /y
echo "add database"
mkdir build\database
xcopy database build\database /s /y
echo "all done"